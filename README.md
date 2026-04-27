# QC Validation App (Erection vs Structural + IFC)

This app checks erection drawing member schedules against:
1. Structural drawing PDF text schedule
2. IFC model member properties

## What it validates
- Quantity differences for each `(element_id, section, length_mm)` tuple
- Length differences above a user-defined tolerance

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Input expectations
- **Erection drawing**: CSV/XLSX with columns (or aliases):
  - `element_id` (aliases: `mark`, `member_id`, `piece_mark`, `id`)
  - `section` (aliases: `profile`, `size`)
  - `length_mm` (aliases: `length`, `member_length`)
  - `quantity` (optional; default 1)
- **Structural drawing**: searchable PDF text containing lines like:
  - `B12 W310x39 L=6000 QTY=2`
- **IFC model**: reads `IfcStructuralMember`, `IfcBeam`, `IfcColumn` and tries to infer `section`/`length` from property sets.

## Notes
- IFC extraction quality depends on how your authoring tool stores properties.
- For production, you may add robust OCR for scanned PDFs and stricter IFC property mapping rules per your BIM standard.
