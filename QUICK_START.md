## 🚀 Travel Agent System - Quick Start Guide

---

## ⚡ FASTEST WAY TO START

### Option 1: Use Workspace UI (Recommended for Quick Start)

```bash
# 1. Ensure Workspace is running on port 3000
# Workspace should already be running from earlier setup

# 2. Navigate to Workspace
browser_navigate(url="http://localhost:3000")

# 3. Create a new swarm
# Click "New Swarm" button

# 4. Create each agent with their configuration

# Agent 1: Researcher
# - Tools: terminal, web_search, browser, read_file, write_file
# - Instructions: See researcher-soul.md

# Agent 2: Designer  
# - Tools: terminal, read_file, write_file
# - Instructions: See designer-soul.md

# Agent 3: Reviewer
# - Tools: terminal, read_file, write_file
# - Instructions: See reviewer-soul.md

# Agent 4: Developer
# - Tools: terminal, write_file, read_file, python
# - Instructions: See developer-soul.md

# Agent 5: Orchestrator
# - Tools: delegate_task, terminal, write_file, read_file
# - Instructions: See orchestrator-soul.md

# 5. Click "Add Swarm" to start processing
```

### Option 2: Use Python Orchestration Script

```bash
# 1. Create the main orchestration script
cd ~/travel-agents

# 2. Create orchestrator script
cat > run_orchestrator.py << 'EOF'
#!/usr/bin/env python3
"""Travel Agent Orchestrator"""
import yaml
from hermes_tools import delegate_task, read_file, write_file

def main():
    print("🚀 Travel Agent Orchestrator")
    print("=" * 40)
    
    # Check which agents are ready
    agents = ["researcher", "designer", "reviewer", "developer", "orchestrator"]
    
    print("\nAgent Ready Status:")
    for agent in agents:
        soul_path = f"~/travel-agents/{agent}-agent/{agent}-soul.md"
        import os
        if os.path.exists(soul_path):
            print(f"  ✅ {agent:12} Ready")
        else:
            print(f"  ❌ {agent:12} NOT SET UP")
    
    # Wait for all agents to be ready
    while True:
        # Check status
        # Run workflow when all agents ready
        break

if __name__ == "__main__":
    main()
EOF

python run_orchestrator.py
```

---

## 📝 EXAMPLE USER REQUESTS

### Request 1: Simple Trip Planning
```
Book me a trip to Tokyo from New York, June 1-10, 2025.
Budget: $3000
Preferences: Luxury hotels, direct flights, include activities
```

### Request 2: European Adventure
```
Plan a 10-day trip to Paris and Rome, Italy.
Dates: July 15-25, 2025
Budget: $5000
Preferences: Mix of luxury and budget, include art and food experiences
```

### Request 3: Beach Vacation
```
Book a beach vacation for 2 people to Thailand, 7 days.
Dates: November 1-8, 2025
Budget: $2500
Preferences: All-inclusive resort, water activities, relaxing
```

### Request 4: Build the Platform
```
Build the booking platform with flight, hotel, and activity booking APIs.
Use FastAPI, mock data for testing.
Include endpoints for:
- Search flights
- Book flights
- Search hotels
- Book hotels
- Search activities
- Book activities
- Payment processing
```

---

## 🔧 SETUP COMMANDS

### Check All Agents are Configured

```bash
# Check for all SOUL.md files
ls ~/hermes-workspace/profiles/travel-agents/

# Expected output (5 agent files)
# ├── developer-soul.md
# ├── designer-soul.md
# ├── orchestrator-soul.md
# ├── reviewer-soul.md
# └── researcher-soul.md
```

### Create Agent Directories

