# Expense Tracker – Fenmo Assignment

## Overview
This is a minimal Expense Tracker application built using Streamlit.  
It allows users to add, view, filter, and analyze expenses.

---

## Features
- Add new expense (amount, category, description, date)
- View all expenses in a table
- Filter expenses by category
- Sort expenses by date (newest first)
- View total expense amount

---

## Tech Stack
- Python
- Streamlit
- Pandas

---

## Data Storage
- Used in-memory storage (Streamlit session_state)
- Chosen due to time constraints and simplicity
- In a real-world scenario, a database (SQLite/PostgreSQL) would be used

---

## Design Decisions
- Used Streamlit for rapid development
- Focused on functionality over UI design
- Ensured clean and readable code structure

---

## Trade-offs
- No persistent storage (data resets on refresh)
- Backend API not implemented separately
- Simplified architecture to meet time constraints

---

## What I Would Improve
- Add proper backend API (Flask/FastAPI)
- Add database persistence
- Improve UI/UX
- Add authentication
- Add automated tests

---

## How to Run Locally
```bash
pip install streamlit pandas
streamlit run app.py
