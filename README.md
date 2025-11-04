# 🌸 Study Flower Pomodoro Timer

A creative-coding prototype for **A2: Code Prototype**.  
It turns the Pomodoro technique into a **calm, visual experience**: a digital flower **blooms** during focus time, **rests** on breaks, and **shrinks** when the cycle ends until you “water” it again.

- Author: Ngoc Tuong Lam Dang - 25088269  
- Course/Assessment: 52685 Working with Data and Code/ A2: Code Prototype Project  
- **Explainer Video (Unlisted):** `https://youtu.be/qcyTlRs2AJc`  
- **Reflection (PDF):** `[link if you host it]`


## Project Overview

The *Study Flower Pomodoro Timer* is a creative-coding prototype designed to visualise the Pomodoro technique as an interactive and emotionally engaging digital experience. Built entirely in Python using the Tkinter library, the project combines timing logic and simple animation to encourage mindful study habits.  

The program represents focus and rest cycles through the growth and contraction of a digital flower, providing a calm and visual representation of productivity. The timer is supported by motivational messages and a simple, pastel-toned interface.

---

## Key Features

- Customisable work and break durations  
- Event-driven timer using Tkinter’s `after()` method for smooth updates  
- Dynamic flower drawing with symmetrical petal placement using trigonometric functions  
- Visual and textual feedback through phase-based transitions  
- Lightweight and self-contained single-file implementation  

---

## Technical Information

**Language:** Python 3.9+  
**Libraries:** Tkinter, Math (standard libraries only)  
**No external dependencies required**

---

## How to Run the Program

1. Ensure that Python 3.9 or higher is installed.  
   - Check version in terminal or command prompt:  
     ```
     python --version
     ```
2. Download or clone the repository from GitHub:  
git clone https://github.com/ngoctuonglamdang-code/Pomodoro-Study-Flower
  
3. Navigate to the project directory and run the script:  
python PomodoroTimer.py

4. The application window will open.  
- Click **“Start Study Session”** to begin a focus period.  
- The timer will automatically switch to a break phase once time runs out.  
- After the break, a **“Water the Flower”** button will appear to restart the cycle.

---

## File Structure

StudyFlower_PomodoroTimer/

├── PomodoroTimer.py # Main Python file containing UI and timer logic
├── README.md # Project documentation

---

## Code Structure Summary

- **`draw_bloom()`**  
  Handles all drawing logic for the flower (petals, stem, and leaves).  
  Uses trigonometry (`math.cos`, `math.sin`) to position six petals evenly in a circular pattern.  

- **`update_timer()`**  
  Manages the countdown process using `root.after(1000, update_timer)` for one-second updates.  
  Switches between “work” and “break” phases automatically when time reaches zero.  

- **`start_work()`, `start_break()`, and `start_water_button()`**  
  Define the transition between phases and determine how the flower’s size and colour change.  

- **`format_mmss()`**  
  Converts raw seconds into minutes and seconds for the timer display.  

---

## Customisation Options

You can modify session durations at the top of the Python file:

```python
WORK_TIME = 25 * 60  # 25 minutes
BREAK_TIME = 5 * 60  # 5 minutes
Other adjustable parameters include flower size, colour scheme, and motivational messages.

Design Rationale
The timer’s design focuses on calm and clarity. The flower metaphor reinforces the idea of growth through consistent work and rest, aligning with reflective creative practice principles. The visual minimalism and positive reinforcement encourage sustained focus while maintaining a relaxing aesthetic.

Testing and Reliability
The program was tested to ensure:

Timer transitions occur smoothly between work and break cycles.

Flower resizing only happens when intended (after break completion).

The interface remains responsive throughout all transitions.

All functions operate within Tkinter’s event-driven framework to avoid performance issues such as window freezing.

Submission Details
Assessment: A2: Code Prototyple Project

Components:
3-minute explainer video (unlisted on YouTube)
1000-word written reflection
GitHub repository with full prototype

Academic Integrity and AI Declaration
This repository contains my original code and documentation for the Study Flower Pomodoro Timer project.
AI tools (ChatGPT) were used only for brainstorming, code explanation drafting, and writing support.
All final implementation and design decisions were completed by the author..
