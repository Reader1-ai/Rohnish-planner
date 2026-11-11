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

# 3. Session State Initialization
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
        st.toast(f"Task added to {category}!", icon="✅")

# Header Section
st.title("🎯 Multi-Category Activity Planner")
st.caption("Organize tasks across music, academic subjects, and project competitions.")

# Sidebar Controls & Analytics
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
    
    st.header("📊 Global Progress")
    total_tasks = len(st.session_state.tasks)
    completed_tasks = sum(1 for t in st.session_state.tasks if t["done"])
    progress = (completed_tasks / total_tasks) if total_tasks > 0 else 0.0
    
    st.progress(progress)
    st.write(f"**{completed_tasks} of {total_tasks}** tasks completed ({int(progress * 100)}%)")

# 4. Navigation Tabs Setup
tab_labels = ["📌 Overview", "🎹 Piano", "🎷 Sax", "🎤 Chorus", "📚 Studies", "🔬 Science Fair", "💻 Tech Fair", "📜 Social Studies Fair"]
tabs = st.tabs(tab_labels)

# --- OVERVIEW TAB ---
with tabs[0]:
    with st.container(border=True):
        st.subheader("📌 Global Summary Across All Categories")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Active Tasks", total_tasks - completed_tasks)
        with col2:
            st.metric("Completed Tasks", completed_tasks)
        with col3:
            st.metric("Total Categories", len(CATEGORIES))
        
        st.divider()
        
        st.write("### Pending Tasks")
        pending_tasks = [t for t in st.session_state.tasks if not t["done"]]
        if not pending_tasks:
            st.success("All tasks across all categories are completed!")
        else:
            for t in pending_tasks:
                st.checkbox(
                    f"[{t['category']}] {t['title']} — Due: {t['due']} ({t['priority']} Priority)",
                    value=t["done"],
                    key=f"overview_task_{t['id']}"
                )

# --- INDIVIDUAL CATEGORY TABS ---
for idx, cat in enumerate(CATEGORIES, start=1):
    with tabs[idx]:
        with st.container(border=True):
            st.subheader(f"📂 {cat} Workspace")
            
            cat_tasks = [t for t in st.session_state.tasks if t["category"] == cat]
            
            if not cat_tasks:
                st.info(f"No tasks listed for {cat}. Add one from the sidebar!")
            else:
                for task in cat_tasks:
                    cols = st.columns([0.05, 0.65, 0.15, 0.15])
                    
                    is_done = cols[0].checkbox("", value=task["done"], key=f"cat_{cat}_{task['id']}")
                    task["done"] = is_done
                    
                    if is_done:
                        cols[1].markdown(f"~~{task['title']}~~")
                    else:
                        cols[1].markdown(f"**{task['title']}**")
                    
                    prio = task["priority"]
                    color = "🔴" if prio == "High" else ("🟡" if prio == "Medium" else "🟢")
                    cols[2].write(f"{color} {prio}")
                    
                    cols[3].write(f"🗓️ {task['due']}")
