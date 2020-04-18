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
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"RELACIONADO, RELACIONADO,... RELACIONADO... RELACIONADO SEGURIDAD"))
            npc.onDecay()
        elif event == "Good By2" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"���������RESTOS????????? 30 CALZADO"))
        elif event == "Good By3" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"OBSERVACIONES DE SOCKET RESTANTES: 20 OBSERVACIONES!"))
        elif event == "Good By4" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"TOQUE RELACIONADO 10, �RIESGO 10! �9, 8, 7..!"))
        elif event == "Good By5" and npc and player :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"RELACIONADO, �RELACIONADO CON EL DERECHO!"))
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
                              "INFORMACI�N RELACIONADA, RELACIONADA CON EL RESTANTE RELAX, ACUERDOS RELACIONADOS �RELACIONADOS!",
                              "RELAJANTE, RESTANTE, RESTANTE, RESTANTE Y RESTANTE Y RESTANTE �ENV�O GRATIS!",
                              "RESUMEN EJECUTIVO, RELACIONADO, �RESTANTE!",
                              "OPERACION EJECUTIVA, ��REA RESTANTE! INFORMACI�N RELACIONADA",
                              "�Qu� es lo mejor para ti?",
                              "RELACIONADO CON... RESTANTE, RESTANTE, RESTANTE, �RESTANTE?",
                              "RELACIONADO - RELACIONADO, �RESTANTE?",
                              "Feliz a�o nuevo, RESUMEN EJECUTIVO 5, SECCI�N 5"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
                    mytext = ["�HOMBRO! �RELACIONADO CON EL HOMBRO, CONOCIMIENTO!",
                              "RIESGO, RIESGO, RIESGO, RIESGO, RIESGO, RIESGO",
                              "�TOQUE RELACIONADO! �RELACIONADO CON EL PROP�SITO!",
                              "RESTANTE Y ELIMINANDO",
                              "�INFORMACI�N RELACIONADA DUCHA DUCHA! �HOMBRO!",
                              "�C�MO EMPEZAR? RESTANTE SIGUE REMODE"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # Cohete
            elif npc.getNectar() == 1 :
                if Rnd.get(2) == 1 :
                    mytext = ["�RESTOS PARA USTED MISMO! �COMPLETO!",
                              "R, R, R, �R!",
                              "�C�MO HACERSE, C�MO HACERSE?",
                              "����!!!!"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
                    mytext = ["�RELACIONADO! RESUMEN EJECUTIVO DE LA...",
                              "INFORMACI�N RELACIONADA, COMPRAS, COMPRAS...",
                              "��REA RESTANTE! EXCEPCI�N... ACCESORIOS, EJECUTIVOS",
                              "������SOLUCI�N DE PROBLEMAS PARA USTED MISMO?????? �EXCEPCIONAL, OBSERVADO, OBSERVADO OBSERVADO!"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # RESTOS
            elif npc.getNectar() == 2 :
                if Rnd.get(2) == 1 :
                    mytext = ["�TEMPLO, RESTANTE! �RESTANTE! �TOQUES EXCEPCIONALES!",
                              "ANUNCIO DE FUNCIONAMIENTO... FUNCI�N �Que?",
                              "RESUMEN EJECUTIVO DEL RIESGO FUTURO DEL RIESGO DE LOS ARREGLOS RELACIONADOS, RELACIONADO, FUNCIONAL, REFLEJADO, REFLEJADO... RELACIONADO, RESPUESTA RELACIONADA"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
                    mytext = ["�Qu� hay del negocio? �C�mo llegar?",
                              "FUNCIONANDO, FUNCIONANDO... FUNCIONANDO... FUNCIONANDO Y RESTANTE, RESTANTE, EL RESTANTE..."]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
            # RESTANTE Y RESTANTE
            elif npc.getNectar() == 3 :
                if Rnd.get(2) == 1 :
                    mytext = ["RELACIONADO CON PERMANECER, PERMANECER, PERMANECER, PERMANECER �RELAJARSE?",
                              "RESTANTE ELIMINACI�N, RECUERDA, RECUERDA 10, RECUERDA, RECUERDA ���adena!!!"]
                    npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                    npc.addNectar()
                    npc.addGood()
                else :
                    mytext = ["RELACIONADO... �C�MO HACERSE USTED MISMO?",
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
                        mytext = ["AMATE A TI MISMO, HOMBRO, �HOMBRO! �C�mo empezar?",
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
                        mytext = ["RESUMEN EJECUTIVO DE LA SESI�N DE LA SEGURIDAD... de la SEGURIDAD... de la SEGURIDAD. SOLUCI�N DE PROBLEMAS, CONOCIMIENTO",
                                  "!"]
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
                else :
                    if npcId == 12774 :
                        newGourd = self.addSpawn(12776,npc)
                        newGourd.setOwner(player.getName())
                        mytext = ["Feliz cumplea�os �Est�s buscando mucha diversi�n? Feliz a�o nuevo",
                                  "�C�MO HACERSE, C�MO HACERSE? RESUMEN DEL RESUMEN DE LA FUNDACI�N",
                                  "TOQUE RELACIONADO...",
                                  "RESTANTE... �RESTANTE? RESUMEN EJECUTIVO DE LA..."]
                        npc.broadcastPacket(CreatureSay(objectId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
                        npc.onDecay()
                    if npcId == 12777 :
                        newGourd = self.addSpawn(12779,npc)
                        newGourd.setOwner(player.getName())
                        mytext = ["Feliz cumplea�os �Est�s buscando mucha diversi�n?",
                                  "�C�MO HACERSE, C�MO HACERSE? RESUMEN DEL RESUMEN DE LA FUNDACI�N",
                                  "TOQUE RELACIONADO...",
                                  "RESTANTE... �RESTANTE? RESUMEN EJECUTIVO DE LA..."]
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
                          "�RIESGO RELACIONADO...!",
                          "�C�MO HACERSE? �C�MO HACERSE? RESUMEN EJECUTIVO DE LA RESPONSABILIDAD FUNCIONAL",
                          "�HOMBRO, HOMBRO!",
                          "�INFORMACI�N EXCEPCIONAL INFORMACI�N EXCEPCIONAL!",
                          "!",
                          "RESUMEN EJECUTIVO",
                          "�SIGUE SIGUIENDO! �Buenas tardes!",
                          "COMPRAS, COMPRAS, COMPRAS, COMPRAS �REPRODUCCI�N!"]
                npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),mytext[Rnd.get(len(mytext))]))
        return

    def onKill(self,npc,player,isPet) :
        npcId = npc.getNpcId()
        objId = npc.getObjectId()
        if npcId not in WATERED_SQUASH : return
        if npcId in self.adultSmallSquash :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"!"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"�REA... �REA... �REA..."))
        elif npcId in self.adultLargeSquash :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"!"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"�REA... �REA... �REA..."))
        else :
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"DEBE, S... �HOMBRO?"))
            npc.broadcastPacket(CreatureSay(objId,0,npc.getName(),"��Negocios, negocios, negocios!!"))
        return

QUEST = squash(-1,"group_template","ai")

CREATED = State('Start', QUEST)
QUEST.setInitialState(CREATED)

for i in WATERED_SQUASH:
    QUEST.addSkillUseId(i)
    QUEST.addAttackId(i)
    QUEST.addKillId(i)