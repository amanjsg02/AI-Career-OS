# AI Career Operating System (AI Career Assistant)

An end-to-end AI-powered career assistant that helps users analyze resumes, generate personalized career roadmaps, answer career-related questions, and provide real-time AI interactions using a modern, production-inspired architecture.

---

# Features

##  AI Chat Assistant

* Conversational AI powered by Google Gemini.
* Supports both general conversations and career-specific guidance.
* Streams responses token-by-token for a smooth user experience.

---

##  Resume Analysis (RAG)

Upload a resume and automatically:

* Extract text from PDF
* Parse resume sections
* Chunk resume content
* Generate embeddings
* Store embeddings in ChromaDB
* Retrieve relevant resume context during conversations

The assistant answers questions using the uploaded resume instead of relying only on the LLM.

---

## Persistent Memory

The assistant remembers important user information across conversations.

Examples:

* Career goals
* Preferred technologies
* Previous discussions
* Learning interests

Memory is embedded, stored, and retrieved to personalize future responses.

---

## Multi-Agent Architecture

The system uses specialized AI agents instead of a single monolithic prompt.

Current agents include:

* **Resume Agent** – analyzes resume information
* **Memory Agent** – retrieves long-term memory
* **Research Agent** – gathers additional knowledge
* **Planner Agent** – combines information into a structured response
* **Critic Agent** – reviews and improves the final answer

Multiple agents execute concurrently using `asyncio.gather()` to reduce latency.

---

## Streaming Responses

Responses are streamed in real time.

Instead of waiting for the complete answer:

```
User Question
      ↓
Gemini
      ↓
StreamingResponse
      ↓
React UI
```

Users see the response being generated live.

---

## Voice AI Support

Supports voice-based interaction through:

* Speech-to-Text
* AI Processing
* Text-to-Speech

Creating a complete voice-enabled AI assistant experience.

---

#  Phase 7 – Real-Time AI Infrastructure

Phase 7 transforms the project from a simple AI application into a production-style AI system.

---

## Background Workers

Long-running tasks no longer block API requests.

Example:

```
Resume Upload
      ↓
Task Created
      ↓
Immediate Response
      ↓
Background Worker
      ↓
Resume Processing
```

Users can continue interacting with the assistant while processing continues in the background.

---

## Redis Shared State

Redis is used for centralized task state management.

Example:

```json
{
  "status": "running",
  "progress": 70
}
```

Workers and API endpoints both read and update the same shared state.

---

## Task Tracking

Each background task receives a unique Task ID.

Example:

```
task:9d3e0...

status
progress
```

This enables tracking of asynchronous operations.

---

## WebSocket-Based Live Updates

Real-time updates are pushed to the frontend using WebSockets.

```
Background Worker
        ↓
Connection Manager
        ↓
WebSocket
        ↓
React UI
```

The UI displays progress instantly without polling.

---

## Resume Processing Pipeline

```
Resume Upload
      ↓
PDF Extraction
      ↓
Resume Parsing
      ↓
Chunking
      ↓
Embedding Generation
      ↓
ChromaDB Storage
      ↓
Progress Updates
      ↓
Completed
```

---

## Background Processing

Long-running tasks execute independently from the request lifecycle.

Examples include:

* Resume indexing
* Embedding generation
* Future research tasks
* Memory extraction
* Interview evaluation

---

# Project Architecture

```
                     React Frontend
                           │
                           ▼
                      FastAPI Backend
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
         Streaming API         Background Workers
                │                     │
                ▼                     ▼
        Multi-Agent System        Redis State
                │                     │
      ┌─────────┼──────────┐          │
      ▼         ▼          ▼          │
 Resume     Memory     Research       │
 Agent       Agent       Agent        │
      └─────────┼──────────┘          │
                ▼                     │
          Planner Agent              │
                ▼                     │
           Critic Agent              │
                ▼                     │
             Gemini LLM              │
                ▼                     │
        Streaming Response           │
                │                     │
                └─────────┬───────────┘
                          ▼
                     React Frontend
```

---

# Tech Stack

### Backend

* FastAPI
* Python
* AsyncIO
* WebSockets
* Redis
* ChromaDB
* Sentence Transformers
* PyPDF

### AI & Machine Learning

* Google Gemini
* RAG (Retrieval-Augmented Generation)
* Embeddings
* Chroma Vector Database
* Sentence Transformers (all-MiniLM-L6-v2)

### Frontend

* React
* JavaScript
* Fetch Streaming API
* WebSocket API

---

# Current Project Structure

```
backend/
│
├── agents/
│   ├── resume_agent.py
│   ├── memory_agent.py
│   ├── research_agent.py
│   ├── planner_agent.py
│   ├── critic_agent.py
│   └── orchestrator.py
│
├── memory/
├── rag/
├── routes/
├── services/
│   ├── websocket_manager.py
│   ├── redis.py
│   └── prompt_builder.py
│
├── data/
└── main.py

frontend/
│
├── components/
├── services/
└── App.jsx
```

---

#  Current Capabilities

* AI-powered career conversations
* Resume-aware question answering
* Personalized memory retrieval
* Multi-agent orchestration
* Streaming AI responses
* Voice interaction
* Background resume processing
* Redis-backed task tracking
* Real-time progress updates using WebSockets
* Production-style asynchronous architecture

---

# Planned Improvements

* Shared agent state across sessions
* Interview simulation with persistent session state
* Event-driven agent workflows
* Task monitoring dashboard
* LangGraph integration
* Advanced workflow orchestration
* Human-in-the-loop approval workflows
* Production deployment with Docker & Kubernetes

---

# Learning Outcomes

This project demonstrates practical experience with:

* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embedding Models
* Multi-Agent AI Systems
* Async Programming
* Streaming APIs
* WebSockets
* Background Task Processing
* Redis
* Real-Time System Design
* AI Infrastructure

---

# Project Status

**Current Progress:** Phase 7 Complete (Real-Time AI Infrastructure)

The project has evolved from a basic chatbot into a production-inspired AI system featuring retrieval, memory, agent orchestration, streaming, background processing, shared state, and real-time updates.
