import streamlit as st

st.set_page_config(page_title="Personal Expense Tracker")

st.title("💰 Personal Expense Tracker")

st.write("Welcome to your Expense Tracker!")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, category = line.strip().split(",")
                st.session_state.expenses.append({
                    "Amount": float(amount),
                    "Category": category
                })
    except FileNotFoundError:
        pass

amount = st.number_input("Enter Amount", min_value=0.0)

category = st.selectbox(
    "Select Category",
    ["Food", "Travel", "Shopping", "Other"]
)

if st.button("Add Expense"):
    if amount > 0:
        st.session_state.expenses.append(
            {"Amount": amount, "Category": category}
        )
        st.success("Expense Added Successfully!")
    else:
        st.warning("Please enter an amount greater than 0.")

st.subheader("📋 Your Expenses")

for expense in st.session_state.expenses:
    st.write(
        f"₹{expense['Amount']} - {expense['Category']}"
    )

total = sum(
    expense["Amount"]
    for expense in st.session_state.expenses
)

st.subheader(f"Total Expenses: ₹{total}")
st.subheader("💾 Save Your Expenses")

if st.button("Save Expenses"):
    with open("expenses.txt", "w") as file:
        for expense in st.session_state.expenses:
            file.write(
                f"{expense['Amount']},{expense['Category']}\n"
            )
    st.success("Expenses Saved Successfully!")
