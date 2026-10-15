
import streamlit as st
import json
from datetime import datetime

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="CyberGuard AI | Security Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# PROFESSIONAL NEON UI
# ==================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --cyan: #00f5ff;
    --purple: #a855f7;
    --pink: #ff3cac;
    --green: #00ffa3;
    --background: #050816;
    --panel: #0c1428;
    --text: #edf7ff;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 5% 0%, #102957 0%, transparent 36%),
        radial-gradient(ellipse at 95% 25%, #24103f 0%, transparent 35%),
        #050816;
    color: var(--text);
}

[data-testid="stHeader"] {
    background: rgba(5, 8, 22, 0.85);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #080e20, #0d1128);
    border-right: 1px solid #00f5ff55;
    box-shadow: 5px 0 30px #00f5ff12;
}

[data-testid="stSidebar"] h2 {
    color: var(--cyan) !important;
}

h1 {
    color: #ffffff !important;
    font-weight: 800 !important;
    text-shadow: 0 0 24px #00f5ff30;
}

h2, h3 {
    color: #dffaff !important;
}

p, label, li {
    color: #b7c8e5;
}

div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #101d3a, #0a1023);
    border: 1px solid #00f5ff65;
    border-radius: 15px;
    padding: 19px;
    box-shadow: 0 0 18px #00f5ff12;
    transition: all 0.25s ease;
}

div[data-testid="stMetric"]:hover {
    border-color: #00f5ff;
    box-shadow: 0 0 25px #00f5ff35;
    transform: translateY(-3px);
}

[data-testid="stMetricLabel"] {
    color: #a8bad8 !important;
}

[data-testid="stMetricValue"] {
    color: #00f5ff !important;
    font-weight: 800;
    text-shadow: 0 0 14px #00f5ff45;
}

