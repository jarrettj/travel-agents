# 🚀 Travel Agent System - Quick Start Guide

A multi-agent travel booking system using Hermes Workspace with 5 specialized agents working together.

## Version

**Current Version:** 1.0.0

## 📋 System Overview

The travel agent system consists of 5 specialized agents working in sequence:

1. **Travel Researcher** - Researches flights, hotels, activities, pricing, and visa requirements
2. **Travel Designer** - Designs detailed itineraries and booking flows
3. **Travel Developer** - Builds booking platforms and executes bookings via APIs
4. **Travel Reviewer** - Validates bookings for feasibility, compliance, and security
5. **Travel Orchestrator** - Coordinates all agents and manages workflow

## 🎯 Prerequisites

- **Hermes Workspace** running on port 3000
- **Hermes Agent Dashboard** (optional) running on port 9119
- Agent profiles configured in `~/.hermes/profiles/`

## ⚡ Quick Start

### Step 1: Start Hermes Workspace

```bash
# Ensure the workspace is running
cd ~/hermes-workspace
# Kill any existing processes
pkill -f "vite.*3000" 2>/dev/null || true
sleep 2

# Start fresh
pnpm dev
```

Verify it's running:
```bash
lsof -i :3000
# Should show: node 8xxxx jjordaan *:3000 (LISTEN)
```

### Step 2: Configure Agent Profiles

Each agent profile is located in `~/.hermes/profiles/`:

```bash
# List all profiles
ls -la ~/.hermes/profiles/
```

You should see:
- `travel-agent-orchestrator` ✓
- `travel-agent-researcher` ✓
- `travel-agent-designer` ✓
- `travel-agent-developer` ✓
- `travel-agent-reviewer` ✓

**Important:** All profiles have been updated with:
- **Model:** `apple/omlx/qwen` (local model)
- **Iterations:** 120
- **Max Turns:** 60

### Step 3: Load the Travel Agent Assistant Skill

This skill provides domain-specific knowledge to all agents working on travel tasks.

```bash
# Load the skill when working on travel tasks
cd ~/travel-agents
hermes -p travel-agent-assistant "Help me research flights to Tokyo"
```

Or have it loaded automatically by adding to your config:
```yaml
# ~/.hermes/config.yaml
skills:
  - travel-agent-assistant
```

### Step 4: Run Travel Agent Tasks

#### Option A: Interactive Mode

```bash
# Run a single agent with a specific task
cd ~/travel-agents

# Example: Run researcher agent
hermes -p travel-agent-researcher "Research flights from NYC to London, June 1-10, 2025"

# Example: Run designer agent
hermes -p travel-agent-designer "Design a 5-day Tokyo itinerary based on this research: [paste research]"

# Example: Run developer agent
hermes -p travel-agent-developer "Build a booking API for flights using this specification: [paste spec]"

# Example: Run reviewer agent
hermes -p travel-agent-reviewer "Review this itinerary for feasibility: [paste itinerary]"
```

#### Option B: Orchestrator Mode

```bash
# Use the orchestrator to manage the full workflow
cd ~/travel-agents

# Example: Book a trip to Paris
hermes -p travel-agent-orchestrator << 'EOF'
User request: "Book me a 7-day trip to Paris from June 1-8, 2025, budget $3000"

Action: Initialize the travel agent workflow:
1. Research: Find flights, hotels, and activities
2. Design: Create a detailed itinerary
3. Review: Validate the plan
4. Book: Execute the bookings

Please execute the workflow and return all booking confirmations.
EOF
```

### Step 5: Work with Travel APIs

The system can integrate with real travel APIs. Here's how to configure and use them:

#### Configure API Keys

Create or update `~/.travel-agents/config.yaml`:

```yaml
# config.yaml
api_keys:
  SKYSCANNER: "your-skyglass-api-key"  # For flight searches
  EXPEDIA: "your-expedia-api-key"     # For comprehensive booking
  STRIPE: "your-stripe-api-key"        # For payment processing
```

#### Search for Flights (via Skyscanner API)

```bash
# Query Skyscanner API
curl -X POST "https://api.skyscanner.com/v2/flights" \
  -H "Authorization: Bearer $SKYSCANNER_API_KEY" \
  -d '{
    "origin": "JFK",
    "destination": "LHR",
    "departDate": "2025-06-01",
    "returnDate": "2025-06-08",
    "passengers": 1
  }' | jq '.data.flights'
```

#### Search for Hotels (via Booking.com API)

```bash
# Query Booking.com API
curl -X POST "https://partners.api.booking.com/hotels/search" \
  -H "Authorization: Bearer $BOOKING_API_KEY" \
  -d '{
    "checkin": "2025-06-08",
    "checkout": "2025-06-15",
    "city": "London",
    "country": "GB",
    "rooms": 1,
    "adults": 2
  }' | jq '.flights'
```

