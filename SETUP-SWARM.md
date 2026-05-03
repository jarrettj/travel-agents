# Travel Agent Swarm - Setup Guide

This guide covers how to set up and start the Travel Agent multi-agent swarm in Hermes Workspace.

## Quick Start (2 Minutes)

```bash
# 1. Navigate to Hermes directory
cd ~/.hermes

# 2. Start Hermes workspace
hermes workspace start

# 3. Navigate to Travel workspace
hermes workspace use travel

# 4. Add the swarm
hermes workspace swarm add travel
```

That's it! Your travel agents are ready to use.

---

## Detailed Setup

### Step 1: Verify Agents Are Present

Open your terminal and check:

```bash
cd ~/.hermes
ls -la swarms/travel.json
```

You should see the swarm configuration file we created.

### Step 2: Start the Workspace

```bash
# Start Hermes Workspace
hermes workspace start

# Select the Travel workspace
hermes workspace use travel

# Verify agents are loaded
hermes workspace list
```

Expected output:
```
Available Workspaces:
  └─ Travel (12 agents)
     ├─ Travel Orchestrator
     ├─ Travel Researcher
     ├─ Travel Designer
     ├─ Travel Developer
     └─ Travel Reviewer
```

### Step 3: Add the Swarm to UI

1. Open your browser at `http://localhost:3000`
2. Navigate to **Swarms** in the sidebar
3. Click **"Add Swarm"**
4. Name: `travel`
5. Select agents from the dropdown:
   - ✓ Travel Orchestrator
   - ✓ Travel Researcher
   - ✓ Travel Designer
   - ✓ Travel Developer
   - ✓ Travel Reviewer
6. Click **"Save Swarm"**

### Step 4: Provision Agents

The agents will show as "not provisioned" initially. To provision:

```bash
# Provision all agents in the swarm
hermes swarm provision travel

# Or provision specific agents
hermes swarm provision travel --agent researcher
hermes swarm provision travel --agent designer
```

### Step 5: Start a Mission

Once agents are provisioned:

1. Click **"New Mission"**
2. Choose **"Multi-Agent Swarm"** mode
3. Select the **travel** swarm
4. Enter your mission:

**Example Mission 1 - Research:**
```
Research available travel APIs for booking flights and hotels
Focus on: Skyscanner, Booking.com, Airbnbcificator APIs
Include: API endpoints, rate limits, pricing models
```

**Example Mission 2 - Build Booking System:**
```
Build a travel booking platform with the following features:
- Flight search and booking
- Hotel search and booking
- Payment processing with Stripe
- User authentication and profiles
Generate: Complete API with tests and documentation
```

---

## Agent Handoff Workflow

The agents work in a sequential handoff pattern:

```
Orchestrator
   ↓ (coordinates workflow)
Researcher  ← → Reviewer (validation)
   ↓
Designer
   ↓
Developer  ← → Reviewer (code review)
   ↓
Orchestrator (deployment)
```

### Handoff Triggers:

1. **Auto-handoff**: When Researcher completes research, it automatically triggers Designer
2. **Manual handoff**: Use `hermes handoff <target>` command
3. **Success criteria**: Each agent must complete its checkpoint before handing off

---

## Environment Variables

Set these before starting the swarm:

```bash
# In ~/.hermes/.env or add to swarm config
export SKYSCANNER_API_KEY="your-key-here"
export BOOKINGCOM_API_KEY="your-key-here"
export STRIPE_API_KEY="your-key-here"
export PAYPAL_CLIENT_ID="your-client-id"
```

Or create a `.env` file:

```env
# ~/.hermes/.env
SKYSCANNER_API_KEY=your-key-here
BOOKINGCOM_API_KEY=your-key-here
STRIPE_API_KEY=your-key-here
```

---

## Running Swarm Tasks

### Option 1: Browser Interface

1. Open `http://localhost:3000`
2. Click **"New Mission"** → **"Multi-Agent Swarm"**
3. Select "travel" swarm
4. Enter mission description
5. Click **"Start"**

### Option 2: CLI Commands

```bash
# Start mission via CLI
hermes mission start --mode swarm --swarm travel --mission "Research flight APIs"

# Add to queue
hermes mission queue add --mode swarm --swarm travel --queue-name "api-research"

# Monitor progress
hermes mission list --swarm travel
```

### Option 3: Direct Agent Invocation

```bash
# Run a single agent
hermes agent run --agent "travel-agent-orchestrator" \
  --mission "Plan travel booking architecture"

# Run multiple agents in sequence
hermes agent run --agent "travel-agent-researcher" \
  --mission "Research flight APIs"

hermes agent run --agent "travel-agent-designer" \
  --mission "Design booking interface based on API requirements"

hermes agent run --agent "travel-agent-developer" \
  --mission "Build booking API from design specs"
```

---

## Troubleshooting

### "Agent not found"

```bash
# Re-provision the agent
hermes swarm provision travel --force

# Check the swarm config
cat ~/.hermes/swarms/travel.json
```

### "Handoff failed"

Check the checkpoint format matches between agents:

```bash
# Check Researcher checkpoint
hermes checkpoint list --agent researcher

# Check Designer checkpoint
hermes checkpoint list --agent designer

# They should have compatible formats
```

### "API key missing"

```bash
# Add env var
export SKYSCANNER_API_KEY="your-key"

# Or edit swarm config
hermes workspace edit --field api_keys
```

### "Agent stuck"

```bash
# Force complete current task
hermes agent complete --agent "travel-agent-<name>"

# Or restart the agent
hermes agent restart --agent "travel-agent-<name>"
```

---

## Monitoring

### CLI Monitoring

```bash
# View agent status
hermes agent status --swarm travel

# View mission logs
hermes mission logs --mission-id <id>

# View checkpoints
hermes checkpoint list --swarm travel
```

### Web UI

- **Dashboard**: Real-time progress of all missions
- **Swarm View**: Live agent handoffs and completions
- **Mission Details**: Step-by-step breakdown of each task

---

## Next Steps

1. **API Integration**: Add your actual API keys from Skyscanner, Booking.com
2. **Custom Agents**: Create travel-specific sub-agents (e.g., `travel-agent-price-comparator`)
3. **Scheduled Tasks**: Set up weekly booking summaries
4. **Webhooks**: Configure notifications for booking completions

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `hermes workspace start` | Start Hermes |
| `hermes workspace use travel` | Use Travel workspace |
| `hermes swarm add travel` | Add travel swarm |
| `hermes swarm provision travel` | Provision all agents |
| `hermes mission start` | Start a new mission |
| `hermes agent run` | Run a single agent |
| `hermes agent status` | Check agent health |

---

## See Also

- [Quick Start Guide](../docs/QUICKSTART.md) - Get started in 5 minutes
- [Swarm API Reference](../docs/SWARM-SETUP.md) - Programmatic access
- [Agent Reference](../docs/agents/) - Individual agent documentation
