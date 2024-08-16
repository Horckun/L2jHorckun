# Exploration of Giants Cave, part 2 version 0.1 
# by DrLecter
import sys
from com.l2jfrozen import Config
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest

#Quest info
QUEST_NUMBER,QUEST_NAME,QUEST_DESCRIPTION = 377,"GiantsExploration2","Exploration of Giants Cave, part 2"
qn = "377_GiantsExploration2"

#Variables
#Titan Ancient Books drop rate in %
DROP_RATE=15*Config.RATE_DROP_QUEST
MAX = 100
#Alternative rewards. Set this to a non-zero value and recipes will be 100% instead of 60%
ALT_RP_100=0

#Quest items
ANC_BOOK = 5955
DICT2    = 5892

#Quest collections
EXCHANGE = [
[5945, 5946, 5947, 5948, 5949], #science basis
[5950, 5951, 5952, 5953, 5954]  #culture
]

#Messages
default   = "<html><body>O no estas llevando a cabo tu mision o no cumples los criterios.</body></html>"
error_1   = "<html><body><font color'LEVEL'>Investigador principal Sobling:</font><br><br>Creo que es demasiado pronto para que me ayudes. Vuelve cuando hayas adquirido mas experiencia.<br>(Busqueda de personajes de nivel 57 y superior)</body></html>"
start     = "<html><body><font color'LEVEL'>Investigador principal Sobling:</font><br><br>Entonces Cliff nos envio este diccionario, ahora puedo verlo claramente. Es muy impresionante... Hay mas reliquias que debemos descubrir y tal vez usted nos ayude como futuro miembro de nuestro equipo de excavacion. Deberiamos buscar <font color=\"LEVEL\">el libro de la ciencia del titan y el libro de la cultura del titan</font>.<br>Nuestro pago por tal descubrimiento no puede ser rechazado tan facilmente, <font color=\"LEVEL\">recetas de grado A</font> utilizadas en la fabricacion de armaduras de alto nivel... Por supuesto que no te dare nada solo. para obtener fragmentos, tendras que reunir cada pieza de un libro determinado.<br><br><a action=\"bypass -h Quest 377_GiantsExploration2 yes\">Buscare libros antiguos.</a><br><a action=\"bypass -h Quest 377_GiantsExploration2 0\">No te ayudare esta vez.</a></body></html>"
starting  = "Starting.htm"
checkout  = "<html><body><font color'LEVEL'>Investigador principal Sobling:</font><br><br>Excelente! Volviste! Fue dificil coleccionar libros antiguos?<br>Dejame ver lo que has encontrado hasta ahora...<br><br><a action=\"bypass -h Quest 377_GiantsExploration2 show\">Muestrale los libros que coleccionaste.</a></body></html>"
checkout2 = "<html><body><font color'LEVEL'>Investigador principal Sobling:</font><br><br>Excelente! Volviste! Fue dificil coleccionar libros antiguos?<br>Que es? Tienes algunos fragmentos de libros sin traducir aqui, pero no me sirven de nada hasta que traduzcas su contenido, no tengo tiempo para hacerlo por mi cuenta y por eso te di el diccionario que Cliff me envio. De todos modos puedo comprobar cualquier otro fragmento traducido que puedas tener...<br><br><a action=\"bypass -h Quest 377_GiantsExploration2 show\">Muestrale los fragmentos.</a></body></html>"
no_items  = "<html><body><font color'LEVEL'>Investigador principal Sobling:</font><br><br>No veo ningun libro valioso o completo aqui, deberias continuar tu investigacion. Estoy bastante seguro de que puedes hacerlo mejor si te esfuerzas mas... Que opinas?<br><br><a action=\"bypass -h Quest 377_GiantsExploration2 Starting.htm\">Voy a continuar.</a><br><a action=\"bypass -h Quest 377_GiantsExploration2 0\">Lo dejare.</a></body></html>"
tnx4items = "<html><body><font color'LEVEL'>Investigador principal Sobling:</font><br><br>Asombroso! Este es el tipo de articulos que estaba buscando... Tome estas raras recetas como prueba de mi gratitud. De todos modos, estoy seguro de que hay mas reliquias antiguas custodiadas por esos monstruos, te gustaria buscar un poco mas?<br><br><a action=\"bypass -h Quest 377_GiantsExploration2 Starting.htm\">Voy a continuar.</a><br><a action=\"bypass -h Quest 377_GiantsExploration2 0\">Lo dejare.</a></body></html>"
ext_msg   = "Mision abortada."

#NPCs
HR_SOBLING = 31147

#Mobs
MOBS = [ 20654,20656,20657,20658 ]

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    id = st.getState() 
    htmltext = event
    if event == "yes" :
       htmltext = starting
       st.setState(STARTED)
       st.set("cond","1")
       st.playSound("ItemSound.quest_accept")
    elif event == "0" :
       htmltext = ext_msg
       st.playSound("ItemSound.quest_finish")
       st.takeItems(DICT2,1)
       st.exitQuest(1)
    elif event == "show" :
       htmltext = no_items
       for i in range(len(EXCHANGE)) :
           dec=2**len(EXCHANGE[i])
           for j in range(len(EXCHANGE[i])) :
               if st.getQuestItemsCount(EXCHANGE[i][j]) > 0 :
                  dec = dec >> 1
           if dec == 1 :
              htmltext = tnx4items
              for k in range(len(EXCHANGE[i])) :
                  st.takeItems(EXCHANGE[i][k], 1)
              luck = st.getRandom(100) 
              if luck > 75   : item=5420 #nightmare leather 60%
              elif luck > 50 : item=5422 #majestic plate 60%
              elif luck > 25 : item=5336 #nightmare armor 60%
              else           : item=5338 #majestic leather 60%
              if ALT_RP_100 != 0 : item +=1
              st.giveItems(item,1)
    return htmltext

 def onTalk (self,npc,player):
   htmltext = default
   st = player.getQuestState(qn)
   if not st : return htmltext

   npcId = npc.getNpcId()
   id = st.getState()
   if st.getQuestItemsCount(DICT2) != 1 :
      st.exitQuest(1) 
   elif id == CREATED :
      st.set("cond","0")
      htmltext = start
      if player.getLevel() < 57 :
         st.exitQuest(1)
         htmltext = error_1
   elif id == STARTED :
      if st.getQuestItemsCount(ANC_BOOK) == 0 :
         htmltext = checkout
      else :
         htmltext = checkout2
   return htmltext

 def onKill(self,npc,player,isPet) :
     partyMember = self.getRandomPartyMemberState(player,STARTED)
     if not partyMember : return
     st = partyMember.getQuestState(qn)
     numItems, chance = divmod(DROP_RATE,MAX)
     drop = st.getRandom(MAX)
     if drop < chance :
        numItems = numItems +1
     if int(numItems) != 0 :
        st.giveItems(ANC_BOOK,int(numItems))
        st.playSound("ItemSound.quest_itemget")
     return  

# Quest class and state definition
QUEST       = Quest(QUEST_NUMBER, str(QUEST_NUMBER)+"_"+QUEST_NAME, QUEST_DESCRIPTION)

CREATED     = State('Start',     QUEST)
STARTED     = State('Started',   QUEST)
COMPLETED   = State('Completed', QUEST)

QUEST.setInitialState(CREATED)

# Quest NPC starter initialization
QUEST.addStartNpc(HR_SOBLING)
# Quest initialization
QUEST.addTalkId(HR_SOBLING)

for i in MOBS :
  QUEST.addKillId(i)

STARTED.addQuestDrop(HR_SOBLING,DICT2,1)