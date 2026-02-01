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
# HELPER: CHECK ROBOT OUTPUT
# -----------------------------
def robot_output_exists():
    return os.path.exists("results/output.xml")

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
st.markdown(
    '<div class="big-title">🤖 Intelligent CI/CD Oriented Automated Testing Framework</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="sub-text">Automated execution, intelligent failure detection, and CI/CD readiness</div>',
    unsafe_allow_html=True
)

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
            <h4>🧠 AI Analysis</h4>
            <p>Failure Pattern Detection</p>
            <p>Root Cause Insights</p>
        </div>
        """, unsafe_allow_html=True)

    st.success("Framework is ready for demonstration 🚀")

# =============================
# RUN TESTS
# =============================
elif menu == "Run Tests":
    st.subheader("🧪 Test Execution")

    st.warning(
        "⚠ Test execution is disabled on cloud deployment.\n\n"
        "Robot Framework tests are executed locally or via CI/CD pipelines "
        "(Jenkins / GitHub Actions)."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎓 Student Management System")
        if st.button("▶ Run Tests", use_container_width=True):
            st.info("Demo mode: Run tests locally or via CI/CD pipeline.")

    with col2:
        st.markdown("### 🛒 Grocery Application")
        if st.button("▶ Run Tests ", use_container_width=True):
            st.info("Demo mode: Run tests locally or via CI/CD pipeline.")

# =============================
# AI FAILURE ANALYSIS
# =============================
elif menu == "AI Failure Analysis":
    st.subheader("🧠 Intelligent Failure Analysis")

    st.info("AI scans Robot Framework logs and identifies failure patterns")

    if st.button("🔍 Run AI Analysis", use_container_width=True):

        # -------- DEMO MODE (NO output.xml) --------
        if not robot_output_exists():
            st.warning(
                "⚠ Robot Framework output not found.\n\n"
                "This application is running in demo / cloud mode.\n\n"
                "In real CI/CD pipelines, tests are executed first and the "
                "generated output.xml is analyzed by the AI module."
            )

            st.text_area(
                "📊 Sample AI Analysis Output (Demo Mode)",
                """Detected Failure Patterns:
- Login test failed due to invalid credentials
- Root Cause: Incorrect test data mapping
- Impacted Module: Authentication
- Severity: High

AI Recommendations:
- Validate credentials before execution
- Add retry logic for flaky tests
- Archive test artifacts in CI/CD pipeline
                """,
                height=320
            )

        # -------- REAL MODE (LOCAL / CI) --------
        else:
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

    st.info(
        "Reports are generated during local or CI/CD test execution.\n\n"
        "Download is available when artifacts exist."
    )

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
