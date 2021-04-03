'''
Created on Feb 19, 2019

@author: User
'''
def ucitajKontrole():
    for line in open('kontrole.txt', 'r').readlines():
        if len(line) > 1:
            kontrola = str2kontrola(line)
            kontrole.append(kontrola)
            
def str2kontrola(line):
    if line[-1] == '\n':
        line = line[:-1]
    datum, opticar, id, vrstaLecenja, cena,  = line.split('|')
    kontrola = {
        'datum': datum,
        'opticar': opticar,
        'id': id,
        'vrstaLecenja': vrstaLecenja,
        'cena': cena,
        }
    return kontrola

def kontrola2str(kontrola):
    return'|'.join([kontrola['datum'], kontrola['opticar'],
    kontrola['id'], kontrola['vrstaLecenja'], kontrola['cena']])
    
#def searchKontrola(field, value):
    #rez = []
    #for kontrola in kontrole:
        #if kontrola[field].upper() == value.upper():
            #rez.append(kontrola)
   #return rez
   
def searchKontrola(field, value):
    rez = []
    val = 0
    for kontrola in kontrole:
        if kontrola[field].upper() == value.upper():
            rez.append(kontrola)
            val = val + int(kontrola['cena'])
    print("\nOvaj opticar je ukupno zaradio " + str(val))
    return rez



def findKontrola(idk):
    for kontrola in kontrole:
        if kontrola['opticar'] == idk:
            return kontrola
    return None

def sacuvajKontrolu():
    file = open('kontrole.txt', 'w')
    for kontrola in kontrole:
        file.write(kontrola2str(kontrola))
        file.write('\n')
    file.close()
    
def formatKontrola(kontrola):
 return u"{0:16}|{1:4}|{2:20}|{3:20}|{4:>10}".format(
 kontrola['datum'],
 kontrola['opticar'],
 kontrola['id'],
 kontrola['vrstaLecenja'],
 kontrola['cena'])

def formatKontrole(lista):
    rez = ""
    for kontrola in lista:
         rez += formatKontrola(kontrola) + '\n'
    return rez
 
def formatSveKontrole():
    return formatKontrole(kontrole)

def dodajKontrolu(kontrola):
    kontrole.append(kontrola)

            
            
            
            
kontrole = []
ucitajKontrole()
        