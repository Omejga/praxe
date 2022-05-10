def dupik():   
    array = []
    char = []
    slovicka = []
    opakovani_char = {}
    ne = True
    pocet = 2
    while ne == True:
        for i in range(0, pocet):
            cisla = input("Zadej co vložit: ")
            array.append(cisla)

            delka = len(array)

            if cisla.isalpha():
                lowerCase = cisla.lower()
                retezce = list(lowerCase)
                char += retezce
                slovicka.append(cisla)
                znakCount = len(char)

                print(f"\nZadaný řetězec: {cisla} | chary : {char}")
            ne = False
        for c in char:
            if c in opakovani_char:
                opakovani_char[c] += 1
            else:
                opakovani_char[c] = 1
        print(f"Počty všech zadaných charakterů: {opakovani_char}")

retezce = []

mystring = input("Něco: ")
split = mystring.split(" ")


print(split) 

join = "".join(split)
print(join)