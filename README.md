# Quality Inspection Management System

A simple Python tool to log quality inspections, with a Statistical Process Control (SPC) dashboard.

**Live dashboard:** https://quality-inspection-management-system-m7hheywolfwudh7tmwfepb.streamlit.app

Guide: [📄 SPC Dashboard Guide](./SPC-Dashboard-Guide.md) | [📂 Docs version](./docs/SPC-Dashboard-Guide.md)

### Why I built this
I've worked in manufacturing quality control for over 9 years at PG Bison. This project is my first step into Python and software, built around something close to the work I already know.

### What it does
- Asks for inspector name, production line, and equipment
- Records a Pass/Fail result for each inspection
- Loops so you can log multiple inspections in one session
- Tells you clearly if action is required on a failed inspection
- Shows a Pass/Fail total at the end of the shift

### SPC Dashboard
- Control chart with mean and 3-sigma upper/lower control limits
- Flags out-of-control points
- Calculates Cp and Cpk against your spec limits (LSL/USL)

### How to run it
pip install -r requirements.txt
python app.py
streamlit run dashboard.py

Built by Lelo - LeloNova Digitals