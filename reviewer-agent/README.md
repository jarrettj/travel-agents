## 🚀 Travel Agent System - Overview

**Purpose:** A multi-agent travel planning system using Hermes Workspace

**Architecture:** Sequential execution with 4 specialized agents

---

## Agents Overview

### 1. Researcher Agent
- **Purpose:** Research flights, hotels, and travel options
- **SOUL.md:** `researcher-soul.md`
- **Key Tasks:**
  - Search for flight options
  - Search for hotel accommodations
  - Compare prices and features
  - Research activities and attractions
  - Check visa requirements
  - Present multiple recommendations

### 2. Designer Agent
- **Purpose:** Design comprehensive travel itineraries
- **SOUL.md:** `designer-soul.md`
- **Key Tasks:**
  - Create day-by-day schedules
  - Design visual layouts
  - Plan transportation between locations
  - Schedule activities and experiences
  - Create packing lists
  - Generate budget breakdowns

### 3. Developer Agent
- **Purpose:** Execute bookings and handle transactions
- **SOUL.md:** `developer-soul.md`
- **Key Tasks:**
  - Book flights via APIs
  - Book hotel accommodations
  - Book activities and experiences
  - Process payments
  - Generate confirmations
  - Manage user travel profiles

### 4. Reviewer Agent
- **Purpose:** Review and validate travel plans
- **SOUL.md:** `reviewer-soul.md`
- **Key Tasks:**
  - Validate research findings
  - Check itinerary feasibility
  - Verify budget allocations
  - Review booking confirmations
  - Approve or request modifications

---

## Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    TRAVEL PLANNING WORKFLOW                 │
└─────────────────────────────────────────────────────────────┘

User Input → Researcher → Reviewer → Designer → Reviewer → Developer
              ↓           ↓          ↓          ↓           ↓
         Research    Validate    Design    Validate    Execute
          (Phase 1)   (Review)    (Phase 2)  (Review)   (Booking)
```

### Phase 1: Research & Design
1. **Researcher** gathers options and recommendations
2. **Designer** creates itinerary based on research
3. **Reviewer 1** validates the plan
4. If issues found: **Researcher** refines, loop back to step 1

### Phase 2: Booking Execution
5. **Reviewer 2** gives final approval
6. **Developer** executes bookings
7. Send confirmations to user

---

## How to Use in Hermes Workspace

### Step 1: Configure the Agents

1. Open Hermes Workspace: http://localhost:3000
2. Click "Swarm" in the sidebar
3. Create a new Swarm for "Travel Agents"

### Step 2: Add Agents to the Swarm

Add these 4 agents in sequence:

**Agent 1: Researcher**
- SOUL.md: `profiles/travel-agents/researcher-soul.md`
- Role: Research
- Model: apple/omlx/qwen
- Iterations: 120

**Agent 2: Designer**
- SOUL.md: `profiles/travel-agents/designer-soul.md`
- Role: Design
- Model: apple/omlx/qwen
- Iterations: 120

**Agent 3: Reviewer (Phase 1)**
- SOUL.md: `profiles/travel-agents/reviewer-soul.md`
- Role: Review
- Model: apple/omlx/qwen
- Iterations: 120

**Agent 4: Reviewer (Phase 2)**
- SOUL.md: `profiles/travel-agents/reviewer-soul.md`
- Role: Review
- Model: apple/omlx/qwen
- Iterations: 120

**Agent 5: Developer**
- SOUL.md: `profiles/travel-agents/developer-soul.md`
- Role: Booking Execution
- Model: apple/omlx/qwen
- Iterations: 120

### Step 3: Run the Swarm

Enter your travel request:

```
I want to travel from [origin] to [destination]
Dates: [departure date] to [return date]
Budget: $[amount]
Preferences: [any specific requirements]
```

The system will:
1. Research options
2. Design itinerary
3. Review and refine (if needed)
4. Final review
5. Execute bookings

---

## Important Notes

### Sequential Execution
- Agents run in series, not parallel
- Each agent must complete before the next starts
- This ensures proper handoff and validation

### Iterations
- Each agent runs 120 iterations
- Allows thorough exploration of options
- Reviewer can loop back for refinements

### Model Configuration
- All agents use `apple/omlx/qwen` model
- Set globally in `swarm.yaml`

### API Integration
- Researcher: Web search for initial options
- Developer: Requires API keys for actual booking
  - Flight booking API
  - Hotel booking API
  - Payment processing API

---

## Files Created

All agent configurations are stored in:

```
/Users/jjordaan/hermes-workspace/profiles/travel-agents/
├── researcher-soul.md
├── designer-soul.md
├── developer-soul.md
└── reviewer-soul.md
```

---

## Testing & Verification

### Test Scenarios

1. **Simple Round Trip**
   - Origin: JFK
   - Destination: LAX
   - Dates: 7 days
   - Budget: $2000

2. **International Trip**
   - Origin: JFK
   - Destination: Tokyo
   - Dates: 10 days
   - Budget: $3000
   - Include: Hotels, activities, flights

3. **Multi-City Trip**
   - Cities: NYC → Boston → DC
   - Dates: 5 days
   - Budget: $2500
   - Include: Flights, hotels, activities

### Expected Behavior

✅ Researcher finds multiple options
✅ Designer creates detailed itinerary
✅ Reviewer validates everything
✅ Developer books everything (once APIs are configured)
✅ User receives all confirmations

---

## Next Steps

1. **Test the workflow** with a simple travel request
2. **Configure APIs** for the Developer agent to execute bookings
3. **Monitor the agents** through the Hermes Dashboard
4. **Iterate on SOUL.md files** based on actual usage

---

## Contact & Support

For issues or questions about the travel agents:
- Check the Hermes Workspace logs
- Review agent SOUL.md configurations
- Contact the development team

---

Created: May 2025
Version: 1.0