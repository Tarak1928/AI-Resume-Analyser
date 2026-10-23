
import pytest

from resume_parser import (
    clean_resume_text,
    extract_skills,
    extract_pdf_text,
    extract_docx_text,
)


def test_clean_resume_text():
    assert clean_resume_text("  Python   Developer  ") == "Python Developer"


def test_extract_skills():
    result = extract_skills("I know Python, SQL and FastAPI")

    assert "Python" in result
    assert "SQL" in result
    assert "FastAPI" in result


def test_no_skills_found():
    assert extract_skills("I enjoy reading books") == []


def test_extract_pdf_text():
    text = extract_pdf_text("sample_resume.pdf")

    assert "Python Developer" in text
    assert "SQL" in text


def test_extract_docx_text():
    text = extract_docx_text("sample_resume.docx")

    assert "Python Developer" in text
    assert "FastAPI" in text


def test_missing_pdf_raises_error():
    with pytest.raises(FileNotFoundError):
        extract_pdf_text("missing_resume.pdf")


def test_wrong_file_extension_raises_error(tmp_path):
    wrong_file = tmp_path / "resume.txt"
    wrong_file.write_text("Sample resume", encoding="utf-8")

    with pytest.raises(ValueError):
        extract_pdf_text(wrong_file)
