# AI Agent

A comprehensive AI Agent development toolkit built with **LangChain**, **LangGraph**, and **Streamlit**, integrated with **Groq** cloud LLM inference. This project provides examples, utilities, and a skill-driven workflow system for building, testing, and deploying AI agents.

## Overview

This repository serves two purposes:

1. **AI Agent Experimentation** — Python scripts and a Jupyter notebook demonstrating LangChain agent patterns including tool calling, parallel workflows, state graphs, and Streamlit-based chat UIs.
2. **AI Coding Agent Skills** — A collection of 23 skill definitions (skills/) that extend AI coding agents (Claude Code, Cursor, Copilot, OpenCode, Gemini CLI) with structured workflows for features like test-driven development, spec-driven development, debugging, code review, and more.

## Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3.13** | Runtime |
| **LangChain** (>=1.3.11) | LLM orchestration, agent creation, prompt templates, tool binding |
| **LangGraph** (langgraph) | Stateful workflow graphs with nodes/edges |
| **LangChain-Groq** (>=1.1.3) | Cloud LLM inference via Groq (supports Llama 3, Qwen, and other models) |
| **LangChain-OpenAI** (>=1.3.3) | OpenAI-compatible model support |
| **LangChain-Ollama** (>=1.1.0) | Local LLM inference via Ollama |
| **Streamlit** (>=1.58.0) | Web UI framework for agent chat interfaces |
| **Tavily** (>=1.1.0) | Web search tool integration for agents |
| **python-dotenv** (>=1.2.2) | Environment variable management |
| **Jupyter** (>=1.1.1) | Interactive notebook experimentation |
| **uv** | Python package manager (see uv.lock) |
| **pytest** | Testing framework |

## Project Structure

`
AI_AGENT/
+¦¦ .env                      # Environment variables (API keys)
+¦¦ .gitignore                # Git ignore rules
+¦¦ .python-version           # Python version (3.13)
+¦¦ AGENTS.md                 # Guidance for AI coding agents working in this repo
+¦¦ README.md                 # This file
+¦¦ pyproject.toml            # Project configuration and dependencies
+¦¦ uv.lock                   # uv lockfile for reproducible installs
-
+¦¦ main.py                   # Simple entry point (prints "Hello from ai-agent!")
+¦¦ app.py                    # Streamlit web app using LangGraph create_react_agent
+¦¦ ai-agent.py               # Streamlit chat application with Groq LLM (chat history)
+¦¦ ai-agent.ipynb            # Jupyter notebook with LangChain experiments
+¦¦ toolCall.py               # Tool-calling example (weather API tool with Groq)
+¦¦ promptTemplate.py         # Prompt template example with LangChain
+¦¦ test_agent.py             # Unit test for agent initialization
+¦¦ test_app.py               # Unit tests for the Streamlit app (4 test cases)
-
+¦¦ langchain/                # LangChain workflow examples
-   +¦¦ langraph.py           # StateGraph example — single chat node graph
-   +¦¦ stepWorkflow.py       # Single-step LLM workflow with structured output
-   +¦¦ parallelWorkflow.py   # Parallel processing (safety + response generation)
-   L¦¦ parallelWorkflowVote.py # Multi-expert parallel voting security review
-
L¦¦ skills/                   # 23 AI coding agent skill definitions
    +¦¦ api-and-interface-design/
    +¦¦ browser-testing-with-devtools/
    +¦¦ ci-cd-and-automation/
    +¦¦ code-review-and-quality/
    +¦¦ code-simplification/
    +¦¦ context-engineering/
    +¦¦ debugging-and-error-recovery/
    +¦¦ deprecation-and-migration/
    +¦¦ documentation-and-adrs/
    +¦¦ doubt-driven-development/
    +¦¦ frontend-ui-engineering/
    +¦¦ git-workflow-and-versioning/
    +¦¦ idea-refine/
    +¦¦ incremental-implementation/
    +¦¦ interview-me/
    +¦¦ performance-optimization/
    +¦¦ planning-and-task-breakdown/
    +¦¦ security-and-hardening/
    +¦¦ shipping-and-launch/
    +¦¦ source-driven-development/
    +¦¦ spec-driven-development/
    +¦¦ test-driven-development/
    L¦¦ using-agent-skills/
`

## Source Files Breakdown

### Core Agent Scripts

| File | Description |
|---|---|
| pp.py | Streamlit web app using langgraph.prebuilt.create_react_agent with Groq's openai/gpt-oss-120b model. Minimal single-input UI. |
| i-agent.py | Full Streamlit chat application with session message history, chat input, streaming spinner, and Groq-based agent. |
| i-agent.ipynb | Jupyter notebook demonstrating ChatGroq usage and LangChain agent creation with init_chat_model. |
| 	oolCall.py | Demonstrates LangChain tool binding — a get_current_weather tool that geolocates via ipinfo.io and fetches weather from Open-Meteo, then uses Groq (qwen/qwen3-32b) to answer weather queries. |
| promptTemplate.py | Minimal example of PromptTemplate chained with ChatGroq (Llama 3.3 70B) for structured Q&A. |

### LangChain Workflows (langchain/)

