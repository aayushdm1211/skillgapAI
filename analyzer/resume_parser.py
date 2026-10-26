import pymupdf


def extract_text_from_pdf(pdf_file):

    document = pymupdf.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    extracted_text = []

    try:
        for page in document:

            page_text = page.get_text()

            if page_text:
                extracted_text.append(page_text)

    finally:
        document.close()

    return "\n".join(extracted_text)