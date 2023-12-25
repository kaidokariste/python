from tabulate import tabulate

v_hinnapakkumine = 300000
v_esimene_hinnang = 100000
v_panga_finantseering = 0.5*v_esimene_hinnang

koondtabel = []
hinnapakkumine = ["Hinnapakkumine", v_hinnapakkumine, 0]
esimene_hinnang = ["Kinnistu väärtus esimesel hinnangul", v_esimene_hinnang, 0]
hinnapakkumine = ["Panga esmane finantseering 50% hindamisest", v_panga_finantseering, 0]
koondtabel.append(hinnapakkumine)
koondtabel.append(esimene_hinnang)
koondtabel.append(hinnapakkumine)
print(tabulate(koondtabel, headers=["Kirjeldus", "Summa", "omafinantseerign"], tablefmt="grid"))
