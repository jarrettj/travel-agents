# Workflows

## Sequential Agent Execution

Hermes Workspace supports sequential execution where agents run one at a time, with each agent waiting for the previous one to complete.

### Configuration Options

#### Option 1: Workspace UI (Recommended for Beginners)

1. **Open Swarm Mode** in Hermes Workspace
2. **Add each agent** with configuration:
   - Researcher: Set `execution_order = 1`
   - Designer: Set `execution_order = 2`
   - Developer: Set `execution_order = 3`
   - Reviewer: Set `execution_order = 4`
3. **Dispatch tasks** — workspace handles sequential handoffs

#### Option 2: API-based Configuration

```bash
# Start with Researcher Agent
curl -X POST http://localhost:3000/api/swarm-dispatch \
  -H 'Content-Type: application/json' \
  -d '{
    "workerIds": ["researcher"],
    "prompt": "Research top 10 travel destinations for 2026",
    "waitForCheckpoint": true,
    "checkpointPollSeconds": 90
  }'

# Wait for completion, then dispatch to Designer
# (Hermes Workspace auto-handles this via workflow config)
```

#### Option 3: Custom Workflow Script

Create `workflow/sequential-runner.py`:

```python
#!/usr/bin/env python3
"""Sequential agent execution runner for travel-agents project."""

import requests
import time
import json
from pathlib import Path

BASE_URL = "http://localhost:3000"
WORKFLOW_FILE = Path("workflow/config.json")

def load_config():
    """Load workflow configuration from file."""
    if WORKFLOW_FILE.exists():
        return json.loads(WORKFLOW_FILE.read_text())
    return {"agents": [], "config": {}}

def dispatch_agent(agent_id: str, task: str, checkpoint: dict = None):
    """Dispatch a task to a specific agent."""
    url = f"{BASE_URL}/api/swarm-dispatch"
    
    payload = {
        "missionTitle": f"Task: {task}",
        "assignments": [
            {
                "workerId": agent_id,
                "task": task,
                "rationale": f"Received checkpoint from previous agent" if checkpoint else "Initial task",
                "inputContext": json.dumps(checkpoint) if checkpoint else None
            }
        ],
        "waitForCheckpoint": True,
        "checkpointPollSeconds": 90
    }
    
    response = requests.post(url, json=payload)
    result = response.json()
    
    if result.get("results") and result["results"][0].get("checkpointStatus") == "checkpointed":
        # Save checkpoint for next agent
        checkpoint = result["results"][0].get("deliverable")
        return checkpoint
    else:
        raise Exception(f"Agent {agent_id} failed to complete")

def run_workflow(agents: list):
    """Run agents sequentially."""
    checkpoint = None
    
    for i, agent in enumerate(agents):
        agent_id = agent.get("id")
        task = agent.get("task")
        
        print(f"\n🔄 Starting agent {agent_id}...")
        checkpoint = dispatch_agent(agent_id, task, checkpoint)
        print(f"✅ Agent {agent_id} completed with checkpoint saved")
    
    return checkpoint

if __name__ == "__main__":
    config = load_config()
    agents = config.get("agents", [])
    checkpoint = run_workflow(agents)
    print("\n✅ Workflow completed successfully!")
```

### Usage

```bash
# Save config.json in workflow/ directory
cat > workflow/config.json << EOF
{
  "agents": [
    {"id": "researcher", "task": "Research market"},
    {"id": "designer", "task": "Design UI"},
    {"id": "developer", "task": "Develop platform"},
    {"id": "reviewer", "task": "Review and test"}
  ],
  "workflow": {
    "mode": "sequential",
    "handoffStrategy": "checkpoint"
  }
}
EOF

# Run the workflow
python workflow/sequential-runner.py
```

---

## Handoff Protocol

### Checkpoint Format

Each agent must return a standardized checkpoint:

```json
{
  "agentId": "researcher",
  "status": "completed",
  "timestamp": "2026-05-03T15:30:00Z",
  "deliverable": {
    "type": "market_research",
    "version": 1,
    "data": {
      "destinations": [...],
      "competitors": [...],
      "insights": [...]
    }
  },
  "confidence": 0.92,
  "nextAgent": "designer",
  "summary": "Brief summary for context"
}
```

### Handoff Validation

Before handoff, validate:
1. ✅ Previous agent returned checkpoint
2. ✅ Checkpoint format matches schema
3. ✅ Required fields present
4. ✅ Confidence score > threshold (e.g., 0.7)

---

## Error Handling

### Agent Failure Scenarios

| Scenario | Recovery Strategy |
|----------|-------------------|
| Agent times out | Retry with extended timeout |
| Agent fails to checkpoint | Move to next agent anyway |
| Checkpoint validation fails | Loop back to previous agent |
| External API failure | Log and continue, mark in report |

### Example Error Handler

```python
def handle_agent_failure(failed_agent: str, agent_id: str):
    """Handle agent failure with appropriate strategy."""
    
    if failed_agent == "developer" and agent_id == "timeout":
        # Developer timed out, let designer continue with partial findings
        print("⚠️ Developer timeout, proceeding with designer...")
        return False  # Skip this agent
    
    elif failed_agent == "researcher":
        # Critical failure, abort workflow
        print("❌ Research failed, aborting workflow")
        return True  # Fail entire workflow
    
    # Default: retry once
    return True
```

---

## Monitoring

### During Execution

```bash
# View agent status
curl -X GET http://localhost:3000/api/swarm/status

# View current checkpoint
curl -X GET http://localhost:3000/api/swarm/checkpoint?mission=travel-research

# View Kanban board
curl -X GET http://localhost:3000/api/kanban/board
```

### Logs

Each agent writes logs to:
- Workspace: Real-time in Swarm view
- File: `~/.hermes/logs/swarm/agent-{id}.log`

---

## Quick Start Commands

```bash
# Start Hermes Workspace
cd ~/hermes-workspace
pnpm dev

# Open browser at http://localhost:3000

# Add agents in Swarm Mode UI
1. Add Researcher (role: researcher)
2. Add Designer (role: designer)
3. Add Developer (role: developer)
4. Add Reviewer (role: reviewer)

# Set execution order in each agent's config
```
