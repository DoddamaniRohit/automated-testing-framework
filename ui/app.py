import streamlit as st
import subprocess
import sys
import os
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Intelligent CI/CD Automated Testing Framework",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
.big-title {
    font-size: 34px;
    font-weight: 700;
}
.sub-text {
    color: #6c757d;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #f8f9fa;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}
.footer {
    text-align: center;
    color: gray;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("⚙ CI/CD Control Panel")
st.sidebar.markdown("Navigate framework modules")

menu = st.sidebar.radio(
    "Select Module",
    ["Dashboard", "Run Tests", "AI Failure Analysis", "Reports"]
)

st.sidebar.markdown("---")
st.sidebar.info("Robot Framework + CI/CD + AI")

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="big-title">🤖 Intelligent CI/CD Oriented Automated Testing Framework</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Automated execution, intelligent failure detection, and CI/CD readiness</div>', unsafe_allow_html=True)

st.markdown("---")

# =============================
# DASHBOARD
# =============================
if menu == "Dashboard":
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h4>🧪 Test Suites</h4>
            <p>Student Management</p>
            <p>Grocery Application</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h4>🤖 Automation</h4>
            <p>Robot Framework</p>
            <p>CI/CD Ready</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h4>🧠 Intelligent System Analysis</h4>
            <p>Failure Pattern Detection</p>
            <p>Root Cause Insights</p>
        </div>
        """, unsafe_allow_html=True)

    st.success("Framework is ready for execution")

# =============================
# RUN TESTS
# =============================
elif menu == "Run Tests":
    st.subheader("🧪 Test Execution")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎓 Student Management System")
        if st.button("▶ Run Tests", use_container_width=True):
            with st.spinner("Executing Student Management tests..."):
                subprocess.run(
                    ["robot", "--outputdir", "results", "tests/student_management"],
                    shell=True
                )
            st.success("Student Management tests completed")

    with col2:
        st.markdown("### 🛒 Grocery Application")
        if st.button("▶ Run Tests ", use_container_width=True):
            with st.spinner("Executing Grocery App tests..."):
                subprocess.run(
                    ["robot", "--outputdir", "results", "tests/grocery_app"],
                    shell=True
                )
            st.success("Grocery App tests completed")


elif menu == "AI Failure Analysis":
    st.subheader("🧠 Intelligent Failure Analysis")

    st.info("AI scans Robot Framework logs and identifies failure patterns")

    if st.button("🔍 Run AI Analysis", use_container_width=True):
        with st.spinner("Analyzing test results using AI..."):
            result = subprocess.run(
                [sys.executable, "ai_module/test_result_analyzer.py"],
                capture_output=True,
                text=True
            )

        if result.returncode == 0:
            st.success("AI Analysis Completed Successfully")
            st.text_area(
                "📊 Intelligent Analysis Output",
                result.stdout,
                height=400
            )
        else:
            st.error("AI Analyzer failed")
            st.text_area(
                "❌ Error Output",
                result.stderr,
                height=250
            )

# =============================
# REPORTS
# =============================
elif menu == "Reports":
    st.subheader("📄 Test Reports")

    report_path = "results/report.html"
    log_path = "results/log.html"

    col1, col2 = st.columns(2)

    with col1:
        if os.path.exists(report_path):
            with open(report_path, "r", encoding="utf-8") as f:
                st.download_button(
                    "⬇ Download Test Report",
                    f.read(),
                    file_name="report.html",
                    mime="text/html",
                    use_container_width=True
                )
        else:
            st.warning("Test report not found")

    with col2:
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as f:
                st.download_button(
                    "⬇ Download Test Log",
                    f.read(),
                    file_name="log.html",
                    mime="text/html",
                    use_container_width=True
                )
        else:
            st.warning("Test log not found")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown(
    f"<div class='footer'>An Intelligent CI/CD Oriented Automated Testing Framework | {datetime.now().year}</div>",
    unsafe_allow_html=True
)