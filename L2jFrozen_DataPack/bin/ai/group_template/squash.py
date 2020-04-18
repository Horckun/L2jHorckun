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
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"¡¡Adiós!! Jajaja"))
            npc.onDecay()
        elif event == "Good By1" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"RELACIONADO, RELACIONADO,... RELACIONADO... RELACIONADO SEGURIDAD"))
            npc.onDecay()
        elif event == "Good By2" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"¿¿¿¿¿¿¿¿¿RESTOS????????? 30 CALZADO"))
        elif event == "Good By3" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"OBSERVACIONES DE SOCKET RESTANTES: 20 OBSERVACIONES!"))
        elif event == "Good By4" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"TOQUE RELACIONADO 10, ¡RIESGO 10! ¡9, 8, 7..!"))
        elif event == "Good By5" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"RELACIONADO, ¡RELACIONADO CON EL DERECHO!"))
        return

    def onSkillUse(self,npc,player,skill):
        npcId = npc.getNpcId()
        skillId = skill.getId()
        if skillId != SKILL_NECTAR : return
        if npcId not in WATERED_SQUASH : return
        objectId = npc.getObjectId()
        if skillId == SKILL_NECTAR :
            # Cohete para la venta
            if npc.getNectar() == 0 :
                if Rnd.get(2) == 1 :
                    mytext = ["Responsabilidad RESUMEN EJECUTIVO... RESUMEN EJECUTIVO",
                              "INFORMACIÓN RELACIONADA, RELACIONADA CON EL RESTANTE RELAX, ACUERDOS RELACIONADOS ¡RELACIONADOS!",
                              "RELAJANTE, RESTANTE, RESTANTE, RESTANTE Y RESTANTE Y RESTANTE ¡ENVÍO GRATIS!",
                              "RESUMEN EJECUTIVO, RELACIONADO, ¡RESTANTE!",
                              "OPERACION EJECUTIVA, ¡ÁREA RESTANTE! INFORMACIÓN RELACIONADA",
                              "¿Qué es lo mejor para ti?",
                              "RELACIONADO CON... RESTANTE, RESTANTE, RESTANTE, ¿RESTANTE?",
                              "RELACIONADO - RELACIONADO, ¿RESTANTE?",
                              "Feliz año nuevo, RESUMEN EJECUTIVO 5, SECCIÓN 5"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
                    mytext = ["¡HOMBRO! ¡RELACIONADO CON EL HOMBRO, CONOCIMIENTO!",
                              "RIESGO, RIESGO, RIESGO, RIESGO, RIESGO, RIESGO",
                              "¡TOQUE RELACIONADO! ¡RELACIONADO CON EL PROPÓSITO!",
                              "RESTANTE Y ELIMINANDO",
                              "¡INFORMACIÓN RELACIONADA DUCHA DUCHA! ¡HOMBRO!",
                              "¿CÓMO EMPEZAR? RESTANTE SIGUE REMODE"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # Cohete
            elif npc.getNectar() == 1 :
                if Rnd.get(2) == 1 :
                    mytext = ["¡RESTOS PARA USTED MISMO! ¡COMPLETO!",
                              "R, R, R, ¡R!",
                              "¿CÓMO HACERSE, CÓMO HACERSE?",
                              "¡¡¡¡!!!!"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
                    mytext = ["¡RELACIONADO! RESUMEN EJECUTIVO DE LA...",
                              "INFORMACIÓN RELACIONADA, COMPRAS, COMPRAS...",
                              "¡ÁREA RESTANTE! EXCEPCIÓN... ACCESORIOS, EJECUTIVOS",
                              "¿¿¿¿¿¿SOLUCIÓN DE PROBLEMAS PARA USTED MISMO?????? ¡EXCEPCIONAL, OBSERVADO, OBSERVADO OBSERVADO!"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # RESTOS
            elif npc.getNectar() == 2 :
                if Rnd.get(2) == 1 :
                    mytext = ["¡TEMPLO, RESTANTE! ¡RESTANTE! ¡TOQUES EXCEPCIONALES!",
                              "ANUNCIO DE FUNCIONAMIENTO... FUNCIÓN ¿Que?",
                              "RESUMEN EJECUTIVO DEL RIESGO FUTURO DEL RIESGO DE LOS ARREGLOS RELACIONADOS, RELACIONADO, FUNCIONAL, REFLEJADO, REFLEJADO... RELACIONADO, RESPUESTA RELACIONADA"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
                    mytext = ["¿Qué hay del negocio? ¿Cómo llegar?",
                              "FUNCIONANDO, FUNCIONANDO... FUNCIONANDO... FUNCIONANDO Y RESTANTE, RESTANTE, EL RESTANTE..."]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # RESTANTE Y RESTANTE
            elif npc.getNectar() == 3 :
                if Rnd.get(2) == 1 :
                    mytext = ["RELACIONADO CON PERMANECER, PERMANECER, PERMANECER, PERMANECER ¿RELAJARSE?",
                              "RESTANTE ELIMINACIÓN, RECUERDA, RECUERDA 10, RECUERDA, RECUERDA ¡¡¡adena!!!"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
                    mytext = ["RELACIONADO... ¿CÓMO HACERSE USTED MISMO?",
                              "RESPONSABILIDAD TEMPORAL"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # RIESGO
            elif npc.getNectar() == 4 :
                if Rnd.get(2) == 1 :
                    npc.addGood()
                if npc.getGood() >= 3 :
                    if npcId == 12774 :
                        newGourd = self.addSpawn(12775,npc)
                        newGourd.setOwner(player.getName())
                        self.startQuestTimer("Good By", 120000, newGourd, player) # REFLECTOR 2, RESUMEN EJECUTIVO
                        self.startQuestTimer("Good By2", 90000, newGourd, player)   # 30 RELOJES
                        self.startQuestTimer("Good By3", 100000, newGourd, player)  # 20 RELOJES
                        self.startQuestTimer("Good By4", 110000, newGourd, player)  # 10 RELOJES
                        mytext = ["AMATE A TI MISMO, HOMBRO, ¡HOMBRO! ¿Cómo empezar?",
                                  "!"]
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
                    else :
                        newGourd = self.addSpawn(12778,npc)
                        newGourd.setOwner(player.getName())
                        self.startQuestTimer("Good By1", 120000, newGourd, player)  # REFLECTOR 2, RESUMEN EJECUTIVO
                        self.startQuestTimer("Good By2", 90000, newGourd, player)   # 30 RELOJES
                        self.startQuestTimer("Good By3", 100000, newGourd, player)  # 20 RELOJES
                        self.startQuestTimer("Good By4", 110000, newGourd, player)  # 10 RELOJES
                        mytext = ["RESUMEN EJECUTIVO DE LA SESIÓN DE LA SEGURIDAD... de la SEGURIDAD... de la SEGURIDAD. SOLUCIÓN DE PROBLEMAS, CONOCIMIENTO",
                                  "!"]
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
                else :
                    if npcId == 12774 :
                        newGourd = self.addSpawn(12776,npc)
                        newGourd.setOwner(player.getName())
                        mytext = ["Feliz cumpleaños ¿Estás buscando mucha diversión? Feliz año nuevo",
                                  "¿CÓMO HACERSE, CÓMO HACERSE? RESUMEN DEL RESUMEN DE LA FUNDACIÓN",
                                  "TOQUE RELACIONADO...",
                                  "RESTANTE... ¿RESTANTE? RESUMEN EJECUTIVO DE LA..."]
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
                    if npcId == 12777 :
                        newGourd = self.addSpawn(12779,npc)
                        newGourd.setOwner(player.getName())
                        mytext = ["Feliz cumpleaños ¿Estás buscando mucha diversión?",
                                  "¿CÓMO HACERSE, CÓMO HACERSE? RESUMEN DEL RESUMEN DE LA FUNDACIÓN",
                                  "TOQUE RELACIONADO...",
                                  "RESTANTE... ¿RESTANTE? RESUMEN EJECUTIVO DE LA..."]
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
        return

    def onAttack(self,npc,player,damage,isPet) :
        npcId = npc.getNpcId()
        objId = npc.getObjectId()
        if npcId not in WATERED_SQUASH : return
        if npcId  in self.adultLargeSquash :
            if Rnd.get(30) < 2 :
                mytext = ["RESUMEN EJECUTIVO...",
                          "¡RIESGO RELACIONADO...!",
                          "¿CÓMO HACERSE? ¿CÓMO HACERSE? RESUMEN EJECUTIVO DE LA RESPONSABILIDAD FUNCIONAL",
                          "¡HOMBRO, HOMBRO!",
                          "¡INFORMACIÓN EXCEPCIONAL INFORMACIÓN EXCEPCIONAL!",
                          "!",
                          "RESUMEN EJECUTIVO",
                          "¡SIGUE SIGUIENDO! ¡Buenas tardes!",
                          "COMPRAS, COMPRAS, COMPRAS, COMPRAS ¡REPRODUCCIÓN!"]
                npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
        return

    def onKill(self,npc,player,isPet) :
        npcId = npc.getNpcId()
        objId = npc.getObjectId()
        if npcId not in WATERED_SQUASH : return
        if npcId in self.adultSmallSquash :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"!"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"ÁREA... ÁREA... ÁREA..."))
        elif npcId in self.adultLargeSquash :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"!"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"ÁREA... ÁREA... ÁREA..."))
        else :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"DEBE, S... ¿HOMBRO?"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"¡¡Negocios, negocios, negocios!!"))
        return

QUEST = squash(-1,"group_template","ai")

CREATED = State('Start', QUEST)
QUEST.setInitialState(CREATED)

for i in WATERED_SQUASH:
    QUEST.addSkillUseId(i)
    QUEST.addAttackId(i)
    QUEST.addKillId(i)