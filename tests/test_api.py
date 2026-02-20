from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_api_summarize():
    payload = {
        "text": "La transition énergétique est devenue un enjeu majeur pour les entreprises du secteur industriel, et EDF ne fait pas exception. Face à l’augmentation de la demande en électricité et aux impératifs environnementaux, l’entreprise investit massivement dans des technologies innovantes pour moderniser ses infrastructures. L’intelligence artificielle joue un rôle central dans cette transformation. Grâce à des modèles prédictifs avancés, EDF peut anticiper les pics de consommation, optimiser la production dans ses centrales et réduire les pertes sur le réseau. L’IA permet également d’améliorer la maintenance des équipements en détectant plus tôt les anomalies, ce qui limite les risques d’incidents et prolonge la durée de vie des installations. Ces innovations s’inscrivent dans une stratégie globale visant à renforcer la sécurité du réseau, améliorer l’efficacité opérationnelle et accélérer la transition vers des sources d’énergie plus durables. En combinant expertise humaine et technologies intelligentes, EDF se positionne comme un acteur clé de l’avenir énergétique."
    }

    response = client.post("/summarize", json=payload)

    # Vérifie que l'API répond correctement
    assert response.status_code == 200
    data = response.json()

    # Vérifie que la réponse contient un résumé
    assert "summary" in data
    assert isinstance(data["summary"], str)
    assert len(data["summary"]) > 0
