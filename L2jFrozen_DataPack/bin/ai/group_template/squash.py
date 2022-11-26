# Traducido por Horckun
<<<<<<< Updated upstream
# FALTA COMPROBAR TEXTOS
########################
=======
#######################
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"¡¡Adiós!! Jajaja"))
            npc.onDecay()
        elif event == "Good By1" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Adiós a todos... Una gran calabaza se despidió..."))
            npc.onDecay()
        elif event == "Good By2" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"¿Puedes más rápido? En 30 segundos huiré..."))
        elif event == "Good By3" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"¡Romperé relaciones contigo en 20 segundos!"))
        elif event == "Good By4" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"¡Solo me quedan 10 segundos! 9, 8, 7..!"))
        elif event == "Good By5" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Hey ¡Quédate feliz! ¡Idiota, olvídate de mí!"))
=======
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Adios!! Jajaja"))
            npc.onDecay()
        elif event == "Good By1" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Adios a todos... Una gran calabaza se despidio..."))
            npc.onDecay()
        elif event == "Good By2" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Puedes mas rapido? En 30 segundos huire..."))
        elif event == "Good By3" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Rompere relaciones contigo en 20 segundos!"))
        elif event == "Good By4" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Solo me quedan 10 segundos! 9, 8, 7..!"))
        elif event == "Good By5" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Hey Quedate feliz! Idiota, olvidate de mi!"))
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
                    mytext = ["Para poder crecer, tengo que beber solo néctar... más a menudo.",
                              "Si me viertes néctar más rápido, ¡creceré más rápido!",
                              ""¡Bueno, créeme, toma un sorbo de néctar! ¡¡¡Sin duda puedo convertirme en una gran calabaza !!!",
                              "¡Trae néctar para cultivar una calabaza!",
                              "¡El fruto de una hermosa calabaza joven comienza a brillar cuando se entierra la semilla! ¡De ahora en adelante podrá volverse saludable y fuerte!",
                              "Oh, ¿mucho tiempo sin verte?",
                              "¿No esperaba ver mi hermosa apariencia?",
                              "Genial ¡Esto es algo! ¿Néctar?",
                              "¡Reabastecimiento de combustible! ¡Recargue 5 botellas para que pueda convertirme en una gran calabaza! ¡Oh!"]
=======
                    mytext = ["Para poder crecer, tengo que beber solo nectar... mas a menudo.",
                              "Si me viertes nectar mas rapido, crecere mas rapido!",
                              "Bueno, creeme, toma un sorbo de nectar! Sin duda puedo convertirme en una gran calabaza!!!",
                              "Trae nectar para cultivar una calabaza!",
                              "El fruto de una hermosa calabaza joven comienza a brillar cuando se entierra la semilla! De ahora en adelante podra volverse saludable y fuerte!",
                              "Oh, mucho tiempo sin verte?",
                              "No esperaba ver mi hermosa apariencia?",
                              "Genial Esto es algo! Nectar?",
                              "Reabastecimiento de combustible! Recargue 5 botellas para que pueda convertirme en una gran calabaza! Oh!"]
>>>>>>> Stashed changes
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
<<<<<<< Updated upstream
                    mytext = ["¡No te apresures! ¡Demasiado a menudo, no tengo tiempo!",
                              "No soy una ametralladora, no me dispararás",
                              "Pero, ¿dónde tienes prisa? ¡Demasiado a menudo, no tengo tiempo!",
                              "Vaya de nuevo demasiado rápido",
                              "¡Reduzcamos la velocidad un poco, no se apresure, tome lentamente la botella y viértala lentamente!",
                              "¿No tienes sentido de la velocidad? Más lento vamos"]
=======
                    mytext = ["No te apresures! Demasiado a menudo, no tengo tiempo!",
                              "No soy una ametralladora, no me dispararas",
                              "Pero, donde tienes prisa? Demasiado a menudo, no tengo tiempo!",
                              "Vaya de nuevo demasiado rapido",
                              "Reduzcamos la velocidad un poco, no se apresure, tome lentamente la botella y viertala lentamente!",
                              "No tienes sentido de la velocidad? Vamos muy lentos"]
>>>>>>> Stashed changes
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # Segundo riego
            elif npc.getNectar() == 1 :
                if Rnd.get(2) == 1 :
<<<<<<< Updated upstream
                    mytext = ["¡Deseo convertirme en una gran calabaza!",
                              "¡Ñam ñam ñam ñam! ¡Fuera! Cuidar - ¡bien!",
                              "¿Crees que estoy maduro o podrido?",
                              "¡El néctar es solo el mejor! ¡Ja! ¡Ja! ¡Ja!"]
=======
                    mytext = ["Deseo convertirme en una gran calabaza!",
                              "Crees que estoy maduro o podrido?",
                              "El nectar es lo mejor! Ja! Ja! Ja!"]
