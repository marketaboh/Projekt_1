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
# slovnik uzivatelu
USER_PASSWORDS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# vyzadani uzivatelskeho jmena a hesla
USER = input("Username: ")
PASSWORD = input("Password: ")
print(USER, PASSWORD)
print("-" * 30)

# kontrola uzivatelskeho jmena a hesla
if USER in USER_PASSWORDS and PASSWORD == USER_PASSWORDS[USER]:
    print("Welcome to the app", USER)
    print("We have 3 texts to be analyzed.")  
    print("-" * 30)

    # vyber textu uzivatelem
    TEXT_NUMBER = input("Enter a number btw. 1 and 3 to select:") 
    print("-" * 30)

    # kontrola zda vstupni hodnota je cislo a zda je v rozsahu
    if TEXT_NUMBER.isdigit() and int(TEXT_NUMBER) in range(1,4):
        TEXT_NUMBER = int(TEXT_NUMBER)
        print(TEXTS[TEXT_NUMBER - 1])
        SELECTED_TEXT = TEXTS[TEXT_NUMBER - 1]
        #print(SELECTED_TEXT.split()) kontrola spravneho deleni
        COUNT_WORDS = len(SELECTED_TEXT.split())
        #print("There are", COUNT_WORDS, "words in the selected text.")

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
    print("Sorry, wrong username or password. The program will end now.")
    quit()