""" #cviceni 1
zamestnanci=['František','Bruno','Anna','Jakub','Klára','Anežka','Anežka','Anežka']
#print(zamestnanci)
posledni_index=len(zamestnanci)-1
print(posledni_index)
print('Na indexu 2 je: ' + str(zamestnanci[2]))
print('Na ' + str(posledni_index) + ' indexu je:'+zamestnanci[posledni_index])
print('V intervalu od 2 do 5 je:'+str(zamestnanci[2:6])) #6 protože horní hranice už nezahrnuje posledni prvek
print('každý třetí člen ne:'+str(zamestnanci[::3])) """

 #cviceni 2
jmeno='Martin'
vaha=80
vyska=2
bmi=vaha/(vyska**2)
print(bmi) 
if bmi<18.5 :
    kategorie='podvýživa'
elif bmi>=18.5 and bmi<25:
    kategorie='Zdravá váha'
elif bmi>=25 and bmi<30:
    kategorie='mírná nadváha'
elif bmi>=30 and bmi<40:
    kategorie='obezita'
else:
    print('těžká obezita')
print(kategorie) 

""" #cviceni 3
zamestnanci=['František','Anna','Jakub','Klára']
print('Zaměstnanci na začátku: ',zamestnanci)
zamestnanci_a=zamestnanci.copy()
zamestnanci_a.append('Bruno')
zamestnanci_a.append('Anežka')
print('Nová jména přidána: ',zamestnanci_a)
zamestnanci_b=zamestnanci.copy()
zamestnanci_b.insert(1,'Bruno')
print('Nová jména vložena: ',zamestnanci_b) """

#cviceni 4
vstupni_cisla=[1,2,3,4,5,6,7]
vstupni_pismena=['p','ú','s','č','p','s','n']
tyden=('pondělí','úterý','středa','čtvrtek','pátek','sobota','neděle')
cislo_dne=3
if cislo_dne in vstupni_cisla :
    print('Správná vstupní hodnota')
else:
    print('špatná vstupní hodnota')