from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from PIL import Image
import qrcode
import os
import subprocess

def convert_image_to_bw(image_path, output_path):
    """
    Convert the input image to black-and-white and save it to the output path.
    """
    with Image.open(image_path) as img:
        # Convert the image to grayscale and then to black-and-white
        bw_image = img.convert("L").point(lambda x: 0 if x < 128 else 255, "1")
        bw_image.save(output_path)

def generate_label_pdf(filename, qr_content, label_text, label_width=50*mm, label_height=25*mm, image_path=None):
    # Create a new PDF canvas
    c = canvas.Canvas(filename, pagesize=(label_width, label_height))

    # Generate QR code image
    qr = qrcode.make(qr_content)
    qr_filename = "qr_code.png"
    qr.save(qr_filename)

    # Draw QR code on the canvas
    c.drawImage(qr_filename, 4*mm, 4*mm, width=17*mm, height=17*mm)

    # Draw additional image if provided
    if image_path and os.path.exists(image_path):
        # Convert the image to black-and-white
        bw_image_path = "bw_image.png"
        convert_image_to_bw(image_path, bw_image_path)

        # Place the black-and-white image next to the QR code
        c.drawImage(bw_image_path, 25*mm, 9*mm, width=12*mm, height=12*mm)

        # Clean up the temporary black-and-white image
        if os.path.exists(bw_image_path):
            os.remove(bw_image_path)

    # Draw label text
    c.setFont("Helvetica", 10)
    c.drawString(22*mm , 6*mm, label_text)

    # Save the PDF
    c.save()

    # Clean up the QR code image
    if os.path.exists(qr_filename):
        os.remove(qr_filename)

def print_pdf(pdf_file, printer_name, timeout=10):
    # Use the lp command to send the PDF to the specified printer

    try:
        subprocess.run(["lp", "-d", printer_name, "-o", "media=Custom.50x25mm", pdf_file], check=True)
        print(f"Printed {pdf_file} to printer {printer_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to print {pdf_file}: {e}")

if __name__ == "__main__":
    # Example usage
    pdf_filename = "label_with_qr.pdf"
    printer_name = "PM-241-BT"  # Replace with your printer name
    additional_image = ".doc/images/git_logo.png"
    generate_label_pdf(pdf_filename, "https://www.github.com", "Hello, World!", image_path=additional_image)

    # Print the generated PDF
    print_pdf(pdf_filename, printer_name)