```bash
mkdir -p ~/travel-agents/{researcher-agent,designer-agent,reviewer-agent,developer-agent,orchestrator-agent}

# Copy SOUL.md files to each agent directory
cp ~/hermes-workspace/profiles/travel-agents/researcher-soul.md \
   ~/travel-agents/researcher-agent/researcher-soul.md

cp ~/hermes-workspace/profiles/travel-agents/designer-soul.md \
   ~/travel-agents/designer-agent/designer-soul.md

cp ~/hermes-workspace/profiles/travel-agents/reviewer-soul.md \
   ~/travel-agents/reviewer-agent/reviewer-soul.md

cp ~/hermes-workspace/profiles/travel-agents/developer-soul.md \
   ~/travel-agents/developer-agent/developer-soul.md

cp ~/hermes-workspace/profiles/travel-agents/orchestrator-soul.md \
   ~/travel-agents/orchestrator-agent/orchestrator-soul.md
```

### Initialize Task Queue

```bash
# Create initial task queue
cat > ~/travel-agents/task_queue.yaml << 'EOF'
project: "Travel Booking Platform"
version: "1.0.0"
agents:
  researcher:
    tools: ["terminal", "web_search", "browser"]
    status: idle
  designer:
    tools: ["terminal", "file"]
    status: idle
  reviewer:
    tools: ["terminal", "file", "python"]
    status: idle
  developer:
    tools: ["terminal", "file", "python", "code_exec"]
    status: idle
  orchestrator:
    tools: ["delegate_task", "terminal", "file"]
    status: ready
pending_tasks: []
active_task: null
completed_tasks: []
EOF
```

---

## 🧪 TESTING THE SYSTEM

### Test 1: Quick Research

```bash
# Use Researcher agent standalone
hermes -p ~/travel-agents/researcher-agent/researcher-soul.md << 'EOF'
User request: Research flights from JFK to Tokyo, June 1, budget $1000
Please: Find 5 flight options, note prices, airlines, durations
EOF
```

### Test 2: Standalone Designer

```bash
# Use Designer agent with research input
hermes -p ~/travel-agents/designer-agent/designer-soul.md << 'EOF'
Input: Research complete - found 5 flight options, 3 hotel options, 10 activities
User request: Design 5-day itinerary for 2 adults, budget $2000
Please: Create detailed day-by-day schedule with timing and costs
EOF
```

### Test 3: Standalone Reviewer

```bash
# Use Reviewer agent to validate
hermes -p ~/travel-agents/reviewer-agent/reviewer-soul.md << 'EOF'
Input files:
- Research report: ~/travel-agents/research/output.md
- Itinerary design: ~/travel-agents/designer/output.md
Please: Validate research quality, itinerary feasibility, budget alignment
EOF
```

### Test 4: Standalone Developer

```bash
# Use Developer agent to build platform
hermes -p ~/travel-agents/developer-agent/developer-soul.md << 'EOF'
Task: Build mock booking platform API
Requirements:
- Search endpoints for flights, hotels, activities
- Booking endpoints for all 3 types
- Payment processing endpoint
- Mock data for testing
- API running on localhost:8080
Please: Build complete platform and return API documentation
EOF
```

### Test 5: Full Workflow

```bash
# Use Orchestrator to run full workflow
cd ~/travel-agents/orchestrator-agent

# Start orchestrator
hermes -p orchestrator-soul.md << 'EOF'
User request: "Book me a trip to Tokyo, June 1-10, $3000"

Action: Initialize system, parse request, create task queue,
       run full workflow through all 4 agents

Workflow:
1. Researcher: Research flights, hotels, activities
2. Designer: Design itinerary based on research
3. Reviewer: Validate itinerary
4. Developer: Build platform and execute bookings

Please: Start the workflow and monitor progress
EOF
```

---

## 📊 EXPECTED OUTPUT

### For a Research Request:
```
📄 RESEARCH OUTPUT

✈️ FLIGHT OPTIONS (5 results):
- Airline: SkyLine, Price: $850, Duration: 14h, Direct: Yes
- Airline: BudgetAir, Price: $600, Duration: 16h, Direct: No
- Airline: Premium, Price: $1200, Duration: 12h, Direct: Yes
...

🏨 HOTEL OPTIONS (3 results):
- Hotel: The Grand Tokyo, $400/night, Category: Luxury
- Hotel: Midtown Inn, $150/night, Category: Economy
- Hotel: Business Suites, $280/night, Category: Mid-range
...

🎪 ACTIVITIES (10 results):
- Activity: Shibuya Crossing, $50, Category: Sightseeing
- Activity: Meiji Shrine, $30, Category: Culture
- Activity: TeamLab Borderless, $85, Category: Art
...

Total estimated cost: $1,500 (within $3000 budget) ✅
```

