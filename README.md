# Agentic Knowledge Research System

A learning-focused agentic AI project built progressively using LangGraph.

## Phase 0 — Project Foundation

Implemented:

- Python virtual environment
- LangGraph setup
- Basic LangGraph State
- Node
- START and END
- Graph compilation
- Graph invocation

### Current Workflow

START → hello_node → END


## Phase 1 — First LLM Agent

Implemented:

- Gemini LLM integration
- LangChain Chat Model
- Environment variable based API key configuration
- LangGraph State
- LLM node
- Graph invocation
- Basic question-answer workflow

### Current Workflow

START → LLM Node → END

### Flow

User Question
↓
LangGraph State
↓
LLM Node
↓
Gemini
↓
AI Response