# NetworkGuard AI: Network Analysis

A PowerGuard AI module for transmission network studies. The network is built from per-equipment data (forms in the app
or one Excel form per equipment, or one Excel file for the whole network) and drawn as a single-line diagram.

## Analyses
- **Load flow** (Newton-Raphson): voltages, flows, loading, losses, outages and reactor switching.
- **Voltage drop** along every circuit and bus voltage margins.
- **Short circuit** (IEC 60909): three-phase and single-phase faults at every bus, breaker, making and short-time duty, branch currents.
- **Protection coordination**: distance zone reaches and times (R-X diagram), overcurrent / earth-fault grading (time-current curves).
- **N-1 contingency**: outage of every circuit and transformer.
- **Validation**: IEEE 9 and 14 bus published load flow results, IEC 60909 hand calculations, IEC 60255-151 relay curves.
- Combined PDF report and CSV / Excel downloads.

## Files
- `NetworkGuard_AI.app.py`: Streamlit app (main file). `networkguard_core.py`: engine. `networkguard_plots.py`: diagrams.
- `report_pdf.py`: PDF report. `pg_paths.py`: file locations. `logo.png`: logo.

Login credentials are read from the Streamlit secrets `APP_USERNAME` and `APP_PASSWORD`. Real network data is uploaded in
the app and must not be committed to this repository. The PowerGuard AI platform copies this module with `tools/sync_modules.py`.

© 2026 PowerGuard AI by Eng. Mahmoud Reda Ibrahim. Confidential and proprietary.
