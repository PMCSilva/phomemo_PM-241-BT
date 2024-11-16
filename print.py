from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import qrcode
import os
import subprocess

def generate_label_pdf(filename, qr_content, label_text, label_width=50*mm, label_height=25*mm):
    # Create a new PDF canvas
    c = canvas.Canvas(filename, pagesize=(label_width, label_height))

    # Generate QR code image
    qr = qrcode.make(qr_content)
    qr_filename = "qr_code.png"
    qr.save(qr_filename)

    # Draw QR code on the canvas
    c.drawImage(qr_filename, 5*mm, 5*mm, width=15*mm, height=15*mm)

    # Draw label text
    c.setFont("Helvetica", 10)
    c.drawString(22*mm , 11*mm, label_text)

    # Save the PDF
    c.save()

    # Clean up the QR code image
    if os.path.exists(qr_filename):
        os.remove(qr_filename)

def print_pdf_linux(pdf_file, printer_name):
    # Use the lp command to send the PDF to the specified printer
    try:
        subprocess.run(["lp", "-d", printer_name, "-o", "media=Custom.50x25mm", pdf_file], check=True)
        print(f"Printed {pdf_file} to printer {printer_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to print {pdf_file}: {e}")

if __name__ == "__main__":
    # Example usage
    pdf_filename = "label_with_qr.pdf"
    printer_name = "_PM_241_BT"  # Replace with your printer name
    generate_label_pdf(pdf_filename, "https://www.github.com", "Hello, World!")

    # Print the generated PDF
    print_pdf_linux(pdf_filename, printer_name)
