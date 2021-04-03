'''
Created on Feb 18, 2019

@author: User
'''
def ucitajKlijente():
    for line in open("klijenti.txt", 'r').readlines():
        if len(line) > 1:
            klijent = str2klijent(line)
            klijenti.append(klijent)
            
def str2klijent(line):
    if line[-1] == '\n':
        line = line[:-1]
    idk, ime, prezime, adresa, telefon, dioptrija = line.split('|')
    klijent = {
        'id': idk,
        'ime': ime,
        'prezime': prezime,
        'adresa': adresa,
        'telefon': telefon,
        'dioptrija': dioptrija,
        }
    return klijent

def klijent2str(klijent):
    return '|'.join([klijent['id'], klijent['ime'],
    klijent['prezime'], klijent['adresa'], klijent['telefon'],
    klijent['dioptrija']])
    
def sacuvajKlijente():
    file = open('klijenti.txt', 'w')
    for klij in klijenti:
        file.write(klijent2str(klij))
        file.write('\n')
    file.close()
    
def findKiljent(idk):
    for klij in klijenti:
        if klij['id'] == idk:
            return klij
    return None

def searchKlijenti(field, value):
    rez = []
    for klijent in klijenti:
        if klijent[field].upper() == value.upper():
            rez.append(klijent)
    return rez

def dodajKlijenta(klijent):
    klijenti.append(klijent)
    
def promeniPodatke(id, klij):
    klijenti[id] = klij
    
def formatHeader():
    return \
        "ID        |IME       |PREZIME |ADRESA   |TELEFON| DIOPTRIJA \n"\
        "----------|----------|--------|---------|-------|-------------"
        
def formatKlijent(kli):
     return u"{0:10}|{1:10}|{2:8}|{3:9}|{4:7}|{5:13}".format(
        kli["id"],
        kli["ime"],
        kli["prezime"],
        kli["adresa"],
        kli["telefon"],
        kli["dioptrija"])
     
def formatKlijenti(klijentLista):
    rez = ""
    for klijent in klijentLista:
        rez += formatKlijent(klijent) + '\n'
    return rez
    
def formatSviKlijenti():
    return formatKlijenti(klijenti)
    
def sortirajKlijente(kljuc):
    klijenti.sort(key = lambda x: x[kljuc])   

        
klijenti = []
ucitajKlijente()
