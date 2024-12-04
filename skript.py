#prvni cviceni

""" retezec='indexování'
print('Prvních 5 písmen:')
print(retezec[:5])
print('Posledních 5 písmen:')
print(retezec[-5:])
print('Každé 3. písmeno (počínaje prvním) od \'i\':')
print(retezec[::3]) """

#2 cviceni
""" kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26
kg_pocet = 80
km_pocet = 54
l_pocet = 5
kg_vysledek=kg_lb*kg_pocet
km_vysledek=km_mile*km_pocet
l_vysledek=l_gal*l_pocet
print('80 kg je '+str(kg_vysledek)+' lb')
print('54 km je '+str(km_vysledek)+' mil')
print('5 l je '+str(l_vysledek)+' gal') """

# 3 cviceni
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000
sleva_merc=5000
cena_2_merc=mercedes*2
cena_merc_a_rolls=mercedes+rolls_royce
cena_2_rolls_s_vybavou=2*(rolls_royce+vybava)
cena_merc_s_vybavou=mercedes+vybava
merc_se_slevou=mercedes-sleva_merc

print('Sleva na Mercedes: '+str(sleva_merc))
print('Cena za dva Mercedesy je: '+str(cena_2_merc))
print('Cena za Mercedes a Rolls-Royce: '+str(cena_merc_a_rolls))
print('Cena za dva Rolls-Royce s příplatkovou výbavou: '+str(cena_2_rolls_s_vybavou))
print('Cena za Mercedes s příplatkovou výbavou: '+str(cena_merc_s_vybavou))
print('Cena za Mercedes po slevě: '+str(merc_se_slevou))