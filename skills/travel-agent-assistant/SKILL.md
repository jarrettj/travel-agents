---
name: travel-agent-assistant
category: autonomous-ai-agents
description: Travel-specific assistant skill that provides domain knowledge and guidance to LLM agents working on travel booking tasks
trigger: user needs assistance with travel planning, booking, or any travel-related LLM agent workflows
---

# Travel Agent Assistant

A domain-specific assistant skill that helps LLM agents with travel booking tasks, providing knowledge about travel APIs, booking workflows, destination insights, and common pitfalls.

## Purpose

This skill assists **any LLM agent** (not just travel agents) with:
- Travel API knowledge and integration patterns
- Booking workflow orchestration
- Destination and itinerary planning
- Budget estimation and optimization
- Travel documentation and compliance
- Common errors and troubleshooting

## When to Use

Load this skill when:
- Agent needs to research travel destinations or APIs
- Agent is building booking integrations
- Agent needs to plan itineraries
- Agent encounters travel-related tasks
- Agent needs travel-specific domain knowledge

## Travel APIs & Services Overview

### Flight Booking APIs

| Service | Type | Key Features | Notes |
|---------|------|--------------|-------|
| **Skyscanner** | Meta-search | Global coverage, flexible dates, price alerts | Good for comparing multiple providers |
| **Expedia** | Provider | Full service (flights, hotels, packages) | Good for US domestic/international |
| **Travelocity** | Provider | Flexible booking, packages | Established brand |
| **Priceline** | Provider | Express deals, non-refundable | Good for budget travelers |
| **Kayak** | Meta-search | Price tracking, hotel finder | Comprehensive comparison |

### Hotel Booking APIs

| Service | Type | Key Features | Notes |
|---------|------|--------------|-------|
| **Booking.com** | Provider | Free cancellation, extensive inventory | Popular worldwide |
| **Hotels.com** | Provider | Loyalty program, last-minute deals | Good for business travelers |
| **Agoda** | Provider | Asia-focused, best price guarantee | Great for Asian destinations |

### Activity & Experience APIs

| Service | Type | Features |
|---------|------|----------|
| Viator | Aggregator | Tours, activities, attractions |
| GetYourGuide | Aggregator | Experiences, day tours, skip-the-line |
| Experience Days | Provider | UK/Europe focused, curated experiences |

### Payment Gateways

| Service | Features | Integration |
|---------|----------|-------------|
| **Stripe** | PCI compliant, fraud detection, refunds | REST API, webhooks |
| **Braintree** | PayPal integration, recurring payments | SDKs for multiple platforms |
| **Adyen** | Enterprise-grade, multiple methods | Complete payment solution |

### Travel Compliance & Requirements

