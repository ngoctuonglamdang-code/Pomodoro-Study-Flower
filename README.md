# 🌸 Study Flower Pomodoro Timer

A creative-coding prototype for **A2: Code Prototype Project**.  
It turns the Pomodoro technique into a **calm, visual experience**: a digital flower **blooms** during focus time, **rests** on breaks, and **shrinks** when the cycle ends until you “water” it again.

- **Author:** Ngoc Tuong Lam Dang - 25088269  
- **Course/Assessment:** 52685 Working with Data and Code, A2: Code Prototype Project
- **Version:** v1.0 – Final Submission (Nov 2025)  
- **Explainer Video (Unlisted):** `https://youtu.be/qcyTlRs2AJc`  
 
---

## 🧠 Overview

**What it is:**  
A small Python/Tkinter app that displays a flower on a canvas and manages work/break cycles (Pomodoro).  
**Why it’s interesting:**  
It blends **event-driven programming** with **emotional design** to make time management feel **gentle and motivating**.

**Core behaviours**

- **Work phase:** flower is **big** (bloomed), timer counts down.
- **Break phase:** flower **stays big** (resting), timer counts down.
- **After break:** flower **shrinks**; a **“Water the Flower”** button appears.
- **Water:** starts the next work cycle and **blooms** the flower again.

---

## ✨ Features

- Event-driven timer loop using `root.after(...)` (no UI freezing)
- Clear state machine via `phase = "work" | "break" | "idle"`
- Custom flower drawing on `Canvas` with **trigonometry** (`cos/sin`) for even petals
- Positive messages and simple controls
- Compact, single-file prototype that’s easy to read and grade

---

## 🧩 Tech Stack

- **Language:** Python 3.9+  
- **GUI:** Tkinter (standard with Python)  
- **Math:** Python `math` module (for petal placement)

> No external packages required.

---

## 🚀 Getting Started

### 1) Prerequisites
- **Python 3.9+** installed  
  - Windows: `py --version`  
  - macOS/Linux: `python3 --version`

### 2) Clone or Download
```bash
# Option A: Clone
git clone https://github.com/ngoctuonglamdang-code/Pomodoro-Study-Flower
cd StudyFlower_PomodoroTimer

# Option B: Download ZIP
# - Click Code ▸ Download ZIP on GitHub, then unzip and cd into the folder.
