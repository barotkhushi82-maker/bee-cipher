import streamlit as st
from cipher_engine import BeeCipherEngine
from bee_ingest import BeeTranscriptIngestor

st.set_page_config(
    page_title="Bee Cipher | Wearable Privacy Shield",
    page_icon="🐝",
    layout="wide"
)

st.title("🐝 Bee Cipher — Wearable Privacy & Security Shield")
st.caption("Real-time PII redaction, vishing detection, and SDK product feedback for Bee wearable AI transcripts.")

tab1, tab2 = st.tabs(["🛡️ Security Dashboard", "💬 Devpost Required Feedback"])

with tab1:
    st.header("Live Bee Transcript Stream Processor")
    
    sample_text = st.selectbox(
        "Load Preset Bee Wearable Log:",
        [
            "Custom Input",
            "Sample 1: Passcode Leak - 'User said: My password is SecurePass2026! Call me at 555-019-2834.'",
            "Sample 2: Vishing Scam - 'Caller said: This is an urgent bank transfer verification. Wire funds now immediately.'"
        ]
    )
    
    if sample_text == "Custom Input":
        raw_text = st.text_area("Raw Ingested Text:", "User said: My credit card is 4111-2222-3333-4444 and passcode is 9988.", height=120)
    else:
        raw_text = sample_text.split(" - ")[1].strip("'")
        st.text_area("Raw Ingested Text:", raw_text, height=120, disabled=True)
        
    if st.button("Run Security Scan"):
        engine = BeeCipherEngine()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔒 Sanitized Bee Transcript")
            st.success(engine.redact_pii(raw_text))
            
        with col2:
            st.subheader("⚠️ Threat Assessment")
            scam = engine.detect_scam(raw_text)
            if scam["is_high_risk"]:
                st.error(f"🚨 Vishing Threat Flagged! Score: {scam['risk_score']}/100")
                st.write("Trigger Words:", scam["detected_threats"])
            else:
                st.info("✅ No active social engineering threats detected.")

with tab2:
    st.header("📝 Required SDK & Tool Feedback")
    st.markdown("""
    * **Tool / SDK Used:** Bee Wearable AI Data Export & Transcript Log Stream (`daily/YYYY-MM-DD/summary.md`).
    * **Primary Use Case:** Ambient filtering layer that strips sensitive credentials (PII) and flags phone scam patterns before transcript data is logged or shared.
    * **What Worked Well:** The structured markdown summary output makes parsing conversation lines straightforward and clean.
    * **What Needs Improvement:** Real-time WebSocket streaming endpoints would allow instant millisecond-level redaction as audio is transcribed.
    * **Onboarding Experience (Zero to Hello World):** Smooth and completed in under 10 minutes; clear file path guidelines in documentation.
    * **Would We Build With It Again?** Yes, Bee's lightweight wearable transcript output provides a great foundation for privacy-focused ambient computing.
    """)
