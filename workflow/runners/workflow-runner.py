#!/usr/bin/env python3
"""Sequential agent execution runner for travel-agents project."""

import requests
import time
import json
from pathlib import Path

BASE_URL = "http://localhost:3000"
CONFIG_PATH = Path("workflow/config.json")

def load_config():
    """Load workflow configuration from file."""
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text())
    return {"agents": [], "config": {}}

def wait_for_checkpoint(agent_id: str, timeout: int = 300, poll_interval: int = 10):
    """Poll for agent checkpoint within timeout period."""
    print(f"⏳ Waiting for {agent_id} to complete...")
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            url = f"{BASE_URL}/api/swarm/checkpoint?workerId={agent_id}"
            response = requests.get(url, timeout=5)
            result = response.json()
            
            if result.get("agent") and result["agent"].get("status") == "checkpointed":
                print(f"✅ Checkpoint received from {agent_id}")
                return result["agent"].get("deliverable")
        except Exception as e:
            pass
        
        time.sleep(poll_interval)
    
    print(f"⚠️ Timeout waiting for {agent_id} to complete")
    return None

def dispatch_agent(agent: dict, input_context: dict = None):
    """Dispatch a task to a specific agent."""
    agent_id = agent.get("id")
    task = agent.get("task")
    
    print(f"\n🔄 Starting agent: {agent_id}")
    print(f"   Task: {task}")
    
    url = f"{BASE_URL}/api/swarm-dispatch"
    
    payload = {
        "missionTitle": f"Travel Agents: {task}",
        "assignments": [
            {
                "workerId": agent_id,
                "task": task,
                "rationale": "Sequential workflow - previous agent completed" if input_context else "Initial task",
                "inputContext": json.dumps(input_context) if input_context else None
            }
        ],
        "waitForCheckpoint": True,
        "checkpointPollSeconds": 90,
        "timeoutSeconds": 600  # 10 minutes per agent
    }
    
    try:
        response = requests.post(url, json=payload, timeout=600)
        result = response.json()
        
        if result.get("results"):
            checkpoint_status = result["results"][0].get("checkpointStatus")
            
            if checkpoint_status == "checkpointed":
                checkpoint = result["results"][0].get("deliverable")
                print(f"✅ Agent {agent_id} completed successfully")
                return checkpoint
            
            elif checkpoint_status == "failed":
                error_msg = result["results"][0].get("error", "Unknown error")
                print(f"❌ Agent {agent_id} failed: {error_msg}")
                return None
                
            else:
                print(f"⏳ Agent {agent_id} still running, waiting...")
                return None
        else:
            print(f"❌ No results from agent {agent_id}")
            return None
            
    except Exception as e:
        print(f"❌ Error dispatching to {agent_id}: {e}")
        return None

def run_workflow(agents: list):
    """Run agents sequentially, waiting for checkpoints."""
    input_context = None
    
    print("\n" + "="*60)
    print("Travel Agents Sequential Workflow")
    print("="*60)
    
    for i, agent in enumerate(agents):
        agent_id = agent.get("id")
        task = agent.get("task")
        next_agent = agent.get("handoffsTo", [])
        
        # Prepare input context from previous agent's output
        input_context = None
        if i > 0 and "output" in locals() and agent.get("expectsInput"):
            input_context = agent.get("expectsInput", {})
        
        # Dispatch the agent
        checkpoint = dispatch_agent(agent, input_context)
        
        if checkpoint is None:
            print(f"\n❌ Workflow failed at agent {agent_id}")
            return None
        
        # Save checkpoint for next iteration
        output = checkpoint
        print(f"\n📋 Checkpoint saved:")
        print(f"   Output type: {output.get('type', 'unknown')}")
        print(f"   Confidence: {output.get('confidence', 0):.2f}")
        
        # Wait for next agent if defined
        if next_agent and i < len(agents) - 1:
            next_agent_id = next_agent[0]
            print(f"\n⏭️  Handoff to next agent: {next_agent_id}")
            checkpoint = wait_for_checkpoint(next_agent_id, timeout=120, poll_interval=5)
            if checkpoint is None:
                print(f"❌ Next agent ({next_agent_id}) timed out")
                return None
            input_context = checkpoint
            output = None  # Next iteration will handle this
    
    print("\n" + "="*60)
    print("✅ Workflow completed successfully!")
    print("="*60)
    
    return output

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python workflow-runner.py <start_agent_index>")
        print("       Start agent by index (0 for first agent)")
        sys.exit(1)
    
    try:
        start_index = int(sys.argv[1])
    except ValueError:
        print("Error: Index must be a number")
        sys.exit(1)
    
    config = load_config()
    agents = config.get("agents", [])
    
    if start_index >= len(agents):
        print(f"Error: Index {start_index} is out of range (0-{len(agents)-1})")
        sys.exit(1)
    
    # Start from specified agent
    agents_to_run = agents[start_index:]
    
    checkpoint = run_workflow(agents_to_run)
    
    if checkpoint is not None:
        # Save final checkpoint to file
        Path("workflow/checkpoints.json").write_text(json.dumps(checkpoint, indent=2))
        print("\n📄 Final checkpoint saved to workflow/checkpoints.json")
