# Made by DrLecter
import sys
from com.l2jfrozen.gameserver.datatables.sql import ItemTable
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest

qn = "7000_HeroItems"

MONUMENTS = [31690]+range(31769,31773)

HERO_ITEMS={
6611:["weapon_the_sword_of_hero_i00","Espada infinita","Durante un ataque critico, disminuye la P. Def de uno y aumenta la capacidad de lanzamiento de la mejora, el efecto de escudo de dano, Max HP, Max MP, Max CP y el poder de defensa del escudo. Tambien mejora el dano al objetivo durante PvP.","379/169","Espada"],
6612:["weapon_the_two_handed_sword_of_hero_i00","Cuchilla de carnicero infinita","Aumenta Max HP, Max CP, potencia critica y posibilidad critica. Inflige dano adicional cuando ocurre un ataque critico y tiene la posibilidad de reflejar la habilidad de nuevo en el jugador. Tambien mejora el dano al objetivo durante PvP.","461/169","Espada a dos manos"],
6613:["weapon_the_axe_of_hero_i00","Hacha infinita","Durante un ataque critico, le otorga a uno la capacidad de causar conflictos internos al oponente. Se aumenta la funcion de escudo de dano, HP maximo, MP maximo, CP maximo, asi como la tasa de defensa del escudo. Tambien aumenta el dano al oponente durante PvP.","379/169","Hacha"],
6614:["weapon_the_mace_of_hero_i00","Vara infinita","Cuando se lanza buena magia sobre un objetivo, aumenta Mx MP, CP maximo, velocidad de lanzamiento y velocidad de regeneracion de MP. Tambien recupera HP 100% y aumenta el dano al objetivo durante PvP.","303/226","Vara"],
6615:["weapon_the_hammer_of_hero_i00","Trituradora infinita","Aumenta Max HP, Max HP y Atk. Spd. Aturde a un objetivo cuando ocurre un ataque critico y tiene la posibilidad de reflejar la habilidad en el jugador. Tambien mejora el dano al objetivo durante PvP.","461/169","Martillo"],
6616:["weapon_the_staff_of_hero_i00","Cetro infinito","Al lanzar una buena magia, puede recuperar HP en un 100% a una velocidad determinada, aumenta MAX MP, Max CP, M. Atk., Reduce el consumo de MP, aumenta la tasa de critico magico y reduce la cancelacion de magia. Mejora el dano al objetivo durante PvP.","369/226","Baston"],
6617:["weapon_the_dagger_of_hero_i00","Aguijon infinito","Aumenta el MP maximo, el CP maximo, la velocidad de ataque, la tasa de regeneracion de MP y la tasa de exito de golpes mortales y mortales desde la parte posterior del objetivo. Silencia al objetivo cuando ocurre un ataque critico y tiene efecto de ira vampirica. Tambien mejora el dano al objetivo durante PvP.","332/169","Daga"],
6618:["weapon_the_fist_of_hero_i00","Colmillo Infinito","Aumenta Max HP, Max MP, Max CP y evasion. Aturde a un objetivo cuando ocurre un ataque critico y tiene la posibilidad de reflejar la habilidad en el jugador con una cierta tasa de probabilidad. Tambien mejora el dano al objetivo durante PvP.","461/169","Doble puno"],
6619:["weapon_the_bow_of_hero_i00","Arco infinito","Aumenta Max MP / Max CP y disminuye el retraso de reutilizacion de un arco. Ralentiza el objetivo cuando ocurre un ataque critico y tiene un efecto de disparo barato. Tambien mejora el dano al objetivo durante PvP.","707/169","Arco"],
6620:["weapon_the_dualsword_of_hero_i00","Ala infinita","Cuando ocurre un ataque critico, aumenta Max HP, Max MP, Max CP y probabilidad critica. Silencia al objetivo y tiene la posibilidad de reflejar la habilidad de nuevo en el objetivo. Tambien mejora el dano al objetivo durante PvP.","461/169","Espadas duales"],
6621:["weapon_the_pole_of_hero_i00","Lanza infinita","Durante un ataque critico, aumenta Max HP, Max CP, velocidad de ataque y precision. Los lanzamientos se disipan en un objetivo y tienen la posibilidad de reflejar la habilidad nuevamente en el objetivo. Tambien mejora el dano al objetivo durante PvP.","379/169","Lanza"]
}

