import os
import subprocess

def convert_pdf_to_jpeg(pdf_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    # Use pdftoppm to convert PDF to PPM image format
    output_prefix = os.path.join(output_folder, "image")
    subprocess.run(["pdftoppm", "-jpeg", pdf_path, output_prefix])

    # Rename the output file
    old_file = output_prefix + "-1.jpg"  # Assuming the output file is named "image-1.jpg"
    new_file = os.path.join(output_folder, "collatz-40.jpeg")  # Replace "output.jpg" with your desired new name
    os.rename(old_file, new_file)

    print("Conversion complete!")

# Example usage
pdf_file = "Pdf/collatz-40.pdf"  # Replace with the path to your PDF file
output_folder = "Png/"  # Replace with the desired output folder

convert_pdf_to_jpeg(pdf_file, output_folder)
