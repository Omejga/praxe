def zadani():
    def kolikratChar():
        for c in char:
            if c in opakovani_char:
                opakovani_char[c] += 1
            else:
                opakovani_char[c] = 1
    def kolikratZnaky():
        for c in znacky:
            if c in opakovani_znaky:
                opakovani_znaky[c] += 1
            else:
                opakovani_znaky[c] = 1

    while True:
        mini = True
        array = []
        char = []
        znacky = []
        slovicka = []
        znaky = []
        symboly = []
        opakovani_char = {}
        opakovani_znaky = {}

        pocet = input("Zadej kolik hodnot by jsi chtěl zadat: ")
        try:
            try:
                pocet = int(pocet)
                while mini == True:
                    for i in range(0, pocet):
                        cisla = input("Zadej hodnotu: ")
                        pureInput = cisla
                        try:
                            split = cisla.split(" ")
                            join = "".join(split)
                            cisla = join
                        except:
                            print("Stala se nějaká výjimka")
                        if cisla.isdigit():
                            array.append(cisla)
                            print(f"\nZadaná čísla: {array}")

                        elif cisla.isalpha():
                            lowerCase = cisla.lower()
                            retezce = list(lowerCase)
                            char += retezce
                            slovicka.append(cisla)
                            znakCount = len(char)
                            print(f"\nZadané řetězce: {pureInput} | chary: {char}")

                        else:
                            znakyProcessing = cisla
                            randomZnaky = list(znakyProcessing)
                            znacky += randomZnaky
                            znaky.append(cisla)
                            symboly = list(znaky)
                            print(f"\nZadané řetězce: {znaky}, chary: {znacky} ")
            #   Jestli se sem koukáš tak si mně nepřej!   #
                    mini = False
            except:
                print("Stala se nějaká výjimka")

            nejmensi = array[0]
            nejvetsi = array[0]
            delka = len(array)

            for i in range(0, delka):
                if array[i] < nejmensi:
                    nejmensi = array[i]

            for i in range(0, delka):
                if array[i] > nejvetsi:
                    nejvetsi = array[i]
            kolikratChar()
            kolikratZnaky()
            print(f"\nNejmenší číslo je: {nejmensi} | Největší číslo je: {nejvetsi}\nVšechny zadané retezce: {slovicka} | Celkově tu je {znakCount} charakterů")
            print(f"Počty všech zadaných charakterů: {opakovani_char}")
            print(f"Všechny miscellaneous inputy: {symboly} | Počty všech zadaných znaků: {opakovani_znaky}")
            break


        except:
            print("Řekl jsem kolik, to znamená že máš napsat číslo ty joudo!")



zadani()