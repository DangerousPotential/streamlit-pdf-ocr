import streamlit as st
from pdf_functions import annotate_pdf_with_ocr
import os

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
    annotated_pdf_path = annotate_pdf_with_ocr(temp_pdf_path)

    # Read the annotated PDF file for download
    with open(annotated_pdf_path, "rb") as f:
        annotated_pdf_data = f.read()

    # Provide download button
    st.download_button("Download Annotated PDF", data=annotated_pdf_data, file_name=os.path.basename(annotated_pdf_path))

    st.success(f"Annotated PDF available for download!")

    # Clean up temporary files
    os.remove(temp_pdf_path)
    os.remove(annotated_pdf_path)
