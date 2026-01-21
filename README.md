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

## 🔹 Mod parolă implicit

Acest mod este activat atunci când aplicația este rulată fără niciun argument.
Programul generează o parolă aleatorie folosind setările implicite.

### Comandă:
```bash
python password_gen.py
## 🔹 Mod generare batch parole

Acest mod permite generarea mai multor parole într-o singură rulare a aplicației.
Este util atunci când este necesar un set de parole pentru mai mulți utilizatori
sau pentru testare. (Mod în curs de dezvoltare)

### Comandă:
```bash
python password_gen.py --batch
## 🔹 Mod vizualizare istoric parole

Acest mod afișează istoricul parolelor generate anterior.
Parolele sunt salvate într-un fișier criptat folosind codare Base64
și sunt afișate împreună cu data generării.

### Comandă:
```bash
python password_gen.py --history view
## 🔹 Mod generare parolă memorabilă

Acest mod generează o parolă ușor de reținut, formată din mai multe cuvinte
separate printr-un caracter implicit. Numărul de cuvinte poate fi configurat
de utilizator.

### Comandă:
```bash
python password_gen.py --memorable --words 4
## 🔹 Mod verificare parolă

Acest mod permite analizarea unei parole introduse de utilizator.
Aplicația calculează scorul de securitate, entropia, penalizările
și oferă sugestii pentru îmbunătățirea parolei.

### Comandă:
```bash
python password_gen.py --check "Parola123!"
## 🔹 Mod rulare implicit

Acest mod este utilizat atunci când aplicația este rulată fără niciun argument
din linia de comandă. Programul generează automat o parolă folosind
setările implicite.

### Comandă:
```bash
python password_gen.py

## Tehnologii folosite

- **Limbaj:** Python 3.10  
- **Biblioteci:**
  - `sys` – procesare argumente CLI
  - `random` – generare caractere aleatorii
  - `math` – calcul entropie
  - `base64` – criptare istoric parole
- **Tools:** Git, Docker, GitHub

---

## Cerințe sistem

- Python 3.10+
- Sistem de operare: Windows / Linux / macOS
- Docker (opțional, pentru rulare containerizată)

---

## Instalare

```bash
# Clone repository
git clone https://github.com/anamaria2005/password-gen.git
cd password-gen

## Instalare (Docker)

Pentru rularea aplicației folosind Docker, este necesar să descărcați imaginea din Docker Hub:

```bash
docker pull anamaria2005/password-gen:latest
Pentru rulare:
docker run --rm anamaria2005/password-gen:latest 
