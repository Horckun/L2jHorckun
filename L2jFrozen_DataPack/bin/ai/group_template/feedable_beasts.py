# Growth-capable mobs: Polymorphing upon successful feeding.
# Written by Fulminus
# Traducido por Horckun.
# # # # # # # # # # #
import sys
from com.l2jfrozen.gameserver.ai import CtrlIntention
from com.l2jfrozen.gameserver.datatables.sql import NpcTable
from com.l2jfrozen.gameserver.idfactory import IdFactory
from com.l2jfrozen.gameserver.model.actor.instance import L2TamedBeastInstance
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
from com.l2jfrozen.gameserver.network.serverpackets import CreatureSay
from com.l2jfrozen.gameserver.network.serverpackets import SocialAction
from com.l2jfrozen.util.random import Rnd

GOLDEN_SPICE = 6643
CRYSTAL_SPICE = 6644
SKILL_GOLDEN_SPICE = 2188
SKILL_CRYSTAL_SPICE = 2189
foodSkill = {GOLDEN_SPICE:SKILL_GOLDEN_SPICE, CRYSTAL_SPICE:SKILL_CRYSTAL_SPICE}

#print "Feedable beasts"

class feedable_beasts(JQuest) :

    # init function.  Add in here variables that you'd like to be inherited by subclasses (if any)
    def __init__(self,id,name,descr):
        # firstly, don't forget to call the parent constructor to prepare the event triggering
        # mechanisms etc.
        JQuest.__init__(self,id,name,descr)
        # DEFINE MEMBER VARIABLES FOR THIS AI
        # all mobs that can eat...
        self.tamedBeasts = range(16013,16019)
        self.feedableBeasts = range(21451,21508)+range(21824,21830)+ self.tamedBeasts
        # all mobs that grow by eating
        # mobId: current_growth_level, {food: [list of possible mobs[possible sublist of tamed pets]]}, chance of growth
        self.growthCapableMobs = {
            # Alpen Kookabura
            21451: [0,{GOLDEN_SPICE:[21452,21453, 21454, 21455],CRYSTAL_SPICE:[21456,21457, 21458, 21459]},100],
            21452: [1,{GOLDEN_SPICE:[21460,21462],CRYSTAL_SPICE:[]},40],
            21453: [1,{GOLDEN_SPICE:[21461,21463],CRYSTAL_SPICE:[]},40],
            21454: [1,{GOLDEN_SPICE:[21460,21462],CRYSTAL_SPICE:[]},40],
            21455: [1,{GOLDEN_SPICE:[21461,21463],CRYSTAL_SPICE:[]},40],
            21456: [1,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[21464,21466]},40],
            21457: [1,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[21465,21467]},40],
            21458: [1,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[21464,21466]},40],
            21459: [1,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[21465,21467]},40],
            21460: [2,{GOLDEN_SPICE:[[21468,21824],[16017,16018]],CRYSTAL_SPICE:[]},25],
            21461: [2,{GOLDEN_SPICE:[[21469,21825],[16017,16018]],CRYSTAL_SPICE:[]},25],
            21462: [2,{GOLDEN_SPICE:[[21468,21824],[16017,16018]],CRYSTAL_SPICE:[]},25],
            21463: [2,{GOLDEN_SPICE:[[21469,21825],[16017,16018]],CRYSTAL_SPICE:[]},25],
            21464: [2,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[[21468,21824],[16017,16018]]},25],
            21465: [2,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[[21469,21825],[16017,16018]]},25],
            21466: [2,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[[21468,21824],[16017,16018]]},25],
            21467: [2,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[[21469,21825],[16017,16018]]},25],
            # Alpen Buffalo
            21470: [0,{GOLDEN_SPICE:[21471,21472, 21473, 21474],CRYSTAL_SPICE:[21475,21476, 21477, 21478]},100],
            21471: [1,{GOLDEN_SPICE:[21479,21481],CRYSTAL_SPICE:[]},40],
            21472: [1,{GOLDEN_SPICE:[21481,21482],CRYSTAL_SPICE:[]},40],
            21473: [1,{GOLDEN_SPICE:[21479,21481],CRYSTAL_SPICE:[]},40],
            21474: [1,{GOLDEN_SPICE:[21480,21482],CRYSTAL_SPICE:[]},40],
            21475: [1,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[21483,21485]},40],
            21476: [1,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[21484,21486]},40],
            21477: [1,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[21483,21485]},40],
            21478: [1,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[21484,21486]},40],
            21479: [2,{GOLDEN_SPICE:[[21487,21826],[16013,16014]],CRYSTAL_SPICE:[]},25],
            21480: [2,{GOLDEN_SPICE:[[21488,21827],[16013,16014]],CRYSTAL_SPICE:[]},25],
            21481: [2,{GOLDEN_SPICE:[[21487,21826],[16013,16014]],CRYSTAL_SPICE:[]},25],
            21482: [2,{GOLDEN_SPICE:[[21488,21827],[16013,16014]],CRYSTAL_SPICE:[]},25],
            21483: [2,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[[21487,21826],[16013,16014]]},25],
            21484: [2,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[[21488,21827],[16013,16014]]},25],
            21485: [2,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[[21487,21826],[16013,16014]]},25],
            21486: [2,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[[21488,21827],[16013,16014]]},25],
            # Alpen Cougar
            21489: [0,{GOLDEN_SPICE:[21490,21491, 21492, 21493],CRYSTAL_SPICE:[21494,21495, 21496, 21497]},100],
            21490: [1,{GOLDEN_SPICE:[21498,21500],CRYSTAL_SPICE:[]},40],
            21491: [1,{GOLDEN_SPICE:[21499,21501],CRYSTAL_SPICE:[]},40],
            21492: [1,{GOLDEN_SPICE:[21498,21500],CRYSTAL_SPICE:[]},40],
            21493: [1,{GOLDEN_SPICE:[21499,21501],CRYSTAL_SPICE:[]},40],
            21494: [1,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[21502,21504]},40],
            21495: [1,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[21503,21505]},40],
            21496: [1,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[21502,21504]},40],
            21497: [1,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[21503,21505]},40],
            21498: [2,{GOLDEN_SPICE:[[21506,21828],[16015,16016]],CRYSTAL_SPICE:[]},25],
            21499: [2,{GOLDEN_SPICE:[[21507,21829],[16015,16016]],CRYSTAL_SPICE:[]},25],
            21500: [2,{GOLDEN_SPICE:[[21506,21828],[16015,16016]],CRYSTAL_SPICE:[]},25],
            21501: [2,{GOLDEN_SPICE:[[21507,21829],[16015,16016]],CRYSTAL_SPICE:[]},25],
            21502: [2,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[[21506,21828],[16015,16016]]},25],
            21503: [2,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[[21507,21829],[16015,16016]]},25],
            21504: [2,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[[21506,21828],[16015,16016]]},25],
            21505: [2,{GOLDEN_SPICE:[],CRYSTAL_SPICE:[[21507,21829],[16015,16016]]},25]
            }
        self.madCowPolymorph = {21824:21468,21825:21469,21826:21487,21827:21488,21828:21506,21829:21507}
