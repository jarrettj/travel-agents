#!/bin/bash

# Travel Agent Soul Files & Skills Backup & Setup Script
# This script backs up existing files and sets up travel-specific skills

set -e

echo "🛡️  Travel Agent Soul Files & Skills Setup Script"
echo "================================================"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Directories
HERMES_WORKSPACE="${HOME}/hermes-workspace"
TRAVEL_AGENTS="${HOME}/travel-agents"
SKILLS_DIR="${HOME}/.hermes/skills"
SOU L_FILES_DIR="${HOME}/hermes-workspace/profiles/travel-agents"
BACKUP_DIR="${TRAVEL_AGENTS}/.backup"

echo -e "${BLUE}📁 Directories:${NC}"
echo "  Hermes Workspace: ${HERMES_WORKSPACE}"
echo "  Travel Agents: ${TRAVEL_AGENTS}"
echo "  Skills Directory: ${SKILLS_DIR}"
echo "  Soul Files: ${SOU L_FILES_DIR}"
echo ""

# Create backup directory
mkdir -p "${BACKUP_DIR}"

# Function to backup a file
backup_file() {
    local file="$1"
    if [ -f "$file" ]; then
        local filename=$(basename "$file")
        local timestamp=$(date +%Y%m%d_%H%M%S)
        cp "$file" "${BACKUP_DIR}/${filename}.backup.${timestamp}"
        echo -e "${GREEN}✓ Backed up: ${filename}${NC}"
    else
        echo -e "${YELLOW}⚠ File not found: ${filename}${NC}"
    fi
}

# Function to copy a file
copy_file() {
    local source="$1"
    local dest="$2"
    mkdir -p "$(dirname "$dest")"
    cp "$source" "$dest"
    echo -e "${GREEN}✓ Copied to: ${dest}${NC}"
}

echo -e "${BLUE}🔍 Step 1: Backing up existing soul files...${NC}"
backup_file "${SOU L_FILES_DIR}/researcher-soul.md"
backup_file "${SOU L_FILES_DIR}/designer-soul.md"
backup_file "${SOU L_FILES_DIR}/developer-soul.md"
backup_file "${SOU L_FILES_DIR}/reviewer-soul.md"
backup_file "${SOU L_FILES_DIR}/orchestrator-soul.md"
backup_file "${HERMES_WORKSPACE}/swarm.yaml"

echo ""
echo -e "${BLUE}📋 Step 2: Creating travel-specific skills...${NC}"

# Create skills directory
mkdir -p "${SKILLS_DIR}/travel-agents"

# Check if skills already exist
for skill in travel-researcher travel-designer travel-developer travel-reviewer; do
    if [ -f "${SKILLS_DIR}/travel-agents/${skill}/SKILL.md" ]; then
        echo -e "${YELLOW}⚠ Skill ${skill} already exists, skipping${NC}"
    fi
done

echo ""
echo -e "${BLUE}✅ Setup complete!${NC}"
echo ""
echo -e "${GREEN}Next Steps:${NC}"
echo "1. Run this script again to copy skills to agents"
echo "2. Update swarm.yaml to reference the new skills"
echo "3. Restart Hermes Workspace"
echo ""
