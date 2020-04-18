import sys
from com.l2jfrozen.gameserver.ai import CtrlIntention
from com.l2jfrozen.gameserver.model.entity.siege.clanhalls import FortressOfResistance
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
from com.l2jfrozen.gameserver.managers import ClanHallManager
from com.l2jfrozen.util.random import Rnd
from java.lang import System

NURKA = 35368
MESSENGER = 35382
CLANLEADERS = []

class Nurka(JQuest):

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onTalk (self,npc,player):
   global CLANLEADERS
   npcId = npc.getNpcId()
   if npcId == MESSENGER :
     for clname in CLANLEADERS:
       if player.getName() == clname :
         return "<html><body>¡Estás registrado!</body></html>"
     if FortressOfResistance.getInstance().Conditions(player) :
       CLANLEADERS.append(player.getName())
       return "<html><body>Te has registrado en la batalla</body></html>"
     else:
       return "<html><body>¡Las condiciones no están permitidas para hacer eso!</body></html>"
   return
 
 def onAttack (self,npc,player,damage,isPet):
   CLAN = player.getClan()
   if CLAN == None :
     return
   CLANLEADER = CLAN.getLeader()
   if CLANLEADER == None :
     return
   global CLANLEADERS
   for clname in CLANLEADERS:
     if clname <> None :
       if CLANLEADER.getName() == clname :
         FortressOfResistance.getInstance().addSiegeDamage(CLAN,damage)
   return


 def onKill(self,npc,player,isPet):
   FortressOfResistance.getInstance().CaptureFinish()
   return

QUEST = Nurka(-1, "nurka", "ai")
CREATED = State('Start', QUEST)
QUEST.setInitialState(CREATED)

QUEST.addTalkId(MESSENGER)
QUEST.addStartNpc(MESSENGER)

QUEST.addAttackId(NURKA)
QUEST.addKillId(NURKA)