<<<<<<< Updated upstream
        self.Text = [["�Qu� me acabas de hacer?","Quieres domesticarme, �eh?","No me des esto. Quiz�s est�s en peligro.","Bah bah. �Qu� es esta cosa desagradable?","Mi barriga se ha estado quejando. Eso dio en el clavo.","�Que es esto? �Puedo comerlo?","No necesitas preocuparte por m�.","Deliciosa comida, gracias.","�Est�s empezando a gustarme!","Trago"], 
                    ["No creo que hayas renunciado a la idea de domesticarme.","Eso es solo comida para m�. Quiz�s yo tambi�n pueda comer tu mano.","�Comer esto me har� engordar? Jaja","�Por qu� siempre me das de comer?","No conf�es en mi. Puedo traicionarte."], 
                    ["Destruir","�Mira lo que has hecho!","Sentimiento raro...! Las malas intenciones crecen en mi coraz�n...!","�Esta pasando!","Esto es triste... �Lo bueno es triste...!"]]
=======
        self.Text = [["Que me acabas de hacer?","Quieres domesticarme, eh?","No me des esto. Quizas estes en peligro.","Bah bah. Que es esta cosa desagradable?","Mi barriga se ha estado quejando. Eso dio en el clavo.","Que es esto? Puedo comerlo?","No necesitas preocuparte por mi.","Deliciosa comida, gracias.","Estas empezando a gustarme!","Trago"], 
                    ["No creo que hayas renunciado a la idea de domesticarme.","Eso es solo comida para m�. Quizas yo tambien pueda comer tu mano.","Comer esto me hara engordar? Jaja","Por que siempre me das de comer?","No confies en mi. Puedo traicionarte."], 
                    ["Destruir","Mira lo que has hecho!","Sentimiento raro...! Las malas intenciones crecen en mi corazon...!","Esta pasando!","Esto es triste... Lo bueno es triste...!"]]
