import streamlit as st
from pdf_functions import annotate_pdf_with_ocr

# Title
st.title(":rainbow[PDF OCR for AI Learning]")

# Save the Uploaded File
uploaded_pdf = st.file_uploader(label="Scanned PDF Here: ", type=['pdf'])

if uploaded_pdf is not None:
    # Save the uploaded file to a temporary location
    temp_pdf_path = f"temp_{uploaded_pdf.name}"
    with open(temp_pdf_path, "wb") as f:
        f.write(uploaded_pdf.getbuffer())

    # Process the File
    annotate_pdf_with_ocr(temp_pdf_path)
    st.success(f"Annotated PDF saved as annotated_{uploaded_pdf.name}")