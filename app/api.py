from fastapi import FastAPI, HTTPException
from .summarizer import Summarizer
from .models import SummarizeRequest, SummarizeResponse
from .logger import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="openai_text_summarizer_v2",
    description="V2 : Résumeur de texte utilisant un LLM local open-source (Phi3 via Ollama).",
    version="2.0.0",
)

summarizer = Summarizer(model_name="phi3")


@app.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    try:
        logger.info("Requête /summarize reçue.")
        summary = summarizer.summarize_text(request.text)
        return SummarizeResponse(summary=summary)
    except ValueError as e:
        logger.error("Erreur de validation : %s", str(e))
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception("Erreur interne lors du résumé.")
        raise HTTPException(status_code=500, detail="Erreur interne lors de la génération du résumé.")
