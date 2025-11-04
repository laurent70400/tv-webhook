from fastapi import FastAPI, Request, HTTPException
import json, datetime, os

app = FastAPI()
SECRET = os.getenv("TV_SECRET", "CHANGE_ME_SECRET")  # aligne avec ton Pine

@app.get("/")
def root():
    return {"status": "up"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    if data.get("secret") != SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret key")

    print("=== ALERT RECEIVED ===")
    print(data)

    # petit log fichier (facultatif, pratique pour débug)
    with open("alerts.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.utcnow().isoformat()}Z {json.dumps(data)}\n")

    # plus tard: place_order(...) vers ton broker
    return {"status": "ok"}
