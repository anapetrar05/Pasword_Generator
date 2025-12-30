from itertools import count
import sys
from generator import generator_passowrd
from analyzer import analyzer_password, label_from_score,problem_and_sugetion,pattern_penalty
from hystory import load_history,save_password_to_history
from memorable import generate_memorable
def main():
    args =sys.argv[1:]
    if "--history" in args:  #daca este in lista o analizam altfel o generam
        print("Mod ISTORIC")
        if "view" in args:
            entries=load_history()
            if not entries:
             print("Nu au fost salvate parole in istoric.")
            else:
                print("Istoric parole cele mai recente:")
                for e in entries:
                    print("-", e["time"],"->",e["password"])
        else:
            print("Foloseste --history view")
    elif "--memorable" in args:
        print("Mod PAROLA MEMORABILA")
        words=3 # daca nu specifici numarul de cuvinte o sa fie 3
        if "--words" in args: # dupa --words pui numarul de cuvinte 
            i=args.index("--words")
            words = int(args[i+1])
            
        parola=generate_memorable(words_count=words,separator="-")
        print("Parola memorabila:", parola)
        # optional: salvezi si in istoric
        save_password_to_history(parola, {"type": "memorable", "words": words})
        print("Salvata in istoric criptat (base64).")

    elif "--check" in args:   
        print("Mod ANALIZA Parola")

        index= args.index ("--check")
        parola= args[index +1]  
        words=3
        if "--words" in args:
            args[index +1]
        
        analysis=analyzer_password(parola)
        label=label_from_score(analysis["score"])
        problems, solutions=problem_and_sugetion(analysis)
        #afisam ce contine parola pe care o verificam 
        print("Parola analizata:", parola)
        print("Scor:", analysis["score"], "/ 100")
        print("Lungime:", analysis["lenght"])
        print("Penalitati:", analysis["penalty"])
        print("Putere:", label)
        print("Entropie:", round(analysis["entropy_bits"], 2))

        print("Contine:")
        print(" - litere mici:", analysis["has_lower"])
        print(" - litere mari:", analysis["has_uper"])
        print(" - cifre:", analysis["has_numbers"])
        print(" - simboluri:", analysis["has_special"])


        #afisam problemele si sugestile necesare
        print("Probleme:")
        if problems:
            for p in problems:
                print("-",p)
        print("Sugestii:")
        if solutions :
            for s in solutions:
                print("-",s)



    elif "--batch" in args:
        print("Mod Generare Batch")
      # generam mai multe  parole cu anumite specificatii
    # 1) cate parole generam
    i = args.index("--batch")
    count = int(args[i + 1])

    # 2) lungime (aceeasi logica ca la generate)
    lenght = 10
    if "--lenght" in args:
        j = args.index("--lenght")
        lenght = int(args[j + 1])

    # 3) flaguri
    use_uper = "--uper" in args
    use_numbers = "--numbers" in args
    use_special = "--special" in args

    # 4) generam "count" parole
    for k in range(count):
        parola = generator_passowrd(lenght, use_uper, use_special, use_numbers)
        print(f"{k+1}. {parola}")

    else :
        print("Mod GENERARE Parola (implicit)")
        lenght=10
        if "--lenght" in args:
            index= args.index("--lenght") #numara unde ii lenght 
            lenght=int(args[index +1]) # transforma in numar ce scrie dupa --lenght in args gen numarul 
        
        #definim argumentele pe care le putem da in functia de generare

        use_uper="--uper" in args
        use_numbers ="--numbers"in args
        use_special ="--special" in args
       
        parola= generator_passowrd(lenght, use_uper, use_special,use_numbers)
        print("Parola generata:", parola)
        save_password_to_history(parola, { # apelam functia cu parametri parola si dictionarul cu toate specificatile parolei
        "length": lenght,
        "upper": use_uper,
        "numbers": use_numbers,
        "special": use_special
        })
print("Salvata in istoric criptat (base64).")

       



if __name__ == "__main__":
    main()
