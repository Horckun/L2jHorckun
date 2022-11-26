import sys
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
from com.l2jfrozen.gameserver.network.serverpackets import CreatureSay
from com.l2jfrozen.util.random import Rnd

# delu_lizardman_special_agent
class delu_lizardman_special_agent(JQuest) :

    # init function.  Add in here variables that you'd like to be inherited by subclasses (if any)
    def __init__(self,id,name,descr):
        self.delu_lizardman_special_agent = 21105
        self.FirstAttacked = False
        # finally, don't forget to call the parent constructor to prepare the event triggering
        # mechanisms etc.
        JQuest.__init__(self,id,name,descr)

    def onAttack (self,npc,player,damage,isPet):
        objId=npc.getObjectId()
        if self.FirstAttacked:
           if Rnd.get(40) : return
<<<<<<< Updated upstream
           npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"�Oye! �Estamos teniendo un duelo aqu�!"))
        else :
           self.FirstAttacked = True
           npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"�C�mo te atreves a interrumpir nuestra lucha? Hola chicos, ayuda!"))
=======
           npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Oye! Estamos teniendo un duelo aqui!"))
        else :
           self.FirstAttacked = True
           npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Como te atreves a interrumpir nuestra lucha? Hola chicos, ayuda!"))
>>>>>>> Stashed changes
        return 

    def onKill (self,npc,player,isPet):
        npcId = npc.getNpcId()
        if npcId == self.delu_lizardman_special_agent:
            objId=npc.getObjectId()
            self.FirstAttacked = False
        elif self.FirstAttacked :
            self.addSpawn(npcId,npc.getX(), npc.getY(), npc.getZ(),npc.getHeading(),True,0)
        return 

QUEST = delu_lizardman_special_agent(-1,"delu_lizardman_special_agent","ai")

CREATED = State('Start', QUEST)
QUEST.setInitialState(CREATED)

QUEST.addKillId(QUEST.delu_lizardman_special_agent)
QUEST.addAttackId(QUEST.delu_lizardman_special_agent)