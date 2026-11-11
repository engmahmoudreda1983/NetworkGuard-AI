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
- **Equipment data from relay settings**: MiCOM .set files, a .zip of the settings project folder (the folder names give the circuit,
  e.g. 41_EAST_NORTH), or settings exports (PDF, picture, Excel, CSV, TXT). Each file is put on its line and line end from the relay's own
  station, the far end in its description and the circuit name; one button applies all recognised files, line data from the newest file
  of each line and relay data from the newest file of each relay, and lines whose relays carry different line data are listed.
- **3D view** of the network (three.js, runs in the browser, no internet needed): the network after it is built, the load flow
  (flows and bus voltages) and the fault playback (fault point, currents, voltage dips and the tripping sequence in time),
  also downloadable as one HTML file. A FaultGuard incident is applied to the network with one button: the line is matched
  from the station names in the incident and the location is turned to the From end of the network line.
- Combined PDF report and CSV / Excel downloads.

## Files
- `NetworkGuard_AI.app.py`: Streamlit app (main file). `networkguard_core.py`: engine. `networkguard_plots.py`: diagrams.
- `report_pdf.py`: PDF report. `pg_paths.py`: file locations. `logo.png`: logo.
- `networkguard_import.py`: single-line diagram from a PDF drawing, equipment data from relay settings and documents.
- `iec60909_4_example.py`: IEC TR 60909-4 example network for the verification.
- `networkguard_3d.py` and `networkguard_assets/`: 3D view (template and three.js r160, MIT licence).
- `faultguard_core.py`, `comtrade_features.py`, `faultguard_model.pkl`: FaultGuard engine used to read disturbance records.

Login credentials are read from the Streamlit secrets `APP_USERNAME` and `APP_PASSWORD`. Real network data is uploaded in
the app and must not be committed to this repository. The PowerGuard AI platform copies this module with `tools/sync_modules.py`.

© 2026 PowerGuard AI by Eng. Mahmoud Reda Ibrahim. Confidential and proprietary.
