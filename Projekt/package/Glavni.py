import Klijenti
import Opticari
import Kontrole
from Klijenti import searchKlijenti, promeniPodatke, dodajKlijenta
from Kontrole import searchKontrola, kontrole

def main():
    print()
    print("O P T I K A")
    print()
    if not login():
        print("Niste dobro uneli podatke")
        return
    komanda = '0'
    while komanda != 'X':
        komanda = menu()
        if komanda == '1':
            findKlijent()
        elif komanda == '2':
            searchKlijenti()
        elif komanda == '3':
            dodajKlijenta()
        elif komanda == '4':
            dodajKontrolu()
        elif komanda == '5':
            listaKlijenata()
        elif komanda == '6':
            promeniPodatke()
        elif komanda == '7':
            promeniCenuKontrole()
        elif komanda == '8':
            searchKontrola()
        print("IZLAZ")
            
def login():
    ime = input("Unesite ime: ")
    lozinka = input("Unesite lozinku: ")
    return Opticari.login(ime, lozinka)

def menu():
    printMenu()
    komanda = input(">>>")
    while komanda.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', 'X'):
        print("\n Uneli ste pogresnu komandu")
        printMenu()
        komanda = input(">>>")
    return komanda.upper()

def printMenu():
    print("\nOdaaberite opciju:")
    print(" 1 - pronalazenje klijenta")
    print(" 2 - pretrazivanje klijenata") 
    print(" 3 - dodavanje novog klijenta")
    print(" 4 - dodavanje kontrole")
    print(" 5 - pregled svih klijenata")
    print(" 6 - izmena podataka o klijentu")
    print(" 7 - izmena cene kontrole")
    print(" 8 - pretrazivanje kontrola")
    print(" x - izlaz iz programa")
 
def findKlijent():
    print( "1: Pronalazenje klijenta\n")
    idk = input("Unesite id klijenta >>> ")
    klijent = Klijenti.findKiljent(idk)
    if klijent != None:
        print(Klijenti.formatHeader())
        print(Klijenti.formatKlijent(klijent))
    else:
        print("Nije pronadjen klijent sa id brojem ", idk)
        
def searchKlijenti():
    print("2: Pretrazivanje klijenata\n")
    command = '0'
    while command != 'X':
        command = meniPretrage()
        if command == '1':
            searchIme()
        elif command == '2':
            searchPrezime()
        print("Izlaz")
        
def meniPretrage():
    printMeniPretrage()
    komanda = input(">>>")
    while komanda.upper() not in ('1', '2', 'X'):
        print("Niste dobro uneli komandu\n")
        printMeniPretrage()
        komanda = input(">>>")
    return komanda.upper()

def printMeniPretrage():
    print("\nIzaberije jednu od opcija za pretragu")
    print("1: Pretraga klijenata po imenu")
    print("2: Pretraga klijenata po prezimenu")
    print("X: izlaz")
    
def searchIme():
    ime = input("Unesite ime klijenta za pretragu")
    lista = Klijenti.searchKlijenti('ime', ime)
    if len(lista) == 0:
        print("\nNe postiji klijent sa tim imenom")
    else:
        print('\n')
        print(Klijenti.formatHeader())
        print(Klijenti.formatKlijenti(lista))
    
def searchPrezime():
    prezime = input("Unesite prezime klijenta za pretragu")
    lista = Klijenti.searchKlijenti('prezime', prezime)
    if len(lista) == 0:
        print("\nNe postiji klijent sa tim prezimenom")
    else:
        print('\n')
        print(Klijenti.formatHeader())
        print(Klijenti.formatKlijenti(lista))
        
