
# kelias = r"data/failiukas.txt"

# with open(kelias,'w') as failas: # write | failas = open("naujas.txt",'w') | istrina kas yra viduje ir uzraso ant virsaus
#     failas.write("Mano vardas yra Antanas, kaip sekasi ? ")

# with open(kelias,'a') as failas: # append | pagrindinis skirtumas nuo w, kad neu=ra6o ant vir6aus, o prideda kaip extra
#     failas.write("Mano vardas yra Antanas, kaip sekasi ? \n")

# with open(kelias,'r') as failas: # r - read
#     # turinys = failas.read()
#     turinys = failas.readlines()

# print(turinys)

#try except
# globalus ir relatyvus kelias

# reliatyvus - nuo čia nuo mano dabartinio failo "failiukas.txt" | "data/failiukas.txt"

# Globalus kelias - nuo pat C disko "C:/Users/Justas/Dekstop/failiukas.txt"

# print("labas \n, kaip sekasi \n")


# import json
# kelias = r"data/duomenys.json"

# with open(kelias,'w') as failas: 
#     # failas.write("Mano vardas yra Antanas, kaip sekasi ? ") # sitas gali irasyti tik teksta (str)
#     json.dump("Mano vardas yra Antanas, kaip sekasi ? ", failas) # sitas gali irasyti beveik bet ka, pvz dict, list, int, float, bool, None


# with open(kelias,'r') as failas: # r - read
#     # turinys = failas.read()
#     turinys = json.load(failas)


import json
kelias = r"data/duomenys.json"

# duomenys_list = [1,2,3,4,5]
# duomenys_dict = {"vardas":"Antanas", "amzius": 25, "miestas": "Vilnius"} # key value pairs

# with open(kelias,'w') as failas: 
    # failas.write("Mano vardas yra Antanas, kaip sekasi ? ") # sitas gali irasyti tik teksta (str)
    # json.dump(duomenys_list, failas) # sitas gali irasyti beveik bet ka, pvz dict, list, int, float, bool, None
    # json.dump(duomenys_dict, failas, indent=4) # sitas gali irasyti beveik bet ka, pvz dict, list, int, float, bool, None


# with open(kelias,'r') as failas: # r - read
#     # turinys = failas.read()
#     turinys = json.load(failas) # paiimk faila ir paversk jo turini i zodyna (dict)
# # failas uzdarytas, mes su juo nieko bendro neturime

# print(turinys) # atspasudink zodyna
# turinys["vardas"] = "Jonas" # uzkrauto zodyno reiksme pakeiciama i kita
# print(turinys) # atspausdink uzkrauta zodyna su pakeista reiksme
# # norint issaugoti pakeitimus, reikia vel atidaryti faila ir perrasyti ji su nauju turiniu
# with open(kelias,'w') as failas: 
#     json.dump(turinys, failas, indent=4) # sitas gali irasyti beveik bet ka, pvz dict, list, int, float, bool, None
# how to write multiple values as proper json format ? | dict, list, int, float, bool, None


# duomenys_dict = {"vardas":"Antanas", "amzius": 25, "miestas": "Vilnius", "pazymiai": [10, 9, 8]} # key value pairs

# with open(kelias,'w') as failas: 
#     json.dump(duomenys_dict, failas, indent=4)
#     json.dump(duomenys_dict, failas, indent=4) # vengti

# duomenys_dict = [{"vardas":"Antanas", "amzius": 25, "miestas": "Vilnius", "pazymiai": [10, 9, 8]},
#                   {"vardas":"Jonas", "amzius": 30, "miestas": "Kaunas", "pazymiai": [7, 8, 9]}] # key value pairs

# with open(kelias,'w') as failas: 
#     json.dump(duomenys_dict, failas, indent=4)


# with open(kelias,'r') as failas: # r - read
#     turinys = json.load(failas) # paiimk faila ir paversk jo turini i zodyna (dict)

# print(turinys[0]) # atspasudink zodyna



# with open(kelias,'r') as failas: # r - read
#     turinys = json.load(failas) 

# turinys.append({"vardas":"Petras", "amzius": 35, "miestas": "Siauliai", "pazymiai": [6, 7, 8]})

# # norint issaugoti pakeitimus, reikia vel atidaryti faila ir perrasyti ji su nauju turiniu
# with open(kelias,'w') as failas: 
#     json.dump(turinys, failas, indent=2)

# import tabulate

# with open(kelias,'r') as failas: # r - read
#     turinys = json.load(failas) 

# print(tabulate.tabulate(turinys, headers="keys", tablefmt="grid"))

