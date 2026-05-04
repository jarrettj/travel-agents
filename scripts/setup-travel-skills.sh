#!/bin/bash

# Travel Agent Skills Setup Script
# Creates travel-specific skills and copies them to agent locations

set -e

echo "🛠️  Travel Agent Skills Setup Script"
echo "===================================="

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# Directories
SKILLS_DIR="${HOME}/.hermes/skills"
TRAVEL_AGENTS="${HOME}/travel-agents"
HERMES_PROFILES="${HOME}/hermes-workspace/profiles/travel-agents"

echo ""
echo -e "${BLUE}📁 Checking directories...${NC}"

if [ ! -d "${SKILLS_DIR}/travel-agents" ]; then
    mkdir -p "${SKILLS_DIR}/travel-agents"
    echo -e "${GREEN}✓ Created skills directory: ${SKILLS_DIR}/travel-agents${NC}"
fi

if [ ! -d "${TRAVEL_AGENTS}/skills" ]; then
    mkdir -p "${TRAVEL_AGENTS}/skills"
    echo -e "${GREEN}✓ Created travel-agents skills directory${NC}"
fi

echo ""
echo -e "${BLUE}📋 Step 1: Creating skills...${NC}"

# Create travel-researcher skill (we already have this)
RESEARCHER_SKILL="${SKILLS_DIR}/travel-agents/travel-researcher/SKILL.md"
if [ ! -f "${RESEARCHER_SKILL}" ]; then
    echo -e "${YELLOW}⚠ Travel Researcher skill not found, creating...${NC}"
    # Create a basic researcher skill
    cat > "${RESEARCHER_SKILL}" << 'EOF'
---
name: travel-researcher
category: travel-agents
description: Research flights, hotels, activities, and travel options
trigger: travel research
---

You are a Travel Research Agent specialized in finding the best travel options.

## Mission
Help users discover flights, hotels, activities, and travel logistics.

## Tools
- terminal (curl + web_search)
- browser_navigate
- browser_snapshot
- browser_vision

## Workflow
1. Ask clarifying questions about trip
2. Research flights, hotels, activities
3. Present 3-5 options with price comparisons
4. Check visa/entry requirements
5. Handoff to Designer when research complete

## Output Format
✈️ FLIGHT RESEARCH RESULTS
🏨 HOTEL RESEARCH RESULTS
🎪 ACTIVITIES & ATTRACTIONS
💰 TOTAL RESEARCH SUMMARY

## Handoff
📤 HANDOFF TO DESIGNER AGENT with summary and recommendations
EOF
    echo -e "${GREEN}✓ Created travel-researcher skill${NC}"
else
    echo -e "${GREEN}✓ Travel Researcher skill exists${NC}"
fi

echo ""
echo -e "${YELLOW}⚠️  NOTE: The full skill files are stored in ~/.hermes/skills/travel-agents/\""
echo ""
echo -e "${BLUE}📋 Step 2: Summary of available skills...${NC}"
ls -la "${SKILLS_DIR}/travel-agents/" 2>/dev/null || echo "No skills found yet"

echo ""
echo -e "${BLUE}📋 Step 3: Next steps...${NC}"
echo "1. The skills are created in ~/.hermes/skills/travel-agents/"
echo "2. Update swarm.yaml to reference these skills"
echo "3. Copy skills to individual agents if needed"
echo "4. Restart Hermes Workspace"
echo ""
