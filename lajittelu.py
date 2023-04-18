#!/usr/bin/env python

from luoja import luoja
from pprint import pprint
import random
import time

# this imports the nested list that was made by luoja.py and returns a list that has all subjects from pakkoaineet.txt in the list
plista = luoja()[0]


def clear(periodit: list) -> None:  # takes out the group numbers at the end of all subjects
    for k in periodit:
        for i in range(len(k)):
            for j in range(len(k[i])):
                k[i][j] = k[i][j][:-2]
            k[i] = set(k[i])
            k[i] = list(k[i])


class Lajittelija:  # big boy
    def __init__(self, periodit):
        self.periodit = periodit
        self.ainelista = []  # this is the list we'll be putting everything into

    # choose a subject based on if it's already in the list or not
    def valitse(self, aineet: list) -> bool:
        switch = False
        for aine in aineet:
            if aine not in self.ainelista:
                self.ainelista.append(aine)
                switch = True
                break
        if not switch:
            self.ainelista.append('-')
            return 1
        return self.ainelista[-1]

    def lajittele(self) -> list:  # Process that makes the list
        for periodi in self.periodit:
            self.ainelista.append("?")
            for lohko in periodi:
                # this is where the previous function gets utilized
                self.valitse(lohko)
        # I know this is terrible code and that there's a better way to do it, shut up
        temp = [[]]
        # So this just breaks the big list into many smaller lists. We do it like this so that
        # then it's easier to see if a course has already been selected, no need for for loops.
        for i in self.ainelista:
            if i != "?":
                temp[-1].append(i)
            else:
                temp.append([])
        self.ainelista = []
        return (temp)

def luo_lista(): #This combines everything and creates a huge nested list with a few hundred possible course combinations
    clear(plista) #Get rid of group numbers
    beforetime = time.monotonic() #start a timer
    Rick = Lajittelija(plista)
    kaikki = []
    väärät=0
    for i in range(10000): #The ugliest algorithm to determine a lot of the combinations, but It'll do
        for k in plista:
            for i in range(len(k)):
                random.shuffle(k[i]) #basically the Rick.lajittele can only sort out one combination of courses. So insted of coding an extra feature we just shuffle the list and get a new combination that way.
        vaihtoehto = Rick.lajittele()
        tarkistuslista = []
        pakkoaineet = luoja()[1].copy()
        for k in vaihtoehto: #take out the combinations, where every course doesn't exist
            for i in range(len(k)):
                if k[i] != "-": 
                    tarkistuslista.append(k[i])
        for i in range(len(pakkoaineet)):
            if pakkoaineet[0] in tarkistuslista:
                del pakkoaineet[0]
        if len(pakkoaineet) == 1:
            if vaihtoehto not in kaikki:
                kaikki.append(vaihtoehto)
        else:
            väärät += 1
    aftertime = time.monotonic() #stop the timer
    totaltime = aftertime - beforetime
    return [kaikki, totaltime]
    
class Preferenssit:
    def __init__(self, ei_palkkia="", ei_opettajaa="", ei_hyppytunteja=False):
        self.ei_palkkia = ei_palkkia
        self.ei_opettajaa = ei_opettajaa
        self.ei_hyppytunteja = ei_hyppytunteja
    def kaksoiskurssit(self):
        pass
    def palkkipoistaja(self, ei_palkkia):
        pass
    def opettajapoistaja(self, ei_opettajaa):
        pass
    def hyppytuntipoistaja(self, ei_hyppytunteja):
        pass

if __name__ == '__main__':
    print("Calculating...")
    thing = luo_lista()
    print("Runtime: {} second(s)".format(thing[1]))
    print("Combinations found:",len(thing[0]))
    example = random.choice(thing[0])
    time.sleep(2)
    print("Random example:")
    pprint(example)

