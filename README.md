# Password Generator & Analyzer

Aplicație CLI scrisă în Python pentru generarea, analizarea și gestionarea parolelor sigure.
Proiectul oferă atât parole aleatorii, cât și parole memorabile, plus analiză de securitate
bazată pe scor, entropie și reguli de complexitate.

---

## Autor

- **Nume:** Anamaria-Alvina Petrar
- **Grupă:**   3.1
- **Email:** anamaria-alvina.petrar@student.upt.ro 
- **An academic:** 2025–2026  

---

## Descriere

Această aplicație rezolvă problema generării parolelor sigure, care sunt în același timp
dificil de spart, dar ușor de gestionat de către utilizator.

Aplicația permite:
- generarea de parole personalizate
- generarea de parole memorabile pe bază de cuvinte
- analiza securității unei parole existente
- salvarea parolelor într-un istoric criptat (Base64)

Scopul proiectului este educațional și demonstrează concepte de securitate, procesare
argumente CLI, modularizare și containerizare Docker.

---
## Moduri de rulare

---
```bash
🔹 Mod generare batch parole

Acest mod permite generarea mai multor parole într-o singură rulare a aplicației.
Este util atunci când este necesar un set de parole pentru mai mulți utilizatori
sau pentru testare. (Mod în curs de dezvoltare)

 Comandă:

python password_gen.py --batch
 Output:
Batch password generation started

Number of passwords to generate: 5
Password length: 12

[1] 9F@kP2!LmQx#
[2] R7$wZ1!AqM8%
[3] Tm4#P!8RkQ2@
[4] Z!3QkM9P$wA2
[5] L@M8P!2Rk#QZ

All passwords generated successfully.
 🔹 Mod vizualizare istoric parole

Acest mod afișează istoricul parolelor generate anterior.
Parolele sunt salvate într-un fișier criptat folosind codare Base64
și sunt afișate împreună cu data generării.

 Comandă:

python password_gen.py --history view
  Outupt:
Password history (Base64 encoded):

[2026-01-08 16:41]
QWJjQDEyMyFAIw==

[2026-01-09 10:22]
U2VjdXJlUEBzczEyMw==

[2026-01-11 19:05]
QDNmU3Ryb25nIVBA

Total passwords stored: 3
🔹 Mod generare parolă memorabilă

Acest mod generează o parolă ușor de reținut, formată din mai multe cuvinte
separate printr-un caracter implicit. Numărul de cuvinte poate fi configurat
de utilizator.


 Comanda:
python password_gen.py --memorable --words 4
 Output:
Generated memorable password:
forest-horizon-cloud-matrix

Password strength score: 76/100
Entropy: 4.63 bits
Status: Acceptable password

🔹 Mod verificare parolă

Acest mod permite analizarea unei parole introduse de utilizator.
Aplicația calculează scorul de securitate, entropia, penalizările
și oferă sugestii pentru îmbunătățirea parolei.

 Comandă:

python password_gen.py --check "Parola123!"
Output:
Password analyzed: Parola123!

Length: 10
Contains uppercase letters: Yes
Contains lowercase letters: Yes
Contains digits: Yes
Contains special characters: Yes

Entropy: 3.21 bits
Security score: 58/100
Status: Weak password

Suggestions:
- Increase password length
- Avoid common words

🔹 Mod rulare implicit

Acest mod este utilizat atunci când aplicația este rulată fără niciun argument
din linia de comandă. Programul generează automat o parolă folosind
setările implicite.

Comandă:

python password_gen.py
Output:
Generated password: A9f!kP3@Lm2
Password strength score: 82/100
Entropy: 5.12 bits
Status: Strong password



- **Limbaj:** Python 3.10  
- **Biblioteci:**
  - `sys` – procesare argumente CLI
  - `random` – generare caractere aleatorii
  - `math` – calcul entropie
  - `base64` – criptare istoric parole
- **Tools:** Git, Docker, GitHub


 Cerințe sistem

- Python 3.10+
- Sistem de operare: Windows / Linux / macOS
- Docker (opțional, pentru rulare containerizată)




Clone repository
git clone https://github.com/anamaria2005/password-gen.git
cd password-gen

Instalare (Docker)

Pentru rularea aplicației folosind Docker, este necesar să descărcați imaginea din Docker Hub:


docker pull anamaria2005/password-gen:latest
Pentru rulare:
docker run --rm anamaria2005/password-gen:latest 
