# Traducido por Horckun
# FALTA COMPROBAR TEXTOS
########################
import sys
from com.l2jfrozen.gameserver.ai import CtrlIntention
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
from com.l2jfrozen.gameserver.network.serverpackets import CreatureSay
from com.l2jfrozen.util.random import Rnd

POLLEN = 6391
SKILL_NECTAR = 9998

# IDs
WATERED_SQUASH = [12774,12775,12776,12777,12778,12779]

class squash(JQuest) :

    def __init__(self,id,name,descr):
        JQuest.__init__(self,id,name,descr)
        
        self.adultSmallSquash = [12775,12776]
        self.adultLargeSquash = [12778,12779]

    def onAdvEvent(self,event,npc,player) :
        objId = npc.getObjectId()
        if event == "Good By" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"��Adi�s!! Jajaja"))
            npc.onDecay()
        elif event == "Good By1" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Adi�s a todos... Una gran calabaza se despidi�..."))
            npc.onDecay()
        elif event == "Good By2" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"�Puedes m�s r�pido? En 30 segundos huir�..."))
        elif event == "Good By3" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"�Romper� relaciones contigo en 20 segundos!"))
        elif event == "Good By4" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"�Solo me quedan 10 segundos! 9, 8, 7..!"))
        elif event == "Good By5" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Hey �Qu�date feliz! �Idiota, olv�date de m�!"))
        return

    def onSkillUse(self,npc,player,skill):
        npcId = npc.getNpcId()
        skillId = skill.getId()
        if skillId != SKILL_NECTAR : return
        if npcId not in WATERED_SQUASH : return
        objectId = npc.getObjectId()
        if skillId == SKILL_NECTAR :
            # Primer riego
            if npc.getNectar() == 0 :
                if Rnd.get(2) == 1 :
                    mytext = ["Para poder crecer, tengo que beber solo n�ctar... m�s a menudo.",
                              "Si me viertes n�ctar m�s r�pido, �crecer� m�s r�pido!",
                              ""�Bueno, cr�eme, toma un sorbo de n�ctar! ���Sin duda puedo convertirme en una gran calabaza !!!",
                              "�Trae n�ctar para cultivar una calabaza!",
                              "�El fruto de una hermosa calabaza joven comienza a brillar cuando se entierra la semilla! �De ahora en adelante podr� volverse saludable y fuerte!",
                              "Oh, �mucho tiempo sin verte?",
                              "�No esperaba ver mi hermosa apariencia?",
                              "Genial �Esto es algo! �N�ctar?",
                              "�Reabastecimiento de combustible! �Recargue 5 botellas para que pueda convertirme en una gran calabaza! �Oh!"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
                    mytext = ["�No te apresures! �Demasiado a menudo, no tengo tiempo!",
                              "No soy una ametralladora, no me disparar�s",
                              "Pero, �d�nde tienes prisa? �Demasiado a menudo, no tengo tiempo!",
                              "Vaya de nuevo demasiado r�pido",
                              "�Reduzcamos la velocidad un poco, no se apresure, tome lentamente la botella y vi�rtala lentamente!",
                              "�No tienes sentido de la velocidad? M�s lento vamos"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # Segundo riego
            elif npc.getNectar() == 1 :
                if Rnd.get(2) == 1 :
                    mytext = ["�Deseo convertirme en una gran calabaza!",
                              "��am �am �am �am! �Fuera! Cuidar - �bien!",
                              "�Crees que estoy maduro o podrido?",
                              "�El n�ctar es solo el mejor! �Ja! �Ja! �Ja!"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
                    mytext = [""�Oh! �Otra vez! �Puedes consumir n�ctar demasiado r�pido?",
                              "Si muero as� ahora, recibir�s solo una calabaza joven...",
                              "�Crece un poco m�s r�pido! Ser�a bueno convertirse en una gran calabaza, �una calabaza joven no es buena!",
                              "�Deber�an todos comer una calabaza tan peque�a? �Trae n�ctar, puedo ser m�s!"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # Tercer riego
            elif npc.getNectar() == 2 :
                if Rnd.get(2) == 1 :
                    mytext = ["�Calabaza, hambrienta! �Pide calmar su sed!",
                              "Bueno, finalmente... �es realmente delicioso! �Hay m�s?",
                              "�Cuidarme solo para comer? Genial, el tuyo es aleatorio... para no dar man� suicida"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
                    mytext = ["�A�ades agua? Que gusto",
                              "Maestro, s�lvame... No tengo el aroma del n�ctar, tengo que morir..."]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # Cuarto riego
            elif npc.getNectar() == 3 :
                if Rnd.get(2) == 1 :
                    mytext = ["�Muy bien, muy bien! �Sabes cu�l es el siguiente paso?",
                              "Si me atrapas, te doy 10 millones de adena !!! Estas de acuerdo"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
                    mytext = ["Tengo hambre �Quieres que me seque?",
                              "Necesito n�ctar para crecer un poco m�s r�pido."]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # Quinto riego
            elif npc.getNectar() == 4 :
                if Rnd.get(2) == 1 :
                    npc.addGood()
                if npc.getGood() >= 3 :
                    if npcId == 12774 :
                        newGourd = self.addSpawn(12775,npc)
                        newGourd.setOwner(player.getName())
                        self.startQuestTimer("Good By", 120000, newGourd, player) # Despu�s de 2 minutos, desaparici�n
                        self.startQuestTimer("Good By2", 90000, newGourd, player)   # 30 segundos para desvanecerse
                        self.startQuestTimer("Good By3", 100000, newGourd, player)  # 20 segundos para desvanecerse
                        self.startQuestTimer("Good By4", 110000, newGourd, player)  # 10 segundos para desvanecerse
                        mytext = ["Joven calabaza, �sediento! �C�mo, ya crecido?",
                                  "Huir� en 2 minutos"]
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
                    else :
                        newGourd = self.addSpawn(12778,npc)
                        newGourd.setOwner(player.getName())
                        self.startQuestTimer("Good By", 120000, newGourd, player) # Despu�s de 2 minutos, desaparici�n
                        self.startQuestTimer("Good By2", 90000, newGourd, player)   # 30 segundos para desvanecerse
                        self.startQuestTimer("Good By3", 100000, newGourd, player)  # 20 segundos para desvanecerse
                        self.startQuestTimer("Good By4", 110000, newGourd, player)  # 10 segundos para desvanecerse
                        mytext = ["La misericordia es un muy buen rasgo. Ahora mira, me siento cada vez mejor",
                                  "Huir� en 2 minutos"]
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
                else :
                    if npcId == 12774 :
                        newGourd = self.addSpawn(12776,npc)
                        newGourd.setOwner(player.getName())
                        mytext = ["�Oh! Fue - �no fue! Hay! Ahora! �No puedes tener el cuidado adecuado? �Me voy a pudrir!",
                                  "Wow �parando? �Por qu� agradecerte?",
                                  "Sed de n�ctar...",
                                  "�Quieres una calabaza grande? Pero quiero quedarme un poco de calabaza..."]
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
                    if npcId == 12777 :
                        newGourd = self.addSpawn(12779,npc)
                        newGourd.setOwner(player.getName())
                        mytext = ["�Oh! Fue - �no fue! Hay! Ahora! �No puedes tener el cuidado adecuado? �Me voy a pudrir!",
                                  "Wow �parando? �Por qu� agradecerte?",
                                  "Sed de n�ctar...",
                                  "�Quieres una calabaza grande? Pero quiero quedarme un poco de calabaza..."]
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
        return

    def onAttack(self,npc,player,damage,isPet) :
        npcId = npc.getNpcId()
        objId = npc.getObjectId()
        if npcId not in WATERED_SQUASH : return
        if npcId  in self.adultLargeSquash :
            if Rnd.get(30) < 2 :
                mytext = ["Las mordeduras son de rata de encaje... para reemplazar... �el cuerpo...!",
                          "Ja, ja, �creciendo! Totalmente en absoluto!",
                          "�No se puede apuntar todo? Mira todo para no huir...",
                          "�Cuento tus golpes! �Oh, recuerda un golpe otra vez!",
                          "�No pierdas tu tiempo!",
                          "Ja, �es realmente bueno escuchar eso?",
                          "�Consumo tus ataques para crecer!",
                          "�Es hora de golpear de nuevo! �Golpea una vez m�s!",
                          "Solo la m�sica �til puede abrir una gran calabaza... �No puedo abrirme con armas!"]
                npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
        return

    def onKill(self,npc,player,isPet) :
        npcId = npc.getNpcId()
        objId = npc.getObjectId()
        if npcId not in WATERED_SQUASH : return
        if npcId in self.adultSmallSquash :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"�Calabaza se abre!!"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"�Eeee! �Abre! Muchas cosas buenas..."))
        elif npcId in self.adultLargeSquash :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"�Calabaza se abre!!"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"�Eeee! �Abre! Muchas cosas buenas..."))
        else :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"�Por qu�, maestro?"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"�Oh, las tripas se cayeron!"))
        return

QUEST = squash(-1,"group_template","ai")

CREATED = State('Start', QUEST)
QUEST.setInitialState(CREATED)

for i in WATERED_SQUASH:
    QUEST.addSkillUseId(i)
    QUEST.addAttackId(i)
    QUEST.addKillId(i)