# Exploration of Giants Cave, part 1 version 0.1 
# by DrLecter
import sys
from com.l2jfrozen import Config
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
#Quest info
QUEST_NUMBER,QUEST_NAME,QUEST_DESCRIPTION = 376,"GiantsExploration1","Exploration of Giants Cave, part 1"
qn = "376_GiantsExploration1"

#Variables
#Ancient parchment drop rate in %
DROP_RATE   = 15*Config.RATE_DROP_QUEST
MAX = 100
#Mysterious Book drop rate in %
DROP_RATE_2 = 5*Config.RATE_DROP_QUEST
#By changing this setting you can make a group of recipes harder to get
RP_BALANCE = 50
#Changing this value to non-zero, will turn recipes to 100% instead of 60%
ALT_RP_100 = 0


#Quest items
ANC_SCROLL = 5944
DICT1  = 5891 
DICT2  = 5892 #Given as a proof for 2nd part
MST_BK = 5890

#Quest items vs rewards (recipes for low sealed armor parts, 60%)
EXCHANGE = [
 #collection items list,     rnd_1, rnd_2
[[5937,5938,5939,5940,5941], 5346, 5354], #medical theory, tallum_tunic,     tallum_hose
[[5932,5933,5934,5935,5936], 5332, 5334], #architecture,   drk_crstl_leather,tallum_leather
[[5922,5923,5924,5925,5926], 5416, 5418], #golem plans,    drk_crstl_breastp,tallum_plate
[[5927,5928,5929,5930,5931], 5424, 5340]  #basics of magic,drk_crstl_gaiters,dark_crystal_legg
]

