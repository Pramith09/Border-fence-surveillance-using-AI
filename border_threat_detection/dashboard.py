import streamlit as st
import json
import os

st.set_page_config(page_title="Smart Border Threat Dashboard", layout="wide")

st.title("🛡️ Smart Border Surveillance Dashboard")
st.markdown("---")

# Load results from JSON
threat_result_path = "output/threat_report.json"
if os.path.exists(threat_result_path):
    with open(threat_result_path) as f:
        results = json.load(f)
else:
    results = {
        "Sensor": {"vibration": 0.87, "seismic": 1.06, "intrusion_detected": True},
        "Vision": {"file": "assets/sample_video.mp4", "label": ["No detections"]},
        "NLP": ["violence", "terrorism"],
        "Threat Level": {"threat_score": 5, "threat_level": "Moderate Threat"}
    }

# Layout
col1, col2 = st.columns(2)

with col1:
    st.header("📡 Sensor Data")
    sensor = results["Sensor"]
    st.metric("Vibration", sensor["vibration"])
    st.metric("Seismic", sensor["seismic"])
    st.metric("Intrusion Detected", "✅" if sensor["intrusion_detected"] else "❌")

with col2:
    st.header("🎥 Vision Analysis")
    st.video(results["Vision"]["file"])
    st.write("Labels Detected:", results["Vision"]["label"])

st.header("📝 NLP Threat Keywords")
st.write(", ".join(results["NLP"]))

st.header("🚨 Final Threat Level")
threat = results["Threat Level"]
st.success(f"Threat Score: {threat['threat_score']}")
st.warning(f"Threat Level: {threat['threat_level']}")
