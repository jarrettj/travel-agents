#!/usr/bin/env python3
"""
Travel Agents Web Interface

A web interface for users to interact with the travel agent swarm.
Users can submit requests and the multi-agent system will handle them.
"""

import asyncio
import json
import os
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Configuration
PORT = int(os.environ.get("PORT", 9999))
API_KEY = os.environ.get("API_KEY", "demo-key")
HOST = os.environ.get("HOST", "127.0.0.1")

app = FastAPI(
    title="Travel Agents API",
    description="Multi-agent system for travel booking platform",
    version="1.0.0"
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True)

# Global state
requests_history = []
active_requests = {}

# Type definitions for Pydantic validation
from pydantic import BaseModel, Field
from typing import Optional, List

class TravelRequest(BaseModel):
    """User travel request"""
    destination: str = Field(..., description="Desired destination")
    dates: str = Field(..., description="Travel dates (e.g., 2025-05-01 to 2025-05-07)")
    travelers: int = Field(default=2, ge=1, description="Number of travelers")
    budget: float = Field(default=1000.0, ge=0.0, description="Total budget in USD")
    preferences: dict = Field(default_factory=dict, description="Travel preferences")
    trip_type: str = Field(default="vacation", description="Vacation, business, other")
    messages: str = Field(default="", description="Additional context for agents")

class RequestStatus(BaseModel):
    """Current status of a request"""
    request_id: str
    status: str
    current_agent: str
    completed_steps: List[str]
    agent_messages: List[dict]
    created_at: datetime
    updated_at: datetime

class SearchResult(BaseModel):
    """Travel search results"""
    flights: List[dict]
    hotels: List[dict]
    activities: List[dict]

# Pydantic validation for requests
def validation_error_handler(exc):
    """Handle validation errors"""
    errors = []
    for error in exc.errors():
        errors.append({
            "field": error["loc"][0],
            "message": error["msg"]
        })
    return JSONResponse(
        status_code=422,
        content={"errors": errors}
    )

app.add_exception_handler(RequestValidationError, validation_error_handler)

@app.get("/")
async def root():
    """Serve the web interface"""
    return FileResponse("web/dist/index.html")

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/api/requests", response_model=List[RequestStatus])
async def get_requests():
    """Get all active requests"""
    return [
        RequestStatus(**req) 
        for req in requests_history 
        if req.get("status") != "completed"
    ]

@app.post("/api/requests", response_model=RequestStatus)
async def create_travel_request(request: TravelRequest):
    """Create a new travel request"""
    request_id = f"req-{datetime.now().strftime('%Y%m%d%H%M%S')}-{os.getpid()}"
    
    # Create initial request state
    state = {
        "request_id": request_id,
        "status": "submitted",
        "destination": request.destination,
        "dates": request.dates,
        "travelers": request.travelers,
        "budget": request.budget,
        "trip_type": request.trip_type,
        "preferences": request.preferences,
        "messages": request.messages,
        "current_agent": "travel-agent-orchestrator",
        "completed_steps": [],
        "agent_messages": [],
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    
    requests_history.append(state)
    active_requests[request_id] = state
    
    # Return initial status
    return RequestStatus(**state)

@app.get("/api/requests/{request_id}", response_model=RequestStatus)
async def get_request(request_id: str):
    """Get status of a specific request"""
    if request_id not in active_requests:
        raise HTTPException(status_code=404, detail="Request not found")
    
    state = active_requests[request_id]
    return RequestStatus(**state)

@app.post("/api/requests/{request_id}/agent/{agent_name}/handoff")
async def handoff_agent(request_id: str, agent_name: str):
    """Manually handoff to a specific agent"""
    if request_id not in active_requests:
        raise HTTPException(status_code=404, detail="Request not found")
    
    state = active_requests[request_id]
    
    # Simulate agent processing
    state["status"] = "processing"
    state["updated_at"] = datetime.now()
    state["completed_steps"].append(f"Handed to {agent_name}")
    state["agent_messages"].append({
        "agent": agent_name,
        "timestamp": datetime.now().isoformat(),
        "message": f"Processing request for {state['destination']}"
    })
    
    active_requests[request_id] = state
    return RequestStatus(**state)

@app.post("/api/search/{request_id}")
async def search_travel(request_id: str):
    """Search for travel options"""
    if request_id not in active_requests:
        raise HTTPException(status_code=404, detail="Request not found")
    
    # Simulate API responses from Skyscanner, Booking.com
    result = SearchResult(
        flights=[
            {
                "id": "flight-1",
                "airline": "Delta",
                "departure": {"airport": "JFK", "time": "10:00", "date": "2025-05-01"},
                "arrival": {"airport": "LAX", "time": "14:00", "date": "2025-05-01"},
                "price": 299.00,
                "duration": "6h 30m"
            },
            {
                "id": "flight-2",
                "airline": "United",
                "departure": {"airport": "JFK", "time": "08:00", "date": "2025-05-01"},
                "arrival": {"airport": "LAX", "time": "11:30", "date": "2025-05-01"},
                "price": 349.00,
                "duration": "6h"
            }
        ],
        hotels=[
            {
                "id": "hotel-1",
                "name": "Hilton LAX",
                "rating": 4.5,
                "stars": 4,
                "price_per_night": 159.00,
                "amenities": ["wifi", "pool", "gym", "parking"]
            }
        ],
        activities=[
            {
                "id": "activity-1",
                "name": "Disney World Tour",
                "duration": "8 hours",
                "price": 89.00
            }
        ]
    )
    
    return result

@app.get("/api/generate-book")
async def generate_booking_form(request_id: str):
    """Generate booking form based on selected options"""
    return {"message": "Booking form generated", "request_id": request_id}

if __name__ == "__main__":
    print(f"Starting Travel Agents Web Interface on http://{HOST}:{PORT}")
    uvicorn.run(app, host=HOST, port=PORT)
