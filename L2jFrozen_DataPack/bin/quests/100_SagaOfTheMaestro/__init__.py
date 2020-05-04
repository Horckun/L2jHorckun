# Made by Emperorc
import sys
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from quests.SagasSuperclass import Quest as JQuest

qn = "100_SagaOfTheMaestro"
qnu = 100
qna = "Saga of the Maestro"

class Quest (JQuest) :

 def __init__(self,id,name,descr):
     # first initialize the quest.  The superclass defines variables, instantiates States, etc
     JQuest.__init__(self,id,name,descr)
     # Next, override necessary variables:
     self.NPC = [31592,31273,31597,31597,31596,31646,31648,31653,31654,31655,31656,31597]
     self.Items = [7080,7607,7081,7515,7298,7329,7360,7391,7422,7453,7108,0]
     self.Mob = [27260,27249,27308]
     self.qn = qn
     self.classid = 118
     self.prevclass = 0x39
     self.X = [164650,47429,47391]
     self.Y = [-74121,-56923,-56929]
     self.Z = [-2871,-2383,-2370]
     self.Text = ["PLAYERNAME! Perseguido hasta aqui! Sin embargo, salte de los limites de Banshouren. Miras al gigante como el signo del poder!",
                  "... Oh Dios! Asi que fue... comencemos!","No tengo paciencia...! He sido una fuerza gigante...! Charla de tos ah ah ah!",
                  "Rendir homenaje a los que interrumpen a los ordenados sera la muerte de PLAYERNAME!","Ahora, mi alma liberada de los grilletes del milenio, Halixia, a la parte de atras vengo...",
                  "Por que interfieres en las batallas de los demas?","Esto es una perdida de tiempo... Di adios...! ","... Ese es el enemigo.",
                  "...Bondad! PLAYERNAME que todavia estas buscando?","PLAYERNAME... No solo a quien la victoria. Solo el personal involucrado en la lucha es elegible para compartir la victoria.",
                  "Tu espada no es un adorno. No crees, PLAYERNAME?","Dios mio! Ya no siento una batalla alli ahora","deja...","Solo participe en la batalla para prohibir su eleccion. Quizas deberias arrepentirte.",
                  "La nacion humana era tonta al tratar de luchar contra la fuerza de un gigante.","Debe... Retirarse... Demasiado... Fuerte","PLAYERNAME. Derrota... reteniendo... y... Mo... Hacker ","....! Lucha... Derrota... Es... Lucha... Derrota... Es..."]
     # finally, register all events to be triggered appropriately, using the overriden values.
     JQuest.registerNPCs(self)

QUEST       = Quest(qnu,qn,qna)

QUEST.setInitialState(QUEST.CREATED)