>>>>>>> Stashed changes
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
<<<<<<< Updated upstream
                    mytext = [""¡Oh! ¡Otra vez! ¿Puedes consumir néctar demasiado rápido?",
                              "Si muero así ahora, recibirás solo una calabaza joven...",
                              "¡Crece un poco más rápido! Sería bueno convertirse en una gran calabaza, ¡una calabaza joven no es buena!",
                              "¿Deberían todos comer una calabaza tan pequeña? ¡Trae néctar, puedo ser más!"]
=======
                    mytext = ["Oh! Otra vez! Puedes consumir nectar demasiado rapido?",
                              "Si muero asi ahora, recibiras solo una calabaza joven...",
                              "Crece un poco mas rapido! Seria bueno convertirse en una gran calabaza, ¡Una calabaza joven no esta buena!",
                              "Deberian comer todos una calabaza tan pequena? Trae nectar, puedo ser mas!"]
>>>>>>> Stashed changes
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # Tercer riego
            elif npc.getNectar() == 2 :
                if Rnd.get(2) == 1 :
<<<<<<< Updated upstream
                    mytext = ["¡Calabaza, hambrienta! ¡Pide calmar su sed!",
                              "Bueno, finalmente... ¡es realmente delicioso! ¿Hay más?",
                              "¿Cuidarme solo para comer? Genial, el tuyo es aleatorio... para no dar maná suicida"]
=======
                    mytext = ["Calabaza, hambrienta! Pide calmar su sed!",
                              "Bueno, finalmente... esta realmente delicioso! Hay mas?",
                              "Cuidarme solo para comer? Genial, el tuyo es aleatorio... para no dar mana suicida"]
>>>>>>> Stashed changes
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
<<<<<<< Updated upstream
                    mytext = ["¿Añades agua? Que gusto",
                              "Maestro, sálvame... No tengo el aroma del néctar, tengo que morir..."]
=======
                    mytext = ["Anades agua? Que gusto",
                              "Maestro, salvame... No tengo el aroma del nectar, tengo que morir..."]
>>>>>>> Stashed changes
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # Cuarto riego
            elif npc.getNectar() == 3 :
                if Rnd.get(2) == 1 :
<<<<<<< Updated upstream
                    mytext = ["¡Muy bien, muy bien! ¿Sabes cuál es el siguiente paso?",
                              "Si me atrapas, te doy 10 millones de adena !!! Estas de acuerdo"]
=======
                    mytext = ["Muy bien, muy bien! Sabes cual es el siguiente paso?",
                              "Si me atrapas, te doy 10 millones de adena!!! Estas de acuerdo?"]
>>>>>>> Stashed changes
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
<<<<<<< Updated upstream
                    mytext = ["Tengo hambre ¿Quieres que me seque?",
                              "Necesito néctar para crecer un poco más rápido."]
=======
                    mytext = ["Tengo hambre Quieres que me seque?",
                              "Necesito nectar para crecer un poco mas rapido."]
>>>>>>> Stashed changes
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
                        self.startQuestTimer("Good By", 120000, newGourd, player) # Después de 2 minutos, desaparición
                        self.startQuestTimer("Good By2", 90000, newGourd, player)   # 30 segundos para desvanecerse
                        self.startQuestTimer("Good By3", 100000, newGourd, player)  # 20 segundos para desvanecerse
                        self.startQuestTimer("Good By4", 110000, newGourd, player)  # 10 segundos para desvanecerse
<<<<<<< Updated upstream
                        mytext = ["Joven calabaza, ¡sediento! ¿Cómo, ya crecido?",
                                  "Huiré en 2 minutos"]
=======
                        mytext = ["Joven calabaza, sediento! Como, ya crecido?",
                                  "Huire en 2 minutos"]
>>>>>>> Stashed changes
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
                    else :
                        newGourd = self.addSpawn(12778,npc)
                        newGourd.setOwner(player.getName())
                        self.startQuestTimer("Good By", 120000, newGourd, player) # Después de 2 minutos, desaparición
                        self.startQuestTimer("Good By2", 90000, newGourd, player)   # 30 segundos para desvanecerse
                        self.startQuestTimer("Good By3", 100000, newGourd, player)  # 20 segundos para desvanecerse
                        self.startQuestTimer("Good By4", 110000, newGourd, player)  # 10 segundos para desvanecerse
                        mytext = ["La misericordia es un muy buen rasgo. Ahora mira, me siento cada vez mejor",
<<<<<<< Updated upstream
                                  "Huiré en 2 minutos"]
=======
                                  "Huire en 2 minutos"]
