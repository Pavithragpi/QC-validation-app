import streamlit as st
from dxf_reader import read_dxf, extract_columns
from ifc_reader import load_ifc, get_ifc_columns
from comparator import compare

st.title("Steel Validation Tool")

# Upload files
struct_file = st.file_uploader("Upload Structural DXF", type=["dxf"])
erect_file = st.file_uploader("Upload Erection DXF", type=["dxf"])
ifc_file = st.file_uploader("Upload IFC", type=["ifc"])

if st.button("Run Validation"):

    if struct_file and erect_file:
        st.write("🔄 Reading DXF files...")

        struct_msp = read_dxf(struct_file)
        erect_msp = read_dxf(erect_file)

        struct_cols = extract_columns(struct_msp)
        erect_cols = extract_columns(erect_msp)

        st.write("📊 Structural Columns:", len(struct_cols))
        st.write("📊 Erection Columns:", len(erect_cols))

        missing = compare(struct_cols, erect_cols)

        st.write("❌ Missing Columns in Erection:")
        st.write(missing)

    if ifc_file:
        st.write("🔄 Reading IFC file...")

        model = load_ifc(ifc_file)
        ifc_cols = get_ifc_columns(model)

        st.write("📊 Total IFC Columns:", len(ifc_cols))
