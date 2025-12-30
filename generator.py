import string  # un modul python special pentru parole tokenuri si securitate
import secrets
# Functie pentru generarea parolelorsecurizatre folosind random sigur 
def generator_passowrd(lenght, use_uper, use_special, use_numbers):
    categories=[string.ascii_lowercase] #lista de seturi de caractere 

    if use_uper:
        categories.append(string.ascii_uppercase) #adaugi la lista  cu append
    if use_special:
        categories.append("!@#$%^&*()-_=+[]{};:,.?/")
    if use_numbers:
        categories.append(string.digits)


    if lenght<=0:
        raise ValueError("Lungimea trebuie sa fie mai mare decat 0")
    if lenght < len(categories):
        raise ValueError("Lungimea trebuie sa fie minima de {len(categories)}")
    poll="".join(categories)
    # garantam 1 caracter din fiecare categorie  obligam sa fie 1 carcater din fiecrae categorie
    password_chars=[secrets.choice(cat) for cat in categories]
    # completam restul parolei cu caractere aleatori din categori 
    for _ in range(lenght -len(password_chars)): #luam restul de caractere 
        password_chars.append(secrets.choice(poll))

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


if __name__ == "__main__":
    print(generator_passowrd(10))
