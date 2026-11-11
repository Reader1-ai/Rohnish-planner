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
        background: linear-gradient(135deg, rgba(124, 45,
