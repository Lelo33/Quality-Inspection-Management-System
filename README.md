# Quality Inspection Management System

A simple Python tool to log quality inspections, with a Statistical Process Control (SPC) dashboard.

**Live dashboard:** https://quality-inspection-management-system-m7hheywoifwudh7tmwfepb.streamlit.app

## Why I built this
I've worked in manufacturing quality control for over 9 years.
This project is my first step into Python and software, built around something close to the work I already know.

## What it does
- Asks for inspector name, production line, and equipment
- Records a Pass/Fail result for each inspection
- Loops so you can log multiple inspections in one session
- Tells you clearly if action is required on a failed inspection
- Shows a Pass/Fail total at the end of the shift

## SPC dashboard
- Control chart with the mean and 3-sigma upper/lower control limits
- Flags out-of-control points
- Calculates Cp and Cpk against your spec limits (LSL/USL)
- Note: the dashboard currently runs on sample data, not real inspection results

## How to run it
1. Make sure you have Python installed
2. Open your terminal in the project folder
3. Run the logger: `python app.py`
4. Run the dashboard: `pip install -r requirements.txt`, then `streamlit run dashboard.py`

## Files
- `app.py` - inspection logger
- `spc.py` - SPC calculations (control limits, out-of-control points, Cp/Cpk)
- `dashboard.py` - Streamlit SPC dashboard

## What's next
- Record real measurements and save inspections to a file
- Connect the dashboard to real inspection data
- Add a defect prediction model (machine learning)