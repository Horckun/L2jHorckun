import sys
from com.l2jfrozen.gameserver.ai import CtrlIntention
from com.l2jfrozen.gameserver.model.entity.siege.clanhalls import DevastatedCastle
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
from com.l2jfrozen.gameserver.managers import ClanHallManager
from com.l2jfrozen.util.random import Rnd
from com.l2jfrozen.gameserver.model import L2Clan
from com.l2jfrozen.gameserver.model import L2ClanMember
from java.lang import System

GUSTAV = 35410
MESSENGER = 35420
CLANLEADERS = []

class Gustav(JQuest):

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onTalk (self,npc,player):
   global CLANLEADERS
   npcId = npc.getNpcId()
   if npcId == MESSENGER :
     for clname in CLANLEADERS:
       if player.getName() == clname :
<<<<<<< Updated upstream
         return "<html><body>¡Ya te has registrado!</body></html>"
     if DevastatedCastle.getInstance().Conditions(player) :
       CLANLEADERS.append(player.getName())
       return "<html><body>Ya te has registrado en el asedio</body></html>"
     else:
       return "<html><body>¡Las condiciones no están permitidas para hacer eso!</body></html>"
=======
         return "<html><body>Ya te has registrado!</body></html>"
     if DevastatedCastle.getInstance().Conditions(player) :
       CLANLEADERS.append(player.getName())
       return "<html><body>Ya te has registrado en el asedio.</body></html>"
     else:
       return "<html><body>Las condiciones no estan permitidas para hacer eso!</body></html>"
>>>>>>> Stashed changes
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
         DevastatedCastle.getInstance().addSiegeDamage(CLAN,damage)
   return

 def onKill(self,npc,player,isPet):
   DevastatedCastle.getInstance().SiegeFinish()
   return

QUEST = Gustav(-1, "gustav", "ai")
CREATED = State('Start', QUEST)
QUEST.setInitialState(CREATED)

QUEST.addTalkId(MESSENGER)
QUEST.addStartNpc(MESSENGER)

QUEST.addAttackId(GUSTAV)
QUEST.addKillId(GUSTAV)