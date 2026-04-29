# AI-Agents-Phase-1-Building-Different-Types-of-AI-Assistants

This project explores 6 different types of AI agents — from the simplest (just ask a question and get an answer) to more advanced ones that can check their own work, route questions to the right specialist, and follow step-by-step instructions from a guide.

---

## What Is This Project About?

Think of an "AI agent" as a smart assistant you can give a job to. But not all assistants work the same way. Some just answer from memory. Others follow a script. Some double-check their own work. Some forward your question to whoever is best at answering it.

This project builds **6 types of AI assistants**, each one more capable than the last, to show how different approaches produce very different results.

---

## The Files in This Folder

| File | What It Is |
|---|---|
| `base_agents.py` | The main code — all 6 agent types are built here |
| `direct_prompt_agent.py` | Demo: the simplest agent |
| `augmented_prompt_agent.py` | Demo: agent with a personality |
| `knowledge_augmented_prompt_agent.py` | Demo: agent with custom facts |
| `rag_knowledge_prompt_agent.py` | Demo: agent that reads a long document |
| `evaluation_agent.py` | Demo: agent that checks and fixes its own answers |
| `routing_agent.py` | Demo: agent that sends questions to the right specialist |
| `action_planning_agent.py` | Demo: agent that extracts steps from a guide |
| `Screen-shots.docx` | Screenshots from the course platform |

---

## The 6 Types of Agents — Explained Simply

---

### Agent 1 — Direct Prompt Agent
**File:** `direct_prompt_agent.py`

**The simplest possible agent.** You ask it a question. It answers from everything it already knows (like asking Google a question). No special setup, no rules, no personality.

**Example used in the code:**
- Question: *"What is the capital of France?"*
- Answer: *"Paris"* — straight from the AI's built-in knowledge

**Think of it like:** Texting a very smart friend and asking them a question. They just answer.

---

### Agent 2 — Augmented Prompt Agent
**File:** `augmented_prompt_agent.py`

**Same as Agent 1, but you give it a personality (called a persona).** The AI still uses its own knowledge to answer, but it responds in a style you define.

**Example used in the code:**
- Persona: *"You are a college professor. Your answers always start with: Dear students,"*
- Question: *"What is the capital of France?"*
- Answer: *"Dear students, the capital of France is Paris..."*

**Think of it like:** Asking the same smart friend the same question, but this time they are roleplaying as a teacher.

---

### Agent 3 — Knowledge Augmented Prompt Agent
**File:** `knowledge_augmented_prompt_agent.py`

**You give this agent a persona AND a set of facts to use.** The important part: it uses YOUR facts instead of what it already knows. Even if your facts are wrong, it will use them.

**Example used in the code (intentionally wrong to prove the point):**
- Persona: *"You are a college professor..."*
- Custom fact given: *"The capital of France is London, not Paris"*
- Question: *"What is the capital of France?"*
- Answer: *"Dear students, the capital of France is London..."*

The agent ignored what it actually knows (Paris) and used the fact you gave it (London). This proves the agent truly follows your instructions.

**Think of it like:** Handing a professor a specific textbook and saying "only use this book to answer, not your own memory."

---

### Agent 4 — RAG Knowledge Prompt Agent
**File:** `rag_knowledge_prompt_agent.py`

**This agent handles long documents.** Instead of pasting an entire book into the agent (which would be too much), it:

1. **Cuts the document into small pieces** (like cutting a book into pages)
2. **Converts each piece into a mathematical fingerprint** (a unique number pattern representing the meaning of that piece)
3. **When you ask a question**, it finds the piece whose fingerprint most closely matches your question
4. **Answers only from that best-matching piece**

This method is called **RAG** — Retrieval Augmented Generation. The word "retrieval" means it first *finds* the right section before *generating* an answer.

**Example used in the code:**
- The document: A long story about a marine biologist named Clara, her family history, her podcast, her research, and her tech projects
- Question: *"What is the podcast that Clara hosts about?"*
- The agent finds the paragraph about the podcast and answers from it — without reading the entire document

