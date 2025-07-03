# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**star-to-review** is a GitHub repository management tool that systematically reviews and tracks starred repositories. It automates GitHub issue creation for repository reviews and manages the review lifecycle through a state machine.

## Technology Stack

- **Python 3.x** with PyGithub, python-statemachine, Jinja2, and Pydantic
- **State persistence** via JSON files
- **GitHub API integration** for issue and PR management
- **Jinja2 templates** for structured review generation

## Core Architecture

### State Machine Design
Repository reviews follow a state machine pattern:
- **UNREVIEWED** → **PENDING** → **REVIEWED/NO_PLAN**
- Supports state transitions like reconsideration (REVIEWED → PENDING)

### Key Components
- **`core/repo.py`** - Repository data models and GitHub integration
- **`core/issue.py`** - GitHub issue creation functionality  
- **`core/review.template.md`** - Jinja2 template for review issues
- **`repo_states.json`** - Persistent storage for repository states

## Common Development Commands

### Environment Setup
```bash
pip install -r requirements.txt
export GITHUB_TOKEN=your_github_token
```

### Main Scripts
```bash
# Create review issues for unreviewed repositories
python create_issue_to_review.py --github-username USERNAME

# Reopen completed reviews for rechecking
python open_reviewed_to_recheck.py --github-username USERNAME

# Handle pull request workflows
python pull_request.py --github-username USERNAME --pull-request-number PR_NUMBER
```

### Development Mode
```bash
# Enable development mode (limits processing)
python create_issue_to_review.py --github-username USERNAME --devel true
```

## Data Models

- **PydanticRepository** - Individual repository with metadata and state
- **PydanticRepositoryState** - Collection manager for all tracked repositories
- **ReviewState** - State machine implementation for review lifecycle

## File Structure

- **`/core/`** - Main application logic and data models
- **`/review/`** - Generated review files and templates
- **`repo_states.json`** - Repository state persistence
- **`digest.txt`** - Large repository analysis data

## Required Environment Variables

- **GITHUB_TOKEN** - GitHub API access token for repository and issue operations

## Review Workflow

1. **Repository Discovery** - Fetches starred repositories from GitHub
2. **State Tracking** - Maintains review status in `repo_states.json`  
3. **Issue Creation** - Generates review issues using templates
4. **Manual Review** - Human review with state transitions
5. **Completion Tracking** - Updates states based on PR completion or labels

## Special Considerations

- The project processes repositories one at a time to avoid rate limiting
- State transitions are persistent and survive application restarts
- Review templates support specialized formats (e.g., AI code editor reviews)
- The system includes backward compatibility for different JSON storage formats