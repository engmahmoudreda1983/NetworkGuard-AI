# NetworkGuard AI: Network Analysis

A PowerGuard AI module for transmission network studies. The network is built from per-equipment data (forms in the app
or one Excel form per equipment, or one Excel file for the whole network) and drawn as a single-line diagram.

## Analyses
- **Load flow** (Newton-Raphson): voltages, flows, loading, losses, outages and reactor switching.
- **Voltage drop** along every circuit and bus voltage margins.
- **Short circuit** (IEC 60909): three-phase and single-phase faults at every bus, breaker, making and short-time duty, branch currents.
- **Protection coordination**: distance zone reaches and times (R-X diagram), overcurrent / earth-fault grading (time-current curves).
- **N-1 contingency**: outage of every circuit and transformer.
- **Fault study**: a real fault on a line, taken from FaultGuard (platform or incidents CSV), read from the disturbance records and event lists
  (FaultGuard engine), or entered by hand: currents from both ends, voltage dips, expected relay operation, comparison with the measured values
  and the fault location that best matches the measured currents.
- **Verification** (internal, `tests/test_engine.py`; document on request or as a report appendix): IEEE 9 and 14 bus published load flow results,
  the IEC TR 60909-4 example network, IEC 60909 hand calculations and IEC 60255-151 relay curves.
- Combined PDF report and CSV / Excel downloads.

## Files
- `NetworkGuard_AI.app.py`: Streamlit app (main file). `networkguard_core.py`: engine. `networkguard_plots.py`: diagrams.
- `report_pdf.py`: PDF report. `pg_paths.py`: file locations. `logo.png`: logo.
- `networkguard_import.py`: single-line diagram from a PDF drawing, equipment data from relay settings and documents.
- `iec60909_4_example.py`: IEC TR 60909-4 example network for the verification.
- `faultguard_core.py`, `comtrade_features.py`, `faultguard_model.pkl`: FaultGuard engine used to read disturbance records.

Login credentials are read from the Streamlit secrets `APP_USERNAME` and `APP_PASSWORD`. Real network data is uploaded in
the app and must not be committed to this repository. The PowerGuard AI platform copies this module with `tools/sync_modules.py`.

© 2026 PowerGuard AI by Eng. Mahmoud Reda Ibrahim. Confidential and proprietary.