def render_list(mode,item) :
  html = "<html><body><font color=\"LEVEL\">Lista de objetos para heroes:</font><table border=0 width=300>"
  if mode == "list" :
    for i in HERO_ITEMS.keys() :
      html += "<tr><td width=35 height=45><img src=icon."+HERO_ITEMS[i][0]+" width=32 height=32 align=left></td><td valign=top><a action=\"bypass -h Quest 7000_HeroItems "+str(i)+"\"><font color=\"FFFFFF\">"+HERO_ITEMS[i][1]+"</font></a></td></tr>"
  else :
    html += "<tr><td align=left><font color=\"LEVEL\">Informacion de objeto:</font></td><td align=right>\
<button value=Volver action=\"bypass -h Quest 7000_HeroItems buy\" width=80 height=27 back=L2UI_ch3.Btn1_normalOn fore=L2UI_ch3.Btn1_normal>\
</td><td width=5><br></td></tr></table><table border=0 bgcolor=\"000000\" width=500 height=160><tr><td valign=top>\
<table border=0><tr><td valign=top width=35><img src=icon."+HERO_ITEMS[item][0]+" width=32 height=32 align=left></td>\
<td valign=top width=400><table border=0 width=100%><tr><td><font color=\"FFFFFF\">"+HERO_ITEMS[item][1]+"</font></td>\
</tr></table></td></tr></table><br><font color=\"LEVEL\">Informacion de objeto:</font>\
<table border=0 bgcolor=\"000000\" width=290 height=220><tr><td valign=top><font color=\"B09878\">"+HERO_ITEMS[item][2]+"</font>\
</td></tr><tr><td><br>Tipo: "+HERO_ITEMS[item][4]+"<br><br>Ataque/Magia: "+HERO_ITEMS[item][3]+"<br><br>\
<table border=0 width=300><tr><td align=center><button value=Obtener action=\"bypass -h Quest 7000_HeroItems _"+str(item)+"\" width=80 height=27 back=L2UI_ch3.Btn1_normalOn fore=L2UI_ch3.Btn1_normal></td></tr></table></td></tr></table></td></tr>"
  html += "</table></body></html>"
  return html

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
   if st.getPlayer().isHero() :
     if event == "buy" :
       htmltext = render_list("list",0)
     elif event.isdigit() and int(event) in HERO_ITEMS.keys() :
       htmltext = render_list("item",int(event))
     elif event.startswith("_") :
       item = int(event.split("_")[1])
       for i in range(6611,6622) :
         if st.getQuestItemsCount(i) :
           st.exitQuest(1)
           return "Ya tienes "+HERO_ITEMS[i][1]
       st.giveItems(item,1)
       htmltext = "Disfruta de tu "+HERO_ITEMS[item][1]
       st.playSound("ItemSound.quest_fanfare_2")
       st.exitQuest(1)
   return htmltext

 def onTalk (Self,npc,player) :
   st = player.getQuestState(qn)
   htmltext = "<html><body>No estas en una mision que involucra a este NPC, o no cumples con los requisitos minimos de la mision de este NPC.</body></html>"
   if player.isHero() :
     htmltext = render_list("list",0)
   else :
     html = "<html><body>Monumento de Heroes:<br>No cumples con los requisitos. Debes convertirte en un heroe primero!<br><a action=\"bypass -h npc_%objectId%_Chat 0\">Volver.</a></body></html>"
     htmltext = html.replace("%objectId%",str(npc.getObjectId()))
     st.exitQuest(1)
   return htmltext

QUEST       = Quest(7000,qn,"Hero Items")

for i in MONUMENTS:
    QUEST.addStartNpc(i)
    QUEST.addTalkId(i)