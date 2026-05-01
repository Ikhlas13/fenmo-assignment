import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Expense Tracker", layout="centered")

st.title("💰 Expense Tracker")

# -------- SESSION STORAGE --------
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# -------- ADD EXPENSE --------
st.header("➕ Add Expense")

with st.form("expense_form"):
    amount = st.number_input("Amount (₹)", min_value=0.0)
    category = st.text_input("Category")
    description = st.text_input("Description")
    date = st.date_input("Date")

    submitted = st.form_submit_button("Add Expense")

    if submitted:
        if amount <= 0:
            st.error("Amount must be greater than 0")
        elif category == "":
            st.error("Category is required")
        else:
            expense = {
                "id": len(st.session_state.expenses) + 1,
                "amount": amount,
                "category": category,
                "description": description,
                "date": date,
                "created_at": datetime.now()
            }
            st.session_state.expenses.append(expense)
            st.success("Expense added successfully!")

# -------- DISPLAY --------
st.header("📊 Expense List")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)

    # FILTER
    categories = ["All"] + sorted(df["category"].unique().tolist())
    selected_category = st.selectbox("Filter by category", categories)

    if selected_category != "All":
        df = df[df["category"] == selected_category]

    # SORT (Newest first)
    df = df.sort_values(by="date", ascending=False)

    # DISPLAY TABLE
    st.dataframe(df[["amount", "category", "description", "date"]])

    # TOTAL
    total = df["amount"].sum()
    st.markdown(f"### 💰 Total: ₹ {total}")

else:
    st.info("No expenses added yet.")
