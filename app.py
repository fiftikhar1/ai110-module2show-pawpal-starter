from datetime import time

import streamlit as st
from scheduler import create_daily_plan

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

availability_col1, availability_col2 = st.columns(2)
with availability_col1:
    available_start = st.time_input("Available from", value=time(8, 0))
with availability_col2:
    available_end = st.time_input("Available until", value=time(17, 0))

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.tasks.append(
        {"title": task_title, "duration_minutes": int(duration), "priority": priority}
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("Tasks are scheduled by priority within the owner's available hours.")

if st.button("Generate schedule"):
    if available_end <= available_start:
        st.error("Available until must be later than Available from.")
    elif not st.session_state.tasks:
        st.info("Add at least one care task to build a schedule.")
    else:
        scheduled_tasks, unscheduled_tasks = create_daily_plan(
            st.session_state.tasks,
            available_start,
            available_end,
        )

        if scheduled_tasks:
            st.write(f"Daily plan for {owner_name} and {pet_name} ({species})")
            st.table(
                [
                    {
                        "Start": task["start_time"],
                        "Task": task["title"],
                        "Duration (minutes)": task["duration_minutes"],
                        "Priority": task["priority"],
                        "End": task["end_time"],
                    }
                    for task in scheduled_tasks
                ]
            )
        else:
            st.warning("No tasks fit within the selected availability window.")

        if unscheduled_tasks:
            st.warning("These tasks did not fit and were left unscheduled:")
            st.table(unscheduled_tasks)
