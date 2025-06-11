"""
Auteur  : Abdoul Moubarak BANSE
Email   : elbrakbanse17@gmail.com
Github  : https://github.com/Elbrak17/convertisseur_de_masse
Projet  : Convertisseur de Masse
Date    : 11 Juin 2025
Version : 1.0
Licence : MIT
"""



# FONCTIONS DE CONVERSION

def kg_hg(val : float):
    return val*10
def kg_dag(val : float):
    return val*100
def kg_g(val : float):
    return val*1000
def kg_dg(val : float):
    return val*10000
def kg_cg(val : float):
    return val*100000
def kg_mg(val : float):
    return val*1000000

def hg_kg(val : float):
    return val/10
def hg_dag(val : float):
    return val*10
def hg_g(val : float):
    return val*100
def hg_dg(val : float):
    return val*1000
def hg_cg(val : float):
    return val*10000
def hg_mg(val : float):
    return val*100000

def dag_kg(val : float):
    return val/100
def dag_hg(val : float):
    return val/10
def dag_g(val : float):
    return val*10
def dag_dg(val : float):
    return val*100
def dag_cg(val : float):
    return val*1000
def dag_mg(val : float):
    return val*10000

def g_kg(val : float):
    return val/1000
def g_hg(val : float):
    return val/100
def g_dag(val : float):
    return val/10
def g_dg(val : float):
    return val*10
def g_cg(val : float):
    return val*100
def g_mg(val : float):
    return val*1000

def dg_kg(val : float):
    return val/10000
def dg_hg(val : float):
    return val/1000
def dg_dag(val : float):
    return val/100
def dg_g(val : float):
    return val/10
def dg_cg(val : float):
    return val*10
def dg_mg(val : float):
    return val*100

def cg_kg(val : float):
    return val/100000
def cg_hg(val : float):
    return val/10000
def cg_dag(val : float):
    return val/1000
def cg_g(val : float):
    return val/100
def cg_dg(val : float):
    return val/10
def cg_mg(val : float):
    return val*10

def mg_kg(val : float):
    return val/1000000
def mg_hg(val : float):
    return val/100000
def mg_dag(val : float):
    return val/10000
def mg_g(val : float):
    return val/1000
def mg_dg(val : float):
    return val/100
def mg_cg(val : float):
    return val/10



print('\tCONVERTISSEUR DE MASSE\t')

print('\n')
print("Unités prises en charge:\n")
print("\tkg pour kilogramme")
print("\thg pour hectogramme")
print("\tdag pour décagramme")
print("\tg pour gramme")
print("\tdg pour décigramme")
print("\tcg pour centigramme")
print("\tmg pour milligramme")
print('\n')

while True:
    unite_de_depart = input("Entrez l'unité de départ de la valeur à convertir : ")
    if unite_de_depart in ('kg', 'hg', 'dag', 'g', 'dg', 'cg', 'mg'):
        break
    else:
        print("Veuillez entrer une unité de départ prise en charge\n")

while True:
    valeur = input("Entrez la valeur à convertir : ")
    try:
        valeur_de_depart = float(valeur)
        break
    except ValueError:
        print("Entrée invalide. Veuillez saisir un nombre !\n")

print('\n')
print("En quelle unité souhaitez-vous convertir votre valeur ?\n")
print("\t1 --> kilogramme (kg)")
print("\t2 --> hectogramme (hg)")
print("\t3 --> décagramme (dag)")
print("\t4 --> gramme (g)")
print("\t5 --> décigramme (dg)")
print("\t6 --> centigramme (cg)")
print("\t7 --> milligramme (mg)")
print('\n')

while True:
    choix = int(input("Entrez le numéro de votre choix : "))
    if choix in (1, 2, 3, 4, 5, 6, 7):
        break
    else:
        print("Entrée invalide. Veuillez saisir un numéro de choix valide !")

valeur_darrive = 0.0
unite_darrive = 'g'

if choix == 1:
    unite_darrive = 'kg'
    if unite_de_depart == 'kg':
        valeur_darrive = valeur_de_depart
    if unite_de_depart == 'hg':
        valeur_darrive = hg_kg(valeur_de_depart)
    if unite_de_depart == 'dag':
        valeur_darrive = dag_kg(valeur_de_depart)
    if unite_de_depart == 'g':
        valeur_darrive = g_kg(valeur_de_depart)
    if unite_de_depart == 'dg':
        valeur_darrive = dg_kg(valeur_de_depart)
    if unite_de_depart == 'cg':
        valeur_darrive = cg_kg(valeur_de_depart)
    if unite_de_depart == 'mg':
        valeur_darrive = mg_kg(valeur_de_depart)