.panel {
    background: linear-gradient(135deg, #101c38ee, #0b1024ee);
    border: 1px solid #40547b;
    border-radius: 16px;
    padding: 22px;
    margin: 10px 0;
    box-shadow: 0 0 18px #7c3aed12;
    transition: all 0.25s ease;
}

.panel:hover {
    border-color: #a855f7;
    box-shadow: 0 0 25px #a855f72b;
    transform: translateY(-2px);
}

.neon-title {
    font-size: 12px;
    font-weight: 700;
    color: #00f5ff;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.status-dot {
    color: #00ffa3;
    text-shadow: 0 0 10px #00ffa3;
    font-weight: 700;
}

.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(100deg, #087eaf, #673de6);
    color: white;
    border: 1px solid #00f5ff75;
    border-radius: 10px;
    font-weight: 700;
    min-height: 44px;
    transition: all 0.25s ease;
    box-shadow: 0 0 16px #00cfff20;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background: linear-gradient(100deg, #00a9c7, #8b35ed);
    border-color: white;
    box-shadow: 0 0 25px #00f5ff55;
    color: white;
}

[data-testid="stExpander"] {
    background: #0b142a;
    border: 1px solid #34486b;
    border-radius: 12px;
}

[data-testid="stExpander"]:hover {
    border-color: #00f5ff90;
}

[data-baseweb="select"] > div {
    background-color: #111b35;
    border-color: #53658a;
}

input, textarea {
    background-color: #101a32 !important;
    color: white !important;
}

hr {
    border-color: #34466a;
}

.muted {
    color: #93a9c8;
    font-size: 13px;
}

.badge {
    display: inline-block;
    border: 1px solid #00f5ff75;
    background: #00f5ff12;
    color: #00f5ff;
    border-radius: 20px;
    padding: 5px 12px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

footer {
    visibility: hidden;
}

/* Hide Streamlit's top toolbar */
[data-testid="stToolbar"] {
    display: none !important;
}

/* Hide the Deploy button */
[data-testid="stDeployButton"] {
    display: none !important;
}

/* Hide the three-dot menu */
[data-testid="stMainMenu"] {
    display: none !important;
}

/* Hide the decoration at the top */
[data-testid="stDecoration"] {
    display: none !important;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# EXPERT KNOWLEDGE BASE
# ==================================================

KB = {
    "BR01": {
        "name": "Brute Force Attack",
        "category": "Account Security",
        "severity": "HIGH",
        "description": "Repeated authentication failures may indicate password guessing.",
        "symptoms": [
            "Repeated failed login attempts",
            "Unexpected account lockout"
        ],
        "recommendations": [
            "Review authentication logs and login history.",
            "Enable multi-factor authentication.",
            "Use strong passwords and rate limiting.",
            "Monitor repeated authentication failures."
        ]
    },

    "UA02": {
        "name": "Unauthorized Access",
        "category": "Account Security",
        "severity": "CRITICAL",
        "description": "Unknown logins or account changes may indicate unauthorized access.",
        "symptoms": [
            "Unknown login from another location",
            "Password changed without permission",
            "Unexpected MFA prompts"
        ],
        "recommendations": [
            "Change your password using a trusted device.",
            "Revoke unknown active sessions.",
            "Review recovery email and MFA settings.",
            "Contact the affected service provider."
        ]
    },

    "PH03": {
        "name": "Phishing Attack",
        "category": "Email Security",
        "severity": "HIGH",
        "description": "Suspicious messages may attempt to steal credentials or personal data.",
        "symptoms": [
            "Suspicious link received",
            "Message requests password or OTP",
            "Unexpected attachment from unknown sender"
        ],
        "recommendations": [
            "Avoid opening suspicious links or attachments.",
            "Never share passwords or OTPs.",
            "Verify the sender through an independent channel.",
            "Report the suspicious message."
        ]
    },

    "NW04": {
        "name": "Suspicious Network Activity",
        "category": "Network Security",
        "severity": "HIGH",
        "description": "Unusual traffic or unknown devices may require investigation.",
        "symptoms": [
            "Unusual network traffic",
            "Unknown device connected to network",
            "Repeated service disruption"
        ],
        "recommendations": [
            "Review router and firewall logs.",
            "Identify unfamiliar connected devices.",
            "Check recent network configuration changes.",
            "Contact a network administrator if activity persists."
        ]
    },

    "MW05": {
        "name": "Possible Malware",
        "category": "Endpoint Security",
        "severity": "CRITICAL",
        "description": "Unexpected software, disabled protection, or altered files may indicate malware.",
        "symptoms": [
            "Unknown application appeared",
            "Security software disabled unexpectedly",
            "Files encrypted or renamed unexpectedly"
        ],
        "recommendations": [
            "Avoid opening suspicious files.",
            "Run an updated, trusted security scan.",
            "Isolate a potentially compromised device if appropriate.",
            "Preserve evidence and contact your security administrator."
        ]
    },

    "DP06": {
        "name": "Possible Data Exposure",
        "category": "Data Privacy",
        "severity": "CRITICAL",
        "description": "Unexpected sharing or public disclosure may expose sensitive information.",
        "symptoms": [
            "Sensitive information appeared publicly",
            "Unexpected data transfer",
            "Files changed without permission"
        ],
        "recommendations": [
            "Identify the potentially exposed information.",
            "Revoke unknown sharing permissions.",
            "Preserve relevant audit logs.",
            "Notify the responsible security or privacy team."
        ]
    }
}

SEVERITY_ORDER = {
    "CRITICAL": 0,
    "HIGH": 1,
    "MEDIUM": 2,
    "LOW": 3
}

SEVERITY_COLORS = {
    "CRITICAL": "#ff3b6b",
    "HIGH": "#ffb020",
    "MEDIUM": "#5c9dff",
    "LOW": "#00ffa3"
}


# ==================================================
# SESSION STATE
# ==================================================

if "history" not in st.session_state:
    st.session_state.history = []

if "last_report" not in st.session_state:
    st.session_state.last_report = None


# ==================================================
# INFERENCE ENGINE
# ==================================================

def analyze_symptoms(selected):
    findings = []

    for rule_id, rule in KB.items():
        matched = [
            symptom
            for symptom in rule["symptoms"]
            if symptom in selected
        ]

        if matched:
            findings.append({
                "rule_id": rule_id,
                "name": rule["name"],
                "category": rule["category"],
                "severity": rule["severity"],
                "description": rule["description"],
                "evidence": matched,
                "recommendations": rule["recommendations"],
                "matched_count": len(matched)
            })

    findings.sort(
        key=lambda item: (
            SEVERITY_ORDER[item["severity"]],
            -item["matched_count"]
        )
    )

    return findings


def make_report(selected):
    findings = analyze_symptoms(selected)

    return {
        "report_id": "CG-" + datetime.now().strftime("%Y%m%d%H%M%S"),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "selected_symptoms": selected,
        "findings": findings,
        "assessment_type": "Rule-Based Expert System",
        "limitations": [
            "Based on user-reported symptoms.",
            "Not a live device or network scan.",
            "Severity is a configured priority, not attack probability."
        ]
    }


# ==================================================
# SIDEBAR NAVIGATION
# ==================================================

with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:12px 0 18px;">
        <div style="font-size:48px;
                    filter:drop-shadow(0 0 14px #00f5ff);">
            🛡️
        </div>
        <h2 style="color:#00f5ff !important;
                   text-shadow:0 0 18px #00f5ff70;
                   margin-bottom:4px;">
            CyberGuard AI
        </h2>
        <p style="font-size:10px;
                  letter-spacing:2px;
                  color:#a855f7;">
            SECURITY INTELLIGENCE
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    page = st.radio(
        "SECURITY CONSOLE",
        [
            "Security Operations Center",
            "Threat Analysis",
            "Threat Knowledge Base",
            "Expert Rules Engine",
            "Incident Reports"
        ],
        label_visibility="visible"
    )

    st.divider()

    st.markdown("### SYSTEM STATUS")
    st.markdown(
        '<p class="status-dot">● Knowledge Base Loaded</p>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="status-dot">● Inference Engine Ready</p>',
        unsafe_allow_html=True
    )

    st.caption("Python · Streamlit · IF–THEN Rules")
    st.caption("CyberGuard AI · v2.0")


# ==================================================
# SECURITY OPERATIONS CENTER
# ==================================================

if page == "Security Operations Center":

    st.markdown(
        '<p class="neon-title">SECURITY OPERATIONS CENTER</p>',
        unsafe_allow_html=True
    )

    st.title("Security Intelligence Dashboard")

    st.write(
        "Monitor assessment activity, explore cybersecurity knowledge "
        "and investigate rule-based threat findings."
    )

    st.markdown("""
    <div class="panel">
        <p class="neon-title">CYBERGUARD INTELLIGENCE ENGINE</p>
        <h2>Understand threats. Evaluate evidence. Act with confidence.</h2>
        <p>
            An explainable cybersecurity expert system that maps reported
            symptoms to security rules and recommended response actions.
        </p>
        <span class="badge">RULE-BASED ANALYSIS</span>
        &nbsp;
        <span class="badge">EXPLAINABLE FINDINGS</span>
        &nbsp;
        <span class="badge">INCIDENT REPORTING</span>
    </div>
    """, unsafe_allow_html=True)

    total_assessments = len(st.session_state.history)

    total_findings = sum(
        len(item["findings"])
        for item in st.session_state.history
    )

    critical_findings = sum(
        1
        for item in st.session_state.history
        for finding in item["findings"]
        if finding["severity"] == "CRITICAL"
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Expert Rules", len(KB))
    c2.metric("Threat Categories", len(KB))
    c3.metric("Assessments", total_assessments)
    c4.metric("Critical Findings", critical_findings)

    st.divider()

    st.subheader("Security Intelligence Tools")

    tools = [
        (
            "Threat Analysis",
            "Evaluate observed security indicators against expert rules.",
            "#00f5ff"
        ),
        (
            "Threat Knowledge Base",
            "Search threat definitions and security indicators.",
            "#a855f7"
        ),
        (
            "Expert Rules Engine",
            "Inspect IF–THEN reasoning and recommendations.",
            "#ff3cac"
        ),
        (
            "Incident Reports",
            "Review assessments and export incident reports.",
            "#00ffa3"
        )
    ]

    cols = st.columns(2)

    for index, (title, description, color) in enumerate(tools):
        with cols[index % 2]:
            st.markdown(
                f"""
                <div class="panel" style="border-left:4px solid {color};">
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.subheader("Recent Assessments")

    if not st.session_state.history:
        st.info(
            "No assessments recorded yet. Open Threat Analysis to begin."
        )
    else:
        for report in st.session_state.history[:5]:
            st.markdown(
                f"""
                <div class="panel">
                    <b>{report["report_id"]}</b>
                    <p class="muted">{report["timestamp"]}</p>
                    <p>Matching findings: {len(report["findings"])}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.caption(
        "Metrics represent this application's current session only."
    )


# ==================================================
# THREAT ANALYSIS
# ==================================================

elif page == "Threat Analysis":

    st.markdown(
        '<p class="neon-title">EXPERT THREAT ANALYSIS</p>',
        unsafe_allow_html=True
    )

    st.title("Threat Assessment")

    st.write(
        "Select the security indicators you have actually observed. "
        "The inference engine evaluates every matching rule."
    )

    st.warning(
        "Reported symptoms are indicators for investigation, not proof "
        "that a cyberattack has occurred."
    )

    all_symptoms = sorted({
        symptom
        for rule in KB.values()
        for symptom in rule["symptoms"]
    })

    with st.form("assessment_form"):

        selected = st.multiselect(
            "Observed security indicators",
            options=all_symptoms,
            placeholder="Search and select symptoms..."
        )

        submitted = st.form_submit_button(
            "⚡ RUN EXPERT ANALYSIS",
            use_container_width=True
        )

    if submitted:
        report = make_report(selected)

        st.session_state.last_report = report
        st.session_state.history.insert(0, report)
        st.session_state.history = st.session_state.history[:100]

    report = st.session_state.last_report

    if report is not None:

        st.divider()
        st.subheader("Analysis Results")

        st.markdown(
            f'<p class="muted">Report ID: {report["report_id"]}'
            f' &nbsp; | &nbsp; {report["timestamp"]}</p>',
            unsafe_allow_html=True
        )

        if not report["selected_symptoms"]:
            st.info(
                "No symptoms selected. No rules were triggered."
            )

        elif not report["findings"]:
            st.info(
                "No matching rules were identified for the selected symptoms."
            )

        else:
            highest = report["findings"][0]["severity"]

            st.markdown(
                f"""
                <div class="panel">
                    <p class="neon-title">ASSESSMENT PRIORITY</p>
                    <h2 style="color:{SEVERITY_COLORS[highest]} !important;">
                        {highest}
                    </h2>
                    <p>
                        {len(report["findings"])} threat category/categories
                        matched the selected indicators.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

            for index, finding in enumerate(report["findings"], start=1):

                color = SEVERITY_COLORS[finding["severity"]]

                with st.expander(
                    f'{index}. {finding["name"]} — {finding["severity"]}',
                    expanded=True
                ):

                    st.markdown(
                        f'<h3 style="color:{color} !important;">'
                        f'{finding["severity"]} PRIORITY</h3>',
                        unsafe_allow_html=True
                    )

                    st.write(finding["description"])

                    st.markdown("#### Matched Evidence")

                    for evidence in finding["evidence"]:
                        st.write(f"✓ {evidence}")

                    st.markdown("#### Recommended Actions")

                    for action in finding["recommendations"]:
                        st.write(f"• {action}")

                    st.markdown("#### Rule Trace")

                    st.code(
                        f'RULE ID: {finding["rule_id"]}\n'
                        f'IF: A configured symptom matches\n'
                        f'THEN: Suggest {finding["name"]}\n'
                        f'EVIDENCE MATCHES: {finding["matched_count"]}\n'
                        f'SEVERITY: {finding["severity"]}',
                        language="text"
                    )

        st.download_button(
            "⬇ Download Incident Report (JSON)",
            data=json.dumps(report, indent=2),
            file_name=f'{report["report_id"]}.json',
            mime="application/json",
            use_container_width=True
        )

        st.caption(
            "Findings are rule-based indicators, not verified incidents."
        )


# ==================================================
# THREAT KNOWLEDGE BASE
# ==================================================

elif page == "Threat Knowledge Base":

    st.markdown(
        '<p class="neon-title">CYBERSECURITY KNOWLEDGE REPOSITORY</p>',
        unsafe_allow_html=True
    )

    st.title("Threat Knowledge Base")

    st.write(
        "Search, filter and inspect the threat definitions used by the "
        "expert system."
    )

    query = st.text_input(
        "Search threats",
        placeholder="Search phishing, malware, network..."
    )

    categories = ["All"] + sorted({
        rule["category"] for rule in KB.values()
    })

    category = st.selectbox(
        "Filter by security domain",
        categories
    )

    visible = 0

    for rule_id, rule in KB.items():

        searchable = " ".join([
            rule_id,
            rule["name"],
            rule["category"],
            rule["description"],
            " ".join(rule["symptoms"]),
            " ".join(rule["recommendations"])
        ]).lower()

        if query.lower() not in searchable:
            continue

        if category != "All" and rule["category"] != category:
            continue

        visible += 1
        color = SEVERITY_COLORS[rule["severity"]]

        with st.expander(f'{rule["name"]} | {rule["severity"]}'):

            st.markdown(
                f'<p class="neon-title">{rule_id} · '
                f'{rule["category"]}</p>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<h3 style="color:{color} !important;">'
                f'{rule["severity"]} PRIORITY</h3>',
                unsafe_allow_html=True
            )

            st.write(rule["description"])

            st.markdown("#### Recognized Indicators")

            for symptom in rule["symptoms"]:
                st.write(f"• {symptom}")

            st.markdown("#### Recommended Response")

            for action in rule["recommendations"]:
                st.write(f"• {action}")

    if visible == 0:
        st.info("No matching knowledge entries found.")


# ==================================================
# EXPERT RULES ENGINE
# ==================================================

elif page == "Expert Rules Engine":

    st.markdown(
        '<p class="neon-title">INFERENCE & REASONING ENGINE</p>',
        unsafe_allow_html=True
    )

    st.title("Expert Rule Repository")

    st.write(
        "Inspect the predefined IF–THEN rules and understand how "
        "the system generates its findings."
    )

    st.markdown("""
    <div class="panel">
        <h3>Inference Workflow</h3>
        <p>01 · Collect reported symptoms</p>
        <p>02 · Match symptoms against the knowledge base</p>
        <p>03 · Evaluate all matching rules</p>
        <p>04 · Group evidence by threat category</p>
        <p>05 · Prioritize findings and display recommendations</p>
    </div>
    """, unsafe_allow_html=True)

    for rule_id, rule in KB.items():

        with st.expander(f'{rule_id} · {rule["name"]}'):

            st.code(
                f'RULE: {rule_id}\n'
                f'IF: Any configured symptom for this rule is selected\n'
                f'THEN: Suggest {rule["name"]}\n'
                f'CATEGORY: {rule["category"]}\n'
                f'SEVERITY: {rule["severity"]}',
                language="text"
            )

            st.markdown("#### Rule Conditions")

            for symptom in rule["symptoms"]:
                st.write(f"• {symptom}")

            st.markdown("#### Response Recommendations")

            for action in rule["recommendations"]:
                st.write(f"• {action}")

    st.caption(
        "Severity is a manually configured priority, not a statistical "
        "probability of an attack."
    )


# ==================================================
# INCIDENT REPORTS
# ==================================================

elif page == "Incident Reports":

    st.markdown(
        '<p class="neon-title">INCIDENT MANAGEMENT</p>',
        unsafe_allow_html=True
    )

    st.title("Incident History & Reports")

    st.write(
        "Review assessments generated during the current application session."
    )

    history = st.session_state.history

    if not history:

        st.info(
            "No assessment records found. Run an analysis to create a report."
        )

    else:

        total = len(history)

        total_findings = sum(
            len(report["findings"]) for report in history
        )

        critical = sum(
            1
            for report in history
            for finding in report["findings"]
            if finding["severity"] == "CRITICAL"
        )

        c1, c2, c3 = st.columns(3)

        c1.metric("Assessment Records", total)
        c2.metric("Total Findings", total_findings)
        c3.metric("Critical Findings", critical)

        st.divider()

        for index, report in enumerate(history):

            with st.expander(
                f'{report["report_id"]} · {report["timestamp"]}'
            ):

                st.write("**Selected Symptoms**")

                if report["selected_symptoms"]:
                    for symptom in report["selected_symptoms"]:
                        st.write(f"• {symptom}")
                else:
                    st.write("No symptoms selected.")

                st.write("**Expert Findings**")

                if report["findings"]:

                    for finding in report["findings"]:

                        color = SEVERITY_COLORS[finding["severity"]]

                        st.markdown(
                            f'<p style="color:{color};font-weight:700;">'
                            f'{finding["severity"]} · {finding["name"]}'
                            f'</p>',
                            unsafe_allow_html=True
                        )

                else:
                    st.write("No rules matched.")

                st.download_button(
                    "Download This Report",
                    data=json.dumps(report, indent=2),
                    file_name=f'{report["report_id"]}.json',
                    mime="application/json",
                    key=f"report_download_{index}"
                )

        st.download_button(
            "⬇ Export All Incident Records",
            data=json.dumps(history, indent=2),
            file_name="cyberguard_incident_history.json",
            mime="application/json",
            use_container_width=True
        )

        if st.button("Clear Session History"):
            st.session_state.history = []
            st.session_state.last_report = None
            st.rerun()

    st.caption(
        "History is stored in the current Streamlit session. "
        "It is not permanently saved to a database."
    )


# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<div style="
    text-align:center;
    padding:28px 0 10px;
    border-top:1px solid #263451;
    margin-top:35px;
">
    <p style="
        color:#00f5ff;
        font-size:12px;
        letter-spacing:2px;
        font-weight:700;
    ">CYBERGUARD AI</p>
    <p style="color:#8499b9;font-size:12px;">
        Security Intelligence · Explainable Rule-Based Analysis
    </p>
</div>
""", unsafe_allow_html=True)
