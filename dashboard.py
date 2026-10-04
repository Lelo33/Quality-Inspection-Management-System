"""SPC dashboard for the Quality Inspection Management System."""
import random

import matplotlib.pyplot as plt
import streamlit as st

from spc import control_limits, out_of_control, process_capability

st.title("SPC Dashboard")
st.caption("Statistical Process Control for QC inspection measurements")

source = st.radio("Data source", ["Sample data", "Paste my own measurements"])

if source == "Sample data":
    random.seed(42)
    samples = [round(random.gauss(50, 1.2), 2) for _ in range(30)]
    samples[17] = 57.0  # one deliberate out-of-control point
    st.info("Showing generated sample data, not real inspection results.")
else:
    raw = st.text_area(
        "Paste at least 5 measurements (commas, spaces or new lines)",
        "50.1, 49.8, 50.3, 50.0, 49.7, 50.2, 50.4, 49.9",
    )
    try:
        samples = [float(x) for x in raw.replace(",", " ").split()]
    except ValueError:
        st.error("Please enter numbers only.")
        st.stop()
    if len(samples) < 5 or len(set(samples)) < 2:
        st.warning("Enter at least 5 measurements that are not all identical.")
        st.stop()

lsl = st.number_input("Lower spec limit (LSL)", value=46.0)
usl = st.number_input("Upper spec limit (USL)", value=54.0)

limits = control_limits(samples)
flagged = out_of_control(samples)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(samples, marker="o", color="tab:blue", label="Measurement")
ax.axhline(limits["mean"], color="green", label="Mean")
ax.axhline(limits["ucl"], color="red", linestyle="--", label="UCL")
ax.axhline(limits["lcl"], color="red", linestyle="--", label="LCL")
if flagged:
    ax.scatter(
        [i for i, _ in flagged],
        [x for _, x in flagged],
        color="red", s=100, zorder=5, label="Out of control",
    )
ax.set_xlabel("Sample")
ax.set_ylabel("Measurement")
ax.legend()
st.pyplot(fig)

capability = process_capability(samples, lsl, usl)
col1, col2, col3 = st.columns(3)
col1.metric("Cp", capability["Cp"])
col2.metric("Cpk", capability["Cpk"])
col3.metric("Out-of-control points", len(flagged))

st.divider()
st.header("Defect prediction (machine learning)")
st.caption(
    "Logistic regression trained on simulated inspection data "
    "(80% train / 20% test). Not real production results."
)

from ml_model import predict_defect_probability, train_and_evaluate


@st.cache_resource
def get_model():
    return train_and_evaluate()


model, metrics = get_model()
m1, m2, m3 = st.columns(3)
m1.metric("Accuracy", metrics["accuracy"])
m2.metric("Precision", metrics["precision"])
m3.metric("Recall", metrics["recall"])

st.subheader("Try a reading")
dev = st.number_input("Deviation from target", value=0.0, step=0.1)
speed = st.number_input("Line speed", value=100.0, step=1.0)
temp = st.number_input("Temperature", value=70.0, step=1.0)

probability = predict_defect_probability(model, dev, speed, temp)
shown = ">99%" if probability > 0.995 else ("<1%" if probability < 0.005 else f"{probability:.0%}")
st.metric("Defect probability", shown)
if probability > 0.5:
    st.warning("High defect risk: action required.")
else:
    st.success("Low defect risk.")