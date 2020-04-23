# Made by L2Emu Team
import sys
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest

qn = "6999_HeroCirclet"

MONUMENTS = [31690]+range(31769,31773)

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onTalk (Self,npc,player) :
   st = player.getQuestState(qn)
   htmltext = "<html><body>No estas en una mision que involucra a este NPC, o no cumples con los requisitos minimos de la mision de este NPC.</body></html>"
   if player.isHero() :
     if st.getQuestItemsCount(6842) :
       htmltext = "No puedes tener más de un círculo."
     else:
       st.giveItems(6842,1)
       htmltext = "Disfruta de tu Círculo de alas del destino."
     st.exitQuest(1)
   else :
     html = "<html><body>Monumento de los heroes:<br> No eres un heroe y no eres elegible para recibir el Circulo de alas del destino. Mas suerte la proxima vez.<br><a action=\"bypass -h npc_%objectId%_Chat 0\">Volver.</a></body></html>"
     htmltext = html.replace("%objectId%",str(npc.getObjectId()))
     st.exitQuest(1)
   return htmltext

QUEST = Quest(-1,qn,"custom")
CREATED     = State('Start', QUEST)

QUEST.setInitialState(CREATED)

for i in MONUMENTS:
    QUEST.addStartNpc(i)
    QUEST.addTalkId(i)