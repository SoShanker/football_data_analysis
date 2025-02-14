from fastapi import FastAPI, HTTPException
import pandas as pd
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser les requêtes du frontend Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adresse de Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_DIR = "../FootballData/"  # Dossier contenant les fichiers CSV

@app.get("/api/rankings")
def get_rankings(year: str, league: str):
    file_path = os.path.join(DATA_DIR, f"{league}/ranking_{year}-{int(year)+1}.csv")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Fichier non trouvé")

    df = pd.read_csv(file_path)
    
    return df.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
