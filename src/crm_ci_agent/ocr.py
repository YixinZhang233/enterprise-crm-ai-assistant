from __future__ import annotations

from pathlib import Path


def ocr_placeholder(input_path: str | Path) -> str:
    """Placeholder for OCR or multimodal screenshot parsing.

    In a production system, replace this function with an OCR or vision model
    integration. For this public demo, the input is a text transcript or a
    screenshot description.
    """

    path = Path(input_path)
    return path.read_text(encoding="utf-8")
