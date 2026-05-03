# Travel Agent Swarm - Quick Start

Get up and running in under 5 minutes!

## Prerequisites

- Hermes Agent installed and running
- Python 3.10+
- Terminal access

## 5-Minute Setup

```bash
# 1. Ensure config exists
cd ~/.hermes

# 2. Add the travel swarm
hermes workspace add
```

Copy this swarm config and save as `travel.json`:

```json
{
  "workerId": "travel-agent-orchestrator",
  "role": "orchestrator",
  "mission": "Coordinate multi-agent travel booking workflows",
  "agents": [
    "travel-agent-orchestrator",
    "travel-agent-researcher",
    "travel-agent-designer",
    "travel-agent-developer",
    "travel-agent-reviewer"
  ]
}
```

## Start the Swarm

```bash
# Start Hermes workspace
hermes workspace start

# Use the travel workspace
hermes workspace use travel

# View the swarm
hermes workspace list
```

## Run Your First Mission

```bash
# Via CLI
hermes mission start \
  --mode swarm \
  --swarm travel \
  --mission "Research flight booking APIs and build a booking platform"

# Via browser
# 1. Open http://localhost:3000
# 2. New Mission → Multi-Agent Swarm
# 3. Select "travel"
# 4. Enter mission description
```

## Example Missions

### Research:
```
Research all available travel booking APIs
Include: flights, hotels, activities
For each API: endpoints, pricing, rate limits, documentation
```

### Build:
```
Build a travel booking platform with these features:
- User authentication and profiles
- Flight search and booking (using Skyscanner API)
- Hotel search and booking (using Booking.com API)
- Payment processing with Stripe
- Booking confirmation emails
- Admin dashboard
```

### Iterate:
```
Review the current booking system
Identify missing features
Generate a development plan for the next sprint
```

## Quick Commands

```bash
# List all swarms
hermes workspace list

# Add new swarm
hermes workspace add

# Provision agents
hermes swarm provision travel

# Start mission
hermes mission start --mode swarm

# View progress
hermes mission list

# Check agent status
hermes agent status
```

## Troubleshooting

**Agents not appearing?**
```bash
hermes workspace reset
hermes workspace add
```

**"Agent not found" error?**
```bash
# Re-provision
hermes swarm provision travel --force
```

**No API key errors?**
```bash
# Add to ~/.hermes/.env
export SKYSCANNER_API_KEY="your-key-here"
```

## What's Next?

1. **Add your API keys** from Skyscanner, Booking.com
2. **Configure payment** with Stripe
3. **Create your first real mission**
4. **Read full setup guide**: `SETUP-SWARM.md`

## Need Help?

- Read [SETUP-SWARM.md](./SETUP-SWARM.md) for detailed instructions
- Check the [Travel Agent Documentation](./) for agent-specific guides