### For a Booking Platform Build Request:
```
✅ BOOKING PLATFORM BUILT SUCCESSFULLY

Platform: ~/travel-booking-api
API Endpoint: http://localhost:8080

Endpoints:
POST /api/search_flights - Search for flights
POST /api/book_flight - Book a flight
POST /api/search_hotels - Search for hotels
POST /api/book_hotel - Book a hotel
POST /api/search_activities - Search activities
POST /api/book_activity - Book an activity

Mock Features:
- 50+ flight routes
- 100+ hotel properties
- 50+ activities
- Payment processing (90% success rate)

Documentation:
- API docs: docs/API.md
- Integration: docs/INTEGRATION.md
```

---

## ⚠️ IMPORTANT NOTES

1. **Each Agent is Independent:** Agents don't share memory - all context must be passed in the request.

2. **Sequential Processing:** Agents run one at a time in the workflow order (Researcher → Designer → Reviewer → Developer).

3. **Task Dependencies:** Each agent waits for the previous agent to complete.

4. **File Paths:** Use absolute paths or paths relative to ~/travel-agents.

5. **Tool Access:** Only include tools the agent actually needs for its role.

6. **Output Format:** Each agent should save its output to a consistent location so the next agent can read it.

---

## 🐛 TROUBLESHOOTING

### Agent Not Found Error:
```
Error: Agent 'researcher' not found in workspace

Solution:
1. Check agent directory exists:
   ls ~/travel-agents/researcher-agent/

2. Check SOUL.md exists:
   ls ~/travel-agents/researcher-agent/researcher-soul.md

3. If missing, copy from:
   cp ~/hermes-workspace/profiles/travel-agents/researcher-soul.md \
      ~/travel-agents/researcher-agent/
```

### Tool Not Available:
```
Error: Tool 'web_search' not found

Solution:
1. Check agent has the required tool installed
2. Update agent-soul.md to use available tools only
3. Common tools: terminal, read_file, write_file, python
```

### Agent Stuck/Hanging:
```
Solution:
1. Check agent is running:
   ps aux | grep hermes

2. Check agent output:
   cat /tmp/hermes/agent-output.log

3. Restart agent:
   Run the agent again with the same prompt
```

### Task Not Progressing:
```
Check:
1. Task queue file exists:
   cat ~/travel-agents/task_queue.yaml

2. Task dependencies are met:
   ls [output files from previous tasks]

3. Agent is available:
   Check agent status in orchestrator
```

---

## 🎯 NEXT STEPS

1. ✅ **Create all 5 agents** with their SOUL.md files
2. ✅ **Set up Orchestrator** to manage workflow
3. ✅ **Create task queue** file
4. ✅ **Test each agent** individually
5. ✅ **Test full workflow** with Orchestrator
6. ⏭️ **Integrate with real APIs** (Duffel, Amadeus, etc.)
7. ⏭️ **Build persistent databases** instead of mocks
8. ⏭️ **Add real payment processing**
9. ⏭️ **Deploy production version**

---

## 📞 SUPPORT

If you run into issues:

1. **Check SOUL.md files** - Make sure all agents have proper configuration
2. **Review error messages** - Agents provide detailed error information
3. **Check tool availability** - Make sure required tools are installed
4. **Review previous outputs** - Make sure output format matches expectations

For detailed documentation, see:
- `~/travel-agents/ARCHITECTURE.md` - Complete system architecture
- `~/travel-agents/QUICK_START.md` - This guide

---

**Happy Travel Planning! 🌍✈️🏨**

---

**Created:** May 2025  
**Version:** 1.0