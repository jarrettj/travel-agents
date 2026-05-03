# Travel Agent Swarm - Quick Start Guide

## What is This?

A multi-agent travel booking system using **Hermes Workspace** where multiple AI agents work together to handle complete travel bookings.

## Current Status

⚠️ **UI Issue:** The "Add Swarm" button in the Hermes Workspace is not functional. Clicking it does not open a modal dialog.

## Recommended Approach

Use the **API directly** to add your travel agents as swarms, bypassing the broken UI.

---

## Quick Start (3 Steps)

### Step 1: Create Agent Profiles

Create profile directories with SOUL.md files:

```bash
mkdir -p ~/.hermes/profiles/travel-agent-booking
mkdir -p ~/.hermes/profiles/travel-agent-reviews

# Booking Agent SOUL.md
cat > ~/.hermes/profiles/travel-agent-booking/SOUL.md << 'EOF'
[
  {"role": "Flights Agent", "desc": "Handles flight searches and bookings", "domain": "travel"},
  {"role": "Hotels Agent", "desc": "Handles accommodation bookings", "domain": "travel"}
]
[
  {"tools": ["skyscanner_api", "api_six", "booking_com_api"], "name": "Travel Booking Tools"}
]
EOF
```

### Step 2: Set API Keys

```bash
# Required for this demo
export SKYSCANNER_API_KEY="demo"  # or your real key
export SIX_REDIS_HOST="localhost"
export SIX_REDIS_USER="default"
export SIX_REDIS_PASSWORD="password"
export BOOKINGCOM_API_KEY="demo"
```

### Step 3: Provision via API

```bash
curl -X POST http://localhost:3000/api/v1/swarms \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Travel-Agent-Swarm",
    "type": "arm_length",
    "arm_length": 3,
    "agents": [
      {
        "profile_id": "travel-agent-booking",
        "role": "Flight/Hotel Agent",
        "description": "Handles flight and hotel bookings",
        "tools": ["skyscanner_api", "api_six", "booking_com_api"]
      },
      {
        "profile_id": "travel-agent-reviews",
        "role": "Review Agent",
        "description": "Reviews travel itineraries",
        "tools": ["travel_advisor_api"]
      },
      {
        "profile_id": "travel-agent-booking",
        "role": "Hotel Agent",
        "description": "Handles hotel booking searches",
        "tools": ["booking_com_api", "agoda_api"]
      }
    ]
  }'
```

---

## Next Actions

After adding the swarm:

1. Navigate to `http://localhost:3000/swarms`
2. Refresh the page
3. Your new swarm should appear in the roster
4. Agents should be "provisioning..." and then become available

---

## What Will Happen Next?

Once the swarm is provisioned:

1. **Agents become available** - Click on your swarm to see member agents
2. **Create a mission** - Click "New Mission" or "Mission Request"
3. **Submit travel request** - Describe what you want to book
4. **Agent collaboration** - Watch as agents:
   - Search for flights
   - Search for hotels
   - Review the itinerary
   - Make bookings
5. **Get results** - Receive a complete travel plan

---

## Troubleshooting

### Problem: "Not Provisioned Yet"

**Solution:** The agents need time to start. Wait 30-60 seconds, then refresh.

### Problem: No swarm appears

**Solution:** Check if the backend is running:
```bash
# On a Mac/Linux terminal
pgrep -f "uvicorn|hermes"  # Check if servers are running

# If not, start them:
cd ~/travel-agents
hermes workspace start
```

### Problem: Permission errors

**Solution:** The profiles need to be readable. Check permissions:
```bash
chmod -R 755 ~/.hermes/profiles/travel-agent-*
```

---

## API Reference

### Add a Swarm

```bash
POST /api/v1/swarms

Request:
{
  "name": string,
  "type": "arm_length" | "hub_and_spoke",
  "arm_length": number,
  "agents": [
    {
      "profile_id": "path_to_profile",
      "role": "Agent role name",
      "description": "Agent description",
      "tools": ["tool1", "tool2", ...]
    }
  ]
}
```

### Get Swarm Details

```bash
GET /api/v1/swarms/:id
```

### Provision a Swarm

```bash
POST /api/v1/swarms/:id/provision
```

### Add Agent to Existing Swarm

```bash
POST /api/v1/swarms/:id/agents

Request:
{
  "profile_id": "profile_path",
  "role": "role_name"
}
```

### Remove Agent from Swarm

```bash
DELETE /api/v1/swarms/:id/agents/:agent_id
```

---

## Complete Example

Here's a comprehensive example of adding a full travel swarm:

```bash
curl -X POST http://localhost:3000/api/v1/swarms \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Comprehensive Travel Agent",
    "type": "arm_length",
    "arm_length": 5,
    "agents": [
      {
        "profile_id": "booking.com-api",
        "role": "Flight Search Agent",
        "description": "Searches and compares flights using Booking.com API",
        "tools": ["booking_com_flights"]
      },
      {
        "profile_id": "api-six-hotels",
        "role": "Hotel Booking Agent",
        "description": "Searches and compares hotels using API Group Six",
        "tools": ["api_six_hotels"]
      },
      {
        "profile_id": "skyscanner-hotels",
        "role": "Alternative Hotel Agent",
        "description": "Alternative hotel search for price comparison",
        "tools": ["skyscanner_hotels"]
      },
      {
        "profile_id": "tripadvisor-reviews",
        "role": "Travel Review Agent",
        "description": "Gathers reviews and ratings for flights and hotels",
        "tools": ["travel_advisor_api"]
      },
      {
        "profile_id": "multi-agent-reviewer",
        "role": "Itinerary Review Agent",
        "description": "Reviews complete itinerary for quality and logic",
        "tools": ["web_search", "google_places"]
      }
    ]
  }'
```

---

## For Developers

If you want to build a custom integration:

```python
import requests

# Add swarm
response = requests.post(
    'http://localhost:3000/api/v1/swarms',
    json={
        "name": "My Travel Swarm",
        "type": "arm_length",
        "arm_length": 3,
        "agents": [
            {
                "profile_id": "~/.hermes/profiles/agent1/SOUL.md",
                "role": "My Agent Role",
                "description": "Does X, Y, Z",
                "tools": ["tool1", "tool2"]
            }
        ]
    }
)

print(f"Swarm created: {response.json()['swarm_id']}")
```

---

## Getting Help

- Check the detailed documentation: [SWARM-SETUP.md](SWARM-SETUP.md)
- Visit the Hermes Workspace docs: https://hermes-agent.nousresearch.com/docs/workspace/
- Check the Multi-Agent Delegation guide: [MULTI-AGENT-DELEGATION.md](MULTI-AGENT-DELEGATION.md)

---

*Last Updated: May 3, 2026*
