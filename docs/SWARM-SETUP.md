# Travel Agent Swarm Setup Documentation

## Current Status: UI Issue

**Date:** May 3, 2026
**Issue:** The "Add Swarm" button in Hermes Workspace is not functional - clicking it does not open a modal or form for creating new swarms.

### Observed Behavior

When attempting to add a new swarm:

1. User clicks "Add Swarm" button (top right)
2. No modal dialog appears
3. No input form is presented
4. Existing swarms remain unchanged

This appears to be a **UI bug** in the current version of Hermes Workspace.

---

## Intended Workflow

The interface is designed to support the following workflow:

### 1. Click "Add Swarm" Button
   - Located at the top right of the Swarm page
   - Should open a modal dialog

### 2. Fill in Swarm Configuration Form

The form should include these fields:

```yaml
Name: [swarm_name]         # e.g., "Travel-Agent-Swarm"
Type: [arm_length]         # e.g., "arm_length" or "hub_and_spoke"
Arm Length: [number]       # e.g., 3, 5, or more agents
```

### 3. Add Agents to the Swarm

For each agent in the swarm, you would:

a) **Select or Create a Profile**
   - Choose from existing profiles in `~/.hermes/profiles/`
   - Or upload/create a new SOUL.md

b) **Configure Role/Purpose**
   - Define the agent's responsibilities
   - e.g., "Flights agent handles flight booking and searches"

c) **Set Capabilities**
   - List tools/APIs the agent should have access to

### 4. Provision the Swarm

After filling the form:
- Click "Create" or "Add"
- System should create the swarm
- Workers should transition from "not provisioned" to "provisioned"
- Agents should start and be available for missions

---

## API Endpoint (For Programmatic Access)

The proper way to add swarms (bypassing the broken UI) is via API:

### Add Swarm Request

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
        "role": "Flight Booking Agent",
        "description": "Handles flight searches and bookings",
        "tools": ["skyscanner_api", "api_six", "booking_com_api"]
      },
      {
        "profile_id": "travel-agent-nights",
        "role": "Accommodation Agent",
        "description": "Handles hotel/nights bookings",
        "tools": ["booking_com_api", "agoda_api"]
      },
      {
        "profile_id": "travel-agent-reviews",
        "role": "Review Agent",
        "description": "Reviews itinerary quality",
        "tools": ["travel_advisor_api", "airbnb_reviews"]
      }
    ]
  }'
```

### Response

On success, the API should return:

```json
{
  "swarm_id": "swarm_travel_001",
  "status": "provisioning",
  "agents": [
    {
      "agent_id": "agent_001",
      "role": "Flight Booking Agent",
      "status": "provisioned"
    }
  ]
}
```

---

## Manual Setup via Configuration

If the UI and API are both unavailable, you can manually add swarms by editing the configuration:

### 1. Create Agent Profiles

Each agent needs a SOUL.md file in `~/.hermes/profiles/`:

```bash
mkdir -p ~/.hermes/profiles/
```

Then create individual agent profiles (example structure):

```bash
# Travel Booking Agent
mkdir -p ~/.hermes/profiles/travel-agent-booking
cat > ~/.hermes/profiles/travel-agent-booking/SOUL.md << 'EOF'
[{"role": "Flights Agent", "desc": "Handles flight booking searches", "domain": "travel"}, {"role": "Hotels Agent", "desc": "Handles accommodation booking", "domain": "travel"}]
[{"tools": ["skyscanner_api", "api_six", "booking_com_api", "agoda_api"], "name": "Travel Agent Toolkit"}]
EOF
```

### 2. Register in Hermes Config

Edit `~/.hermes/config.yaml`:

```yaml
# Add new worker profiles
profiles:
  travel-agent-booking:
    path: ~/travel-agents/profiles/travel-agent-booking/SOUL.md
    agent_role: "Flight/Hotel Booking"
    api_keys:
      - name: SKYSCANNER
        value: ${SKYSCANNER_API_KEY}
      - name: BOOKINGCOM
        value: ${BOOKINGCOM_API_KEY}
  travel-agent-reviews:
    path: ~/travel-agents/profiles/travel-agent-reviews/SOUL.md
    agent_role: "Itinerary Review"
```

### 3. Register in Travel-Agents Workspace Config

Edit `~/travel-agents/workspace.yml`:

```yaml
name: Travel Agent Swarm
type: arm_length
arm_length: 3

