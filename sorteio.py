from PyQt5 import QtWidgets, uic
import random
import operator


playersDictionary = {}

def initializePlayersDict():
    playersDictionary.update({"Miguel" : getRandom()})
    playersDictionary.update({"Napoleão" : getRandom()})
    playersDictionary.update({"André" : getRandom()})
    playersDictionary.update({"Nicolau" : getRandom()})
    playersDictionary.update({"Nuno" : getRandom()})
    playersDictionary.update({"Maurício" : getRandom()})
    playersDictionary.update({"Salvador" : getRandom()})
    playersDictionary.update({"Santiago" : getRandom()})
    playersDictionary.update({"Vasco" : getRandom()})
    call.label_4.setText("Lista de jogadores: \n" + str(", ".join(playersDictionary.keys())))


def getRandom():
    for x in range(10):
        return random.randint(1,101)


def addPlayer():
    v = call.lineEdit.text()
    playersDictionary.update({v : getRandom()})
    print(playersDictionary)
    call.lineEdit.setText("")
    #call.label_4.setText("Lista de jogadores: \n" + str(playersDictionary.keys()))
    call.label_4.setText("Lista de jogadores: \n" + str(", ".join(playersDictionary.keys())))


def sortPlayers():
    numPlayers = len(playersDictionary)
    numPlayersTeam1 = round(numPlayers/2,0)
    numPlayersTeam2 = numPlayers - numPlayersTeam1
    #print("numPlayers= " + str(numPlayers))
    #print("numPlayersTeam1= " + str(numPlayersTeam1))
    #print("numPlayersTeam2= " + str(numPlayersTeam2))
    sortedPlayers = sorted(playersDictionary.items(), key=operator.itemgetter(1))
    #print(sortedPlayers)
    sortedPlayersList = [ seq[0] for seq in sortedPlayers ]
    print(sortedPlayersList)
    #Sort first team
    team1 = []
    for x in range(0, int(numPlayersTeam1)):
        team1.append(sortedPlayersList[x])
        call.label_5.setText("Equipa 1: \n" + str("\n".join(team1)))
    #print("Team1 size: " + str(len(team1)))
    #Sort second team
    team2 = []
    for x in range(int(numPlayersTeam1), int(numPlayers)):
        team2.append(sortedPlayersList[x])
        call.label_6.setText("Equipa 2: \n" + str("\n".join(team2)))
    #print("Team2 size: " + str(len(team2)))



app = QtWidgets.QApplication([])
call = uic.loadUi("sorteio.ui")

call.btnAdicionar.clicked.connect(addPlayer)
call.btnSortear.clicked.connect(sortPlayers)
#initializePlayersDict()

call.show()
app.exec()
