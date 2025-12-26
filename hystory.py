import base64 # transforma textul intr-o forma codificat un fel de criptare
import json  #ne ajuta sa salvam date de forma dictionar
from datetime import datetime #pentru a salva monemtul in care am generat parola

HISTORY_FILE="history.enc"

def _encode_text( text: str)->str:
    #tranforma string->bites->in base64 ne da un text ciudar dar reversibil 
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")

def _decode_text(text: str)->str:
        #decodifica din text cudat in text nomal 
    return base64.b64decode(text.encode("utf-8")).decode("utf-8")

def save_password_to_history(password: str, info: dict | None = None) -> None:
    entry = { #slavam fiecare in dictioan daca nu primim info o sa fie gol
    "time": datetime.now().isoformat(timespec="seconds"),
    "password": password,
    "info": info or {},
    }

    #transformam dictionaul in json in base si dupa in lini usor de citit
    line = _encode_text(json.dumps(entry, ensure_ascii=False)) + "\n"

    #scriem in fisier ficare linie o parola noua 
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(line)

def load_history() -> list[dict]: # citim linie cu linie istoricul
    entries = []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                decoded = _decode_text(line) # decodam ce am citit 
                entries.append(json.loads(decoded))
    except FileNotFoundError: # daca nu exista sounem istoric gol
        return []

    return entries