agents:
  - name: flight-booking
    role: Flight Booking Agent
    profile_ref: travel-agent-booking
    capabilities:
      - search_flights
      - book_flights
      - compare_prices
  
  - name: hotel-booking
    role: Hotel Booking Agent
    profile_ref: travel-agent-booking
    capabilities:
      - search_hotels
      - book_hotels
      - check_availability
  
  - name: itinerary-reviewer
    role: Review Agent
    profile_ref: travel-agent-reviews
    capabilities:
      - validate_itinerary
      - check_timings
      - review_prices
```

### 4. Provision the Swarm

Then provision:

```bash
cd ~/travel-agents
hermes workspace provision
```

---

## Recommended Agent Structure

For a comprehensive travel booking system, I recommend this swarm structure:

### Swarm: `Travel-Agent-Swarm` (Arm Length: 3)

| Agent | Role | Responsibilities | Tools |
|-------|------|------------------|-------|
| Flight Agent | Flight Booking & Search | Search flights, compare prices, book flights | Skyscanner, API Group Six, Booking.com |
| Hotel Agent | Accommodation Booking | Search hotels, compare prices, book stays | Booking.com, Agoda |
| Review Agent | Quality Assurance | Review itineraries, validate flights + hotels, check logic | TravelAdvisor, Review Aggregation |

### Alternative: Extended Swarm (Arm Length: 5)

| Agent | Role | Responsibilities | Tools |
|-------|------|------------------|-------|
| Flight Agent | Flights | Search, compare, book flights | Skyscanner, API Group Six |
| Hotel Agent | Hotels | Search, compare, book hotels | Booking.com, Agoda |
| Car Rental Agent | Car Rentals | Search, compare, book car rentals | Rentalcars, Expedia |
| Itinerary Planner | Planning | Create day-by-day itinerary | Travel Planner Tools |
| Review Agent | QA | Review entire travel plan | TravelAdvisor, Multiple Sources |

---

## API Keys Setup

Set environment variables for the required APIs:

```bash
# Skyscanner (Search Engine)
export SKYSCANNER_API_KEY="your_key"

# API Group Six (Hotels + Flights)
export SIX_REDIS_HOST="your_redis_host"
export SIX_REDIS_USER="your_user"
export SIX_REDIS_PASSWORD="your_password"

# Booking.com (Hotels)
export BOOKINGCOM_API_KEY="your_key"

# Agoda (Hotels)
export AGODA_API_KEY="your_key"

# Load into config
~/.hermes/config.yaml
```

---

## Troubleshooting

### Issue: "Not Provisioned Yet" Status

**Symptom:** Agents show as "not provisioned yet" even after clicking "Add Swarm"

**Causes:**
1. API keys not configured
2. Profile paths incorrect
3. Backend server not running
4. Workspace not properly registered

**Solutions:**
```bash
# 1. Check API keys
echo "SKYSCANNER_API_KEY: $SKYSCANNER_API_KEY"

# 2. Verify profile paths
ls -la ~/.hermes/profiles/travel-agent-booking/

# 3. Start backend server
cd ~/travel-agents
python -m uvicorn travel_agents.api:app --host 0.0.0.0 --port 8000

# 4. Provision workspace
hermes workspace provision
```

### Issue: "Agent already exists" Error

**Symptom:** Cannot add agent with same role/name

**Solution:** Use unique names for each agent instance

### Issue: Modal doesn't appear

**Symptom:** Clicking "Add Swarm" button does nothing

**Current Status:** This is a known UI bug. Use API or manual config instead.

**Workarounds:**
1. Use the API endpoint directly (see above)
2. Edit config files manually
3. Use the API CLI tool (if available)

---

## Next Steps

1. [ ] Fix the "Add Swarm" UI modal
2. [ ] Document API usage
3. [ ] Create quick-start guide
4. [ ] Add validation for required fields
5. [ ] Implement auto-save for swarm configurations

---

## References

- [Multi-Agent Delegation Guide](./MULTI-AGENT-DELEGATION.md)
- [Hermes Agent Profiles](https://hermes-agent.nousresearch.com/docs/agent/)
- [Hermes Workspace: Managing Swarms](https://hermes-agent.nousresearch.com/docs/workspace/)

---

*Document Version: 1.0*
*Last Updated: May 3, 2026*
