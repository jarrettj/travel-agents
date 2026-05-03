# Travel Agent Swarm - Setup Checklist

Use this checklist to set up the Travel Agent swarm.

## Phase 1: Agent Configuration ✓

- [x] Created `travel-agent-orchestrator` with proper runtime.json
- [x] Created `travel-agent-researcher` with proper runtime.json  
- [x] Created `travel-agent-designer` with proper runtime.json
- [x] Created `travel-agent-developer` with proper runtime.json
- [x] Created `travel-agent-reviewer` with proper runtime.json

## Phase 2: Duplicate Removal ✓

- [x] Removed generic `developer` agent
- [x] Removed generic `researcher` agent
- [x] Removed generic `designer` agent
- [x] Removed generic `reviewer` agent
- [x] Kept only travel-specific versions

## Phase 3: Swarm Configuration ✓

- [x] Created `~/.hermes/swarms/travel.json`
- [x] Defined agent handoff chain
- [x] Added API endpoints
- [x] Added required environment variables

## Phase 4: Documentation ✓

- [x] Created `QUICKSTART.md` - 5-minute setup guide
- [x] Created `SETUP-SWARM.md` - comprehensive setup instructions
- [x] Pushed to GitHub repository

## Phase 5: Starting the Swarm

### Step 1: Ensure Environment Variables

Create or update `~/.hermes/.env`:

```env
# Skyscanner API - Flight searches
SKYSCANNER_API_KEY="your-skyscanner-api-key"

# Booking.com API - Hotel bookings
BOOKINGCOM_API_KEY="your-booking-com-api-key"

# Payment processing - Stripe
STRIPE_API_KEY="your-stripe-secret-key"

# For development mode (optional)
TRAVEL_AGENCY_MODE="true"
```

### Step 2: Start the Workspace

```bash
cd ~/.hermes

# Start Hermes
hermes workspace start

# Use travel workspace
hermes workspace use travel

# Verify agents loaded
hermes workspace list
```

Expected output:
```
Available Workspaces:
  └─ Travel (5 agents)
     ├─ Travel Orchestrator
     ├─ Travel Researcher
     ├─ Travel Designer
     ├─ Travel Developer
     └─ Travel Reviewer
```

### Step 3: Add Swarm to UI (Web Interface)

1. Open browser: `http://localhost:3000`
2. Click **"Swarms"** in left sidebar
3. Click **"Add Swarm"** button
4. Enter name: `travel`
5. Select all 5 agents from the dropdown

### Step 4: Provision the Agents

```bash
cd ~/.hermes

# Provision all agents
hermes swarm provision travel
```

Expected output:
```
✅ Travel Swarm created
✅ 5 agents provisioned
```

### Step 5: Start Your First Mission

#### Via Browser (Recommended):

1. Click **"New Mission"**
2. Select **"Multi-Agent Swarm"** mode
3. Choose **"travel"** from the swarm dropdown
4. Enter mission:

```
Research flight and hotel booking APIs
Focus on Skyscanner, Booking.com, and Airbnb APIs
Include: endpoints, rate limits, pricing models
```

5. Click **"Start Mission"**

#### Via CLI:

```bash
hermes mission start \
  --mode swarm \
  --swarm travel \
  --mission "Research flight and hotel booking APIs"
```

## Phase 6: Verify Everything Works

### Check Agent Status

```bash
hermes agent status
```

Expected: All 5 agents should be "active" or "idle"

### Check Mission Progress

Open browser at `http://localhost:3000` → **Missions** → View your mission

### Check Handoffs

The agents should hand off automatically:

```
Orchestrator → Researcher → Designer → Developer → Reviewer → Orchestrator
```

## Phase 7: Configure Production (Optional)

### Add More Agents

Create additional travel-specific agents:

```bash
# Example: Price Comparison Agent
mkdir ~/.hermes/profiles/travel-agent-price-comparator

# Copy from template
cp ~/.hermes/profiles/travel-agent-*/SOUL.md ~/.hermes/profiles/travel-agent-price-comparator/

# Edit for price comparison role
# Edit runtime.json
```

### Configure Webhooks

```yaml
# In swarm config
webhooks:
  booking_completed: "https://your-app.com/webhooks/booking"
  price_change: "https://your-app.com/webhooks/price-alerts"
  status_change: "https://your-app.com/webhooks/status"
```

## Troubleshooting

### Problem: "Agent not found"

**Solution:**
```bash
# Re-provision the specific agent
hermes swarm provision travel --agent "travel-agent-<name>"

# If still not working
rm ~/.hermes/swarms/travel.json
hermes workspace add
```

### Problem: "Handoff failed"

**Solution:**

1. Check checkpoint compatibility:
```bash
hermes checkpoint list --agent "travel-agent-researcher"
hermes checkpoint list --agent "travel-agent-designer"
```

2. Ensure the output format of one matches the input of the next

### Problem: "API key missing"

**Solution:**
```bash
# Add to ~/.hermes/.env
export SKYSCANNER_API_KEY="your-key"

# Restart the agent
hermes agent restart --agent "travel-agent-researcher"
```

### Problem: "Agent stuck in loop"

**Solution:**
```bash
# Force complete current task
hermes agent complete --agent "travel-agent-<name>"

# Or skip to next agent
hermes handoff --target "travel-agent-designer"
```

## Example Workflows

### Workflow 1: New Booking Request

```
User requests: Book flight from NYC to London for 2 people

1. Researcher: Check available APIs for flight booking
2. Designer: Create booking interface based on available APIs
3. Developer: Build booking API with payment integration
4. Reviewer: Test booking flow and validate payment
5. Orchestrator: Deploy to production

Result: Fully functional booking system ready for user
```

### Workflow 2: API Integration

```
New API available: Amadeus

1. Researcher: Analyze Amadeus API documentation
2. Designer: Create integration endpoints in API design
3. Developer: Implement API client and server endpoints
4. Reviewer: Test integration with Amadeus sandbox
5. Orchestrator: Update travel platform with new API

Result: Travel platform now supports Amadeus bookings
```

## Resources

- **Quick Start**: [QUICKSTART.md](./QUICKSTART.md)
- **Full Setup**: [SETUP-SWARM.md](./SETUP-SWARM.md)
- **API Reference**: [docs/API-REFERENCE.md](./docs/API-REFERENCE.md)
- **Agent Docs**: [docs/agents/](./docs/agents/)

## Support

- Email: support@travelagency.example.com
- Slack: #travel-agents
- GitHub Issues: https://github.com/jarrettj/travel-agents/issues