if choix == 2:
    unite_darrive = 'hg'
    if unite_de_depart == 'kg':
        valeur_darrive = kg_hg(valeur_de_depart)
    if unite_de_depart == 'hg':
        valeur_darrive = valeur_de_depart
    if unite_de_depart == 'dag':
        valeur_darrive = dag_hg(valeur_de_depart)
    if unite_de_depart == 'g':
        valeur_darrive = g_hg(valeur_de_depart)
    if unite_de_depart == 'dg':
        valeur_darrive = dg_hg(valeur_de_depart)
    if unite_de_depart == 'cg':
        valeur_darrive = cg_hg(valeur_de_depart)
    if unite_de_depart == 'mg':
        valeur_darrive = mg_hg(valeur_de_depart)

if choix == 3:
    unite_darrive = 'dag'
    if unite_de_depart == 'kg':
        valeur_darrive = kg_dag(valeur_de_depart)
    if unite_de_depart == 'hg':
        valeur_darrive = hg_dag(valeur_de_depart)
    if unite_de_depart == 'dag':
        valeur_darrive = valeur_de_depart
    if unite_de_depart == 'g':
        valeur_darrive = g_dag(valeur_de_depart)
    if unite_de_depart == 'dg':
        valeur_darrive = dg_dag(valeur_de_depart)
    if unite_de_depart == 'cg':
        valeur_darrive = cg_dag(valeur_de_depart)
    if unite_de_depart == 'mg':
        valeur_darrive = mg_dag(valeur_de_depart)

if choix == 4:
    unite_darrive = 'g'
    if unite_de_depart == 'kg':
        valeur_darrive = kg_g(valeur_de_depart)
    if unite_de_depart == 'hg':
        valeur_darrive = hg_g(valeur_de_depart)
    if unite_de_depart == 'dag':
        valeur_darrive = dag_g(valeur_de_depart)
    if unite_de_depart == 'g':
        valeur_darrive = valeur_de_depart
    if unite_de_depart == 'dg':
        valeur_darrive = dg_g(valeur_de_depart)
    if unite_de_depart == 'cg':
        valeur_darrive = cg_g(valeur_de_depart)
    if unite_de_depart == 'mg':
        valeur_darrive = mg_g(valeur_de_depart)

if choix == 5:
    unite_darrive = 'dg'
    if unite_de_depart == 'kg':
        valeur_darrive = kg_dg(valeur_de_depart)
    if unite_de_depart == 'hg':
        valeur_darrive = hg_dg(valeur_de_depart)
    if unite_de_depart == 'dag':
        valeur_darrive = dag_dg(valeur_de_depart)
    if unite_de_depart == 'g':
        valeur_darrive = g_dg(valeur_de_depart)
    if unite_de_depart == 'dg':
        valeur_darrive = valeur_de_depart
    if unite_de_depart == 'cg':
        valeur_darrive = cg_dg(valeur_de_depart)
    if unite_de_depart == 'mg':
        valeur_darrive = mg_dg(valeur_de_depart)

if choix == 6:
    unite_darrive = 'cg'
    if unite_de_depart == 'kg':
        valeur_darrive = kg_cg(valeur_de_depart)
    if unite_de_depart == 'hg':
        valeur_darrive = hg_cg(valeur_de_depart)
    if unite_de_depart == 'dag':
        valeur_darrive = dag_cg(valeur_de_depart)
    if unite_de_depart == 'g':
        valeur_darrive = g_cg(valeur_de_depart)
    if unite_de_depart == 'dg':
        valeur_darrive = dg_cg(valeur_de_depart)
    if unite_de_depart == 'cg':
        valeur_darrive = valeur_de_depart
    if unite_de_depart == 'mg':
        valeur_darrive = mg_cg(valeur_de_depart)

if choix == 7:
    unite_darrive = 'mg'
    if unite_de_depart == 'kg':
        valeur_darrive = kg_mg(valeur_de_depart)
    if unite_de_depart == 'hg':
        valeur_darrive = hg_mg(valeur_de_depart)
    if unite_de_depart == 'dag':
        valeur_darrive = dag_mg(valeur_de_depart)
    if unite_de_depart == 'g':
        valeur_darrive = g_mg(valeur_de_depart)
    if unite_de_depart == 'dg':
        valeur_darrive = dg_mg(valeur_de_depart)
    if unite_de_depart == 'cg':
        valeur_darrive = cg_mg(valeur_de_depart)
    if unite_de_depart == 'mg':
        valeur_darrive = valeur_de_depart


print("{0}{1} ==> {2}{3}".format(valeur_de_depart, unite_de_depart, valeur_darrive, unite_darrive))