from .llm_client import LocalLLM
from .logger import get_logger

logger = get_logger(__name__)

class Summarizer:
    """
    Pipeline de résumé :
    - validation du texte
    - appel au LLM local
    - retour du résumé
    """

    def __init__(self, model_name: str = "phi3"):
        self.llm = LocalLLM(model=model_name)

    def summarize_text(self, text: str) -> str:
        logger.info("Début du pipeline de résumé.")
        cleaned_text = self._preprocess(text)
        summary = self.llm.summarize(cleaned_text)
        summary = self._postprocess(summary)
        logger.info("Fin du pipeline de résumé.")
        return summary

    def _preprocess(self, text: str) -> str:
        if not text or not text.strip():
            raise ValueError("Le texte fourni est vide.")
        return text.strip()

    def _postprocess(self, summary: str) -> str:
        return summary.strip()
