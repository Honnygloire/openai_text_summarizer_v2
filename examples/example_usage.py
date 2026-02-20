from app.summarizer import Summarizer

if __name__ == "__main__":
    texte = """
    EDF est un acteur majeur de la production et de la distribution d'électricité en France.
    La transition énergétique, l'optimisation des ressources et l'innovation autour de l'IA
    sont au cœur de ses enjeux stratégiques.
    """

    summarizer = Summarizer(model_name="mistral")
    resume = summarizer.summarize_text(texte)
    print("=== TEXTE ORIGINAL ===")
    print(texte.strip())
    print("\n=== RÉSUMÉ ===")
    print(resume)