| File | Description |
|---|---|
| langraph.py | LangGraph StateGraph with a single chat node — demonstrates building and compiling a state graph with nodes, edges, START/END. |
| stepWorkflow.py | Single-step LLM workflow with Pydantic structured output (ReviewSentiment) for sentiment analysis. |
| parallelWorkflow.py | RunnableParallel processing — runs safety analysis and response generation in parallel, both with structured Pydantic outputs. |
| parallelWorkflowVote.py | Multi-expert parallel voting — three expert reviewers (SQL, auth, general) analyze code for security issues and vote on vulnerabilities via majority consensus. |

### Tests

| File | Description |
|---|---|
| 	est_agent.py | Verifies that create_react_agent initializes correctly with the Groq model and a square_root tool. |
| 	est_app.py | Four unit tests covering: model initialization params, agent creation with model, agent invocation on user input, and response display. Uses mocking for Streamlit and LangChain. |

## Skills Directory

The skills/ directory contains **23 skill definitions** designed for AI coding agents. Each skill follows a standard format (SKILL.md + optional scripts/ folder) and defines a workflow with steps, exit criteria, and verification checklists.

### Core Skills

| Skill | Description |
|---|---|
| **test-driven-development** | Write failing tests first, then implement. Includes the Prove-It Pattern for bug fixes. |
| **spec-driven-development** | Write structured specs before coding with a gated workflow: Specify -> Plan -> Tasks -> Implement. |
| **debugging-and-error-recovery** | Systematic root-cause debugging with the "Stop-the-Line" rule and triage checklist. |
| **code-review-and-quality** | Five-axis code review (correctness, readability, architecture, security, performance). |
| **incremental-implementation** | Implement changes in small, reversible steps. |
| **planning-and-task-breakdown** | Break work into discrete, ordered tasks. |
| **code-simplification** | Simplify without changing behavior. |
| **api-and-interface-design** | Design clean, consistent APIs. |
| **frontend-ui-engineering** | UI development workflows. |
| **security-and-hardening** | Security review and hardening. |
| **performance-optimization** | Profile and optimize performance. |
| **git-workflow-and-versioning** | Git best practices and versioning. |
| **ci-cd-and-automation** | CI/CD pipeline workflows. |
| **shipping-and-launch** | Production release workflows. |

### Meta and Process Skills

| Skill | Description |
|---|---|
| **using-agent-skills** | Meta-skill describing how to use skills effectively. |
| **doubt-driven-development** | Challenge assumptions before coding. |
| **context-engineering** | Load the right context at each step. |
| **idea-refine** | Refine vague ideas into concrete plans. |
| **interview-me** | Agent interview preparation. |
| **documentation-and-adrs** | Documentation and Architecture Decision Records. |
| **deprecation-and-migration** | Safe deprecation and migration strategies. |
| **browser-testing-with-devtools** | Browser testing via Chrome DevTools. |
| **source-driven-development** | Build from authoritative sources. |

## Setup / Installation

### Prerequisites

- **Python 3.13+**
- **uv** (recommended package manager) or pip
- A **Groq API key** (or other supported LLM provider)

### Installation Steps

`ash
# 1. Clone the repository
git clone <repo-url>
cd AI_AGENT

# 2. Create a virtual environment and install dependencies with uv
uv venv
uv sync

# Or with pip:
# python -m venv .venv
# .venv\Scripts\activate  (Windows)
# pip install -e .

# 3. Set up environment variables
# Edit .env and add your API keys:
# GROQ_API_KEY=gsk_your_key_here

# 4. Run the Streamlit apps
streamlit run app.py
streamlit run ai-agent.py

# 5. Run scripts directly
python toolCall.py
python promptTemplate.py
python langchain/parallelWorkflow.py
python langchain/langraph.py
`

### Environment Variables

Create a .env file in the project root:

`env
GROQ_API_KEY=gsk_your_groq_api_key_here
`

The following providers are also available (add their keys as needed):
- OPENAI_API_KEY — for OpenAI models
- TAVILY_API_KEY — for Tavily web search

## Usage Examples

### Streamlit Chat App

`ash
streamlit run ai-agent.py
`

Opens a browser-based chat interface where you can converse with a Groq-powered AI agent.

### Tool-Calling Agent

`ash
python toolCall.py
`

Demonstrates an agent that can call a weather tool to answer "What's the current temperature?"

### LangGraph State Machine

`ash
python langchain/langraph.py
`

Builds and runs a LangGraph state machine with a single chat node.

### Parallel Workflow

`ash
python langchain/parallelWorkflow.py
`

Runs safety analysis and response generation in parallel on a given query.

### Multi-Expert Security Review

`ash
python langchain/parallelWorkflowVote.py
`

Runs three expert reviewers (SQL, auth, general security) in parallel and votes on code vulnerability.

## Git History

- **1 commit** (initial): Initial commit: AI Agent project with LangChain workflows

## AGENTS.md — AI Agent Workflow Integration

The AGENTS.md file defines how AI coding agents (Claude Code, Cursor, Copilot, OpenCode, Gemini CLI) should interact with this repository. Key rules:

- **Skills are mandatory** — if a task matches a skill, the agent MUST invoke it before implementing
- **Intent mapping** — features map to spec-driven-development + incremental-implementation, bugs map to debugging-and-error-recovery, etc.
- **Orchestration** — three composable layers: Skills (how), Personas (who), Slash Commands (when)
- **Anti-rationalization** — agents must not skip skills for reasons like "this is too small"
