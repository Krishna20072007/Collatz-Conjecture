import os
from pdf2image import convert_from_path
from PyPDF2 import PdfReader

def convert_pdf_to_jpeg(pdf_path, output_folder):
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)

    images = convert_from_path(pdf_path, dpi=300)

    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"collatz-40.jpg")
        image.save(image_path, "JPEG")

    print("Conversion complete!")

# Example usage
pdf_file = "Pdf/collatz-40.pdf"  # Replace with the path to your PDF file
output_folder = "Png/"  # Replace with the desired output folder

convert_pdf_to_jpeg(pdf_file, output_folder)