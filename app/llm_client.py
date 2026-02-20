import requests
from .logger import get_logger

logger = get_logger(__name__)

class LocalLLM:
    """
    Client pour un LLM local via Ollama (ex : phi3).
    Nécessite Ollama lancé en local :
    - installer Ollama
    - `ollama pull phi3`
    - `ollama serve` (souvent automatique)
    """

    def __init__(self, model: str = "phi3", base_url: str = "http://localhost:11434"):
        self.model = model
        self.url = f"{base_url}/api/generate"

    def summarize(self, text: str) -> str:
        if not text or not text.strip():
            raise ValueError("Le texte à résumer est vide.")

        prompt = (
            "Tu es un assistant qui résume des textes en français.\n"
            "Résume le texte suivant de manière claire, concise et structurée.\n\n"
            f"Texte :\n{text}\n\n"
            "Résumé :"
        )

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        logger.info("Appel au LLM local (modèle=%s)", self.model)
        response = requests.post(self.url, json=payload, timeout=60)
        response.raise_for_status()

        data = response.json()
        summary = data.get("response", "").strip()

        if not summary:
            raise RuntimeError("Le LLM n'a pas renvoyé de résumé exploitable.")

        logger.info("Résumé généré avec succès.")
        return summary
