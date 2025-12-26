import secrets

DEFAULT_WORDS=["lup","cer","casa","masa","copil","inger","craciun","facultate","clase","obiecte","pisica","caine","inginer"]
def generate_memorable(words_count: int=3,separator: str="-"): 
#genereaza o parola memorabila cu cuvintele din lista de mai sus 
    if words_count < 2:
        raise ValueError("Foloseste minim 2 cuvinte pentru o parola memorabila.")
    chosen = [secrets.choice(DEFAULT_WORDS) for _ in range(words_count)]
    return separator.join(chosen)