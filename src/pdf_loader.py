import requests
from io import BytesIO
from pypdf import PdfReader


def extract_text_from_url(pdf_url):

    response = requests.get(pdf_url)

    response.raise_for_status()

    reader = PdfReader(BytesIO(response.content))

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    if not text.strip():
        raise ValueError("PDF has no readable text.")

    return text.strip()