# class Zmogus:
#     def __init__(self, vardas, amzius, miestas):
#         self.vardas = vardas
#         self.amzius = amzius
#         self.miestas = miestas

# import pickle
# # turinys = {"vardas":"Antanas", "amzius": 25, "miestas": "Vilnius", "pazymiai": [10, 9, 8]} # key value pairs
# turinys = Zmogus("Antanas", 25, "Vilnius")
# with open("duomenys.pickle",'wb') as failas: 
#     pickle.dump(turinys, failas)

# with open("duomenys.pickle",'rb') as failas: 
#     turinys = pickle.load(failas)
#     print(turinys)


#       a. Turėtų būti galima pridėti naują į knygą į biblioteką (knyga, privalo turėti bent, autorių pavadinimą išleidimo metus ir žanrą). +
#       b. Turėtų būti galima pašalinti senas/nebenaudojamas knygas, galima daryti pagal išleidimo metus, jeigu senesnis nei x išmetam. +
#       c. Skaitytojai turėtų galėti pasiimti knygą išsinešimui (knygų kiekis ribotas) +
#       d. Turėtų būti galimybė ieškoti knygų bibliotekoje, pagal knygos pavadinimą arba autorių. +
#       e. Knygos išduodamos tik tam tikram laikui, jeigu knygos negrąžinamos iki išduotos datos, jos skaitomos vėluojančiomis (angl. Overdue). 
#       f. Turi būti galima peržiūrėti visas bibliotekos knygas +
#       g. Turi būti galima peržiūrėti visas vėluojančias knygas
#       h. Turi būti neleidžiama pasiimti knygos, jeigu skaitytojas turi vėluojančią knygą ir jis turi būti įspėtas, kad knyga vėluoja
# Bonus Balai (neprivaloma padaryti)
# Dvi rolės bibliotekininkas ir skaitytojas, bibliotekininkas prisijungia
#  įvedęs naudotojo vardą ir slaptažodį, o skaitytojas savo skaitytojo kortelės numerį.
#  Skaitytojas negali pridėti/išimti knygų.
# Knygas galima pasiimti tik su skaitytoje kortele, skaitytojo korteles reikia galėti užregistruoti
#  ir priskirti naudotojui.
# Turėtų būti galimybė išvesti statistiką, koks yra vidutinis vėluojančių knygų kiekis
#  ir kitus aktualius rodiklius, tokius kaip, kokio žanro knygų yra daugiausiai,
#  kokio žanro knygas, dažniausiai ima skaitytojai ir t.t
# Galite pamėginti padaryti grafinę sąsają ir per įrankius, kaip tkinter arba streamlit
#  (jeigu turite noro, mokytis papildomai).


# if "l" in "hello": # vartotojo_paieska in knygu_pavadinimas or vartojo_paieska in knygu_autorius
#     print("yep")
# with open("biblioteka.json",'w') as failas: 
#         turinys = json.dump([], failas) # sukuriam tuscia sarasa, kad galetume i ji deti knygas
# class Knyga:
#     def __init__(self, pavadinimas, autorius, metai, zanras):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.metai = metai
#         self.zanras = zanras

# def prideti_knyga(knyga):
#     with open("biblioteka.json",'r') as failas: 
#         turinys = json.load(failas) 

#     turinys.append(knyga.__dict__)

#     with open("biblioteka.json",'w') as failas: 
#         json.dump(turinys, failas, indent=4)

# while True:
#     pasirinkimas = input("Pasirinkite veiksmą: 1 - pridėti knygą, 2 - peržiūrėti visas knygas, 3 - išeiti: ")
#     if pasirinkimas == "1":
#         pavadinimas = input("Įveskite knygos pavadinimą: ")
#         autorius = input("Įveskite knygos autorių: ") # autorius = ""
#         metai = int(input("Įveskite knygos išleidimo metus: ")) # reikia patikrinimo kad metai būtų skaičius ir neigali būti ateityje
#         zanras = input("Įveskite knygos žanrą: ")
#         nauja_knyga = Knyga(pavadinimas, autorius, metai, zanras)
#         prideti_knyga(nauja_knyga)
#     elif pasirinkimas == "2":
#         with open("biblioteka.json",'r') as failas:
#             turinys = json.load(failas)
#         for knyga in turinys:
#             print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}, Metai: {knyga['metai']}, Zanras: {knyga['zanras']}")
#     elif pasirinkimas == "3":
#         break
#     else:
#         print("Neteisingas pasirinkimas. Bandykite dar kartą.")