
from pathlib import Path

import pymupdf
from docx import Document


def clean_resume_text(text):
    """Clean extracted resume text."""
    text = text.strip()
    text = " ".join(text.split())
    return text


def extract_skills(text):
    """Find selected technical skills in resume text."""
    skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "NLP",
        "LLM",
        "FastAPI",
    ]

    found_skills = []

    for skill in skills:
        if skill.casefold() in text.casefold():
            found_skills.append(skill)

    return found_skills


def extract_pdf_text(file_path):
    """Extract text from a PDF resume."""
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("Expected a PDF file.")

    extracted_text = []

    with pymupdf.open(path) as pdf:
        for page in pdf:
            extracted_text.append(page.get_text())

    return clean_resume_text("\n".join(extracted_text))


def extract_docx_text(file_path):
    """Extract text from a Word resume."""
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".docx":
        raise ValueError("Expected a DOCX file.")

    document = Document(path)

    paragraphs = [
        paragraph.text
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    return clean_resume_text("\n".join(paragraphs))