### Step 6: Use the Travel Agent Assistant Skill

The skill provides comprehensive travel knowledge. Use it for:

- **Research assistance:**
  ```bash
  hermes -p travel-agent-assistant "What are the best budget airlines for Europe?"
  ```

- **Booking guidance:**
  ```bash
  hermes -p travel-agent-assistant "How do I book a multi-city trip?"
  ```

- **Error troubleshooting:**
  ```bash
  hermes -p travel-agent-assistant "Why is my booking failing with error 'EN481543'?"
  ```

## 📝 Example Workflow

### Complete Trip Booking Example

```bash
# Step 1: Run Research Agent
hermes -p travel-agent-researcher << 'EOF'
Research destination: Paris, France
Travel dates: June 1-8, 2025
Budget: $3000
Preferences: Luxury hotels, fine dining, cultural experiences
Output: Structured research report with flight options, hotel recommendations, and activity ideas
EOF

# Step 2: Run Designer Agent (provides research output)
hermes -p travel-agent-designer << 'EOF'
Design a detailed 7-day Paris itinerary based on this research:
[PASTE RESEARCH OUTPUT]

Include:
- Day-by-day schedule with specific times
- Hotel recommendations with addresses
- Transportation between locations
- Budget breakdown
- Dining recommendations
EOF

# Step 3: Run Reviewer Agent (provides research and design)
hermes -p travel-agent-reviewer << 'EOF'
Review this itinerary for the following:
1. Flight feasibility (arrival time before hotel check-in)
2. Budget alignment with $3000 limit
3. Visa requirements for France
4. Activity times vs. opening hours

Research output: [PASTE]
Design output: [PASTE]
EOF

# Step 4: Run Developer Agent (provides approved itinerary)
hermes -p travel-agent-developer << 'EOF'
Execute bookings based on approved itinerary:
[PASTE APPROVED ITINERARY]

Booking steps:
1. Search and book flights via Skyscanner/Expedia API
2. Search and book hotels via Booking.com API
3. Search and book activities via Viator/GetYourGuide API
4. Process payment via Stripe
5. Generate booking confirmations

Return all confirmation numbers and details.
EOF

# Step 5: Review Final Output
echo "Booking workflow complete! Save confirmation numbers:"
echo "- Flight Confirmation: ..."
echo "- Hotel Confirmation: ..."
echo "- Activity Confirmations: ..."
```

## 🛠️ Troubleshooting

### Agent Not Responding

```bash
# Check if agent profile exists
ls ~/.hermes/profiles/travel-agent-{agent}/

# If missing, create it
mkdir -p ~/.hermes/profiles/travel-agent-{agent}

# Add runtime.json
cat > ~/.hermes/profiles/travel-agent-{agent}/runtime.json << 'EOF'
{
  "workerId": "travel-agent-{agent}",
  "displayName": "Travel {Agent}",
  "role": "{agent}",
  "model": "apple/omlx/qwen",
  "iteration": 120,
  "maxTurns": 60,
  "tools": ["tool1", "tool2"]
}
EOF
```

### Model Configuration Issues

```bash
# Check current model
grep "model" ~/.hermes/profiles/travel-agent-{agent}/runtime.json

# Update model if needed
sed -i '' 's/"model": ".*"/"model": "apple\/omlx\/qwen"/' ~/.hermes/profiles/travel-agent-{agent}/runtime.json
```

### Workspace Not Running

```bash
# Kill existing processes
pkill -f "vite.*3000"

# Start fresh
cd ~/hermes-workspace
pnpm dev

# Verify
lsof -i :3000
```

## 📚 Next Steps

1. **Load the skill** in your agent prompts
2. **Test individual agents** to understand their capabilities
3. **Set up API keys** for real booking integrations
4. **Create workflows** for specific use cases (simple bookings, multi-city trips, group travel)
5. **Monitor agent performance** and adjust configurations

## 🎉 You're Ready!

Your travel agent system is now configured and ready to:
- Research travel destinations and options
- Design comprehensive itineraries
- Build booking platforms and execute bookings
- Validate bookings for feasibility and compliance
- Orchestrate multi-agent workflows

For more detailed information, see:
- `ARCHITECTURE.md` - Complete system architecture
- `IMPLEMENTATION_SUMMARY.md` - What's been implemented
- `travel-agent-assistant/SKILL.md` - Travel-specific knowledge base
- `travel-agents-swarm.yaml` - Workspace worker configuration

---

**Need help?** Check the skill's documentation or refer to the architecture docs!
