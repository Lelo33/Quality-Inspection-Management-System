# Quality Inspection Management System

A simple Python tool to log quality inspections, with a Statistical Process Control (SPC) dashboard.

Live dashboard: https://quality-inspection-management-system-m7hheywoifwudh7tmwfepb.streamlit.app

Guide (PDF)/(SPC-Dashboard-Guide.pdf)

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
- Runs on sample data by default, or paste your own measurements to see your own chart

## Defect prediction (machine learning)
- Logistic regression classifier that estimates the probability an inspection is a defect
- Trained with an 80/20 train/test split and evaluated on accuracy, precision and recall
- Uses the absolute deviation from target as a feature, since a reading too high or too low is equally risky
- Note: trained on simulated data, not real inspection results. The simulated data has little noise, so predictions at extreme readings are very confident.

## Labs
Three short Python exercises with starter code, solutions and self-checks. See the `labs` folder:
- Pass rate and failed inspections
- SPC run rule (7 points on one side of the mean)
- Rank production lines by defect rate

## How to run it
1. Make sure you have Python installed
2. Open your terminal in the project folder
3. Run the logger: `python app.py`
4. Run the dashboard: `pip install -r requirements.txt`, then `streamlit run dashboard.py`

## Files
- `app.py` - inspection logger
- `spc.py` - SPC calculations (control limits, out-of-control points, Cp/Cpk)
- `dashboard.py` - Streamlit SPC dashboard
- `ml_model.py` - defect prediction model
- `requirements.txt` - Python libraries the dashboard needs
- `labs/` - Python exercises with solutions and self-checks
- `GUIDE.md` - SPC Dashboard Guide

## What's next
- Record real measurements and save inspections to a file
- Connect the dashboard to real inspection data
