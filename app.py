import streamlit as st
import pandas as pd
from datetime import datetime, date

# 1. Page Configuration
st.set_page_config(
    page_title="Personal Category Planner",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Background & Styling
st.markdown("""
    <style>
    /* Gradient Dark Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
        color: #f8fafc;
    }
    
    /* Card Styles for Categories */
    .category-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 15px;
        backdrop-filter: blur(10px);
    }
    
    /* Custom Header Styling */
    .main-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 8px 16px;
        background-color: rgba(30, 41, 59, 0.5);
    }

    .stTabs [aria-selected="true"] {
        background-color: #4f46e5 !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Initialize Session State for Data Persistence
if 'tasks' not in st.session_state:
    st.session_state.tasks = [
        {"title": "Practice Vivaldi Summer Presto", "category": "Piano", "due": date.today(), "priority": "High", "done": False},
        {"title": "Work on Band Arrangement", "category": "Sax", "due": date.today(), "priority": "Medium", "done": False},
        {"title": "Social Studies Fair Data Analysis", "category": "Social Studies Fair", "due": date.today(), "priority": "High", "done": False},
    ]

CATEGORIES = [
    "Piano", 
    "Sax", 
    "Chorus", 
    "Studies", 
    "Science Fair", 
    "Tech Fair", 
    "Social Studies Fair"
]

# Helper Functions
def add_task(title, category, due_date, priority):
    if title.strip():
        st.session_state.tasks.append({
            "title": title,
            "category": category,
            "due": due_date,
            "priority": priority,
            "done": False
        })
        st.toast(f"Task added to **{category}**!", icon="✅")

def get_category_tasks(cat):
    return [t for t in st.session_state.tasks if t["category"] == cat]

# Header Section
st.markdown('<h1 class="main-title">🎯 Personal Activity & Fair Planner</h1>', unsafe_allow_html=True)
st.caption("Organize tasks across music, academics, and competition projects.")

# Sidebar - Quick Add Task
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
    
    # Progress Summary Dashboard
    st.header("📊 Global Progress")
    total_tasks = len(st.session_state.tasks)
    completed_tasks = sum(1 for t in st.session_state.tasks if t["done"])
    progress = (completed_tasks / total_tasks) if total_tasks > 0 else 0.0
    
    st.progress(progress)
    st.write(f"**{completed_tasks} of {total_tasks}** tasks completed ({int(progress * 100)}%)")

# Main Content - Category Tabs
tab_list = st.tabs(["Overview"] + CATEGORIES)

# --- OVERVIEW TAB ---
with tab_list[0]:
    st.subheader("📌 Task Overview Across All Categories")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Active Tasks", total_tasks - completed_tasks)
    with col2:
        st.metric("Completed Tasks", completed_tasks)
    with col3:
        st.metric("Total Tracked Categories", len(CATEGORIES))
    
    st.divider()
    
    # Show pending tasks grouped by priority
    st.write("### Upcoming Priority Items")
    for t in st.session_state.tasks:
        if not t["done"]:
            st.checkbox(
                f"**[{t['category']}]** {t['title']} — *Due: {t['due']}* ({t['priority']} Priority)",
                value=t["done"],
                key=f"overview_{t['category']}_{t['title']}"
            )

# --- CATEGORY SPECIFIC TABS ---
for idx, cat in enumerate(CATEGORIES, start=1):
    with tab_list[idx]:
        st.subheader(f"📂 {cat} Tasks")
        
        cat_tasks = get_category_tasks(cat)
        
        if not cat_tasks:
            st.info(f"No tasks in **{cat}** yet. Add one from the sidebar!")
        else:
            for i, task in enumerate(cat_tasks):
                cols = st.columns([0.05, 0.65, 0.15, 0.15])
                
                # Task checkbox
                is_done = cols[0].checkbox("", value=task["done"], key=f"{cat}_check_{i}")
                task["done"] = is_done
                
                # Title formatting
                if is_done:
                    cols[1].markdown(f"~~{task['title']}~~")
                else:
                    cols[1].markdown(f"**{task['title']}**")
                
                # Priority badge
                prio = task["priority"]
                color = "🔴" if prio == "High" else ("🟡" if prio == "Medium" else "🟢")
                cols[2].write(f"{color} {prio}")
                
                # Due date
                cols[3].write(f"🗓️ {task['due']}")
