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
    "ELA",
    "Studies", 
    "Science Fair", 
    "Tech Fair", 
    "Social Studies Fair"
]

# Default Tasks Dataset
DEFAULT_TASKS = [
    # --- MUSIC & PROJECTS ---
    {"id": 1, "title": "Practice Vivaldi Summer Presto", "category": "Piano", "due": "2026-11-15", "priority": "High", "done": False},
    {"id": 2, "title": "Review concert band arrangement", "category": "Sax", "due": "2026-11-15", "priority": "Medium", "done": False},
    {"id": 3, "title": "Finalize Pratfall Effect project outline", "category": "Social Studies Fair", "due": "2026-11-20", "priority": "High", "done": False},
    
    # --- ELA (CANVAS ADVANCED ENG LIT/COMP 7) ASSIGNMENTS ---
    {"id": 4, "title": "Unit 2 Introduction Summary and EQ Answer", "category": "ELA", "due": "2026-10-14", "priority": "Low", "done": True},
    {"id": 5, "title": "Compound-Complex Sentence Quiz", "category": "ELA", "due": "2026-10-16", "priority": "Low", "done": True},
    {"id": 6, "title": "Timed Writing Compare and Contrast", "category": "ELA", "due": "2026-10-16", "priority": "Low", "done": True},
    {"id": 7, "title": "Story Synopsis", "category": "ELA", "due": "2026-10-20", "priority": "Medium", "done": True},
    {"id": 8, "title": "Noun Function Warm-up Quiz", "category": "ELA", "due": "2026-10-23", "priority": "Low", "done": True},
    {"id": 9, "title": "Selection Text: DTWAGE", "category": "ELA", "due": "2026-10-27", "priority": "Low", "done": True},
    {"id": 10, "title": "DTWAGE Essential Question Response", "category": "ELA", "due": "2026-10-28", "priority": "Low", "done": True},
    {"id": 11, "title": "DTWAGE Analysis Guide", "category": "ELA", "due": "2026-10-30", "priority": "Medium", "done": True},
    {"id": 12, "title": "Selection Text: Japan", "category": "ELA", "due": "2026-10-30", "priority": "Low", "done": True},
    {"id": 13, "title": "DLD 11/3", "category": "ELA", "due": "2026-11-03", "priority": "Low", "done": True},
    {"id": 14, "title": "Research Summary DLD", "category": "ELA", "due": "2026-11-03", "priority": "Medium", "done": True},
    {"id": 15, "title": "Japan Research on Moon and Mars Analysis Guide", "category": "ELA", "due": "2026-11-06", "priority": "High", "done": True},
    {"id": 16, "title": "Researching Plans for Human Settlement on the Moon and Mars", "category": "ELA", "due": "2026-11-06", "priority": "High", "done": True},
]

# Sidebar
