# Hevy Data Visualizer

A tool for processing and cleaning workout logs exported from the Hevy training app. This script prepares raw CSV files for direct use in Power BI.

## Configuration
1. Body weight (kg) for calculations is defined in the `BODY_WEIGHT` variable within the script.
2. Input file path is set in line 6 of `prepare_data.py`.

## Power BI Setup
1. Open Power BI Desktop.
2. Go to **Transform data**.
3. In **Applied Steps**, click on the cogwheel next to **Source**.
4. Change the file path to your prepared CSV file (ensure Delimiter is set to **Semicolon**).
5. Click **Close & Apply**.
6. Refresh the dashboard.
