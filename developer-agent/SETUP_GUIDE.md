## Travel Agent Setup Guide

---

## ✅ What Has Been Created

I've created 4 travel agent profiles for you in:

```
/Users/jjordaan/hermes-workspace/profiles/travel-agents/
```

### Created Files:

1. **researcher-soul.md** - Researches flights, hotels, and travel options
2. **designer-soul.md** - Designs comprehensive travel itineraries
3. **developer-soul.md** - Executes bookings and handles transactions
4. **reviewer-soul.md** - Reviews and validates all travel plans
5. **README.md** - Full documentation of the system

---

## 🚀 How to Configure in Hermes Dashboard

### Step 1: Navigate to Profiles

1. Open http://localhost:3000
2. Click **"Profiles"** in the left sidebar

### Step 2: Create New Agents

You'll need to create 5 agents in the swarm (4 roles + 1 repeat reviewer):

#### Agent 1: Researcher
- **Name:** `travel-researcher`
- **Profile:** `researcher`
- **SOUL.md:** Browse to `/Users/jjordaan/hermes-workspace/profiles/travel-agents/researcher-soul.md`
- **Role:** Research

#### Agent 2: Designer
- **Name:** `travel-designer`
- **Profile:** `designer`
- **SOUL.md:** Browse to `/Users/jjordaan/hermes-workspace/profiles/travel-agents/designer-soul.md`
- **Role:** Design

#### Agent 3: Reviewer (Phase 1)
- **Name:** `travel-reviewer-1`
- **Profile:** `reviewer`
- **SOUL.md:** Browse to `/Users/jjordaan/hermes-workspace/profiles/travel-agents/reviewer-soul.md`
- **Role:** Review

#### Agent 4: Reviewer (Phase 2)
- **Name:** `travel-reviewer-2`
- **Profile:** `reviewer`
- **SOUL.md:** Browse to `/Users/jjordaan/hermes-workspace/profiles/travel-agents/reviewer-soul.md`
- **Role:** Review

#### Agent 5: Developer
- **Name:** `travel-developer`
- **Profile:** `developer`
- **SOUL.md:** Browse to `/Users/jjordaan/hermes-workspace/profiles/travel-agents/developer-soul.md`
- **Role:** Booking Execution

---

## 📋 How to Run the Travel Agents

### Option 1: Via Chat Interface

1. Create a new session
2. Select the "Travel Agents" swarm
3. Send your travel request:

```
I want to travel from New York to Tokyo
Dates: June 15 to June 25
Budget: $3000
Preferences: First class, luxury hotels, include day trips
```

### Option 2: Via Sequential Mode

1. Select Researcher agent
2. Send your request
3. Wait for research results
4. Select Designer agent
5. Send "Research results received, design itinerary"
6. Continue through each agent

---

## 🔄 How the Agents Work Together

### Example Flow:

**User:** "Book me a trip to Paris, 5 days, $2000 budget"

**Researcher:** Researches flights, hotels, activities
→ Presents 3-5 options for each category

**Reviewer 1:** Reviews research quality
→ Approves or requests more research

**Designer:** Creates detailed itinerary
→ Day-by-day schedule with activities

**Reviewer 2:** Validates the itinerary
→ Checks timing, budget, feasibility
→ Approves for booking

**Developer:** Executes bookings
→ Books flights, hotels, activities
→ Sends confirmations

---

## ⚙️ Important Configuration

### Sequential Execution
All agents are configured to run **sequentially**, not in parallel. This means:

```
Researcher → Reviewer → Designer → Reviewer → Developer
```

Each agent must complete before the next starts.

### Model Configuration
- Model: `apple/omlx/qwen`
- Iterations: 120 (each agent)
- Sequential: `true`

These are already set in your `swarm.yaml`.

---

## 🛠️ API Integration (For Developer Agent)

To enable actual bookings, you need to configure APIs:

### Required APIs:

1. **Flight Booking API**
   - Example: Sabre, Amadeus, or Duffel API
   - Endpoint: POST /bookings/flights

2. **Hotel Booking API**
   - Example: Booking.com API, Expedia, or Amadeus
   - Endpoint: POST /bookings/hotels

3. **Payment API**
   - Example: Stripe, PayPal
   - For processing payments

### How to Configure:

In the `developer-soul.md`, locate the section about tools:

```markdown
#### Tools (API Configuration Needed)
- Flight booking API: [ADD ENDPOINT AND KEYS]
- Hotel booking API: [ADD ENDPOINT AND KEYS]
- Payment API: [ADD ENDPOINT AND KEYS]
```

Add your API keys and endpoints there.

---

## 🧪 Testing

Start with a simple test:

```
I want to travel from NYC to Boston, 2 days, $1000 budget
Just give me research and itinerary, no booking yet
```

This tests the Researcher and Designer agents without needing API keys.

---

## 📊 Monitoring

Use the Hermes Dashboard (http://localhost:9119) to:

1. View agent execution status
2. Check iteration progress
3. Monitor API calls
4. View errors and logs

---

## 🔧 Troubleshooting

### Agents Not Running

1. Check if Hermes Workspace is running:
   ```bash
   curl http://localhost:3000
   ```

2. Check workspace logs:
   ```bash
   tail -f ~/hermes-workspace/logs/*.log
   ```

### Agents Running but No Output

1. Verify SOUL.md files are properly formatted
2. Check model connectivity:
   ```bash
   curl http://localhost:3000/api/models
   ```

3. Check if agent has required permissions:
   - Add to your user role in dashboard

### Sequential Execution Too Slow

1. Check if agents are actually running one at a time
2. Reduce iterations if 120 is too slow
3. Review if agents need to complete all before passing to next

---

## 📝 Tips for Best Results

1. **Be Specific:** Include dates, budget, preferences
2. **Flexible:** Give the system options to choose
3. **Review Output:** Check results before proceeding
4. **Clear Boundaries:** Tell the system when to stop researching and start designing

---

## 🎯 Next Steps

1. ✅ **Test the agents** with a simple travel request
2. 🔧 **Configure APIs** if you want real bookings
3. 📊 **Monitor performance** through the dashboard
4. 🔄 **Iterate on SOUL.md** files based on actual usage
5. 🏗️ **Build additional agents** if needed (e.g., specialized destination experts)

---

## 📞 Support

If you encounter issues:

1. Check the `profiles/travel-agents/README.md` for full documentation
2. Review agent SOUL.md files for role-specific guidance
3. Check Hermes Workspace logs for errors

---

## 🎉 You're Ready!

Your travel agent system is configured and ready to use. You can now:

- Create travel itineraries
- Research flight and hotel options
- Design comprehensive schedules
- Execute bookings (once APIs are configured)

Have a great trip planning experience! ✈️🗺️