#Messages
default   = "<html><body>O no estas llevando a cabo tu mision o no cumples los criterios.</body></html>"
error_1   = "<html><body><font color='LEVEL'>Investigador principal Sobling:</font><br><br>Creo que es demasiado pronto para que me ayudes. Vuelve cuando hayas adquirido mas experiencia.<br>(Busqueda de personajes de nivel 51 y superior)</body></html>"
start     = "<html><body><font color='LEVEL'>Investigador principal Sobling:</font><br><br>Como lider del equipo de investigacion, estoy buscando aventureros experimentados que se unan a nosotros. En realidad estamos buscando reliquias de la antigua cultura de los gigantes. Hay cuatro scripts que aun no podemos encontrar: <font color=\"LEVEL\">planos para la construccion de golems, bases de la magia del gigante, manual de tecnologia de la construccion y teoria medica del gigante.</font><br>Dado el valor de los articulos que estamos buscando, no es necesario decirles cuan generosas seran mis recompensas.<br><br><a action=\"bypass -h Quest 376_GiantsExploration1 yes\">Buscare objetos antiguos.</a><br><a action=\"bypass -h Quest 376_GiantsExploration1 0\">No te ayudare.</a></body></html>"
starting  = "Starting.htm"
checkout  = "<html><body><font color='LEVEL'>Investigador principal Sobling:</font><br><br>Excelente! Volviste! Fue dificil coleccionar piezas antiguas?<br>Dejame ver lo que has encontrado hasta ahora...<br><br><a action=\"bypass -h Quest 376_GiantsExploration1 show\">Muestrale los libros que coleccionaste.</a><br><a action=\"bypass -h Quest 376_GiantsExploration1 myst\">Muestrale otros articulos que hayas encontrado.</a></body></html>"
checkout2 = "<html><body><font color='LEVEL'>Investigador principal Sobling:</font><br><br>Excelente! Volviste! Fue dificil coleccionar piezas antiguas?<br>Hum... Que es? Tienes algunos pergaminos antiguos aqui, pero no me sirven de nada hasta que traduzcas su contenido, no tengo tiempo para hacerlo por mi cuenta y por eso te di el diccionario. De todos modos puedo comprobar cualquier otro objeto antiguo que puedas tener...<br><br><a action=\"bypass -h Quest 376_GiantsExploration1 show\">Muestrale los pergaminos que coleccionaste.</a><br><a action=\"bypass -h Quest 376_GiantsExploration1 myst\">Muestrale otros articulos que hayas encontrado.</a></body></html>"
no_items  = "<html><body><font color='LEVEL'>Investigador principal Sobling:</font><br><br>Hum... No veo ningun articulo valioso aqui, deberias continuar tu investigacion. Estoy bastante seguro de que puedes hacerlo mejor si te esfuerzas mas... Que opinas?<br><br><a action=\"bypass -h Quest 376_GiantsExploration1 Starting.htm\">Voy a continuar.</a><br><a action=\"bypass -h Quest 376_GiantsExploration1 0\">Lo dejare.</a></body></html>"
tnx4items = "<html><body><font color='LEVEL'>Investigador principal Sobling:</font><br><br>Asombroso! Este es el tipo de articulos que estaba buscando... Tome estas raras recetas como prueba de mi gratitud. De todos modos, estoy seguro de que hay mas reliquias antiguas custodiadas por esos monstruos, te gustaria buscar un poco mas?<br><br><a action=\"bypass -h Quest 376_GiantsExploration1 Starting.htm\">Voy a continuar.</a><br><a action=\"bypass -h Quest 376_GiantsExploration1 0\">Lo dejare.</a></body></html>"
go_part2  = "<html><body><font color='LEVEL'>Investigador principal Sobling:</font><br><br>Interesante. Que podria ser este misterioso libro? Me temo que no podremos descifrar su contenido sin ayuda. Pero no te preocupes, se quien puede ayudarnos, ve ahora y habla con el <font color=\"LEVEL\">encargado del almacen Cliff en Oren</font>, ensenale el tomo y probablemente sabra que que ver con eso.</body></html>"
no_part2  = "<html><body><font color='LEVEL'>Investigador principal Sobling:</font><br><br>No encuentro nada util aqui... Ya conozco algunos descubrimientos relacionados con la vida de los gigantes, pero no hay ningun valor arqueologico en las letras o dibujos que puedas encontrar. Como te dije, estamos en una busqueda desesperada de <font color=\"LEVEL\">planos para la construccion de golems, bases de la magia del gigante, tecnologia de construccion y teoria medica del gigante</font>. Debes traer cualquiera de esos libros completo. Pocos podemos hacer solo con fragmentos.</body></html>"
ok_part2  = "<html><body><font color='LEVEL'>Encargado de almacen Cliff:</font><br><br>Que es ese libro? Sobling te dijo que me lo trajeras? Bueno... Esta escrito en un idioma muy antiguo... Si... Toma este diccionario de idiomas antiguos: nivel intermedio y conoce a <font color=\"LEVEL\">Sobling</font> nuevamente. Con esto podra traducirlo. Vete ahora.</body></html>"
gogogo_2  = "<html><body><font color='LEVEL'>Investigador principal Sobling:</font><br><br>Sigues ahi con el libro? No hay forma de leer su contenido con nuestro conocimiento actual. Lleva el libro al <font color=\"LEVEL\">encargado del almacen Cliff en la ciudad castillo de Oren</font>.</body></html>"
ext_msg   = "Mision abortada."

#NPCs
HR_SOBLING = 31147
WF_CLIFF   = 30182

