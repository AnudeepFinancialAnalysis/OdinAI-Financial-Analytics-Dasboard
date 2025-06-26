import streamlit as st
from data_loader import load_data
from charts import (
    growth_scatter_plot,
    funding_per_employee_competitors_chart,
    valuation_per_employee_competitors_chart,
    headcount_vs_valuation_competitors_chart,
    funding_vs_founding_year,
    valuation_competitors_chart   # <--- ADD THIS
)


import base64
from pathlib import Path

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title='Odin AI vs Peers | Analytics',
    layout='wide',
    initial_sidebar_state='collapsed'
)

# ---- BACKGROUND IMAGE (BASE64) ----
def set_bg_from_local(png_file):
    with open(png_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    bg_style = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

set_bg_from_local("pure.webp")

# ---- CUSTOM STYLING ----
st.markdown("""
    <style>
        .caption-text {
            font-size: 0.9rem;
            color: #BBBBBB;
            margin-top: -10px;
            margin-bottom: 30px;
        }
        .stTabs [data-baseweb="tab-list"] {
            margin-bottom: 20px;
        }
        h1, h2, h3 {
            color: #FAFAFA;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# ---- TITLE & INTRO ----
st.title("🧠 Odin AI vs the AI World")
st.markdown(
    """
    <div style="color:#9cdcf5; font-size:1.15em; font-weight:500; margin-bottom:1em;">
        <span>Analysis by <b>Anudeep Koneru</b> &mdash; using publicly available data from sources including <b>Crunchbase</b>, <b>Growjo</b>, and <b>Wellfound</b> (AngelList).</span>
    </div>
    """, unsafe_allow_html=True
)

# ---- LOAD DATA ----
df = load_data()

# ---- CHART TABS ----
tabs = st.tabs([
    "📈 Growth vs Funding",
    "💸 Capital Intensity",
    "👥 Headcount vs Valuation",
    "📅 Year Founded vs Funding",
    "🏆 Valuation Leaders"
])

with tabs[0]:
    st.header("Growth vs Funding")
    st.plotly_chart(growth_scatter_plot(df), use_container_width=True)
    st.markdown('<div class="caption-text">Each company’s funding is compared against its employee growth rate. Odin AI appears as a high-growth, well-funded outlier.</div>', unsafe_allow_html=True)

with tabs[1]:
    st.header("Capital Intensity")
    st.plotly_chart(funding_per_employee_competitors_chart(df), use_container_width=True)
    st.plotly_chart(valuation_per_employee_competitors_chart(df), use_container_width=True)
    st.markdown('<div class="caption-text">These charts assess capital intensity by dividing funding and valuation by headcount.</div>', unsafe_allow_html=True)

with tabs[2]:
    st.header("Headcount vs Valuation")
    st.plotly_chart(headcount_vs_valuation_competitors_chart(df), use_container_width=True)
    st.markdown('<div class="caption-text">This scatter plot shows how company valuations correlate with team size.</div>', unsafe_allow_html=True)

with tabs[3]:
    st.header("Funding vs Founding Year")
    st.plotly_chart(funding_vs_founding_year(df), use_container_width=True)
    st.markdown('<div class="caption-text">Visualizing the speed of fundraising relative to founding date.</div>', unsafe_allow_html=True)

with tabs[4]:
    st.header("Valuation of Competitors")
    st.plotly_chart(valuation_competitors_chart(df), use_container_width=True)
    st.markdown('<div class="caption-text">This chart ranks the top 10 companies by valuation.</div>', unsafe_allow_html=True)

st.markdown("---")
st.header("Why I’m the Right Hire for Your Data Science & AI Team")

st.markdown("""
<div style="font-family: 'Segoe UI', 'Roboto', Arial, sans-serif; padding: 1.5em; background: rgba(36,36,36,0.82); border-radius: 18px; box-shadow: 0 2px 16px rgba(0,0,0,0.18);">
    <h2 style="color:#FFC300; margin-bottom:0.25em; font-size:2.3em; font-weight:800; letter-spacing:-2px;">Anudeep Koneru</h2>
    <div style="margin-bottom: 1em; font-size: 1.2em;">
        <a href="mailto:anudeepk@umd.edu" style="color:#fff; text-decoration:none;" target="_blank">📧 anudeepk@umd.edu</a> &nbsp;|&nbsp;
        <a href="https://www.linkedin.com/in/anudeepkoneru" style="color:#0a66c2; text-decoration:none;" target="_blank"><b>in</b> LinkedIn</a> &nbsp;|&nbsp;
        <a href="https://anudeepkoneru.com/" style="color:#ff7e21; text-decoration:none;" target="_blank">🌐 Portfolio</a> &nbsp;|&nbsp;
        <a href="https://github.com/anudeepkoneru14" style="color:#d7d7d7; text-decoration:none;" target="_blank"><b>🐙 GitHub</b></a>
    </div>
    <p style="font-size:1.13em; color:#eaeaea; font-weight:400; margin-bottom:1.3em;">
        <b style="color:#ffd700;">MSIS grad</b> from the University of Maryland (<b>GPA 4.0</b>, Phi Kappa Phi), deeply hands-on in data science, machine learning, and analytics.<br>
        My journey: <b>TA</b> for advanced analytics, built LLM chatbots, graph-based recsys, and AI dashboards used by real decision-makers.<br>
        <span style="color:#c4e17f;"><b>Tech Stack:</b></span> Python, Spark, Neo4j, SQL, Scikit-learn, PyTorch, GCP, Databricks, Tableau, and more.<br>
        I thrive where data, business, and product intersect—delivering not just code or charts, but insights that move the needle.<br>
        <b style="color:#F7941E;">Storytelling + Analysis + Execution = Impact.</b>
    </p>
    <hr style="border-top: 1.3px dashed #777; margin: 1.2em 0 1.1em 0;">
    <h3 style="color:#71fae9; font-size:1.38em; margin-bottom:0.45em; font-family: 'Fira Sans', Arial, sans-serif;">Why Odin AI?</h3>
    <p style="font-size:1.08em; color:#e4f6fa;">
        Odin AI sits at the intersection of <b>real-world ML, product innovation, and impact</b>—right where I want to be.<br>
        My analytical rigor, ML know-how, and energy can help unlock your data's full value and push the company’s vision to the next level.<br>
        Let's build, experiment, and create solutions that scale—together.
    </p>
</div>
""", unsafe_allow_html=True)
