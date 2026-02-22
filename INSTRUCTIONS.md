# Exercise 2: Navigating a Codebase

> **Time:** 20 minutes
> **Goal:** Practice the 3-minute orientation routine on a mini project.

---

## Instructions

### Part A: Study the Reference (5 min)
Read `REFERENCE.md` — it explains how to navigate any task's file structure.

### Part B: Navigate the Sample Project (15 min)
The `sample_project/` folder contains a small CLI task manager. Pretend you just
received this as a sprint task. Use the 3-minute orientation routine:

**Minute 1 — Scan the structure:**
`ash
ls sample_project/
ls sample_project/src/
ls sample_project/tests/
`
Write down: How many source files? How many test files? What language?

**Minute 2 — Read the entry point:**
Open `sample_project/src/taskManager.py` and read the first 20 lines.
Write down: What classes exist? What do they do?

**Minute 3 — Find the markers:**
Search for markers in the source files:
`ash
grep -rn "BUG\|TODO\|FIXME" sample_project/src/
`
Write down: What type of task is this? (Bug Fix / Feature Ship / Maintenance / Debugging)

### Self-Check
You should be able to orient yourself in any codebase in under 3 minutes.

---

## Files in This Folder

| File | Purpose |
|------|---------|
| `REFERENCE.md` | The complete code navigation guide |
| `sample_project/` | A mini project to practice navigating |