def dodajKlijenta():
    print("3: Dodavanje novog klijenta u optiku\n")
    klijent = {}
    klijent['id'] = input("Unesite id novog klijenta: ")
    klijent['ime'] = input("Unesite ime novog klijenta: ")
    klijent['prezime'] = input("Unesite prezime novog klijenta: ")
    klijent['adresa'] = input("Unesite adresu stanovanja novog klijenta: ")
    klijent['telefon'] = input("Unesite broj telefona novog klijenta: ")
    klijent['dioptrija'] = input("Unesite dioptriju novog klijenta: ")
    Klijenti.dodajKlijenta(klijent)
    Klijenti.sacuvajKlijente()
    
def dodajKontrolu():
    print("4: Dodavanje nove kontrole\n")
    kontrola = {}
    kontrola['datum'] = input("Unesite datum kontrole: ")
    kontrola['opticar'] = input("Unesite opticara koji je izvrsio kontrolu")
    kontrola['id'] = input("Unesite id: ")
    kontrola['vrstaLecenja'] = input("Unesite vrstu lecenja: ")
    kontrola['cena'] = input("Unesite cenu kontrole")
    Kontrole.dodajKontrolu(kontrola)
    Kontrole.sacuvajKontrolu()
        
def listaKlijenata():
    print("5: Lista svih klijenata\n")
    Klijenti.sortirajKlijente('id')
    print(Klijenti.formatHeader())
    print(Klijenti.formatSviKlijenti())
    
def promeniPodatke():
    print("6: Promena podataka o klijentu\n")
    idk = input("Unesite id klijenta cije podatke zelite da izmenite: ")
    klijent = Klijenti.findKiljent(idk)
    if klijent == None:
        print("Klijent sa unetim id brojem ne postoji")
    else:
        print(Klijenti.formatHeader())
        print(Klijenti.formatKlijent(klijent))
        print()
        print("Odaberite podatak koji zelite da izmenite")
        komanda = '0'
        while komanda != 'X':
            komanda = meniPromene()
            if komanda == '1':
                klijent['adresa'] = input("Unesite novu adresu: ")
            elif komanda == '2':
                klijent['telefon'] = input("Unesite novi broj telefona: ")
            elif komanda == '3':
                klijent['dioptrija'] = input("Unesite novu dioptriju klijenta: ")
        Klijenti.sacuvajKlijente()
        print("Zavrsili ste promenu podataka.")
        
def meniPromene():
    printMeniPromene()
    komanda = input(">>>")
    while komanda.upper() not in ('1', '2', '3', 'X'):
        print("Niste zadali dobru komandu\n")
        printMeniPromene()
        komanda = input(">>>")
    return komanda.upper()

def printMeniPromene():
    print("\nIzaberite opciju promene: ")
    print("1: Promena adrese klijenta")
    print("2: Promena broja telefona klijenta")
    print("3: Promena dioptrije klijenta")
    
def promeniCenuKontrole():
    print("7: promena cene kontrole")
    idk = input("Unesite id kontrole ciju cenu zelite da promenite: ")
    kont = Kontrole.findKontrola(idk)
    if kont == None:
        print("Ne postoji kontrola sa tim id")
    print(Kontrole.formatKontrola(kont))
    print()
    komanda = '0'
    while komanda != 'X':
        komanda = meniCena()
        if komanda == '1':
            kont['cena'] = input("Unesite novu cenu: ")
    Kontrole.sacuvajKontrolu()
    print("Izlaz")
    
def meniCena():
    printMeniCena()
    komanda = input(">>>")
    while komanda.upper() not in ('1', 'X'):
        print("Uneli ste pogresnu komandu\n")
        printMeniCena()
        komanda = input(">>>")
    return komanda.upper()

def printMeniCena():
    print("\n Odaberite opciju")
    print("1: promena cene")
    print("X: izlaz")
    
def searchKontrola():
    ime = input("Unesite ime i prezime opticara koji je radio kontrolu")
    lista = Kontrole.searchKontrola('opticar', ime)
    if len(lista) == 0:
        print("\nNe postije pregledi sa tim opticarem")
    else:
        print('\n')
        print(Kontrole.formatKontrole(lista))
        
        
main()
    
            
    
    
    
            
    



















            
        