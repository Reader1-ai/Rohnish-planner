import streamlit as st
from datetime import date

# 1. Page Configuration
st.set_page_config(
    page_title="Personal Category Planner",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Base Dark Theme & Dynamic Styling
st.markdown("""
<style>
    /* Global App Background */
    .stApp {
        background: #090d16;
        color: #f8fafc;
    }
    
    /* Card Container Base */
    .category-box {
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
    }

    /* Category Specific Themes */
    .theme-overview {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(148, 163, 184, 0.2);
    }
    .theme-piano {
        background: linear-gradient(135deg, rgba(88, 28, 135, 0.4) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(168, 85, 247, 0.4);
    }
    .theme-sax {
        background: linear-gradient(135deg, rgba(120, 53, 15, 0.4) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(245, 158, 11, 0.4);
    }
    .theme-chorus {
        background: linear-gradient(135deg, rgba(131, 24, 67, 0.4) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(244, 63, 94, 0.4);
    }
    .theme-studies {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.4) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(59, 130, 246, 0.4);
    }
    .theme-science {
        background: linear-gradient(135deg, rgba(6, 78, 59, 0.4) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(16, 185, 129, 0.4);
    }
    .theme-tech {
        background: linear-gradient(135deg, rgba(14, 116, 144, 0.4) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(6, 182, 212, 0.4);
    }
    .theme-social {
        background: linear-gradient(135deg, rgba(124, 45, 18, 0.4) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(249, 115, 22, 0.4);
    }

    /* Tab Header Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(15, 23, 42, 0.8);
        padding: 8px;
        border-radius: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 8px 16px;
        color: #94a3b8 !important;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4f46e5 !important;
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Category Definitions & Color Mapping
CATEGORIES = [
    "Piano", 
    "Sax", 
    "Chorus", 
    "Studies", 
    "Science Fair", 
    "Tech Fair", 
    "Social Studies Fair"
]

THEME_CLASSES = {
    "Piano": "theme-piano",
    "Sax": "theme-sax",
    "Chorus": "theme-chorus",
    "Studies": "theme-studies",
    "Science Fair": "theme-science",
    "Tech Fair": "theme-tech",
    "Social Studies Fair": "theme-social"
}

# 4. Session State Initialization
if 'tasks' not in st.session_state:
    st.session_state.tasks = [
        {"id": 1, "title": "Practice Vivaldi Summer Presto", "category": "Piano", "due": date.today(), "priority": "High", "done": False},
        {"id": 2, "title": "Review concert band arrangement", "category": "Sax", "due": date.today(), "priority": "Medium", "done": False},
        {"id": 3, "title": "Finalize Pratfall Effect project outline", "category": "Social Studies Fair", "due": date.today(), "priority": "High", "done": False},
    ]

# Task Addition Helper
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
st.caption("Organize tasks with distinct atmospheric visual themes for every category.")

# Sidebar Controls
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

# 5. Create Navigation Tabs
tab_labels = ["📌 Overview", "🎹 Piano", "🎷 Sax", "🎤 Chorus", "📚 Studies", "🔬 Science Fair", "💻 Tech Fair", "📜 Social Studies Fair"]
tabs
