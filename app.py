import streamlit as st
from datetime import date

# 1. Page Configuration
st.set_page_config(
    page_title="Personal Category Planner",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Category Definitions
CATEGORIES = [
    "Piano", 
    "Sax", 
    "Chorus", 
    "Studies", 
    "Science Fair", 
    "Tech Fair", 
    "Social Studies Fair"
]

# 3. Initialize Session State
if 'tasks' not in st.session_state:
    st.session_state.tasks = [
        {"id": 1, "title": "Practice Vivaldi Summer Presto", "category": "Piano", "due": date.today(), "priority": "High", "done": False},
        {"id": 2, "title": "Review concert band arrangement", "category": "Sax", "due": date.today(), "priority": "Medium", "done": False},
        {"id": 3, "title": "Finalize Pratfall Effect project outline", "category": "Social Studies Fair", "due": date.today(), "priority": "High", "done": False},
    ]

# Helper Function to Add Tasks
def add_task(title, category, due_date, priority):
    if title.strip():
        new_id = max([t["id"] for t in st.session_state.tasks], default=0) + 1
        st.session_state.tasks.append({
            "id": new_id,
            "title": title,
            "category": category,
            "due": due_date,
            "priority": priority,
            "done": False
        })
        st.toast(f"Task added to **{category}**!", icon="✅")

# Header Section
st.title("🎯 Multi-Category Activity Planner")
st.caption("Organize tasks across music, academic subjects, and project competitions.")

# Sidebar - Add Task & Analytics
with st.sidebar:
    st.header("➕ Add New Task")
    with st.form("add_task_form", clear_on_submit=True):
        task_title = st.text_input("Task Description")
        task_cat = st.selectbox("Category", CATEGORIES)
        task_due = st.date_input("Due Date", value=date.today())
        task_prio = st.selectbox("Priority", ["Low", "Medium", "High"], index=1)
        
        submitted = st.form_submit_button("Add Task", use_container_width=True)
        if submitted:
            add_task(task_title, task_cat, task_due, task_prio)

    st.divider()
    
    # Progress Calculation
    st.header("📊 Total Progress")
    total_tasks = len(st.session_state.tasks)
    completed_tasks = sum(1 for t in st.session_state.tasks if t["done"])
    progress = (completed_tasks / total_tasks) if total_tasks > 0 else 0.0