#Mobs
MOBS = range(20647,20651)

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    id = st.getState() 
    htmltext = event
    if event == "yes" :
       htmltext = starting
       st.setState(STARTING)
       st.set("cond","1")
       st.set("awaitBook","1")
       st.giveItems(DICT1,1)
       st.playSound("ItemSound.quest_accept")
    elif event == "0" :
       htmltext = ext_msg
       st.playSound("ItemSound.quest_finish")
       st.takeItems(DICT1,-1)
       st.takeItems(MST_BK,-1)
       st.exitQuest(1)
    elif event == "show" :
       htmltext = no_items
       for i in range(len(EXCHANGE)) :
           dec=2**len(EXCHANGE[i][0])
           for j in range(len(EXCHANGE[i][0])) :
               if st.getQuestItemsCount(EXCHANGE[i][0][j]) :
                  dec = dec >> 1
           if dec == 1 :
              htmltext = tnx4items
              for k in range(len(EXCHANGE[i][0])) :
                  st.takeItems(EXCHANGE[i][0][k], 1)
              if st.getRandom(100) < RP_BALANCE :
                 item = EXCHANGE[i][1]
              else :
                 item = EXCHANGE[i][2]
              if ALT_RP_100 != 0 : item += 1
              st.giveItems(item,1)
    elif event == "myst" :
       if st.getQuestItemsCount(MST_BK) :
          if id == STARTING :
             st.setState(STARTED)
             st.set("cond","2")
             htmltext = go_part2
          elif id == STARTED :
             htmltext = gogogo_2
       else :
           htmltext = no_part2
    return htmltext

 def onTalk (self,npc,player):
   htmltext = default
   st = player.getQuestState(qn)
   if not st : return htmltext

   npcId = npc.getNpcId()
   id = st.getState()
   if npcId == HR_SOBLING:
      if id == CREATED :
         st.set("cond","0")
         htmltext = start
         if player.getLevel() < 51 :
            st.exitQuest(1)
            htmltext = error_1
      elif id in [ STARTING,STARTED ] :
         if st.getQuestItemsCount(ANC_SCROLL) == 0 :
            htmltext = checkout
         else :
            htmltext = checkout2
   elif npcId == WF_CLIFF :
      if id == STARTED and st.getQuestItemsCount(MST_BK) :
            htmltext = ok_part2
            st.takeItems(MST_BK,1)
            st.giveItems(DICT2,1)
            st.set("cond","3")
            st.playSound("ItemSound.quest_middle")
   return htmltext

 def onKill(self,npc,player,isPet) :
     # a Mysterious Book may drop to any party member that still hasn't gotten it
     partyMember = self.getRandomPartyMember(player,"awaitBook","1")
     if partyMember :
        st = partyMember.getQuestState(qn)
        drop = st.getRandom(100)
        if drop < DROP_RATE_2  and not st.getQuestItemsCount(MST_BK):
           st.giveItems(MST_BK,1)
           st.unset("awaitBook")
           st.playSound("ItemSound.quest_middle")
     # In addition, drops go to one party member among those who are either in
     # STARTING or in STARTED state
     partyMember1 = self.getRandomPartyMemberState(player, STARTING)
     partyMember2 = self.getRandomPartyMemberState(player, STARTED)
     partyMember = partyMember1  # initialize
     # if there exist no party members for either state, do nothing
     if not partyMember1 and not partyMember2 : return
     # if there exist only party members for STARTED, use the one we got from STARTED
     elif not partyMember1 :
         partyMember =  partyMember2
     # if there exist only party members for STARTING, use the one we got from STARTING
     elif not partyMember2 :
         partyMember =  partyMember1
     # if there exist party members from both states, choose one randomly
     else :
         if partyMember.getQuestState(qn).getRandom(2) :
             partyMember = partyMember2
     st = partyMember.getQuestState(qn)  
     numItems, chance = divmod(DROP_RATE,MAX)
     if st.getRandom(MAX) < chance :
        numItems = numItems + 1
     if int(numItems) != 0 :
        st.giveItems(ANC_SCROLL,int(numItems))
        st.playSound("ItemSound.quest_itemget")
     return  

# Quest class and state definition
QUEST       = Quest(QUEST_NUMBER, str(QUEST_NUMBER)+"_"+QUEST_NAME, QUEST_DESCRIPTION)

CREATED     = State('Start',     QUEST)
STARTING    = State('Starting',  QUEST)
STARTED     = State('Started',   QUEST)
COMPLETED   = State('Completed', QUEST)

QUEST.setInitialState(CREATED)

# Quest NPC starter initialization
QUEST.addStartNpc(HR_SOBLING)
# Quest initialization
QUEST.addTalkId(HR_SOBLING)

QUEST.addTalkId(WF_CLIFF)

for i in MOBS :
  QUEST.addKillId(i)
  
STARTED.addQuestDrop(HR_SOBLING,DICT1,1)
STARTED.addQuestDrop(HR_SOBLING,MST_BK,1)