>>>>>>> Stashed changes

        self.feedInfo = {} # : feedInfo[objectId of mob] = objectId of player feeding it

        for i in self.feedableBeasts :
            self.addSkillUseId(i)
            self.addKillId(i)

    def onAdvEvent(self,event,npc,player) :
        if event == "polymorph Mad Cow" and npc and player:
            if npc.getNpcId() in self.madCowPolymorph.keys() :
                # remove the feed info from the previous mob
                if self.feedInfo[npc.getObjectId()] == player.getObjectId() :
                    self.feedInfo.pop(npc.getObjectId())
                # despawn the mad cow
                npc.deleteMe()
                # spawn the new mob 
                nextNpc = self.addSpawn(self.madCowPolymorph[npc.getNpcId()],npc)
                
                # register the player in the feedinfo for the mob that just spawned
                self.feedInfo[nextNpc.getObjectId()] = player.getObjectId()
                nextNpc.setRunning()
                nextNpc.addDamageHate(player,0,99999)
                nextNpc.getAI().setIntention(CtrlIntention.AI_INTENTION_ATTACK, player)

    def spawnNext(self, npc, growthLevel,player,food) :
        npcId = npc.getNpcId()
        nextNpcId = 0

        # find the next mob to spawn, based on the current npcId, growthlevel, and food.
        if growthLevel == 2:
            rand = Rnd.get(2)
            # if tamed, the mob that will spawn depends on the class type (fighter/mage) of the player!
            if rand == 1 :
                if player.getClassId().isMage() :
                    nextNpcId = self.growthCapableMobs[npcId][1][food][1][1]
                else :
                    nextNpcId = self.growthCapableMobs[npcId][1][food][1][0]
  
            # if not tamed, there is a small chance that have "mad cow" disease.
            # that is a stronger-than-normal animal that attacks its feeder
            else :
                if Rnd.get(5) == 0 :
                    nextNpcId = self.growthCapableMobs[npcId][1][food][0][1]
                else :
                    nextNpcId = self.growthCapableMobs[npcId][1][food][0][0]
        # all other levels of growth are straight-forward
        else :            
            nextNpcId = self.growthCapableMobs[npcId][1][food][Rnd.get(len(self.growthCapableMobs[npcId][1][food]))]
        
        # remove the feedinfo of the mob that got despawned, if any
        if self.feedInfo.has_key(npc.getObjectId()) :
            if self.feedInfo[npc.getObjectId()] == player.getObjectId() :
                self.feedInfo.pop(npc.getObjectId())
        
        # despawn the old mob
        if self.growthCapableMobs[npcId][0] == 0 :
            npc.onDecay()
        else :
            npc.deleteMe()
        
        # if this is finally a trained mob, then despawn any other trained mobs that the
        # player might have and initialize the Tamed Beast.
        if nextNpcId in self.tamedBeasts :
            oldTrained = player.getTrainedBeast()
            if oldTrained :
                oldTrained.doDespawn()

            #the following 5 commented lines are not needed, but they provide a plausible alternate implementation...just in case...
            #nextNpc = self.addSpawn(nextNpcId,npc)
            #nextNpc.setOwner(player)
            #nextNpc.setFoodType(foodSkill[food])
            #nextNpc.setHome(npc)
                
            template = NpcTable.getInstance().getTemplate(nextNpcId)
            nextNpc = L2TamedBeastInstance(IdFactory.getInstance().getNextId(), template, player, foodSkill[food], npc.getX(), npc.getY(), npc.getZ())
            nextNpc.setRunning()

            objectId = nextNpc.getObjectId()
            
            st = player.getQuestState("20_BringUpWithLove")
            if st :
                if Rnd.get(100) <= 5 and st.getQuestItemsCount(7185) == 0 :
                    st.giveItems(7185,1) #if player has quest 20 going, give quest item
                    st.set("cond","2")   #it's easier to hardcode it in here than to try and repeat this stuff in the quest

            # also, perform a rare random chat
            rand = Rnd.get(20)
            if rand > 4 : pass
