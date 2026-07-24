import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

import streamlit as st
import pandas as pd
from src.ai.retail_assistant import ask_retail_ai

# --- Page Configuration ---
st.set_page_config(
    page_title="Retail Analytics Copilot",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom High-End SaaS Styling (Dark Mode Theme) ---
st.markdown("""
    <style>
    /* Main Background & Font Color */
    .stApp {
        background-color: #0b0f19;
        color: #f8fafc;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid #1e293b;
    }
    
    /* Input Fields */
    .stTextInput>div>div>input {
        background-color: #111827;
        color: #f8fafc;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        font-size: 0.95rem;
    }
    .stTextInput>div>div>input:focus {
        border-color: #38bdf8;
        box-shadow: 0 0 0 1px #38bdf8;
    }
    
    /* Action Buttons */
    .stButton>button, div.stFormSubmitButton>button {
        width: 100%;
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: white;
        border-radius: 8px;
        font-weight: 600;
        border: none;
        padding: 0.6rem 1.2rem;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover, div.stFormSubmitButton>button:hover {
        background: linear-gradient(135deg, #0369a1 0%, #075985 100%);
        box-shadow: 0 4px 12px rgba(56, 189, 248, 0.25);
        color: white;
    }
    
    /* Metric Cards */
    .metric-card {
        background-color: #111827;
        padding: 1.25rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        border: 1px solid #1e293b;
        margin-bottom: 1rem;
    }
    .metric-title {
        font-size: 0.75rem;
        font-weight: 600;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.35rem;
    }
    .metric-value {
        font-size: 1.65rem;
        font-weight: 700;
        color: #38bdf8;
    }
    
    /* Tabs & Expander Adjustments */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #0b0f19;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #111827;
        border-radius: 6px;
        color: #94a3b8;
        border: 1px solid #1e293b;
        padding: 8px 16px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0284c7 !important;
        color: white !important;
        border-color: #0284c7 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("### ⚡ Retail Analytics Copilot")
    st.caption("Enterprise Retail Intelligence")
    st.markdown("---")
    
    st.markdown("**Capabilities**")
    st.markdown("""
    * **Text-to-SQL Engine**
    * **Low-Latency Execution**
    * **Automated Insights**
    """)
    
    st.markdown("---")
    st.markdown("**Quick Prompts**")
    if st.button("Top 5 Products by Revenue"):
        st.session_state.quick_prompt = "What are the top 5 best-selling products by revenue?"
    if st.button("Highest Spending Customers"):
        st.session_state.quick_prompt = "Who are the top 5 highest spending customers?"
    if st.button("Sales by Region"):
        st.session_state.quick_prompt = "Which city generated the highest sales revenue?"

# --- Main Interface Header ---
st.markdown("## 🛒 Retail Intelligence Workspace")
st.markdown("Ask anything about inventory, sales trends, or customer metrics in plain language.")

# --- Session State Initialization ---
if "response" not in st.session_state:
    st.session_state.response = None
if "quick_prompt" not in st.session_state:
    st.session_state.quick_prompt = ""

# --- Input Section with Form ---
default_q = st.session_state.quick_prompt if "quick_prompt" in st.session_state else ""
with st.form("ai_query_form", clear_on_submit=False):
    question = st.text_input(
        "**Query Workspace**",
        value=default_q,
        placeholder="e.g., What are the top 5 best-selling products?"
    )
    col_sub1, col_sub2 = st.run_cols([4, 1]) if hasattr(st, "run_cols") else st.columns([5, 1])
    with col_sub1:
        analyze_clicked = st.form_submit_button("Run Analysis ⚡")

# Reset quick prompt after capturing
if analyze_clicked:
    st.session_state.quick_prompt = ""

if analyze_clicked:
    if not question.strip():
        st.warning("⚠️ Please enter a valid business question before analyzing.")
    else:
        with st.spinner("Synthesizing query and scanning data warehouse..."):
            try:
                st.session_state.response = ask_retail_ai(question)
            except Exception as e:
                st.error(f"❌ Execution failed: {str(e)}")
                st.session_state.response = None

# --- Results Section ---
if st.session_state.response:
    response = st.session_state.response
    st.markdown("---")
    
    # --- Dynamic KPI Cards Extraction ---
    result_data = response.get("result")
    if result_data and isinstance(result_data, dict) and "data" in result_data and "columns" in result_data:
        df = pd.DataFrame(
            result_data["data"],
            columns=result_data["columns"]
        )
        
        if not df.empty and len(df.columns) >= 2:
            col_kpi1, col_kpi2 = st.columns(2)
            col_name_0 = df.columns[0]
            col_name_1 = df.columns[1]
            
            val_0 = str(df.iloc[0][col_name_0])
            val_1 = df.iloc[0][col_name_1]
            
            if pd.api.types.is_numeric_dtype(df[col_name_1]):
                formatted_val_1 = f"{val_1:,.2f}" if isinstance(val_1, float) else f"{val_1:,}"
            else:
                formatted_val_1 = str(val_1)
                
            with col_kpi1:
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-title">Top {col_name_0.replace('_', ' ').title()}</div>
                        <div class="metric-value">{val_0}</div>
                    </div>
                """, unsafe_allow_html=True)
                
            with col_kpi2:
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-title">{col_name_1.replace('_', ' ').title()}</div>
                        <div class="metric-value">{formatted_val_1}</div>
                    </div>
                """, unsafe_allow_html=True)

    # --- Interactive Output Tabs ---
    tab_insight, tab_sql, tab_data = st.tabs(["💡 Executive Summary", "💻 Generated SQL", "📋 Raw Data Output"])
    
    with tab_insight:
        st.markdown("### Key Takeaway")
        insight_text = response.get("insight", "No insight generated.")
        st.info(insight_text)
        
    with tab_sql:
        st.markdown("### Executed SQL Query")
        st.code(response.get("sql", "SELECT 1;"), language="sql")
        
    with tab_data:
        st.markdown("### Grid View")
        if result_data:
            if isinstance(result_data, dict) and "data" in result_data and "columns" in result_data:
                st.dataframe(df, use_container_width=True)
            else:
                st.json(result_data)
        else:
            st.warning("No data returned for this query.")