>>>>>>> Stashed changes
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
                else :
                    if npcId == 12774 :
                        newGourd = self.addSpawn(12776,npc)
                        newGourd.setOwner(player.getName())
<<<<<<< Updated upstream
                        mytext = ["¡Oh! Fue - ¡no fue! Hay! Ahora! ¿No puedes tener el cuidado adecuado? ¡Me voy a pudrir!",
                                  "Wow ¿parando? ¿Por qué agradecerte?",
                                  "Sed de néctar...",
                                  "¿Quieres una calabaza grande? Pero quiero quedarme un poco de calabaza..."]
=======
                        mytext = ["Oh! Fue - no fue! Hay! Ahora! No puedes tener mas cuidado? Me voy a pudrir!",
                                  "Wow parando? Por que agradecerte?",
                                  "Sed de nectar...",
                                  "Quieres una calabaza grande? Pero quiero quedarme un poco de calabaza..."]
>>>>>>> Stashed changes
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
                    if npcId == 12777 :
                        newGourd = self.addSpawn(12779,npc)
                        newGourd.setOwner(player.getName())
<<<<<<< Updated upstream
                        mytext = ["¡Oh! Fue - ¡no fue! Hay! Ahora! ¿No puedes tener el cuidado adecuado? ¡Me voy a pudrir!",
                                  "Wow ¿parando? ¿Por qué agradecerte?",
                                  "Sed de néctar...",
                                  "¿Quieres una calabaza grande? Pero quiero quedarme un poco de calabaza..."]
=======
                        mytext = ["Oh! Fue - no fue! Hay! Ahora! No puedes tener mas cuidado? Me voy a pudrir!",
                                  "Wow parando? Por que agradecerte?",
                                  "Sed de nectar...",
                                  "Quieres una calabaza grande? Pero quiero quedarme un poco de calabaza..."]
>>>>>>> Stashed changes
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
        return

    def onAttack(self,npc,player,damage,isPet) :
        npcId = npc.getNpcId()
        objId = npc.getObjectId()
        if npcId not in WATERED_SQUASH : return
        if npcId  in self.adultLargeSquash :
            if Rnd.get(30) < 2 :
<<<<<<< Updated upstream
                mytext = ["Las mordeduras son de rata de encaje... para reemplazar... ¡el cuerpo...!",
                          "Ja, ja, ¡creciendo! Totalmente en absoluto!",
                          "¿No se puede apuntar todo? Mira todo para no huir...",
                          "¡Cuento tus golpes! ¡Oh, recuerda un golpe otra vez!",
                          "¡No pierdas tu tiempo!",
                          "Ja, ¿es realmente bueno escuchar eso?",
                          "¡Consumo tus ataques para crecer!",
                          "¡Es hora de golpear de nuevo! ¡Golpea una vez más!",
                          "Solo la música útil puede abrir una gran calabaza... ¡No puedo abrirme con armas!"]
=======
                mytext = ["Las mordeduras son de rata de encaje... para reemplazar... el cuerpo...!",
                          "Ja, ja, creciendo! Totalmente en absoluto!",
                          "No se puede apuntar todo? Mira todo para no huir...",
                          "Cuento tus golpes! Oh, recuerda un golpe otra vez!",
                          "No pierdas el tiempo!",
                          "Ja, esta bien escuchar eso?",
                          "Consumo tus ataques para crecer!",
                          "Es hora de golpear de nuevo! Golpea una vez mas!",
                          "Solo la musica util puede abrir una gran calabaza... No puedo abrirme con armas!"]
>>>>>>> Stashed changes
                npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
        return

    def onKill(self,npc,player,isPet) :
        npcId = npc.getNpcId()
        objId = npc.getObjectId()
        if npcId not in WATERED_SQUASH : return
        if npcId in self.adultSmallSquash :
<<<<<<< Updated upstream
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"¡Calabaza se abre!!"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"¡Eeee! ¡Abre! Muchas cosas buenas..."))
        elif npcId in self.adultLargeSquash :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"¡Calabaza se abre!!"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"¡Eeee! ¡Abre! Muchas cosas buenas..."))
        else :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"¿Por qué, maestro?"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"¡Oh, las tripas se cayeron!"))
=======
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Calabaza se abre!!"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Eeee! Abre! Muchas cosas buenas..."))
        elif npcId in self.adultLargeSquash :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Calabaza se abre!!"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Eeee! Abre! Muchas cosas buenas..."))
        else :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Por que, maestro?"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"Oh, las tripas se cayeron!"))
>>>>>>> Stashed changes
        return

QUEST = squash(-1,"group_template","ai")

CREATED = State('Start', QUEST)
QUEST.setInitialState(CREATED)

for i in WATERED_SQUASH:
    QUEST.addSkillUseId(i)
    QUEST.addAttackId(i)
    QUEST.addKillId(i)