| Requirement | Resources | Agent Actions |
|-------------|-----------|---------------|
| **Visa requirements** | [Travel.State.Gov](https://www.travel.state.gov), [IATA Visa Check](https://iata.org/what-we-offer/iata-go-visit/) | Agent should check before recommending |
| **ESTA (USA)** | [esta.cbp.dhs.gov](https://esta.cbp.dhs.gov) | Auto-check for US travel |
| **ETA (Canada)** | [ice.canada.ca](https://www.ice.canada.ca) | Auto-check for Canada travel |
| **Passport validity** | [usa.gov/passport](https://www.usa.gov/passport) | Check 6-month rule for international |
| **Insurance requirements** | [hic.coverage](https://hic.coverage), [Travel Insured](https://www.travelinsured.com) | Recommend for international travel |

## Common Travel Booking Workflows

### 1. Simple Booking (Single Flight)

```
┌─────────────────────────────────────────────────────────────┐
│ User Request: "Book me a flight from NYC to London, June 1" │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ 1. Agent analyzes request:                                  │
│    - Origin: NYC (JFK/LGA/EWR)                              │
│    - Destination: London (LHR/GAT/STN)                     │
│    - Date: June 1, 2025                                    │
│    - Passengers: Not specified → Ask or assume 1 adult      │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Research phase (multiple APIs):                          │
│    - Search flights via Skyscanner                         │
│    - Search flights via Expedia                            │
│    - Get price estimates                                   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Present options to user:                                 │
│    - Flight number, times, duration, price, airline         │
│    - Ask: "Would you like me to book the cheapest option?"  │
└─────────────────────────────────────────────────────────────┘
                              ↓ (if confirmed)
┌─────────────────────────────────────────────────────────────┐
│ 4. Booking phase:                                           │
│    - Collect passenger details                              │
│    - Enter payment information                              │
│    - Process booking via provider API                       │
│    - Return confirmation number                             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. Post-booking:                                            │
│    - Send confirmation email                               │
│    - Set reminders (if enabled)                             │
│    - Add to calendar                                        │
└─────────────────────────────────────────────────────────────┘
```

### 2. Complete Travel Package

```
Booking Package Workflow:
1.  Research flights (multiple dates, airports)
2.  Research hotels (based on flight landing, preferences)
3.  Research activities (based on dates, location, interests)
4.  Research transportation (airport transfers, local transit)
5.  Compile budget estimate
6.  Present full package to user
7.  Get approval
8.  Execute bookings (one by one or bulk if supported)
9.  Create itinerary document
10. Send all confirmations
```

### 3. Multi-City Itinerary

```
Example: London → Paris → Rome → Milan → London

Agent Tasks:
1. Research connections between all cities
2. Book each leg of journey separately (usually cheaper)
3. Optimize route order for cost/time
4. Create day-by-day itinerary with transfer times
5. Check visa requirements for each country
6. Book accommodations in each city
```

## Destination Knowledge Database

### Popular Destinations (with key info)

#### London, UK
- **Best time to visit:** April-June, September-October
- **Average temperature:** 10-20°C (summer), 5-10°C (winter)
- **Must-see:** British Museum, Tower of London, Westminster Abbey
- **Transport:** Heathrow (LHR) - Oyster card, TfL Rail
- **Budget:** $150-250/day (mid-range)

#### Tokyo, Japan
- **Best time to visit:** March-May (spring), October-November (autumn)
- **Visa:** 90 days for US/UK/EU tourists (visa-free)
- **Must-see:** Shibuya Crossing, Senso-ji Temple, teamLab Planets
- **Transport:** Narita/Haneda, Suica/Pasmo IC cards
- **Budget:** $200-400/day (mid-range)

#### Paris, France
- **Best time to visit:** April-June, September-October
- **Visa:** Schengen rules apply (90/180 day limit)
- **Must-see:** Eiffel Tower, Louvre, Notre-Dame
- **Transport:** CDG/Orly, Metro, RER A
- **Budget:** $180-300/day (mid-range)

## Booking API Integration Patterns

### Pattern 1: Meta-Search (Recommended for Initial Booking)

```python
# Strategy: Use multiple providers, pick best option

api_comparison_results = []

# 1. Query Skyscanner
skyscanner_response = search_flights_api(
    origin="JFK",
    destination="LHR",
    departure_date="2025-06-01",
    passengers=1
)
api_comparison_results.append({
    "provider": "Skyscanner",
    "price": skyscanner_response["price"],
    "options": skyscanner_response["flights"]
})

# 2. Query Expedia (add more providers as needed)
expedia_response = search_flights_api(
    origin="JFK",
    destination="LHR",
    departure_date="2025-06-01",
    passengers=1,
    provider="expedia"
)
api_comparison_results.append({
    "provider": "Expedia",
    "price": expedia_response["price"],
    "options": expedia_response["flights"]
})

# 3. Filter and sort by criteria
filtered_options = filter_results(
    api_comparison_results,
    max_price=1000,
    duration_hours=9.0,
    min_rating=4.0
)

# 4. Present best options to user
present_options(filtered_options[:5], user_preferences)
```

### Pattern 2: Direct Provider Booking

```python
# Strategy: Book directly through airline/hotel APIs

# 1. Get airline partner IDs
airline_id = get_airline_by_iata("BA")  # British Airways

# 2. Search via airline's GDS or direct API
search_response = airline_api.search_flights(
    origin_code="JFK",
    destination_code="LHR",
    departure_date="2025-06-01",
    passenger_count=1,
    cabin_class="economy"
)

# 3. Book selected flight
booking_ref = airline_api.create_booking(
    itinerary=search_response["selected_option"]["itinerary"],
    passenger_details=passenger_details,
    payment_info=payment_info
)

# 4. Confirm booking
confirmation = airline_api.confirm_booking(
    booking_ref=booking_ref,
    passenger_details=passenger_details
)
```

### Pattern 3: Booking Engine Pattern

```python
# For complex bookings with multiple steps

def execute_booking_workflow(user_request):
    """Execute multi-step booking workflow"""
    
    # Step 1: Parse request
    parsed = parse_travel_request(user_request)
    
    # Step 2: Research phase
    research_results = research_travel_components(parsed)
    
    # Step 3: Design itinerary
    itinerary = design_travel_itinerary(research_results, user_preferences)
    
    # Step 4: Validation
    validation_report = validate_itinerary(itinerary)
    
    # Step 5: Execute bookings (if approved)
    if validation_report["status"] == "approved":
        bookings = []
        
        # Book flights
        flight_bookings = book_flights(itinerary["flights"])
        bookings.append(flight_bookings)
        
        # Book hotels
        hotel_bookings = book_hotels(itinerary["hotels"])
        bookings.append(hotel_bookings)
        
        # Book activities
        activity_bookings = book_activities(itinerary["activities"])
        bookings.append(activity_bookings)
        
        return compile_booking_summary(bookings)
    
    else:
        return validation_report["recommendations"]
```

## Budget Estimation Guidelines

### Flight Cost Estimators

| Route Type | One-Way | Round-Trip |
|------------|---------|------------|
| Domestic (US) | $200-500 | $400-1000 |
| Continental (within Americas) | $300-600 | $600-1200 |
| Transcontinental (US-Europe) | $400-800 | $800-1600 |
| Long-haul (US-Asia) | $600-1200 | $1200-2400 |
| Ultra-long-haul (US-Oceania) | $900-1800 | $1800-3600 |

### Hotel Cost Estimators

| Category | US/Europe | Asia | Middle East |
|----------|-----------|------|-------------|
| Budget | $50-100/night | $30-80/night | $60-120/night |
| Mid-range | $100-250/night | $80-200/night | $150-300/night |
| Luxury | $250-600/night | $200-500/night | $300-800/night |

### Activity Cost Estimators

| Activity Type | Typical Cost |
|---------------|--------------|
| Museum entry | $15-30 |
| Skip-the-line tour | $50-150 |
| City walking tour | $20-50 |
| Full-day tour | $80-300 |
| Premium experience | $200-800 |

## Common Travel Booking Errors

### Error 1: Currency Mismatch

```
❌ Problem: API returns prices in different currencies
   - Skyscanner: GBP for UK searches
   - Expedia: USD for US searches
   - Agoda: THB for Thailand

✅ Solution:
   1. Always specify currency parameter in API calls
   2. Use exchange rate API to normalize all prices to user's currency
   3. Display original price + converted price
```

### Error 2: Date Format Conflicts

```
❌ Problem: Different APIs use different date formats
   - Some: YYYY-MM-DD
   - Some: DD/MM/YYYY
   - Some: MM/DD/YYYY

✅ Solution:
   1. Standardize internally to ISO 8601 (YYYY-MM-DD)
   2. Convert to API-specific format before each call
   3. Store user's preferred date format
```

### Error 3: Time Zone Confusion

```
❌ Problem: Agent searches for 6:00 PM but API returns local time
   - Searches NYC time, gets results in destination time

✅ Solution:
   1. Always specify timezone in API calls (e.g., "America/New_York")
   2. Convert departure/arrival times to user's timezone
   3. Show both local time and user's time
```

### Error 4: Invalid Airport Codes

```
❌ Problem: User says "New York" but agent searches "LGA"
   - JFK, LGA, and EWR are all valid NYC airports

✅ Solution:
   1. Map city names to major airport hub
   2. When searching, use all major airports in city
   3. Present options clearly labeled with airport codes
```

## Travel Compliance Checklist

Before recommending any international trip, agent should verify:

### Passport Requirements
- [ ] User's passport is valid (at least 6 months beyond travel dates)
- [ ] User has the right type of passport (regular vs. diplomatic)
- [ ] User needs an e-Passport for automated border control

### Visa Requirements
- [ ] Check destination country's visa requirements for user's citizenship
- [ ] If visa required, provide link to apply
- [ ] Note processing time (can take weeks for some countries)

### Entry Requirements
- [ ] Return ticket required?
- [ ] Proof of funds required?
- [ ] Hotel booking confirmation required?
- [ ] Vaccination certificate required?

### Airline Specific Rules
- [ ] Some airlines require visa before booking
- [ ] Some have citizenship restrictions for certain routes
- [ ] Unaccompanied minor policies for children

## Destination-Specific Pitfalls

### Southeast Asia (Thailand, Vietnam, Singapore, etc.)

```
⚠️ Pitfall: Multiple currency traps
   - Many places accept USD but give you poor exchange rate
   - Always pay in local currency
   - ATMs often have high foreign transaction fees

⚠️ Pitfall: Tourist tax not included in bookings
   - Thailand: 200 THB (~$5) per person for international flights
   - Not typically shown in search results

✅ Recommendation:
   - Tell user to budget +$5-10 per person for tourist taxes
   - Use local currency when paying
   - Use credit cards with no foreign transaction fees
```

### Europe (Schengen Area)

```
⚠️ Pitfall: 90/180 day visa rules
   - Non-EU citizens can stay up to 90 days in 180-day period
   - The clock starts from first entry
   - Crossing out of Schengen resets the counter

⚠️ Pitfall: Border crossing documentation
   - Even for short stays, need to show return tickets
   - Border guards may ask about purpose of visit
   - Insurance with medical coverage recommended

✅ Recommendation:
   - Check if user is a Schengen visa national
   - Confirm total planned days in Schengen area
   - Remind user to check visa validity before travel
```

### Middle East

```
⚠️ Pitfall: Dress code requirements
   - Dubai/Abu Dhabi: Conservative dress required (knees/elbows covered)
   - Public beaches have specific times (usually after 4 PM)

⚠️ Pitfall: Alcohol regulations
   - Dubai: Alcohol license required (though hotels have permitted areas)
   - Saudi Arabia: Alcohol is prohibited

✅ Recommendation:
   - Set expectations about dress code for destinations
   - Inform about alcohol availability
   - Suggest licensed venues (hotels, licensed bars)
```

## Booking Confirmation Management

### What Every Confirmation Should Include

```
✈️ Flight Confirmation:
   - Confirmation number (PNR)
   - Passenger name(s)
   - Flight numbers
   - Dates and times (local + origin timezone)
   - Departure/arrival airports (city + airport code)
   - Seat assignments (if booked)
   - Baggage allowance
   - Check-in deadline
   - Contact number for airline

🏨 Hotel Confirmation:
   - Confirmation number
   - Hotel name and address
   - Check-in and check-out dates/times
   - Room type and number
   - Cancellation policy
   - Contact number for hotel
   - Wi-Fi password (if included)

🎫 Activity Confirmation:
   - Booking reference
   - Activity name and location
   - Date and time (including meeting points)
   - Duration
   - What's included (ticket, guide, equipment)
   - Cancellation policy
   - Payment receipt
```

### Organizing Confirmations

```
Recommended File Structure:
~/.travel-agents/confirmations/YYYY-MM-DD/
  ├── flights/
  │   ├── flight_JFK-LHR_2025-06-01.xml
  │   └── flight_LHR-TYO_2025-06-15.xml
  ├── hotels/
  │   ├── hotel_London-Kensington.xml
  │   └── hotel_Tokyo-Shibuya.xml
  └── activities/
      ├── activity_Tokyo-Senso-Ji.xml
      └── activity_Paris-Louvre.xml
```

## Post-Booking Support

### What Agents Should Advise Users To Do

```
✈️ Before Flight:
   - Check in online (24-48 hours before)
   - Verify visa status if applicable
   - Confirm reservation (call airline if no confirmation received)
   - Download airline app for boarding passes

🏨 Before Hotel:
   - Save digital confirmation on phone
   - Download hotel app (optional, for mobile check-in)
   - Set reminder for check-in time

🚨 Flight Changes:
   - Monitor for price changes (24 hours before)
   - Check if ticket is refundable or changeable
   - Save contact info for 24/7 support

🏨 Hotel Changes:
   - Review cancellation deadline
   - Know if free cancellation period applies
```

## Agent Workflow Recommendations

### Research Agent (travel-agent-researcher)

```yaml
Tools to use:
  - web_search: Search for destinations, prices, availability
  - terminal: Query local APIs, parse data
  - browser_navigate: Check airline/booking sites directly

Output format:
  - Structured JSON with multiple options
  - Include price range (not just single price)
  - List pros/cons of each option
  - Check booking availability (not just search)
```

### Designer Agent (travel-agent-designer)

```yaml
Use research output to:
  - Create day-by-day itinerary with specific times
  - Calculate total budget with breakdown
  - Include transfer times between activities
  - Add contingency buffer (1-2 hours per day)

Tools to use:
  - write_file: Save itinerary in multiple formats
  - terminal: Query calendar APIs for availability
  - vision (if using sketch/design tools)
```

### Reviewer Agent (travel-agent-reviewer)

```yaml
Checklist for validation:
  [ ] All flights connect (departure before arrival)
  [ ] Hotel check-in is after last flight arrival
  [ ] Hotel check-out is before departure flight
  [ ] Budget aligns with options selected
  [ ] No duplicate bookings
  [ ] Visa/passport requirements met
  [ ] Activities within available times
  [ ] Reasonable travel days

Tools to use:
  - read_file: Review all previous outputs
  - terminal: Run validation scripts
  - python: Validate dates/times programmatically
```

### Developer Agent (travel-agent-developer)

```yaml
Integration tasks:
  - Build API client for booking providers
  - Implement booking workflow orchestration
  - Create payment processing (via Stripe/Braintree)
  - Build confirmation document generator
  - Implement cancellation/refund handling

Tools to use:
  - terminal: Run build/test commands
  - subagent-driven-development: Delegate to subagents
  - github-pr-workflow: Create test PRs
```

### Orchestrator Agent (travel-agent-orchestrator)

```yaml
Workflow management:
  - Parse user request into structured tasks
  - Route to correct agent based on task type
  - Maintain context between handoffs
  - Handle errors and retries
  - Compile final deliverable

Tools to use:
  - delegate_task: Spawn subagents for workflow execution
  - write_file: Maintain task queue state
  - terminal: Monitor process status
```

## Communication Templates

### When Asking User for Clarification

```
Message: "I need a bit more information to complete your booking:"

Fields to collect:
  - Number of travelers and ages (adults, children, infants)
  - Specific dates (departure and return)
  - Origin city and preferred airports
  - Destination(s)
  - Budget range per person
  - Preferred cabin class
  - Any special requirements (wheelchair, meals, etc.)

Example:
"Could you please provide:
1. How many travelers? (I assume 1 adult, please confirm)
2. Departure date: June 1, 2025 (please confirm)
3. Origin: New York City (JFK/LGA/EWR)
4. Destination: London, UK (LHR preferred)"
```

### When Presenting Options

```
Message: "Here are your best flight options:"

Structure:
  ┌─────────────────────────────────────────────────┐
  │ Option 1 (Recommended)                          │
  │   Airline: British Airways                      │
  │   Flight: BA177                                  │
  │   Date: Sat, June 1, 2025                       │
  │   Depart: 06:30 PM (JFK) → 10:45 PM (LHR)      │
  │   Duration: 7h 15m                              │
  │   Price: $650 USD                               │
  │   Baggage: 1 checked bag included               │
  │   Reviews: ★★★★☆ (4.5/5, 12,000 reviews)      │
  │                                                 │
  │ Would you like me to book this option? (Yes/No) │
  └─────────────────────────────────────────────────┘
```

### When Confirming Booking

```
Message: "✅ Booking confirmed!"

Booking summary:
  Flight: BA177 from JFK to LHR
  Date: Saturday, June 1, 2025
  Departure: 6:30 PM (New York time)
  Arrival: 10:45 PM (London time)
  Passenger: [User's Name]
  Price: $650 USD
  Confirmation Number: BA123456

Next steps:
  1. Save this confirmation (or I can email it to you)
  2. Check in online 24 hours before departure
  3. Arrive at airport 2 hours before international flight

Anything else I can help you with?
```

## Quick Reference Commands

### Search for Flights
```bash
# Via Skyscanner API
curl -X POST "https://api.skyscanner.com/v2/flights" \
  -d '{"origin":"JFK","destination":"LHR","departure":"2025-06-01"}'

# Via Expedia API (example structure)
curl -X POST "https://api.expedia.com/search" \
  -H "Authorization: Bearer $EXPEDIA_API_KEY" \
  -d '{"originCity":"New York","destinationCity":"London"}'
```

### Check Visa Requirements
```bash
# Via IATA API
curl "https://www.iatagobusiness.com/api/go-visit/visa-requirements?citizenship=US&destination=United+Kingdom"
```

### Get Exchange Rates
```bash
# Via ExchangeRate-API
curl "https://api.exchangerate-api.com/v4/latest/USD"
```

### Check Flight Availability
```bash
# Via Google Flights (through scraper or API)
# Note: Google Flights doesn't have a public API
# Use as reference, book through provider
```

## Next Steps

The travel agent system is structured to work with **Hermes Workspace**, not as a standalone web server. To implement this skill:

1. **Load the skill** in your agent's context
2. **Use the knowledge base** when encountering travel tasks
3. **Follow the workflow patterns** for booking operations
4. **Apply the error handling** for common pitfalls

## References

- **Travel APIs**: https://www.iata.org, https://developer.skyscanner.net
- **Booking Providers**: https://www.expedia.com, https://www.booking.com, https://www.agoda.com
- **Visa Requirements**: https://www.iata.org/what-we-offer/iata-go-visit/
- **Payment APIs**: https://stripe.com, https://developer.braintreepayments.com

---

**Author:** Travel Agent System  
**Version:** 1.0  
**Last Updated:** May 2026