**Think of it like:** A librarian who, instead of reading an entire encyclopaedia to answer your question, quickly scans the index, finds the right page, and reads only that page to you.

---

### Agent 5 — Evaluation Agent
**File:** `evaluation_agent.py`

**This agent checks and corrects its own work in a loop.** It has three roles working together:

- **Worker** — gives an answer
- **Judge** — checks if the answer meets a specific rule
- **Fixer** — if the answer fails, tells the worker exactly what to fix

It keeps looping (up to 10 times) until the answer passes the judge's check.

**Example used in the code:**
- The worker agent is the Knowledge Agent from Agent 3 (which says the capital of France is London)
- The rule (evaluation criteria): *"The answer should be only the name of a city, not a full sentence"*
- The worker first answers with a full sentence like: *"Dear students, the capital of France is London..."*
- The judge says: FAIL — that is a sentence, not just a city name
- The fixer tells the worker: "Remove everything except the city name"
- The worker tries again: *"London"*
- The judge says: PASS

**Think of it like:** A student writes an essay. The teacher marks it and says what is wrong. The student rewrites it. The teacher checks again. This repeats until it passes.

---

### Agent 6 — Routing Agent
**File:** `routing_agent.py`

**This agent decides which specialist to send your question to.** You set up multiple specialist agents, each with a description of what they know. When a question comes in, the routing agent compares it to each specialist's description and picks the best match.

**Example used in the code:**

Three specialists are set up:
- **Texas Agent** — knows everything about Texas
- **Europe Agent** — knows everything about Europe
- **Math Agent** — handles questions with numbers

Questions asked:
- *"Tell me about the history of Rome, Texas"* → routed to the **Texas Agent**
- *"Tell me about the history of Rome, Italy"* → routed to the **Europe Agent**
- *"One story takes 2 days, and there are 20 stories"* → routed to the **Math Agent**

The router does not read rules — it uses mathematical similarity scores to figure out which agent is the best fit.

**Think of it like:** Calling a company's phone line and an automated system listens to your question, then transfers you to the right department (billing, tech support, sales) without you having to choose yourself.

---

### Agent 7 — Action Planning Agent
**File:** `action_planning_agent.py`

**This agent reads a guide or instructions and figures out the right steps for what you want to do.** You give it a knowledge base (like a recipe book), and when someone describes what they want, it extracts only the relevant steps.

**Example used in the code:**
- Knowledge given: Recipes for Fried Egg, Scrambled Eggs, and Boiled Eggs
- Request: *"One morning I wanted to have scrambled eggs"*
- Output: The 8 steps for making scrambled eggs — nothing else

**Think of it like:** You hand a cooking assistant a recipe book. They don't read every recipe aloud — they listen to what you want, find the right recipe, and just tell you those steps.

---

## How They All Fit Together

Each agent builds on the previous idea:

```
Agent 1 — Just answer (no setup)
    ↓
Agent 2 — Answer with a personality
    ↓
Agent 3 — Answer using facts YOU provide
    ↓
Agent 4 — Answer from a long document (smart search first)
    ↓
Agent 5 — Answer, check, fix, repeat until correct
    ↓
Agent 6 — Pick the right specialist for the question
    ↓
Agent 7 — Extract the right steps from a guide
```

---

## How to Run This Project

**What you need:**
- Python installed on your computer
- An OpenAI API key

**Install dependencies:**
```
pip install openai python-dotenv numpy pandas
```

**Create a `.env` file in this folder and add your API key:**
```
OPENAI_API_KEY=your_key_here
```

**Run any demo file:**
```
python direct_prompt_agent.py
python augmented_prompt_agent.py
python knowledge_augmented_prompt_agent.py
python rag_knowledge_prompt_agent.py
python evaluation_agent.py
python routing_agent.py
python action_planning_agent.py
```

Each file runs independently and prints the result to the screen.

---

## Course

This project is part of the **AI Agents with LLMs** course on Udacity.
