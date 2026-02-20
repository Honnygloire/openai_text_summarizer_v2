#  **openai_text_summarizer_v2**  
### *API de résumé de texte utilisant un LLM local open‑source via Ollama (phi3, Mistral, etc.)*

---

## 🚀 **Présentation**

`openai_text_summarizer_v2` est une API FastAPI permettant de **résumer automatiquement du texte** en utilisant un **LLM local open‑source** exécuté via **Ollama**.  
Le projet est conçu pour être :

- **modulaire** (pipeline clair et séparé)  
- **testable** (FakeLLM + tests unitaires)  
- **rapide** (phi3 par défaut)  
- **professionnel** (architecture propre, logs, API documentée)  

Il s’agit d’une version améliorée et optimisée du premier prototype, avec une architecture plus robuste et une meilleure gestion des modèles.

---

## 🧱 **Architecture du projet**

```
openai_text_summarizer_v2/
│
├── app/
│   ├── api.py              # API FastAPI (endpoints)
│   ├── summarizer.py       # Pipeline de résumé
│   ├── llm_client.py       # Client LLM (Ollama + FakeLLM)
│   └── __init__.py
│
├── tests/
│   ├── test_summarizer.py  # Tests du pipeline + FakeLLM
│   ├── test_api.py         # Tests de l’API FastAPI
│   └── __init__.py
│
├── examples/               # Exemples d’utilisation
├── requirements.txt        # Dépendances
└── README.md               # Documentation
```

---

## ⚙️ **Fonctionnement du pipeline**

Le pipeline suit 4 étapes :

1. **Réception du texte** via l’API  
2. **Nettoyage et préparation** du texte  
3. **Appel au modèle local** via Ollama  
4. **Retour du résumé** dans un JSON propre

Le pipeline est totalement indépendant du modèle utilisé.

---

## 🧠 **Modèles supportés**

Le projet supporte plusieurs modèles open‑source via Ollama :

| Modèle | Avantages | Usage |
|--------|-----------|--------|
| **phi3** | Très rapide, léger, idéal pour Mac | Modèle par défaut |
| **mistral** | Plus puissant mais très lent | Optionnel |
| **FakeLLM** | Instantané, idéal pour les tests | Utilisé dans pytest |

---

## 📡 **API FastAPI**

L’API expose un endpoint principal :

### `POST /summarize`

#### Exemple de requête :

```json
{
  "text": "Votre texte long ici..."
}
```

#### Exemple de réponse :

```json
{
  "summary": "Résumé généré par le modèle."
}
```

La documentation interactive est disponible sur :

```
http://127.0.0.1:8000/docs
```

---

## 🧪 **Tests unitaires**

Le projet inclut **3 tests essentiels** :

### ✔️ Test du faux modèle (FakeLLM)  
Vérifie que FakeLLM renvoie un résumé factice.

### ✔️ Test du pipeline Summarizer  
Vérifie que le pipeline fonctionne même sans vrai modèle.

### ✔️ Test de l’API FastAPI  
Vérifie que `/summarize` renvoie bien un résumé (HTTP 200 + champ `summary`).

### Lancer les tests :

```bash
export PYTHONPATH=$(pwd)
pytest -q
```

Résultat attendu :

```
3 passed
```

---

## 🛠️ **Installation**

### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 2. Installer Ollama  
Télécharger depuis : https://ollama.com

### 3. Télécharger un modèle

```bash
ollama pull phi3
```

ou

```bash
ollama pull mistral
```

---

## ▶️ **Lancer l’API**

```bash
uvicorn app.api:app --reload
```

L’API démarre sur :

```
http://127.0.0.1:8000
```

---

## 🎯 **Objectifs atteints**

- API fonctionnelle  
- Pipeline IA robuste  
- Modèle local rapide  
- Tests unitaires complets  
- Architecture professionnelle  
- Documentation claire  

---

## 🚀 **Améliorations possibles**

- Dockerisation du projet  
- Interface web (Streamlit / React)  
- Choix du modèle via un paramètre API  
- Résumé court / moyen / long  
- Logging avancé  
