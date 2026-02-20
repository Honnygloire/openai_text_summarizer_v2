import pytest
from app.summarizer import Summarizer

class FakeLLM:
    def summarize(self, text: str) -> str:
        return "Résumé factice."

def test_summarizer_with_valid_text(monkeypatch):
    s = Summarizer()
    monkeypatch.setattr(s, "llm", FakeLLM())
    result = s.summarize_text("Ceci est un texte de test.")
    assert result == "Résumé factice."

def test_summarizer_with_empty_text():
    s = Summarizer()
    with pytest.raises(ValueError):
        s.summarize_text("")
