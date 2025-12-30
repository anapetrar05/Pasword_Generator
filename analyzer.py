import string 
import math
import re
SPECIALS = "!@#$%^&*()-_=+[]{};:,.?/"

#scorul parolei bazat pe entropie calculat - penalizari pentru tipare slabe
#entropia se calculeaza folosind formula: Entropie = L * log2(N)
def analyzer_password(password=str )->dict: #returneaza un dictionar 
    #detectam tipurile de caractere 
    has_lower= any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_special =any(c in SPECIALS for c in password)
    has_numbers=any(c in string.digits for c in password)

    lenght= len(password)
    
    pool_size =0 # calculam N din formula de calcul al entropiei

    if has_lower:
        pool_size+=26
    if has_upper:
        pool_size+=26
    if has_numbers:
        pool_size+=10
    if has_special:
        pool_size+=len(SPECIALS)

    entropy_bits= 0.0

    if lenght >0 and  pool_size>0:
        entropy_bits=lenght * math.log2(pool_size)

        # scor "teoretic" din entropie (0-100)
    base_score = int(min(100, round(entropy_bits)))

    # penalizari pentru tipare slabe (scor "practic")
    penalty = pattern_penalty(password,lenght, has_upper, has_numbers, has_special)
    final_score = max(10, min(100, base_score - penalty))



    return { # returnam tot intr-un dictionar
        "lenght":lenght,
        "password":password,
        "has_lower":has_lower,
        "has_uper":has_upper,
        "has_numbers": has_numbers,
        "has_special":has_special,
        "base_score":base_score,
        "pool_size":pool_size,     
        "entropy_bits":entropy_bits,
        "penalty":penalty,
        "score":final_score
    }



def pattern_penalty(password: str,lenght: int, has_upper: bool, has_numbers: bool, has_special: bool) -> int:
    pw_lower = password.lower()
    penalty = 0

# scurta
    if lenght < 12:
        penalty += 10   

# lipsuri de diversitate
    if not has_upper:
        penalty += 8    
    if not has_special:
        penalty += 8    
    if not has_numbers:
        penalty += 5

# cuvinte foarte comune
    if "parola" in pw_lower or "password" in pw_lower:
        penalty += 20   

# cifre la final
    if re.search(r"\d+$", password) and re.search(r"[A-Za-z]", password):
        penalty += 5    
# apare in lista de parole comune 
    common = load_comon_password()
    if is_common_password(password, common):
        penalty += 20

    return penalty

def label_from_score(score: int) -> str:
    print("Parola este una:")
    if score >= 80:
        return "FOARTE PUTERNICA"
    if score >= 60:
        return "PUTERNICA"
    if score >= 40:
        return "MEDIE"
    return "SLABA"

# functia ia dictionarul de la funcia anterioara si returneaza doua liste probleme si sugesti
def problem_and_sugetion(analysis: dict)-> tuple[list,list]:
    problems=[]
    sugestion=[]

    # folosindune de if verificam anumite reguli 
    if analysis["lenght"]<12:
        problems.append("Prea scurta (minim recomandat 12 caracter)")
        sugestion.append("Mareste lungime la cel putin 12-16 caractere")
    if not analysis["has_uper"]:
        problems.append("Nu are majuscule!")
        sugestion.append("Este recomandat sa folosesti majuscule")
    if not analysis["has_numbers"]:
        problems.append("Nu are numere!")
        sugestion.append("Este recomandat sa adaugi numere")
    if not analysis["has_special"]:
        problems.append("Nu contine caractere speciale")
        sugestion.append("Este recomandat sa contina caractere speciale")
    pw_lower= analysis["password"].lower() # punem in pw_lower parola cu litere mici
    if "parola" in pw_lower or "password" in pw_lower:
        problems.append("Parola contine un cuvant foate comun ")
        sugestion.append("Evita cuvintele comune precum parola/password")
    
    if analysis["password"].isdigit():
        problems.append("Parola contine doar cifree")
        sugestion.append("Parola ar trebui sa contina si liters si caractere speciale")
    common=load_comon_password()
    if is_common_password(analysis["password"],common):
        problems.append("Parola apare in lista de parole comune")
        sugestion.append("Schimba parola cu una unica nu folosi parole comune")


    return problems,sugestion

def load_comon_password(filename="common_pasword.tst")-> set:
    try: # deschidem fisierul in citire si il citim linie cu linie
        with open (filename,"r", encoding="utf-8") as f:
            return { line.strip().lower() for line in f if line.strip()}
    except FileNotFoundError:
        return set()

def is_common_password(password:str,comon_set:set)->bool: # functia returneaza bool 
    return password.lower() in comon_set # verifica daca parola ii in comon_set in lista din fisierul txt