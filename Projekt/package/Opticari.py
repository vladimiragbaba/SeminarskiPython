'''
Created on Feb 18, 2019

@author: User
'''
def login(ime, lozinka):
    print(opticari)
    for opt in opticari:
        if opt["ime"] == ime and opt ["lozinka"] == lozinka:
            return True
        return False
    
def ucitajOpticare():
    for opt in open("opticari.txt", 'r').readlines():
        if len(opt) > 1:
            opticar = str2opt(opt)
            opticari.append(opticar)
            
def str2opt(line):
    if line[-1] == '\n':
        line = line[:-1]
    ime, lozinka = line.split('|')
    opt = {
        'ime' : ime,
        'lozinka' : lozinka,
        }
    return opt

def opt2str(opt):
    return "|".join(opt['ime'], opt['lozinka'])

            
opticari = []
ucitajOpticare()