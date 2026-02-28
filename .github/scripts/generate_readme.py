import os
from pathlib import Path
from collections import defaultdict
import re

DIFFICULTIES = {"Easy": 0, "Medium": 0, "Hard": 0}
TOPICS = defaultdict(lambda: {"Easy": 0, "Medium": 0, "Hard": 0})
PROBLEMS = []


def parse_problem_folder(folder: Path):
    readme = folder / "README.md"
    if not readme.exists():
        return None

    try:
        content = readme.read_text(encoding="utf-8")

        # Extract difficulty from <h3>Easy</h3> or ## Easy etc
        difficulty = None
        for diff in ["Easy", "Medium", "Hard"]:
            if f"<h3>{diff}</h3>" in content or f"**{diff}**" in content or f"#{diff}" in content.replace(" ", ""):
                difficulty = diff
                break
            if re.search(rf'\b{diff}\b', content):
                difficulty = diff
                break

        # Extract title from first <h2> or # heading
        title = folder.name
        title_match = re.search(r'<h2[^>]*>(.*?)</h2>', content, re.IGNORECASE)
        if title_match:
            title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
        else:
            h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if h1_match:
                title = h1_match.group(1).strip()

        # Extract topic from tags or infer from title
        topic = "Other"
        topic_match = re.search(r'(?:Topics?|Category)[:\s]+([^\n]+)', content, re.IGNORECASE)
        if topic_match:
            topic = topic_match.group(1).strip()
        else:
            name = folder.name.lower()
            if any(x in name for x in ["array", "matrix", "subarray", "sum", "product"]):
                topic = "Arrays"
            elif any(x in name for x in ["string", "palindrome", "anagram", "substring"]):
                topic = "Strings"
            elif any(x in name for x in ["linked-list", "add-two-numbers", "reverse-linked"]):
                topic = "Linked Lists"
            elif any(x in name for x in ["tree", "bst", "binary-tree", "level-order"]):
                topic = "Trees"
            elif any(x in name for x in ["graph", "island", "course", "network"]):
                topic = "Graphs"
            elif any(x in name for x in ["dynamic", "climb", "coin", "house-robber", "knapsack"]):
                topic = "Dynamic Programming"
            elif any(x in name for x in ["binary-search", "search-in"]):
                topic = "Binary Search"
            elif any(x in name for x in ["stack", "queue", "valid-parentheses", "min-stack"]):
                topic = "Stack & Queue"
            elif any(x in name for x in ["two-pointer", "three-sum", "container"]):
                topic = "Two Pointers"
            elif any(x in name for x in ["sliding-window", "maximum-subarray", "longest-substring"]):
                topic = "Sliding Window"
            elif any(x in name for x in ["heap", "top-k", "kth-largest"]):
                topic = "Heap"
            elif any(x in name for x in ["backtrack", "permutation", "combination", "subsets"]):
                topic = "Backtracking"

        if difficulty:
            return {"difficulty": difficulty, "topic": topic, "title": title, "folder": folder.name}

    except Exception as e:
        print(f"Error parsing {folder}: {e}")
    return None


# Scan all problem folders
for folder in sorted(Path(".").iterdir()):
    if not folder.is_dir():
        continue
    if folder.name.startswith(".") or folder.name in ["venv", "__pycache__"]:
        continue
    result = parse_problem_folder(folder)
    if result:
        PROBLEMS.append(result)
        diff = result["difficulty"]
        topic = result["topic"]
        if diff in DIFFICULTIES:
            DIFFICULTIES[diff] += 1
        TOPICS[topic][diff] += 1

total = sum(DIFFICULTIES.values())

# Build topic table
topic_rows = ""
topic_totals = {"Easy": 0, "Medium": 0, "Hard": 0}
for topic, counts in sorted(TOPICS.items()):
    e, m, h = counts["Easy"], counts["Medium"], counts["Hard"]
    t = e + m + h
    topic_rows += f"| {topic} | {e} | {m} | {h} | {t} |\n"
    topic_totals["Easy"] += e
    topic_totals["Medium"] += m
    topic_totals["Hard"] += h

te = topic_totals["Easy"]
tm = topic_totals["Medium"]
th = topic_totals["Hard"]
tt = te + tm + th

# Build recent problems list
recent = PROBLEMS[-10:][::-1]
recent_rows = ""
for p in recent:
    recent_rows += f"- `{p['difficulty']}` — {p['title']}\n"

if not recent_rows:
    recent_rows = "_No problems solved yet — start grinding!_\n"

readme = f"""# DSA Practice

Systematic problem-solving practice in Python. Organized by topic and difficulty.

---

## Progress

![Problems Solved](https://img.shields.io/badge/Solved-{total}-brightgreen)
![Easy](https://img.shields.io/badge/Easy-{DIFFICULTIES['Easy']}-green)
![Medium](https://img.shields.io/badge/Medium-{DIFFICULTIES['Medium']}-orange)
![Hard](https://img.shields.io/badge/Hard-{DIFFICULTIES['Hard']}-red)

| Topic | Easy | Medium | Hard | Total |
|---|---|---|---|---|
{topic_rows}| **Total** | **{te}** | **{tm}** | **{th}** | **{tt}** |

---

## Recent Solutions

{recent_rows}
---

## Structure

Each solution file follows this format:
```python
\"\"\"
Problem: <name>
Link: <leetcode url>
Difficulty: Easy / Medium / Hard
Topic: <topic>

Approach: <brief description>
Time: O(?)
Space: O(?)
\"\"\"
```

---

## Order of Study

1. Arrays & Strings
2. Two Pointers
3. Sliding Window
4. Binary Search
5. Linked Lists
6. Stack & Queue
7. Trees
8. Heap
9. Graphs
10. Dynamic Programming
11. Backtracking

---

_Auto-generated by GitHub Actions — updates on every push_
"""

Path("README.md").write_text(readme, encoding="utf-8")
print(f"README updated — {total} problems solved")
for p in PROBLEMS:
    print(f"  {p['difficulty']:6} | {p['topic']:20} | {p['title']}")