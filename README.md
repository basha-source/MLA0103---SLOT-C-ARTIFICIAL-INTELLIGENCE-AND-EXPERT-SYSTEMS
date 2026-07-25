<h1 align="center">🧠 Artificial Intelligence & Expert Systems Lab</h1>

<p align="center">
  <b>Course Code:</b> MLA0103 &nbsp;•&nbsp; <b>Slot:</b> C<br/>
  A complete collection of laboratory experiments in <b>Artificial Intelligence</b> and <b>Expert Systems</b>,<br/>
  covering knowledge representation in <b>Prolog</b> and intelligent programs in <b>Python</b>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Prolog-blue?style=for-the-badge&logo=prolog" alt="Prolog"/>
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Domain-Artificial%20Intelligence-orange?style=for-the-badge" alt="AI"/>
  <img src="https://img.shields.io/badge/Expert-Systems-green?style=for-the-badge" alt="Expert Systems"/>
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status"/>
</p>

---

## 📌 About This Repository

This repository contains hands-on **AI & Expert Systems** lab work. It demonstrates the two core pillars of classical Artificial Intelligence:

- 🧩 **Logic Programming & Knowledge Representation** using **SWI-Prolog** — facts, rules, recursion, inference, and expert-system reasoning.
- 🐍 **AI Programming** using **Python** — graph search algorithms with visualization.

Each experiment is a small, self-contained program built to illustrate one AI concept clearly.

---

## 📂 Table of Contents

- [Tech Stack](#-tech-stack)
- [Python Programs](#-python-programs)
- [Prolog Experiments](#-prolog-experiments)
- [Diagrams & Assets](#-diagrams--assets)
- [How to Run](#-how-to-run)
- [Project Structure](#-project-structure)
- [Author](#-author)

---

## 🛠 Tech Stack

| Category | Tools / Libraries |
|----------|-------------------|
| **Logic Programming** | SWI-Prolog |
| **Programming** | Python 3.x |
| **Python Libraries** | NetworkX, Matplotlib |
| **Visualization** | Matplotlib |

---

## 🐍 Python Programs

| File | Description |
|------|-------------|
| `Bfs and Dfs.py` | Interactive **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** traversal. Takes user-defined nodes and edges, builds an adjacency list, prints both traversals, and renders the graph using **NetworkX + Matplotlib**. Supports both directed and undirected graphs. |

---

## 🧩 Prolog Experiments

A series of experiments demonstrating facts, rules, recursion, and expert-system reasoning.

| Exp | File | Concept |
|-----|------|---------|
| 1 | `exp1.pl` | Sum of first *N* natural numbers using **recursion** |
| 2 | `exp2.pl` | **Facts** — student records with dates of birth |
| 3 | `exp3.pl` | **Rules & relations** — mapping students → teachers via subjects |
| 4 | `exp4.pl` | Facts — list of planets |
| 5 | `exp5.pl` | Facts — list of planets |
| 6 | `exp6.p` | **Tower of Hanoi** — classic recursive problem |
| 7 | `exp7.pl` | **Non-monotonic reasoning** — birds that can fly (penguin exception) |
| 8 | `exp8.pl` | **Family relationships** — male / female / parent facts |
| 9 | `exp9,pl` | **Expert system** — diet recommendation by condition |
| 10 | `exp10.pl` | **Monkey & Banana** problem — goal-based reasoning |
| 11 | `exp11.pl` | Facts — fruits and their colors |
| 12 | `exp12.pl` | **Graph edges** and best-path relation |
| 13 | `exp13.pl` | **Medical expert system** — diseases and diagnoses |
| 14 | `exp14.pl` | **Inference** — rain → wet ground |
| 15 | `exp15.pl` | **Syllogism** — Socrates is a human, therefore mortal |
| ⭐ | `Marcus_caesar_problem.pl` | Classic **Marcus & Caesar** knowledge-representation & inference problem |

---

## 🖼 Diagrams & Assets

| File | Description |
|------|-------------|
| `bfs.png` | BFS / DFS traversal output visualization |
| `exp3.png` | Output of experiment 3 (student–teacher mapping) |
| `Marcus_caesar_problem.png` | Marcus & Caesar reasoning diagram |
| `Marcus_caesar_pseudocode` | Pseudocode for the Marcus & Caesar problem |
| `perl outputs1–5.png` | Prolog experiment output screenshots |

---

## ▶ How to Run

### Prolog Experiments

Install **[SWI-Prolog](https://www.swi-prolog.org/download/stable)**, then:

```bash
# Start SWI-Prolog with a file
swipl exp1.pl
```

```prolog
% Example query for exp1.pl (sum of first N numbers)
?- sum(5, X).
X = 15.

% Example query for exp15.pl (Socrates syllogism)
?- mortal(socrates).
true.
```

> 💡 **Note:** `exp6.p` and `exp9,pl` use non-standard filenames.
> Rename them to `exp6.pl` and `exp9.pl` for them to load correctly in SWI-Prolog.

### Python Program

Install the required libraries:

```bash
pip install networkx matplotlib
```

Run the program:

```bash
# Graph traversal (BFS & DFS)
python "Bfs and Dfs.py"
```

---

## 🗂 Project Structure

```
MLA0103---SLOT-C-ARTIFICIAL-INTELLIGENCE-AND-EXPERT-SYSTEMS/
│
├── 🐍 Python
│   └── Bfs and Dfs.py             # BFS & DFS graph traversal + visualization
│
├── 🧩 Prolog
│   ├── exp1.pl → exp15.pl         # AI & Expert System experiments
│   ├── exp6.p                     # Tower of Hanoi
│   ├── exp9,pl                    # Diet recommendation expert system
│   └── Marcus_caesar_problem.pl   # Knowledge representation problem
│
├── 🖼 Diagrams & Outputs
│   ├── bfs.png
│   ├── exp3.png
│   ├── Marcus_caesar_problem.png
│   ├── Marcus_caesar_pseudocode
│   └── perl outputs1–5.png
│
└── README.md
```

---

## 👨‍💻 Author

<table>
  <tr>
    <td>
      <b>Shaik Jabbar Basha</b><br/>
      🎓 Artificial Intelligence & Expert Systems — MLA0103 (Slot C)<br/>
      🔗 GitHub: <a href="https://github.com/basha-source">@basha-source</a>
    </td>
  </tr>
</table>

---

<p align="center">
  ⭐ If you find this repository helpful, consider giving it a star!
</p>

<p align="center">
  <i>Made with 💙 for learning Artificial Intelligence & Expert Systems</i>
</p>
