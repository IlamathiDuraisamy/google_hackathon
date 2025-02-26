import pytesseract
import cv2
import sqlite3
from pdf2image import convert_from_path
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    extracted_text = ""
    
    for image in images:
        img_path = "temp_img.png"
        image.save(img_path, "PNG")
        extracted_text += extract_text_from_image(img_path) + "\n"
        os.remove(img_path)

    return extracted_text.strip()

def save_to_database(document_type, extracted_text):
    conn = sqlite3.connect('automation.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO documents (document_type, extracted_text) VALUES (?, ?)", 
                   (document_type, extracted_text))
    
    conn.commit()
    conn.close()
    print("Data saved to database successfully!")

def process_document(file_path):
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
        document_type = "PDF"
    else:
        text = extract_text_from_image(file_path)
        document_type = "Image"

    save_to_database(document_type, text)

file_path = "C:\\Users\\prabakaran.r\\Downloads\\image2.png" 
process_document(file_path)
