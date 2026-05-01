import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Expense Tracker")

# Initialize session state
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# -------- ADD EXPENSE --------
st.header("Add Expense")

amount = st.number_input("Amount", min_value=0.0)
category = st.text_input("Category")
description = st.text_input("Description")
date = st.date_input("Date")

if st.button("Add Expense"):
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date,
        "created_at": datetime.now()
    }
    st.session_state.expenses.append(expense)
    st.success("Expense added!")

# -------- SHOW EXPENSES --------
st.header("Expense List")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)

    # Filter
    unique_categories = df["category"].unique()
    selected_category = st.selectbox("Filter by category", ["All"] + list(unique_categories))

    if selected_category != "All":
        df = df[df["category"] == selected_category]

    # Sort
    df = df.sort_values(by="date", ascending=False)

    # Show table
    st.dataframe(df)

    # Total
    total = df["amount"].sum()
    st.write(f"### Total: ₹{total}")

else:
    st.write("No expenses yet.")
