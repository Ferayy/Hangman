# Hangman made by Ferdi Deveci 
# Studentennummer: 1006990

aantalPogingen = 9
vraagWoord = input("Vul hier je woord in: ")
gokjes = []
goedeGokjes = []
for index in vraagWoord:
    goedeGokjes += "_"

while True:
    geefLetter = input("Raad een letter: ")
    zitInWoord = geefLetter in vraagWoord
    
    if geefLetter in gokjes:
        print("Je hebt deze letter al geraden. Kies een andere letter")
    else:
        gokjes.append(geefLetter)

        if zitInWoord == False:
            aantalPogingen -=1
            print("Je hebt nog", aantalPogingen, "pogingen te gaan")
        else:
            for index in range(len(vraagWoord)):
                if vraagWoord[index] == geefLetter:
                    goedeGokjes[index] = geefLetter
    
        if aantalPogingen == 0:
            print("Game over")
            break;
        
        geradenWoord = ''.join(goedeGokjes)
        if geradenWoord == vraagWoord:
            print("Je hebt gewonnen! Het woord is:", vraagWoord)
            break;
            
        print(goedeGokjes)
