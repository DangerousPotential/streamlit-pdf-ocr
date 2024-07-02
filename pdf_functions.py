import os
import fitz
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

# Convert PDF into Images
def add_annotation_to_pdf(pdf_path, annotations):
    doc = fitz.open(pdf_path)
    for page_num, text in annotations.items():
        page = doc.load_page(page_num)
        rect = fitz.Rect(50, 50, 550, 800)
        page.add_freetext_annot(rect, text, fontsize=12)
    annotated_pdf_path = "annotated_" + os.path.basename(pdf_path)
    doc.save(annotated_pdf_path)
    return annotated_pdf_path

# Perform OCR on a single image
def ocr_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

# Process each page of the PDF and annotate
def annotate_pdf_with_ocr(pdf_path):
    images = convert_from_path(pdf_path)
    annotations = {}
    for i, image in enumerate(images):
        # Save image to a temporary file
        temp_image_path = f"temp_image_{i}.png"  # Create a unique temporary file name
        image.save(temp_image_path)
        
        text = ocr_image(temp_image_path)  # Pass the file path to ocr_image
        annotations[i] = text
        
        # Remove temporary file (optional, but good practice)
        os.remove(temp_image_path)
        
    # Add annotations to pdf
    annotated_pdf_path = add_annotation_to_pdf(pdf_path, annotations)
    return annotated_pdf_path