<<<<<<< Updated upstream
            elif rand == 0 : npc.broadcastPacket(CreatureSay(objectId,0,nextNpc.getName(), player.getName()+", �me vas a mostrar tu escondite?"))
            elif rand == 1 : npc.broadcastPacket(CreatureSay(objectId,0,nextNpc.getName(), player.getName()+", cada vez que veo especias, pienso en ti."))
            elif rand == 2 : npc.broadcastPacket(CreatureSay(objectId,0,nextNpc.getName(), player.getName()+", No es necesario volver al pueblo. Te dare fuerzas"))
            elif rand == 3 : npc.broadcastPacket(CreatureSay(objectId,0,nextNpc.getName(), "Gracias, "+player.getName()+". Espero poder ayudarle."))
            elif rand == 4 : npc.broadcastPacket(CreatureSay(objectId,0,nextNpc.getName(), player.getName()+", �qu� puedo hacer para ayudarte?"))
=======
            elif rand == 0 : npc.broadcastPacket(CreatureSay(objectId,0,nextNpc.getName(), player.getName()+", me vas a mostrar tu escondite?"))
            elif rand == 1 : npc.broadcastPacket(CreatureSay(objectId,0,nextNpc.getName(), player.getName()+", cada vez que veo especias, pienso en ti."))
            elif rand == 2 : npc.broadcastPacket(CreatureSay(objectId,0,nextNpc.getName(), player.getName()+", No es necesario volver al pueblo. Te dare fuerzas"))
            elif rand == 3 : npc.broadcastPacket(CreatureSay(objectId,0,nextNpc.getName(), "Gracias, "+player.getName()+". Espero poder ayudarle."))
            elif rand == 4 : npc.broadcastPacket(CreatureSay(objectId,0,nextNpc.getName(), player.getName()+", que puedo hacer para ayudarte?"))
