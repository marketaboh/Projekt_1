'''¨
projekt_1.py: první projekt do Engeto Online Python Akademie
author = Markéta Boháčková
email: bohackovama@gmail.com
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# uzivatelska jmena a hesla
USER_PASSWORDS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# vyzadani uzivatelskeho jmena a hesla
USER = input("Username: ")
PASSWORD = input("Password: ")
print("-" * 30)

# kontrola uzivatelskeho jmena a hesla
if USER in USER_PASSWORDS and PASSWORD == USER_PASSWORDS[USER]:
    print("Welcome to the app", USER)
    print("We have 3 texts to be analyzed.")  
    print("-" * 30)

    # vyber textu uzivatelem
    TEXT_NUMBER = input("Enter a number btw. 1 and 3 to select: ") 
    print("-" * 30)

    # kontrola zda vstupni hodnota je cislo a zda je v rozsahu
    if TEXT_NUMBER.isdigit() and int(TEXT_NUMBER) in range(1,4):
        TEXT_NUMBER = int(TEXT_NUMBER)
        # vezme text z listu TEXTS
        SELECTED_TEXT = TEXTS[TEXT_NUMBER - 1]
        # rozdeleni textu na slova
        SPLIT_TEXT = SELECTED_TEXT.split()
        # pocet slov ve vybranem textu
        COUNT_WORDS = len(SPLIT_TEXT)
        TITLECASE_WORDS = 0
        UPPERCASE_WORDS = 0
        LOWERCASE_WORDS = 0
        NUMERIC_STRING = 0
        SUM_NUMBERS = 0
        WORD_LENGHTS = list()

        # analyza slov v textu
        for WORD in SPLIT_TEXT:
           
            # Očištění slov od nežádoucích znaků a zjisteni delky slova
            WORD_LENGHTS.append(len(WORD.strip(",.!?")))    

            # slova s velkym pocatecnim pismenem
            if WORD.istitle():
                TITLECASE_WORDS += 1

            # slova velkymi pismeny
            elif  WORD.isalpha() and WORD.isupper():
                UPPERCASE_WORDS += 1

            # slova malymi pismeny
            elif WORD.islower():
                LOWERCASE_WORDS += 1

            # slova ktera jsou cisla a secteni techto cisel (funguje pouze v pripade celych cisel)
            elif WORD.isdigit():
                NUMERIC_STRING += 1
                SUM_NUMBERS += int(WORD)

        #Vypis vysledku
        print("There are", COUNT_WORDS, "words in the selected text.")
        print("There are", TITLECASE_WORDS, "titlecase words.")
        print("There are", UPPERCASE_WORDS, "uppercase words.")
        print("There are", LOWERCASE_WORDS, "lowercase words.")
        print("There are", NUMERIC_STRING, "numeric strings.")
        print("The sum of all the numbers", SUM_NUMBERS)
        print("-" * 30)

        # Počítání četnosti délek
        LENGTH_FREQUENCIES = {}
        for LENGHT in sorted(WORD_LENGHTS):
            if LENGHT in LENGTH_FREQUENCIES:
                LENGTH_FREQUENCIES[LENGHT] += 1
            else:
                LENGTH_FREQUENCIES[LENGHT] = 1
        
        #vypis sloupcoveho grafu
        # Tisk záhlaví tabulky
        print(f"{'LEN':>5} {'|'} {'OCCURRENCES':^20} {'|'} {'NR.':<5}")
        print("-" * 30)
        
        # Tisk řádků tabulky
        for LENGHT in LENGTH_FREQUENCIES:
            print(f"{LENGHT:>5} {'|'} {'*' * LENGTH_FREQUENCIES[LENGHT]:<20} {'|'} {LENGTH_FREQUENCIES[LENGHT]:<5}")

    # pokud je vstupni hodnota cislo a neni v rozsahu -> konec programu
    elif TEXT_NUMBER.isdigit() and int(TEXT_NUMBER) not in range(1,4):
        print("Sorry, you have selected a wrong number. The program will end now.")
        quit()

    # pokud vstupni hodnota neni cislo -> konec programu
    else:
        print("Sorry, you have entered a wrong input. The program will end now.")
        quit()

# ukonceni programu v pripade spatneho uzivatelskeho jmena nebo hesla
else:
    print("unregistered user, terminating the program..")
    quit()