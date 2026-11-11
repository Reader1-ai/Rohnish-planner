import streamlit as st
from datetime import date

# 1. Page Configuration
st.set_page_config(
    page_title="Personal Category Planner",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Background & Tab Styling
st.markdown("""
<style>
    /* Dark Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
        color: #f8fafc;
    }
    
    /* Main Title Styling */
    .main-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }

    /* Customizing Streamlit Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: rgba(15, 23, 42, 0.6);
        padding: 6px;
        border-radius: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 6px;
        padding: 8px 14px;
        background-color: rgba(30, 41, 59, 0.5);
        color: #94a3b8 !important;
        font-weight: 600;
    }

    .stTabs [aria-selected="true"] {
        background-color: #6366f1 !important;
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Category Definitions
CATEGORIES = [
    "Piano", 
    "Sax", 
    "Chorus", 
    "Studies", 
    "Science Fair", 
    "Tech Fair", 
    "Social Studies Fair"
]

# 4. Initialize Session State
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
st.markdown('<h1 class="main-title
            