>>>>>>> Stashed changes

        # if not trained, the newly spawned mob will automatically be agro against its feeder
        # (what happened to "never bite the hand that feeds you" anyway?!)
        else :
            # spawn the new mob
            nextNpc = self.addSpawn(nextNpcId,npc)

            if nextNpcId in self.madCowPolymorph :
                self.startQuestTimer("polymorph Mad Cow", 10000, nextNpc, player)            
            
            # register the player in the feedinfo for the mob that just spawned
            self.feedInfo[nextNpc.getObjectId()] = player.getObjectId()
            nextNpc.setRunning()
            nextNpc.addDamageHate(player,0,99999)
            nextNpc.getAI().setIntention(CtrlIntention.AI_INTENTION_ATTACK, player)

    def onSkillUse (self,npc,player,skill):
        # gather some values on local variables
        npcId = npc.getNpcId()
        skillId = skill.getId()
        # check if the npc and skills used are valid for this script.  Exit if invalid.
        if npcId not in self.feedableBeasts : return
        if skillId not in [SKILL_GOLDEN_SPICE,SKILL_CRYSTAL_SPICE] : return

        # first gather some values on local variables
        objectId = npc.getObjectId()
        growthLevel = 3  # if a mob is in feedableBeasts but not in growthCapableMobs, then it's at max growth (3)
        if self.growthCapableMobs.has_key(npcId) :
            growthLevel = self.growthCapableMobs[npcId][0]

        # prevent exploit which allows 2 players to simultaneously raise the same 0-growth beast
        # If the mob is at 0th level (when it still listens to all feeders) lock it to the first feeder!       
        if (growthLevel==0) and self.feedInfo.has_key(objectId):
            return
        else :
            self.feedInfo[objectId] = player.getObjectId()

        food = 0
        if skillId == SKILL_GOLDEN_SPICE :
            food = GOLDEN_SPICE
        elif skillId == SKILL_CRYSTAL_SPICE :
            food = CRYSTAL_SPICE

        # display the social action of the beast eating the food.
        npc.broadcastPacket(SocialAction(objectId,2))

        # if this pet can't grow, it's all done.
        if npcId in self.growthCapableMobs.keys() :
            # do nothing if this mob doesn't eat the specified food (food gets consumed but has no effect).
            if len(self.growthCapableMobs[npcId][1][food]) == 0 : return

            # rare random talk...
            if Rnd.get(20) == 0 :
                npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),self.Text[growthLevel][Rnd.get(len(self.Text[growthLevel]))]))

            if growthLevel > 0 :
                # check if this is the same player as the one who raised it from growth 0.
                # if no, then do not allow a chance to raise the pet (food gets consumed but has no effect).
                if self.feedInfo[objectId] != player.getObjectId() : return

            # Polymorph the mob, with a certain chance, given its current growth level
            if Rnd.get(100) < self.growthCapableMobs[npcId][2] :
                self.spawnNext(npc, growthLevel,player,food)
        elif npcId in self.tamedBeasts :
            if skillId == npc.getFoodType() :
                npc.onReceiveFood()
<<<<<<< Updated upstream
                mytext = ["�Recargas! �Si!","Soy una bestia tan glotona, �es vergonzoso! Jaja",
                          "Su sentimiento cooperativo ha ido mejorando cada vez m�s.",
                          "�Te ayudar�!",
                          "El clima es muy bueno. �Quieres ir de picnic?",
                          "�Realmente me gustas! Esto es sabroso...",
                          "Si no tiene que abandonar este lugar, entonces puedo ayudarlo.",
                          "�En qu� puedo ayudarte?",
                          "�No estoy aqu� solo por comida!",
                          "�ame, �ame, �ame, �ame, �ame!"]
=======
                mytext = ["Recargas! Si!","Soy una bestia tan glotona, es vergonzoso! Jaja",
                          "Su sentimiento cooperativo ha ido mejorando cada vez mas.",
                          "Te ayudare!",
                          "El clima es muy bueno. Quieres ir de picnic?",
                          "Realmente me gusta! Esto es sabroso...",
                          "Si no tiene que abandonar este lugar, entonces puedo ayudarlo.",
                          "En que puedo ayudarte?",
                          "No estoy aqui solo por comida!"]
>>>>>>> Stashed changes
                npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
        return

    def onKill (self,npc,player,isPet):
        # remove the feedinfo of the mob that got killed, if any
        if self.feedInfo.has_key(npc.getObjectId()) :
            self.feedInfo.pop(npc.getObjectId())


# now call the constructor (starts up the ai)
QUEST = feedable_beasts(-1,"feedable_beasts","ai")