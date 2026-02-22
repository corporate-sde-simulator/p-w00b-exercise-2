# Module 02: Navigating a Multi-File Project 📂

> In college, you write one file. In companies, code lives in 10+ files.
> This module teaches you how real projects are organized and how to find
> your way around code you've never seen before.

---

## The Standard Task Structure

Every task in this simulator follows this structure:

```
Task-3/
├── TICKET.md                ← Your assignment (read FIRST)
├── docs/
│   ├── DESIGN.md            ← Architecture decisions
│   └── GUIDE.md             ← Learning guide with examples
├── src/
│   ├── mainModule.py        ← Primary source code (bugs live here!)
│   └── helperModule.py      ← Supporting code (may also have bugs)
├── tests/
│   └── test_module.py       ← Tests to verify your fixes
└── .context/
    └── pr_comments.md       ← Previous PR review feedback (clues!)
```

---

## What Each Folder Does

### 📋 `TICKET.md` (Root)
**Read this FIRST.** It's your assignment — what to fix and why.

### 📖 `docs/` — Documentation
- **DESIGN.md** — Explains WHY the code is built this way. Useful when the
  architecture confuses you.
- **GUIDE.md** — A learning guide with syntax examples in the task's language.
  If you forgot how Python classes work, check here before Googling.

### 💻 `src/` — Source Code
**This is where you do your work.** What you look for depends on the **Task Type**:

| Task Type | What to Look For | What to Do |
|-----------|-----------------|------------|
| **Bug Fix** | `# BUG:` or `// BUG:` comments | Fix the code near the comment |
| **Feature Ship** | `// TODO:` comments with specs | Implement the method following the spec |
| **Maintenance** | `# TODO (code review):` comments | Refactor the flagged code quality issues |
| **Debugging** | No markers! Read symptoms in TICKET.md | Trace the code to find the root cause |

> **Tip:** Always check the `Task Type` field in TICKET.md FIRST — it tells you
> which markers to search for. See [Module 07](07-Task-Types.md) for details.

### 🧪 `tests/` — Tests
- Run these to check if your fix works
- Commands:
  - Python: `python -m pytest tests/ -v`
  - JavaScript: `npm test` or `node tests/test_file.js`
  - Go: `go test -v ./...`
  - Java: `javac *.java && java TestRunner`
- **Add your own tests** here to prove your fix handles edge cases

### 🔍 `.context/` — Background Context
- **pr_comments.md** — Simulates code review comments from senior devs
- Often contains HINTS about what's wrong
- Sometimes contains red herrings (misleading comments) — just like real life!

---

## How to Navigate Code You've Never Seen

### Step 1: Start with the Entry Point
Every program has a starting point. Find it:
- **Python:** Look for `if __name__ == "__main__":` or the main class
- **JavaScript:** Look for `module.exports` (what's being exported?)
- **Go:** Look for `func main()` or the exported functions
- **Java:** Look for `public static void main` or the class declaration

### Step 2: Follow the Function Calls
Read code like a story:
```python
class TaskScheduler:
    def schedule(self, task):        # ← Start here
        priority = self.get_priority(task)  # ← Then go to get_priority
        self.queue.add(task, priority)       # ← Then go to queue.add
        self.log(f"Scheduled: {task}")       # ← Then go to log
```

### Step 3: Look at the Tests
Tests tell you what the code SHOULD do:
```python
def test_schedule_critical_first(self):
    scheduler.schedule(low_priority_task)
    scheduler.schedule(critical_task)
    next_task = scheduler.get_next()
    assert next_task == critical_task  # ← Critical should come first!
```
If a test says `assert result == X`, that's what the correct behavior should be.

### Step 4: Check Imports
Imports tell you which files are connected:
```python
from src.priorityQueue import PriorityQueue  # ← This file also matters!
from src.taskScheduler import TaskScheduler
```

---

## The 3-Minute Code Orientation Routine

When you open any new task, do this:

| Step | Action | Time |
|------|--------|------|
| 1 | `ls` or `dir` — see the file structure | 10 sec |
| 2 | Open `TICKET.md` — read the assignment + **check Task Type** | 1 min |
| 3 | Open `src/` files — scan for markers matching your task type | 1 min |
| 4 | Open `tests/` — read what tests expect | 1 min |
| 5 | Open `.context/` — check for hints | 30 sec |

**Only then start fixing.**

---

## Common Navigation Mistakes

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Editing the wrong file | Tests still fail | Check which file the tests import |
| Not reading all src/ files | You miss a related bug | Always scan ALL files in src/ |
| Ignoring .context/ folder | You miss helpful clues | It's only 1-2 minutes to read |
| Changing test files instead of src/ | "Tests pass" but code is still broken | Never change existing tests (only ADD new ones) |
