import streamlit as st
import pandas as pd

from utils.log_reader import read_log_file
from agents.log_parser_agent import LogParserAgent
from agents.threat_intel_agent import ThreatIntelAgent
from agents.containment_agent import ContainmentAdvisorAgent
from memory.incident_db import save_incident, get_all_incidents

st.set_page_config(page_title="Cybersecurity Incident Response Agent", layout="wide")

log_parser = LogParserAgent()
threat_agent = ThreatIntelAgent()
containment_agent = ContainmentAdvisorAgent()

st.title("Cybersecurity Incident Response Agent")
st.subheader("Multi-Agent SOC Triage Workspace")

menu = st.sidebar.selectbox(
    "Choose Option",
    ["Analyze Incident", "View Incident History", "About"]
)

if menu == "Analyze Incident":
    st.header("Upload System Logs or Security Alerts")

    uploaded_file = st.file_uploader(
        "Upload a TXT or LOG file",
        type=["txt", "log"]
    )

    if uploaded_file:
        log_text = read_log_file(uploaded_file)

        if log_text.startswith("ERROR:"):
            st.error(log_text)
        else:
            st.subheader("Log Preview")
            st.code(log_text[:5000], language="text")

            if st.button("Analyze Incident"):
                with st.spinner("Log Parser Agent analyzing logs..."):
                    parsed_output = log_parser.run(log_text[:6000])

                if parsed_output.startswith("ERROR:"):
                    st.error(parsed_output)
                else:
                    with st.spinner("Threat Intelligence Agent reasoning..."):
                        threat_output = threat_agent.run(parsed_output)

                    if threat_output.startswith("ERROR:"):
                        st.error(threat_output)
                        st.subheader("Parsed Findings")
                        st.write(parsed_output)
                    else:
                        with st.spinner("Containment Advisor Agent generating response actions..."):
                            containment_output = containment_agent.run(threat_output)

                        if containment_output.startswith("ERROR:"):
                            st.error(containment_output)
                            st.subheader("Parsed Findings")
                            st.write(parsed_output)
                            st.subheader("Threat Analysis")
                            st.write(threat_output)
                        else:
                            save_incident(
                                uploaded_file.name,
                                parsed_output,
                                threat_output,
                                containment_output
                            )

                            st.success("Incident analysis completed and saved.")

                            st.subheader("Log Parser Findings")
                            st.write(parsed_output)

                            st.subheader("Threat Intelligence Analysis")
                            st.write(threat_output)

                            st.subheader("Containment Recommendations")
                            st.write(containment_output)

elif menu == "View Incident History":
    st.header("Stored Incident Sessions")
    incidents = get_all_incidents()

    if incidents:
        df = pd.DataFrame(incidents)
        st.dataframe(df[["timestamp", "filename"]], use_container_width=True)

        selected_index = st.number_input(
            "Select incident index",
            min_value=0,
            max_value=len(incidents) - 1,
            step=1
        )

        selected = incidents[selected_index]

        st.subheader(f"File: {selected['filename']}")
        st.write(f"Timestamp: {selected['timestamp']}")

        st.markdown("### Log Parser Findings")
        st.write(selected["parsed_output"])

        st.markdown("### Threat Intelligence Analysis")
        st.write(selected["threat_output"])

        st.markdown("### Containment Recommendations")
        st.write(selected["containment_output"])
    else:
        st.info("No incident sessions found yet.")

else:
    st.header("How It Works")
    st.markdown("""
**Workflow**
1. Upload system logs or alert text  
2. Log Parser Agent extracts suspicious events  
3. Threat Intelligence Agent infers possible threats  
4. Containment Advisor Agent recommends response actions  
5. Results are stored for future review  

**Use Cases**
- SOC triage assistance
- suspicious login analysis
- server alert investigation
- incident response support
- security operations demos
""")