import sys
import re

try:
    from pypdf import PdfReader
except ImportError:
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        print("No PDF library found.")
        sys.exit(1)

try:
    reader = PdfReader("/Users/duyanhle1501/Duy Anh Le Code/anhld.github.io/CV:DuyAnh.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    print(text)
except Exception as e:
    print(f"Error reading PDF: {e}")
