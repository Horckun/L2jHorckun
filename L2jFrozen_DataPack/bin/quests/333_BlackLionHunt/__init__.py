#written by Rolarga
##################################FEEL FREE TO CHANGE IDs, REWARDS, PRICES, NPCs AND DROPDATAS THEY ARE JUST CUSTOM BY ME##################################

qn = "333_BlackLionHunt"

#Technical relatet Items
BLACK_LION_MARK = 1369
ADENA_ID = 57

#Drops & Rewards
CARGO_BOX1,CARGO_BOX2,CARGO_BOX3,CARGO_BOX4 = range(3440,3444)
UNDEAD_ASH,BLOODY_AXE_INSIGNIAS,DELU_FANG,STAKATO_TALONS = range(3848,3852)
SOPHIAS_LETTER1,SOPHIAS_LETTER2,SOPHIAS_LETTER3,SOPHIAS_LETTER4,LIONS_CLAW,LIONS_EYE,GUILD_COIN = range(3671,3678)
ALACRITY_POTION = 735
SCROLL_ESCAPE = 736
SOULSHOT_D = 1463
SPIRITSHOT_D = 2510
HEALING_POTION=1061
#Box rewards
GLUDIO_APPLE,CORN_MEAL,WOLF_PELTS,MONNSTONE,GLUDIO_WEETS_FLOWER,SPIDERSILK_ROPE,ALEXANDRIT,              \
SILVER_TEA,GOLEM_PART,FIRE_EMERALD,SILK_FROCK,PORCELAN_URN,IMPERIAL_DIAMOND,STATUE_SHILIEN_HEAD,         \
STATUE_SHILIEN_TORSO,STATUE_SHILIEN_ARM,STATUE_SHILIEN_LEG,COMPLETE_STATUE,FRAGMENT_ANCIENT_TABLE1,      \
FRAGMENT_ANCIENT_TABLE2,FRAGMENT_ANCIENT_TABLE3,FRAGMENT_ANCIENT_TABLE4,COMPLETE_TABLET = range(3444,3467)

#Price to Open a Box
OPEN_BOX_PRICE=650


#Lists
#List of all NPCs this Quest: Sophya,Redfoot,Rupio,Undinas(Shilien Temple),Lockirin(Dwarfen Village)
NPC=[30735,30736,30471,30130,30531,30737]
#List for some Item Groups
statue_list=[STATUE_SHILIEN_HEAD,STATUE_SHILIEN_TORSO,STATUE_SHILIEN_ARM,STATUE_SHILIEN_LEG]
tablet_list=[FRAGMENT_ANCIENT_TABLE1,FRAGMENT_ANCIENT_TABLE2,FRAGMENT_ANCIENT_TABLE3,FRAGMENT_ANCIENT_TABLE4]

#This Handels the Drop Datas npcId:[part,allowToDrop,ChanceForPartItem,ChanceForBox,PartItem]
#--Part, the Quest has 4 Parts 1=Execution Ground, 2=Partisan Hideaway 3=Near Giran Town, Delu Lizzards 4=Cruma Tower Area.
#--AllowToDrop --> if you will that the mob can drop, set allowToDrop==1. This is because not all mobs are really like official.
#--ChanceForPartItem --> set the dropchance for Ash in % for the mob with the npcId in same Line.
#--ChanceForBox --> set the dropchance for Boxes in % to the mob with the npcId in same Line. 
#--PartItem --> this defines wich Item should this Mob drop, because 4 Parts.. 4 Different Items.
DROPLIST={
#Execturion Ground - Part 1
20160:[1,1,67,29,UNDEAD_ASH],      #Neer Crawler
20171:[1,1,76,31,UNDEAD_ASH],      #Specter
20197:[1,1,89,25,UNDEAD_ASH],      #Sorrow Maiden
20200:[1,1,60,28,UNDEAD_ASH],      #Strain  
20201:[1,1,70,29,UNDEAD_ASH],      #Ghoul
20202:[1,0,60,24,UNDEAD_ASH],      #Dead Seeker (not official Monster for this Quest)
20198:[1,1,60,35,UNDEAD_ASH],      #Neer Ghoul Berserker
#Partisan Hideaway - Part 2
20207:[2,1,69,29,BLOODY_AXE_INSIGNIAS],  #Ol Mahum Guerilla
20208:[2,1,67,32,BLOODY_AXE_INSIGNIAS],  #Ol Mahum Raider
20209:[2,1,62,33,BLOODY_AXE_INSIGNIAS],  #Ol Mahum Marksman
20210:[2,1,78,23,BLOODY_AXE_INSIGNIAS],  #Ol Mahum Sergeant
20211:[2,1,71,22,BLOODY_AXE_INSIGNIAS],  #Ol Mahum Captain
#Delu Lizzardmans near Giran - Part 3
20251:[3,1,70,30,DELU_FANG],        #Delu Lizardman
20252:[3,1,67,28,DELU_FANG],        #Delu Lizardman Scout
20253:[3,1,65,26,DELU_FANG],        #Delu Lizardman Warrior
20781:[3,0,69,31,DELU_FANG],        #Delu Lizardman Shaman (not official Monster for this Quest)
#Cruma Area - Part 4
20157:[4,1,66,32,STAKATO_TALONS],    #Marsh Stakato
20230:[4,1,68,26,STAKATO_TALONS],    #Marsh Stakato Worker
20232:[4,1,67,28,STAKATO_TALONS],    #Marsh Stakato Soldier
20234:[4,1,69,32,STAKATO_TALONS]    #Marsh Stakato Drone
}

######################################## DO NOT MODIFY BELOW THIS LINE ####################################################################################

#Messages
#technical relatet messages
html        = "<html><body>"
htmlend        = "</body></html>"
back        = "<a action=\"bypass -h Quest 333_BlackLionHunt f_more_help\">Volver</a>"
#Sophya
sophia        = "<font color='LEVEL'>Mercenaria Sophia:</font><br><br>"
#-Item information
p_redfoot      = html+sophia+"Pie rojo puede que no te guste mucho personalmente. Pero el es el tipo de persona que se extrana cuando no esta cerca. Aunque esta a cargo de la entrega de suministros militares, tambien trabaja como intermediario en botin y trofeos de guerra robados. Tambien es una gran fuente de informacion para nuestras tropas mercenarias. Dado que trae consigo mucha informacion util, visitenos con frecuencia para hacerle preguntas.<br><a action=\"bypass -h Quest 333_BlackLionHunt p_trader_info\">Pregunta por el sindicato de comerciantes.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt continue\">Continue con su mision.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt leave\">Deten la mision en la que has estado involucrado.</a>"+htmlend
p_no_items      = html+sophia+"Querido hermano del Leon Negro. No crees que el lugar donde deberias estar no es este pueblo sino el campo de batalla donde los espiritus malignos corren salvajemente?<br><br><a action=\"bypass -h Quest 333_BlackLionHunt continue\">Continue con su mision.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt leave\">Deten la mision en la que has estado involucrado.</a>"+htmlend
p_trader_info    = html+sophia+"Esta caja de carga pertenece definitivamente al sindicato de comerciantes de Aden. Lo puedo ver por el sello que esta estampado en la caja. Si desea devolverles la carga, vaya a ver a Morgan, miembro del sindicato el comerciante Union, en la tienda magica. Trabaja para el sindicato de comerciantes de Aden.<br><br><a action=\"bypass -h Quest 333_BlackLionHunt p_redfoot\">Pregunte por Pie rojo.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt continue\">Continue con su mision.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt leave\">Deten la mision en la que has estado involucrado.</a>"+htmlend
p_both_info      = html+sophia+"Querido hermano. Aprecio su arduo trabajo en el cumplimiento de la mision. Te dare tu recompensa de acuerdo con la cantidad de pruebas que hayas traido.<br>Que es esa caja? Parece que has traido una caja de carga que pertenece a un sindicato de comerciantes. Dado que no existe ninguna clausula sobre la devolucion de una caja de carga escrita en nuestro contrato, supongo que no tenemos el deber de devolver la carga a los comerciantes. Pero si se lo devolvemos al sindicato de comerciantes, tal vez nos daran algun tipo de recompensa? Si no tiene ganas de ayudar a los comerciantes, puede ir a ver a Pie rojo. Es un experto en lidiar con despojos de los que es dificil deshacerse.<br><br><a action=\"bypass -h Quest 333_BlackLionHunt p_redfoot\">Pregunte por Pie rojo.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt p_trader_info\">Pregunta por el sindicato de comerciantes.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt continue\">Continue con su mision.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt leave\">Deten la mision en la que has estado involucrado.</a>"+htmlend
p_only_item_info  = html+sophia+"Querido hermano. Aprecio su arduo trabajo en el cumplimiento de la mision. Te dare tu recompensa de acuerdo con la cantidad de pruebas que hayas traido.<br><br><a action=\"bypass -h Quest 333_BlackLionHunt continue\">Continuar llevando a cabo la mision.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt leave\">Deten la mision en la que has estado involucrado.</a>"+htmlend
p_leave_mission    = html+sophia+"Aprecio tu arduo trabajo hasta ahora. Incluso un leon necesita un descanso. Retirate al pueblo y repone energias mientras descansas alli. Mantener la propia fuerza fisica es una de las habilidades basicas de ser un mercenario.<br><br><a action=\"bypass -h Quest 333_BlackLionHunt start_chose_parts\">Dile que te gustaria emprender una nueva mision.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt r_exit\">Deja la tropa mercenaria.</a>"+htmlend
p_only_box_info    = html+sophia+"Querido hermano. Aprecio su arduo trabajo en el cumplimiento de la mision. Te dare tu recompensa de acuerdo con la cantidad de pruebas que hayas traido.<br><br><a action=\"bypass -h Quest 333_BlackLionHunt continue\">Continuar llevando a cabo la mision.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt leave\">Deten la mision en la que has estado involucrado.</a>"+htmlend
p_first_eye      = html+sophia+"Espera un momento. Les presento la <font color=\"LEVEL\">marca del ojo del leon</font>. Este es un premio para reconocer los distinguidos servicios que ha demostrado en el campo de batalla. Y se han entregado nuevos suministros para usted. Dado que son bienes prescindibles que seran utiles en el combate, guardalos y guardalos bien! Ahora espero que continue logrando grandes logros."+htmlend
p_eye        = html+sophia+"Espera un momento. Les presento la <font color=\"LEVEL\">marca del ojo del leon</font>. Este es un premio para reconocer los distinguidos servicios que ha demostrado en el campo de batalla. Y se han entregado nuevos suministros para usted. Dado que son bienes prescindibles que seran utiles en el combate, guardalos y guardalos bien! Ahora espero que continue logrando grandes logros."+htmlend
#-exit messages
r_exit        = html+sophia+"Que?! Quieres abandonar la tropa del leon negro? Bueno, supongo que debes tener tus propios motivos. No preguntare sobre eso. Sin embargo, te dire una cosa. El unico lugar para alguien como tu que nacio con la sangre de un luchador es en una tropa mercenaria. No importa a donde vayas, estas destinado a terminar en el campo de batalla.<br>De todos modos, si realmente quieres retirarte de la tropa mercenaria, ten esto en cuenta. A tu salida, tendras que devolver la marca del leon negro. Ademas, de acuerdo con tus contribuciones de servicio que hayas logrado hasta ahora, recibiras el pago de baja correspondiente.<br><br><a action=\"bypass -h Quest 333_BlackLionHunt continue\">Continua trabajando para la tropa mercenaria.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt exit\">Deja la tropa mercenaria.</a>"+htmlend
exit        = html+sophia+"Si realmente ya has tomado una decision, no te detendre mas. Por favor, devuelve la Marca del Leon Negro. Lamento que nuestra relacion como camaradas termine de aqui en adelante. Oh, toma esto antes de irte. Esta es la recompensa por tus servicios que has ganado hasta ahora para la tropa mercenaria. Vayas donde vayas, puedes utilizarlo como capital inicial para establecerte en un lugar nuevo. Bueno, hasta el dia en que volvamos a desenvainar nuestras espadas. Buena suerte hermano!"+htmlend
#-Start
start_error1    = html+sophia+"Como dije antes, nuestra mision actual es expulsar a los espiritus malignos de esta zona. Sin embargo, dado que la fuerza principal de la tropa mercenaria ha sido enviada a Gludio, nuestra fuerza militar esta sufriendo una escasez. Lo unico que estamos logrando hacer ahora es contener a los espiritus malignos para que no ataquen la aldea. Incluso ahora, si puedo encontrar algunos luchadores de piel dura, estoy dispuesto a contratarlos de inmediato para complementar nuestra fuerza!<br>(Esta es una mision que puede llevar a cabo un personaje de nivel 25 o superior y en posesion de la marca del leon negro)"+htmlend
start_error2    = html+sophia+"Como dije antes, nuestra mision actual es expulsar a los espiritus malignos de esta zona. Sin embargo, dado que la fuerza principal de la tropa mercenaria ha sido enviada a Gludio, nuestra fuerza militar esta sufriendo una escasez. Lo unico que estamos logrando hacer ahora es contener a los espiritus malignos para que no ataquen la aldea. Incluso ahora, si puedo encontrar algunos luchadores de piel dura, estoy dispuesto a contratarlos de inmediato para complementar nuestra fuerza!<br>Parece que tienes mucha experiencia luchando contra espiritus malignos. Alguien de su calibre y experiencia calificaria facilmente para unirse a nuestra tropa mercenaria. Sin embargo, de acuerdo con nuestra politica, para ser miembro de nuestra tropa mercenaria, aun tendra que pasar nuestra prueba. Si estas interesado, ve a ver al <font color=\"LEVEL\">capitan Leopold en Gludin</font>. Si el te aprueba y puedes recuperar la marca del leon negro, te aceptare como uno de nuestros hermanos y te dare la oportunidad de unirte a nosotros en la lucha.<br>(Esta es una mision que se puede llevar a cabo por un personaje de nivel 25 o superior y en posesion de la marca del leon negro)"+htmlend
start_start      = html+sophia+"Querido hermano del leon negro. Nuestra situacion actual es la siguiente. Como dije antes, nuestra mision actual es expulsar a los espiritus malignos de esta zona. Sin embargo, dado que la fuerza principal de la tropa mercenaria ha sido enviada a Gludio, nuestra fuerza militar esta sufriendo una escasez. Lo unico que estamos logrando hacer ahora es contener a los espiritus malignos para que no ataquen la aldea.<br>Afortunadamente, el capitan Leopoldo de Gludin ha enviado muchos hermanos mercenarios recien seleccionados. Para que podamos lanzar nuestro ataque en serio contra la fortaleza de los espiritus malignos. Hermano, me gustaria que te unieras a nosotros en esta lucha.<br><br><a action=\"bypass -h Quest 333_BlackLionHunt start\">Dile que te uniras a ellos en la lucha.</a>"+htmlend
start_explain    = html+sophia+"Esta bien! Ha llegado el momento de que los leones negros que han estado agachados hasta ahora, muestren sus garras y comiencen a cazar!<br>Ahora, explicare nuestra situacion de combate. Actualmente tenemos cuatro objetivos de ataque. Son el campo de ejecucion, el escondite partisano, la zona de la costa sur y las marismas de Cruma. Como no tenemos suficiente poder de combate para mantener una guerra prolongada, enviaremos un pequeno grupo de soldados como fuerza de ataque para llevar a cabo la estrategia de atacar y huir para expulsar a los espiritus malignos.<br><br><a action =\"bypass -h Quest 333_BlackLionHunt start_parts\">Escuche la mision de cada area.</a>"+htmlend
start_parts      = html+sophia+"Sobre que mision te gustaria saber mas?<br><br><a action=\"bypass -h Quest 333_BlackLionHunt p1_explanation\">Limpiar a los no-muertos en el campo de ejecucion.</a><br><a action =\"bypass -h Quest 333_BlackLionHunt p2_explanation\">Expulsa al Ol Mahum en el escondite partidista.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt p3_explanation\">Expulsa al hombre lagarto Delu en el area de la costa sur.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt p4_explanation\">Aplasta al stakato del pantano en Cruma Marshlands.</a>"+htmlend
start_ask_again    = html+sophia+"Querido hermano leon negro, la guerra contra los espiritus malignos ya ha comenzado! No crees que deberias participar activamente en esta lucha con nosotros?<br><br><a action=\"bypass -h Quest 333_BlackLionHunt start_parts\">Escucha la explicacion sobre la mision.</a>"+htmlend
start_continue    = html+sophia+"Apurase! Corre al campo de batalla, destruye a tus enemigos y prueba la dulzura de la victoria!"+htmlend
#-Part 1
p1_explanation    = html+sophia+"El campo de ejecucion esta ubicado en la parte este del pueblo. Es un lugar inquietante donde la gente puede escuchar los interminables gritos de las almas muertas. Tu mision es limpiar los muertos vivientes que infestan el lugar. Segun un rumor, para pagar por la sangre derramada de personas inocentes que fueron asesinadas durante el levantamiento de los agricultores, los no-muertos regresaron a este mundo. Bueno, todo lo que se es que debemos llevar a cabo la tarea encomendada. Aun asi, por alguna razon no me siento bien con esto.<br><br><a action=\"bypass -h Quest 333_BlackLionHunt p1_t\">Asume la mision.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt start_chose_parts\">Escucha la explicacion sobre otra mision.</a>"+htmlend
p1_take        = html+sophia+"Los muertos vivientes que debemos expulsar son <font color=\"LEVEL\">espectros, doncellas tristes, rastreadores cercanos, demonio frenetico cercano, cepas y demonios</font>. No se si sabes sobre esto o no. Pero cuando un no-muerto es destruido, deja un punado de cenizas. Traeme eso como prueba de victoria. Cuantas mas <font color=\"LEVEL\">cenizas de muertos vivientes</font> traigas, mas recompensas recibiras. Como alguna vez trabajo con el capitan Leopold, ya conoce la regla sobre pruebas y recompensas, no?<br>Ahora bien, date prisa. Preparate para el combate y ve inmediatamente al campo de ejecucion. Demuestren a todos que ni siquiera los muertos vivientes que han resucitado de las mazmorras del purgatorio seran rival para nosotros, la tropa del leon negro!"+htmlend
#-Part 2
p2_explanation    = html+sophia+"Esta mision es expulsar a los restos de la fuerza militar griega que actualmente esta acampada en la parte noroeste del valle de la herradura. No los tomes demasiado a la ligera pensando que son una simple chusma de soldados derrotados. Tus oponentes son viejos Mahums del ejercito Hacha sangrienta liderado por el senor de la sangre Nurka. Son un enemigo formidable que no debes tomar demasiado a la ligera.<br><br><a action=\"bypass -h Quest 333_BlackLionHunt p2_t\">Asume la mision.<\a><br><a action=\"bypass - h Quest 333_BlackLionHunt start_chose_parts\">Escucha la explicacion sobre otra mision.</a>"+htmlend
p2_take        = html+sophia+"Los enemigos que tendras que derrotar son <font color=\"LEVEL\">Ol Mahum guerrillas, asaltantes Ol Mahum, tirador Ol mahum, Ol Mahum sargentos y Ol Mahum capitanes</font>.<br>Como prueba de que has derrotado al enemigo, traeme de vuelta la <font color=\"LEVEL\">insignia del hacha de sangre</font>, el simbolo del ejercito partisano. Cuantas mas pruebas traigas, mayor sera tu recompensa. Bueno, como alguna vez trabajaste con el capitan Leopold, ya conoces la regla sobre pruebas y recompensas, no?<br>Ahora bien, date prisa y vete al escondite partidista. Muestrales la ira de la tropa del leon negro contra esos viejos Mahums arrasadores!"+htmlend
#-Part 3
p3_explanation    = html+sophia+"La sede de los hombres lagarto delu estaba originalmente ubicada en la zona costera en la parte sur de Giran. Sin embargo, ultimamente, muchos de ellos se estan infiltrando en territorio Dion. Aun no sabemos si estan entrando en Dion solo para encontrar comida o para preparar una invasion a gran escala. Pero lo que esta claro es que estan haciendo sus movimientos con algun objetivo claro. Nuestra mision es aplastar a sus unidades una por una e infundirles miedo, disuadiendolos de establecerse en esta area.<br><br><a action=\"bypass -h Quest 333_BlackLionHunt p3_t\">Asume la mision.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt start_chose_parts\">Escucha la explicacion sobre otra mision.</a>"+htmlend
p3_take        = html+sophia+"Los enemigos con los que te enfrentaras son <font color=\"LEVEL\">Delu Lizardmen, Delu Lizardman exploradores y Delu Lizardman guerreros</font>. Como prueba de que los mataste, trae de vuelta los <font color=\"LEVEL\">Dientes de Delu Lizardmens</font>. Pero ten cuidado. En comparacion con la tribu Felim en Gludio o hombre lagarto Langk, son mucho mas violentos y hostiles.<br>Cuantas mas pruebas de victoria traigas, mayor sera tu recompensa. Bueno, ya que una vez trabajaste con el capitan Leopold, ya deberias conocer la regla sobre pruebas y recompensas, no?<br>Bueno, entonces vete al campo de batalla. Pisotea y destruye esos lagartos que se vuelven locos sin saber su lugar correcto!"+htmlend
#-Part 4
p4_explanation    = html+sophia+"Esta mision tiene que lidiar con extranas criaturas malvadas llamadas Stakato que estan infestando las marismas de Cruma. Alguna vez has visto un Stakato? Parece un insecto. Es una carrera siniestra que te da una sensacion espeluznante. Su cuerpo esta cubierto por una apretada quitina Stakato y tienen garras afiladas en lugar de manos. Tambien tienen movimientos sorprendentemente rapidos. Nunca debes subestimarlos.<br>Para empeorar las cosas, las marismas estan habitadas por sanguijuelas gigantes, aranas y extranos espiritus malignos que revolotean alrededor de la torre de los gigantes. Esto hace que el lugar sea muy traicionero cuando uno tiene que llevar a cabo operaciones militares.<br><br><a action=\"bypass -h Quest 333_BlackLionHunt p4_t\">Asume la mision.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt start_chose_parts\">Escuche la explicacion sobre otra mision.</a>"+htmlend
p4_take        = html+sophia+"Los enemigos que tendras que destruir son <font color=\"LEVEL\">stakatos Marsh, trabajadores de stakato Marsh, soldados de stakato Marsh y drones de stakato Marsh</font>. Como prueba de tu victoria, traeme las garras de los stakatos que mates. Como siempre, cuantas mas pruebas de victoria traigas, mayor sera tu recompensa.<br>Ahora, preparate para el combate y parte hacia Cruma Marshlands de inmediato. Esta vez, asegurate de ensenarles a esos Stakatos la terrible leccion de la tropa del leon negro!"+htmlend
#Redfoot
redfoot        = "<font color=\"LEVEL\">Mercenario Pie rojo:</font><br><br>"
f_no_box      = html+redfoot+"Oye hermano! Me dijiste que estas actualmente en servicio activo? Se que debe ser un trabajo duro! Hay algo en lo que pueda ayudarte?<br><br><a action=\"bypass -h Quest 333_BlackLionHunt f_info\">Preguntale si tiene alguna informacion util.</a>"+htmlend
f_give_box      = html+redfoot+"Oye hermano! Me dijiste que estas actualmente en servicio activo? Se que debe ser un trabajo duro! Hay algo en lo que pueda ayudarte?<br>Que tipo de caja es esa? Oh, lo se. Esa es una caja de carga utilizada por los comerciantes. Ya que me lo trajiste, puedo asumir que no tienes ninguna intencion de devolverselo al comerciante, verdad? Esta bien. Te abrire la caja. Por supuesto, puedes quedarte con el contenido de la caja. En cambio, te cobrare una pequena tarifa. Creo que <font color=\"LEVEL\">650 adenas</font> sera apropiado. Piensa en ello como el precio por abrir la caja y por mantener la boca cerrada.<br><br><a action=\"bypass -h Quest 333_BlackLionHunt f_give\">Pidele que abra la caja por ti.</a><br>"+back+htmlend
f_rnd_list      = ["Hace algun tiempo, escuche a unos enanos hablando entre ellos en una herreria. El jefe de los enanos, tal vez se llama el primer anciano? De todos modos, estaba buscando desesperadamente un pergamino que tuviera caracteres jeroglificos de gigantes. Aunque no pude escuchar los detalles, parecia que en el estaba escrito algun secreto muy critico sobre la tecnologia cientifica del gigante. Siempre pense que los enanos simplemente se ocupaban de su trabajo en herrerias y de almacenistas. Pero, que sabes? Creo que han estado trabajando en cosas secretas evitando el escrutinio de los humanos.<br>",
             "Hace algun tiempo, mientras hablaba con los miembros del gremio de elfos oscuros, descubri que los elfos oscuros adoran a la diosa Shilen!! Estas diciendo que todo el mundo ya lo sabe? Bueno, escuche sobre eso por primera vez. Por que querrias adorar a una diosa de la muerte? No tiene ningun sentido para mi. Pero segun quienes han estado en el bosque oscuro, el templo de Shilen construido por los elfos oscuros es verdaderamente magnifico. Me dijeron que los celebrantes abisales en el templo estan recolectando fragmentos de la estatua de la diosa Shilen de todas partes!<br>",
             "Alguna vez has oido hablar de una cria? Es un lindo dragon bebe que nacio del huevo de un wyrm o un draco. Entre los cuidadores de mascotas, escuche que hay alguien que sabe como criar una cria como propia mascota. Creo que se llama Cooper o algo asi. Si estas interesado en tener una cria como mascota, por que no vas a verla?<br>",
             "Te dare la informacion que un lider de clan, que quiera aumentar el poder de su clan, estaria interesado en obtener. En cada zona hay aristocratas que dan apoyo a pequenos clanes. Estos aristocratas incluirian a Sir Kristof Rodemai en la ciudad castillo de Giran y Sir Gustaf Athebaldt de la ciudad castillo de Oren. Por supuesto, no son solo filantropos. Yo diria que querrian algo a cambio de su apoyo a un clan, no te parece?<br>",
             "Hace algun tiempo escuche el rumor de que existe una sociedad de coleccionistas de monedas antiguas. Al principio pense que debian ser coleccionistas de algunas monedas de aniversario que no tienen mucho valor. Pero luego descubri que el valor de las monedas que recolectan es extremadamente alto. Y los miembros de esta sociedad estan muy entusiasmados con sus actividades de recoleccion y quien les traiga algunas monedas raras, las cambiaran por algunos articulos de alto precio! Escuche que para unirte a la sociedad de recoleccion de monedas, debes ir a ver a un enano llamado Sorint en el pueblo de cazadores.<br>",
             "Escuche que si te acercas a la torre de marfil en Oren, encontraras un alquimista falso. Se dice que anda diciendole a la gente que puede hacer una pocion magica que hara realidad los deseos de la gente. Muchas personas han sido victimas de su pocion falsa. Pero lo sorprendente es que de vez en cuando, despues de usar la pocion, los deseos de la gente se hacian realidad. El problema es que esto ocurre muy raramente.<br>",
             "Callate! Acercase mas a mi. Te dare informacion de gran valor. Escuche a los comerciantes hablando entre ellos. Hace algun tiempo, el vagon de carga de la asociacion Empresarial de Aden que viajaba de Giran a Dion fue asaltado y sustrajeron un objeto de gran valor. Es una gema llamada Diamante imperial y es una joya de valor incalculable. Bueno, dado que era una piedra preciosa que solia decorar la corona de un rey, ahora no seria un articulo comun, verdad? Ojala pudiera tener la oportunidad de verlo aunque sea una vez en mi vida.<br>",
             "Has oido hablar del rumor? Antharas, el dragon de tierra que habia estado durmiendo es el valle del dragon, ha despertado. Esta es una noticia terrible. Si sale de la guarida de Antharas y se vuelve loca, toda la region de Giran caera en un estado de caos en poco tiempo. Sin embargo, hay alguien que esta reclutando personas para formar una milicia para atrapar. Antharas. Es una mujer llamada Gabrielle en la ciudad castillo de Giran. Sin embargo, realmente cree que tendran alguna posibilidad contra el dragon? Desafortunadamente, creo que esta mucho mas alla de su poder!<br>",
             "En este pueblo vive un joven que suena con convertirse en el mejor chef del reino. Su nombre es Jonas. Ultimamente ha estado trabajando duro para prepararse para competir en un concurso culinario. Busca un aventurero que pueda encontrar ingredientes para preparar platos exoticos.<br>",
             "En la ciudad del castillo de Giran hay un joven cuyo unico objetivo en la vida es vengarse. Todo el mundo le ha dicho que es inutil, pero el esta decidido a matar al dragon de tierra Antharas con sus propias manos. Todos los dias fabrica flechas especiales. Ademas, si alguien le trae la materia prima que necesita para fabricar las flechas, le pagara una gran recompensa. Si estas interesado, por que no vas a verlo? Su nombre es Belton y trabaja como guardia en la ciudad castillo de Giran.<br>",
             "Te dare informacion que sera util para alguien que viaja mucho como tu. Segun la ley del pais, a los comerciantes de este reino no se les permite tratar con criminales. Pero hay algunos comerciantes que ignoran esta regla y venden sus articulos a forajidos. Estas personas incluyen al tendero Pano de la aldea Floran y a Twyla, que ha establecido su negocio en la seccion occidental del bosque oscuro. Aunque son gente de negocios, creo que es una verguenza de su parte tratar con delincuentes solo para ganar dinero.<br>",
             "Quieres que te presente una oportunidad laboral? Si vas a la zona noroeste de Gludio, hay un granjero que se llama Peter. Actualmente esta contratando mercenarios para expulsar a los orcos turk que se han establecido cerca de su granja. Con tu habilidad, podrias lidiar con los orcos turk sin problemas, verdad?<br>Por cierto, sabias que a menudo se encuentran reliquias de reinos antiguos en esa zona? Mientras trataba con los orcos turk, escuche que algunas personas descubrieron preciosas reliquias antiguas por accidente.<br>",
             "Have you heard of the Aden Business Guild?  It is an association of human traders.  Since they saw that dwarven traders and warehouse keepers were generating a lot of profit while engaging in their organizational activities, humans decided to imitate them by forming a guild of their own.  However, it seems to me that the business savvy of a dwarf is inborn  No matter how hard humans try, I dont think they can keep up with dwarves.<br>On top of that, adding insult to injury, evil spirits frequently attack the guilds cargo wagons and steal their valuable goods making the humans suffer great losses.<br>",
             "Some time ago, while I was talking with the members of the Dark Elf Guild, I found out that Dark Elves worship the Goddess Shilen!!   Are you saying that everybody already knows about that?   Well, I heard about it for the first time <br>Why would you want to worship a goddess of death  It doesnt make any sense to me.  But according to those who have been to the Dark Forest, the Temple of Shilen built by the Dark Elves is truly magnificent.  They told me that the Abyssal Celebrants at the temple are gathering fragments of the statue of Goddess Shilen from everywhere!<br>",
             "Have you ever heard of a hatchling?  It is a cute baby dragon that has been hatched from the egg of a wyrm or a drake.  Among pet handlers, I heard that there is someone who knows how to raise a hatchling as ones own pet  I think his name is Cooper or something like that.  If you are interested in keeping a hatchling as a pet, why dont you go see him!<br>",
             "I will give you the information that a clan leader, who wants to grow the power of his clan would be interested in obtaining.  In each area, there are aristocrats who give support to small clans.  These aristocrats would include Sir Kristof Rodemai in Giran Castle Town and Sir Gustaf Athebaldt of Oren Castle Town.  Of course they are not just philanthropists.  I would say they would want something in return for their support of a clan, wouldnt you agree?<br>",
             "Some time ago, I heard a rumor that there is a society of ancient coin collectors.  At first, I thought that they must be collectors of some anniversary coins that are not very valuable.  But later, I found out that the value of the coins they collect is extremely high.  And members of this society are very enthusiastic about their collection activities that whoever brings some rare coins to them, they will trade them for some high priced items!  I heard that in order to join the coin collection society, you have to go see a dwarf called Sorint at the Hunters Village.<br>",
             "I heard that if you go near the Ivory Tower in Oren, you will find a fake alchemist.  It is said that he goes around telling people that he can make some magic potion that will make peoples wishes come true  Many people have fallen victim to his fake potion.  But what is surprising is that once in a blue moon, after using the potion peoples wishes actually did come true.  The problem is that this only happens very very rarely<br>",
             "Mercenary Red Foot<br>",
             "Has oido hablar del rumor? Antharas, el dragon de tierra que habia estado durmiendo en el valle del dragon, ha despertado. Esta es una noticia terrible. Si sale de la guarida de Antharas y se vuelve loca, toda la region de Giran caera en un estado de caos en poco tiempo. Sin embargo, hay alguien que esta reclutando personas para formar una milicia para atrapar. Antharas. Es una mujer llamada Gabrielle en la ciudad castillo de Giran. Sin embargo, realmente cree que tendran alguna posibilidad contra el dragon? Desafortunadamente, creo que esta mucho mas alla de su poder!<br>",
             ]
f_no_news      = html+redfoot+"Lo siento. No tengo ninguna informacion nueva para usted. Por que no vuelves a visitarnos mas tarde?<br>"+back+htmlend
f_more_help      = html+redfoot+"Hay algo mas en lo que pueda ayudarte?<br><br><a action=\"bypass -h Quest 333_BlackLionHunt f_give\">Pidele que abra la caja por ti.</a>"+htmlend
f_no_more_box    = html+redfoot+"No se que decirte! Ni siquiera llevas contigo una caja de carga. Pero todavia me pides que abra uno?<br><br><a action=\"bypass -h Quest 333_BlackLionHunt f_info\">Preguntale si tiene alguna informacion util.</a>"+htmlend
f_more_help2    = html+redfoot+"Hay algo mas en lo que quieras que te ayude?<br><br><a action=\"bypass -h Quest 333_BlackLionHunt f_give\">Pidele que abra la caja de carga por ti.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt f_info\">Preguntale si tiene alguna informacion util para ti.</a>"+htmlend
f_not_adena      = html+redfoot+"Escucha aqui hermano! Esto no es suficiente dinero!!! No pensaste por casualidad que te daria la informacion gratis, verdad? Esto tambien es un negocio para mi, entiendelo!<br>"+back+htmlend
#Rupio
rupio        = "<font color=\"LEVEL\">Herrero Rupio:</font><br><br>"
r_no_items      = html+rupio+"Eres un mercenario del leon negro? Cual es el motivo de visitar nuestra herreria? Has venido para que te fabriquen un arma?"+htmlend
r_items        = html+rupio+"En que puedo ayudar?<br><br><a action=\"bypass -h Quest 333_BlackLionHunt r_give_statue\">Pide armar piezas de estatua.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt r_give_tablet\">Pide que te armen una tablilla de piedra."+htmlend
r_statue_pieces    = html+rupio+"Como supiste que mi hobby era la restauracion de reliquias? Pero para restaurar un objeto de piedra a su estado original, no puede faltar ni una sola pieza. Si quieres que vuelva a armar la estatua de la diosa, necesitaras todas las piezas, que son: <font color=\"LEVEL\">cabeza, torso, brazos y piernas</font>), verdad?"+htmlend
r_statue_brockes  = html+rupio+"Bien, debo demostrar mis talentos ahora? Primero... Une las piernas a la base... Luego el torso encima de eso... Y si unimos bien las articulaciones de los brazos y la cabeza... Eh? La estatua simplemente se derrumbo... Sabia que era muy vieja y que el material era debil, pero... Cuando aplique un poco de presion para conectarme... Oh, lo siento mucho."+htmlend
r_statue_complete  = html+rupio+"Bien, debo demostrar mis talentos ahora? Primero... Une las piernas a la base... Luego el torso encima de eso... Y si unimos bien las articulaciones de los brazos y la cabeza... OK! Esta terminado! Las uniones de las piezas de conexion aun son visibles pero en general parece perfecto, no crees? Es la imagen de la diosa de Shilen? Mirandola con atencion, es realmente una estatua hermosa."+htmlend
r_tablet_pieces    = html+rupio+"Como supiste que mi hobby era la restauracion de reliquias? Pero con reliquias como tablillas en las que estan escritas palabras, no podemos leerlas si falta siquiera una pieza, por lo que realmente no tiene sentido simplemente juntar las otras piezas. En mi experiencia, las reliquias de forma cuadrada, como las tablas de piedra, a menudo se rompen en <font color=\"LEVEL\">cuatro pedazos</font>."+htmlend
r_tablet_brockes  = html+rupio+"Bien, debo demostrar mis talentos ahora? Bueno, parece que este fragmento va hasta la seccion inferior de la tabla de piedra... Y esta pieza esta encima de eso... Oh! La tableta simplemente se desmorono... Deberia haber esperado que el material fuera realmente debil por haber estado expuesto a la lluvia y al viento durante tanto tiempo... Maldita sea! Realmente lamento haber cometido un error tan grande."+htmlend
r_tablet_complete  = html+rupio+"Bien, debo demostrar mis talentos ahora? Bueno, este fragmento parece que va hasta la seccion inferior de la tabla de piedra... Y esta pieza esta encima de eso... Es como armar un rompecabezas... OK... Esta terminado! Es una antigua tablilla de piedra... Tengo mucha curiosidad por saber si en ella estan registrados algunos secretos de la historia! Pero estas cartas parecen escrituras de los titanes... He visto esto en alguna parte antes! En que parte del mundo podria?!"+htmlend
#Lockirin
lockirin      = "<font color=\"LEVEL\">Primer anciano Lockirin:</font><br><br>"
l_no_tablet      = html+lockirin+"Estoy extremadamente interesado en la civilizacion de los titanes. En particular, pagaria cualquier cantidad por tener en mis manos una tablilla de arcilla en la que esta escrita la escritura del titan. Si yo fuera una persona de clase alta como usted, podria haber visto algo asi. Dicen que en la region de Dion se encuentran a menudo antiguas tablillas de arcilla..."+htmlend
l_just_pieces    = html+lockirin+"Esta tablilla de arcilla... En que parte del mundo podria?! Es solo una parte, pero... Mahr!<br>Mira esto, joven! En que parte del mundo encontraste esto? Si tambien puedes juntar las otras piezas y unirlas en un solo articulo, te dare algo grandioso en agradecimiento! Lo prometo en nombre del primer anciano de la federacion de gremios!"+htmlend
l_tablet      = html+lockirin+"Esta tablilla de arcilla... En que parte del mundo podria?! Es solo una parte, pero... Mahr! De donde salio algo tan precioso? Mira esto, jovencito! Te presentare un gran regalo de gratitud, asi que por favor dame esta tableta!<br><a action=\"bypass -h Quest 333_BlackLionHunt l_give\">Entrega la tableta de arcilla.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt l_info\">No entregar."+htmlend
l_give        = html+lockirin+"Estoy realmente agradecido! Por fin el trabajo arraigado de nuestra federacion gremial! Toma, toma este regalo de gratitud! Y si encuentras mas de estas tablillas de arcilla en el futuro, traemelas tambien! Expresare mi agradecimiento adecuadamente!"+htmlend
l_info        = html+lockirin+"Dije que le agradeceria abundantemente pero usted todavia se niega... Mire, jovencito. De verdad crees que podras vender esa tableta en otro lugar a un precio mas alto? Te garantizo que por mucho que busques, no encontraras a nadie que te de tanto como yo. Si tu opinion cambia, por favor vuelve a verme. Entregame esa tableta en cualquier momento y te dare un gran regalo de gratitud como te prometi!"+htmlend
#Undiras
undiras        = "<font color=\"LEVEL\">Celebrante abisal Undrias:</font><br><br>"
u_no_statue      = html+undiras+"En todo el continente este templo es el unico lugar donde se consagra a la diosa Shilen. Debido a la reforma religiosa distorsionada de los humanos, nuestra diosa a la que adoramos ha sido malinterpretada como un ser siniestro que trae muerte y destruccion. Pero nosotros, los elfos oscuros, todavia adoramos a Shilen como nuestro creador y como una diosa que esta a cargo de la vida y la muerte.<br>Desafortunadamente, cuando este lugar fue invadido por las fuerzas aliadas de humanos y elfos, muchos objetos sagrados que decoraban el templo se perdieron. Especialmente, fueron robadas muchas estatuas de la diosa Shilen que estaban exquisitamente elaboradas. Nosotros, los celebrantes abisales, estamos dispuestos a dar una gran recompensa a quienes puedan recuperar las estatuas para nosotros."+htmlend
u_just_pieces    = html+undiras+"Oh, esta pieza debe ser? Aunque es la unica parte que aun queda, esta pieza proviene de una de las estatuas de Shilen que se perdieron! En que parte del mundo lo encontraste? Podras encontrar el resto de piezas y traernos una estatua completamente restaurada? Si lo hace, le pagaremos una gran suma de dinero como recompensa!"+htmlend
u_statue      = html+undiras+"Oh, esta pieza debe ser? Aunque es la unica parte que aun queda, esta pieza proviene de una de las estatuas de Shilen que se perdieron! En que parte del mundo lo encontraste? Donde encontraste este objeto sagrado? Esta estatua es un objeto sagrado para nosotros los elfos oscuros. Te pagare una gran suma de dinero si me la entregas. Despues de todo, no te resulta de mucha utilidad, verdad?<br><br><a action=\"bypass -h Quest 333_BlackLionHunt u_give\">Dale la estatua de Shilen.</a><br><a action=\"bypass -h Quest 333_BlackLionHunt u_info\">Niegate a darle la estatua de Shilen.</a>"+htmlend
u_give        = html+undiras+"Debido a la reforma religiosa distorsionada de los humanos, nuestra diosa a la que adoramos ha sido malinterpretada como un ser siniestro que trae muerte y destruccion. Pero nosotros, los elfos oscuros, todavia adoramos a Shilen como nuestra creadora y como una diosa que esta a cargo de la vida y la muerte. Desafortunadamente, cuando este lugar fue invadido por las fuerzas aliadas de humanos y elfos, muchos objetos sagrados que decoraban el templo se perdieron. Especialmente, fueron robadas muchas estatuas de la diosa Shilen que estaban exquisitamente elaboradas. La estatua que trajiste aqui es una de las estatuas que se perdieron en ese momento. Muchas gracias. Aqui esta el dinero de recompensa que te prometi. Si encuentras mas estatuas como esta, traemelas. Bien, entonces que la proteccion divina del abismo este contigo!"+htmlend
u_info        = html+undiras+"Esa estatua es un objeto sagrado para nosotros los elfos oscuros. De todos modos, si lo guardas para ti, no le servira de mucho. Ademas, si llevas contigo una estatua de Shilen y caminas entre humanos, la gente te acusara de ser pagano. Tendrias suerte si no mueres quemado en la hoguera. De todos modos, si cambias de opinion, vuelve a verme. Si me entrega la estatua, estoy dispuesto a pagarle una generosa suma de dinero como recompensa. Bueno, entonces que la proteccion divina del abismo este contigo."+htmlend
#Morgan
morgan        = "<font color=\"LEVEL\">Morgan, miembro del gremio:</font><br><br>"
m_no_box      = html+morgan+"Eres miembro de los mercenarios del leon negro, no? Escuche que recientemente estas trabajando duro para deshacerte de las criaturas malvadas en esta area. Continuen con el buen trabajo tambien en el futuro!"+htmlend
m_box        = html+morgan+"Eres miembro de los mercenarios del leon negro, no? Escuche que recientemente estas trabajando duro para deshacerte de las criaturas malvadas en esta area. Continuen con el buen trabajo tambien en el futuro! Pero tienes algun negocio conmigo?<br><br><a action=\"bypass -h Quest 333_BlackLionHunt m_give\">Entregue la caja de carga.</a>"+htmlend
m_rnd_1        = html+morgan+"Es una caja de carga de nuestro gremio comercial!? Es carga que fue robada de nuestros carros despues de haber sido atacada recientemente por criaturas malvadas. Pero hay mucha carga que fue saqueada y por eso nuestras perdidas son realmente grandes. Aun asi, es una gran suerte que hayas podido recuperar esta pieza.<br>Como representante del gremio comercial, te agradezco tus esfuerzos. Toma, toma este regalo de gratitud, aunque no sea mucho. Y les presento estas (<font color=\"LEVEL\">monedas de nuestro gremio</font>). Es como una placa de agradecimiento que damos a las personas que han contribuido al gremio comercial.<br><br><a action=\"bypass -h Quest 333_BlackLionHunt m_reward\">Regresar.</a>"+htmlend
m_rnd_2        = html+morgan+"Tienes otra caja de carga. Estoy agradecido de nuevo. El cargamento saqueado por las criaturas malvadas aumenta dia a dia, pero sin la ayuda de mercenarios como usted, las perdidas de nuestro gremio comercial serian mucho mayores. Toma, toma este regalo de gratitud!. Y, como siempre, os presento estas <font color=\"LEVEL\">monedas de nuestro gremio</font>). Continua con el buen trabajo tambien en el futuro!<br><br><a action=\"bypass -h Quest 333_BlackLionHunt m_reward\">Regresa.</a>"+htmlend
m_rnd_3        = html+morgan+"Realmente les agradezco que hayan recuperado tantas cajas como esta para nosotros. Si la situacion financiera de nuestro gremio comercial fuera un poco mejor, contratariamos mercenarios competentes como usted como guardaespaldas... En ese caso, las criaturas malvadas nunca podrian saquear nuestras cosas, no?<br>OK! Toma, toma el regalo de la gratitud! La cantidad del dinero de gratitud aumento enormemente despues de que hable con mis superiores sobre el arduo trabajo que han estado haciendo para nuestro gremio. Como este es un reconocimiento apropiado por su arduo trabajo, tomelo sin negarse. Y, como siempre, te presento estas <font color=\"LEVEL\">monedas de nuestro gremio.</font><br><br><a action=\"bypass -h Quest 333_BlackLionHunt m_reward\">Regresa.</a>"+htmlend
m_no_more_box       = html+morgan+"Caja de carga? De que caja estas hablando? No me parece que tengas uno de esos..."+htmlend
m_reward      = html+morgan+"Hay algo que pueda hacer por usted?<br><br><a action=\"bypass -h Quest 333_BlackLionHunt m_give\">Entregue la caja de transporte.</a>"+htmlend

import sys
from com.l2jfrozen import Config 
from com.l2jfrozen.gameserver.model.quest import State
from com.l2jfrozen.gameserver.model.quest import QuestState
from com.l2jfrozen.gameserver.model.quest.jython import QuestJython as JQuest
#This Put all Mob Ids from dictionari in a list. So its possible to add new mobs, to one of this 4 Areas, without modification on the addKill Part.
MOBS=DROPLIST.keys()

def giveRewards(st,item,count):
  st.giveItems(ADENA_ID,35*count)
  st.takeItems(item,count)
  if count < 20:
    return
  if count<50:
    st.giveItems(LIONS_CLAW,1)
  elif count<100:
    st.giveItems(LIONS_CLAW,2)
  else:
    st.giveItems(LIONS_CLAW,3)
  return

class Quest (JQuest) :

  def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

  def onEvent (self,event,st) :
    part = st.getInt("part")
    if event == "start" :
      st.set("cond","1")
      st.setState(STARTED)
      st.playSound("ItemSound.quest_accept")
      #just to go with the official, until we have the option to make the take part invisible, like on officials.
      st.takeItems(BLACK_LION_MARK,1)
      st.giveItems(BLACK_LION_MARK,1)
      return start_explain
    elif event == "p1_t":
      st.set("part","1")
      st.giveItems(SOPHIAS_LETTER1,1)
      return p1_take
    elif event == "p2_t":
      st.set("part","2")
      st.giveItems(SOPHIAS_LETTER2,1)
      return p2_take
    elif event == "p3_t":
      st.set("part","3")
      st.giveItems(SOPHIAS_LETTER3,1)
      return p3_take
    elif event == "p4_t":
      st.set("part","4")
      st.giveItems(SOPHIAS_LETTER4,1)
      return p4_take
    elif event == "exit":
      st.takeItems(BLACK_LION_MARK,1)
      st.exitQuest(1)
      return exit
    elif event == "continue":
      claw=int(st.getQuestItemsCount(LIONS_CLAW)/10)
      check_eye=st.getQuestItemsCount(LIONS_EYE)
      if claw :
        st.giveItems(LIONS_EYE,claw)
        eye=st.getQuestItemsCount(LIONS_EYE)
        st.takeItems(LIONS_CLAW,claw*10)
        ala_count=3
        soul_count=100
        soe_count=20
        heal_count=20
        spir_count=50
        if eye > 9:
          ala_count=4
          soul_count=400
          soe_count=30
          heal_count=50
          spir_count=200
        elif eye > 4:
          spir_count=100
          soul_count=200
          heal_count=25
        while claw > 0:
          n = st.getRandom(5)
          if n < 1 :
            st.giveItems(ALACRITY_POTION, int(ala_count*Config.RATE_QUESTS_REWARD))
          elif n < 2 :
            st.giveItems(SOULSHOT_D, int(soul_count*Config.RATE_QUESTS_REWARD))
          elif n < 3:
            st.giveItems(SCROLL_ESCAPE, int(soe_count*Config.RATE_QUESTS_REWARD))
          elif n < 4:
            st.giveItems(SPIRITSHOT_D,int(spir_count*Config.RATE_QUESTS_REWARD))
          elif n == 4:
            st.giveItems(HEALING_POTION,int(heal_count*Config.RATE_QUESTS_REWARD))
          claw-=1
        if check_eye:
          return p_eye
        else:
          return p_first_eye
      else:
        return start_continue
    elif event == "leave":
      if part == 1:
        order = SOPHIAS_LETTER1
      elif part == 2:
        order = SOPHIAS_LETTER2
      elif part == 3:
        order = SOPHIAS_LETTER3
      elif part == 4:
        order = SOPHIAS_LETTER4
      else:
        order = 0
      st.set("part","0")
      if order:
        st.takeItems(order,1)
      return p_leave_mission
    elif event == "f_info":
      text = st.getInt("text")
      if text<4:
        rnd=int(st.getRandom(20))
        st.set("text",str(text+1))
        text_rnd = html+redfoot+f_rnd_list[rnd]+back+htmlend
        return text_rnd
      else:
        return f_no_news
    elif event == "f_give":
      if st.getQuestItemsCount(CARGO_BOX1) :
        if st.getQuestItemsCount(ADENA_ID)>=OPEN_BOX_PRICE:
          st.takeItems(CARGO_BOX1,1)
          st.takeItems(ADENA_ID,650)
          random = st.getRandom(162)
          standart = "Muy bien, sigamos adelante y abramos esta caja. Abrir un candado como este es pan comido. Alla vamos! Ahi eso fue demasiado facil. Ahora, veamos que hay en la caja.<br>"
          statue = "Que es esto? Un fragmento de una estatua de piedra? Parece una estatua de Shilen, la diosa. No es ella la diosa de la muerte? Por alguna razon, no tengo un buen presentimiento sobre esto. Pero, si esto no fuera un fragmento sino la estatua completa, podria haberse vendido por una gran cantidad de dinero. Hay alguien que puede armar una reliquia rota como esta, es el herrero Rupio. Si recoges todos los fragmentos de la estatua y se los llevas, el los juntara para restaurarla y completarla.<br>" 
          tablet = "Un fragmento de tableta rota? Tiene algunos simbolos incomprensibles. Es esta una reliquia de la antiguedad? Si no se tratara de un fragmento sino de una tablilla completa, podria haber sido un objeto historico muy valioso. Si puedes encontrar todos los fragmentos de la tableta, puedes restaurarlos a su forma completa. Si estas interesado, ve a ver a <font color=\"LEVEL\">Rupio</font> el herrero. Es un experto en restauracion de reliquias.<br>"
          if random < 21 :
            st.giveItems(GLUDIO_APPLE,int(Config.RATE_QUESTS_REWARD))
            return html+redfoot+standart+"<br>Fruta? Oh, deben ser manzanas cultivadas en Gludio! Mmmm se ven deliciosos. Si los llevas al mercado antes de que se echen a perder, supongo que podras ganar algo de dinero.<br>"+back+htmlend
          elif random < 41:
            st.giveItems(CORN_MEAL,int(Config.RATE_QUESTS_REWARD))
            return html+redfoot+standart+"No es esto harina de maiz? No se usa esto para alimentar a los cerdos? Bueno, de todos modos, como no es algo que puedas usar tu mismo, deberias llevarlo al mercado para venderlo.<br>"+back+htmlend
          elif random < 61:
            st.giveItems(WOLF_PELTS,int(Config.RATE_QUESTS_REWARD))
            return html+redfoot+standart+"<br>Que son estas pieles? Pieles de lobo terrible? Parecen haber sido curtidas por un artesano del cuero. Pero no son de alta calidad. Quizas puedan usarse para hacer sombreros de cuero? Bueno, de todos modos, si los llevas al mercado, obtendras algo de dinero por ellos.<br>"+back+htmlend
          elif random < 74:
            st.giveItems(MONNSTONE,int(Config.RATE_QUESTS_REWARD))
            return html+redfoot+standart+"<br>Una gema? Vaya, una piedra lunar! Deberia poder venderlo a un precio bastante bueno.<br>"+back+htmlend
          elif random < 86:
            st.giveItems(GLUDIO_WEETS_FLOWER,int(Config.RATE_QUESTS_REWARD))
            return html+redfoot+standart+"<br>Que es este polvo? Deberia probarlo? Si, debe ser harina de trigo Gludio! Supongo que se puede utilizar para hornear pan. Bueno, de todos modos deberias poder venderlo a un precio decente en el mercado.<br>"+back+htmlend
          elif random < 98:
            st.giveItems(SPIDERSILK_ROPE,int(Config.RATE_QUESTS_REWARD))
            return html+redfoot+standart+"Que es esto? Su cuerda de seda de arana! Es una cuerda muy fuerte y liviana que esta hecha de seda de arana que se recolecta de las telas de arana tarantula en la cordillera de la columna vertebral. Si lo llevas a una tienda, estoy seguro de que podras conseguir un precio realmente bueno.<br>"+back+htmlend
          elif random < 99:
            st.giveItems(ALEXANDRIT,int(Config.RATE_QUESTS_REWARD))
            return html+redfoot+standart+back+htmlend
          elif random < 109:
            st.giveItems(SILVER_TEA,int(Config.RATE_QUESTS_REWARD))
            return html+redfoot+standart+"Un cuenco de plata? Y una taza de te? Parecen ser de bastante alta calidad! Parece que fueron hechos por artesanos elficos. No me interesan articulos tan exquisitos pero, de todas formas, si los llevas a una tienda, deberias poder venderlos a un precio bastante bueno.<br>"+back+htmlend
          elif random < 119:
            st.giveItems(GOLEM_PART,int(Config.RATE_QUESTS_REWARD))
            return html+redfoot+standart+"Partes de maquina? Esta marca del gremio parece ser la del gremio Yunque negro, que opinas? Aunque no lo se con certeza, estas parecen ser piezas que utilizan los enanos para reparar los golems. Si los llevas a una tienda, creo que podras venderlos a un precio bastante razonable.<br>"+back+htmlend
          elif random < 123:
            st.giveItems(FIRE_EMERALD,int(Config.RATE_QUESTS_REWARD))
            return html+redfoot+standart+"Que es esta joya? Ah! Es una esmeralda de fuego! No lo sabes? Es una piedra preciosa rara y preciosa que emite una fuerte luz roja cuando se expone a la luz del sol. Eres tan afortunado! Puedes llevarlo a una tienda y venderlo a un precio muy alto.<br>"+back+htmlend
          elif random < 127:
            st.giveItems(SILK_FROCK,int(Config.RATE_QUESTS_REWARD))
            return html+redfoot+standart+"No es esto un vestido?! Este es un vestido de seda para mujer. Parece bastante caro, no crees? Echa un vistazo a este diseno. Este es un articulo importado de Avella del este. En un momento como este, quien usaria un articulo tan lujoso? Esto debe ser ordenado por una mujer noble a la que le gusten los productos extranjeros, no crees? Deberias llevar esto a una tienda y venderlo! Estoy seguro de que obtendra un precio muy alto por ello.<br>"+back+htmlend
          elif random < 131:
            st.giveItems(PORCELAN_URN,int(Config.RATE_QUESTS_REWARD))
            return html+redfoot+standart+back+htmlend
          elif random < 132:
            st.giveItems(IMPERIAL_DIAMOND,int(Config.RATE_QUESTS_REWARD))
            return html+redfoot+standart+"No me digas! No lo creo!!! Vaya, un diamante imperial? No es este el que adornaba la corona del rey de Elmo-Aden? Es realmente hermoso! Tienes mucha suerte! Te conseguiste un articulo de valor incalculable. Si lo lleva al mercado, estoy seguro de que podra obtener una gran cantidad de dinero por el.<br>"+back+htmlend
          elif random < 147:
            random_stat=st.getRandom(4)
            if random_stat == 3 :
              st.giveItems(STATUE_SHILIEN_HEAD,1)
              return html+redfoot+standart+statue+back+htmlend
            elif random_stat == 0 :
              st.giveItems(STATUE_SHILIEN_TORSO,1)
              return html+redfoot+standart+statue+back+htmlend
            elif random_stat == 1 :
              st.giveItems(STATUE_SHILIEN_ARM,1)
              return html+redfoot+standart+statue+back+htmlend
            elif random_stat == 2 :
              st.giveItems(STATUE_SHILIEN_LEG,1)
              return html+redfoot+standart+statue+back+htmlend
          elif random < 162:
            random_tab=st.getRandom(4)
            if random_tab == 0 :
              st.giveItems(FRAGMENT_ANCIENT_TABLE1,1)
              return html+redfoot+standart+tablet+back+htmlend
            elif random_tab == 1:
              st.giveItems(FRAGMENT_ANCIENT_TABLE2,1)
              return html+redfoot+standart+tablet+back+htmlend
            elif random_tab == 2 :
              st.giveItems(FRAGMENT_ANCIENT_TABLE3,1)
              return html+redfoot+standart+tablet+back+htmlend
            elif random_tab == 3 :
              st.giveItems(FRAGMENT_ANCIENT_TABLE4,1)
              return html+redfoot+standart+tablet+back+htmlend
        else:
          return f_not_adena
      else:
        return f_no_more_box
    elif event in  ["r_give_statue","r_give_tablet"]:
      if event == "r_give_statue":
        items = statue_list
        item = COMPLETE_STATUE
        pieces = r_statue_pieces
        brockes = r_statue_brockes
        complete = r_statue_complete
      elif event == "r_give_tablet":
        items = tablet_list
        item = COMPLETE_TABLET
        pieces = r_tablet_pieces
        brockes = r_tablet_brockes
        complete = r_tablet_complete
      count=0
      for id in items:
        if st.getQuestItemsCount(id):
          count+=1
      if count>3:
        for id in items:
          st.takeItems(id,1)
        if st.getRandom(2)==1 :
          st.giveItems(item,1)
          return complete
        else:
          return brockes 
      elif count<4 and count!=0:
        return pieces
      else:
        return r_no_items
    elif event == "l_give" :
      if st.getQuestItemsCount(COMPLETE_TABLET):
        st.takeItems(COMPLETE_TABLET,1)
        st.giveItems(ADENA_ID,30000)
        return l_give
      else:
        return no_tablet
    elif event == "u_give" :
      if st.getQuestItemsCount(COMPLETE_STATUE) :
        st.takeItems(COMPLETE_STATUE,1)
        st.giveItems(ADENA_ID,30000)
        return u_give
      else:
        return no_statue
    elif event == "m_give":
      if st.getQuestItemsCount(CARGO_BOX1):
        coins = st.getQuestItemsCount(GUILD_COIN)
        count = int(coins/40)
        if count > 2 : count = 2
        st.giveItems(GUILD_COIN,1)
        st.giveItems(ADENA_ID,(1+count)*100)
        st.takeItems(CARGO_BOX1,1)
        random = st.getRandom(3)
        if random == 0:
          return m_rnd_1
        elif random == 1:
          return m_rnd_2
        else:
          return m_rnd_3
      else:
        return m_no_box
    elif event == "start_parts":
      return start_parts
    elif event == "m_reward":
      return m_reward
    elif event == "u_info":
      return u_info
    elif event == "l_info":
      return l_info
    elif event == "p_redfoot":
      return p_redfoot
    elif event == "p_trader_info":
      return p_trader_info
    elif event == "start_chose_parts":
      return start_parts
    elif event == "p1_explanation":
      return p1_explanation
    elif event == "p2_explanation":
      return p2_explanation
    elif event == "p3_explanation":
      return p3_explanation
    elif event == "p4_explanation":
      return p4_explanation
    elif event == "f_more_help":
      return f_more_help
    elif event == "r_exit":
      return r_exit
    
  def onTalk (self,npc,player):
    htmltext = "<html><body>O no estas llevando a cabo tu mision o no cumples los criterios.</body></html>"
    st = player.getQuestState(qn)
    if not st : return htmltext

    npcId = npc.getNpcId()
    id = st.getState()
    if npcId != NPC[0] and id != STARTED : return htmltext

    if id == CREATED :
      st.setState(STARTING)
      st.set("cond","0")
      st.set("part","0")
      st.set("text","0")
      if npcId == NPC[0]:
        if st.getQuestItemsCount(BLACK_LION_MARK) :
          if player.getLevel() >24 :
            return  start_start
          else:
            st.exitQuest(1)
            return start_error1
        else:
          st.exitQuest(1)
          return start_error2
    else: 
      part=st.getInt("part")
      if npcId==NPC[0]:
          if part == 1:
            item = UNDEAD_ASH
          elif part == 2:
            item = BLOODY_AXE_INSIGNIAS
          elif part == 3:
            item = DELU_FANG
          elif part == 4:
            item = STAKATO_TALONS
          else:
            return start_ask_again
          count=st.getQuestItemsCount(item)
          box=st.getQuestItemsCount(CARGO_BOX1)
          if box and count:
            giveRewards(st,item,count)
            return p_both_info
          elif box:
            return p_only_box_info
          elif count:
            giveRewards(st,item,count)
            return p_only_item_info
          else:
            return p_no_items
      elif npcId==NPC[1]:
          if st.getQuestItemsCount(CARGO_BOX1):
            return f_give_box
          else:
            return f_no_box
      elif npcId==NPC[2]:
          count=0
          for items in statue_list:
            if st.getQuestItemsCount(items):
              count+=1
          for items in tablet_list:
            if st.getQuestItemsCount(items):
              count+=1
          if count:
            return r_items
          else:
            return r_no_items
      elif npcId==NPC[3]:
        if st.getQuestItemsCount(COMPLETE_STATUE):
          return u_statue
        else:
          count=0
          for items in statue_list:
            if st.getQuestItemsCount(items):
              count+=1
          if count:
            return u_just_pieces
          else:
            return u_no_statue
      elif npcId==NPC[4]:
        if st.getQuestItemsCount(COMPLETE_TABLET):
          return l_tablet
        else:
          count=0
          for items in tablet_list:
            if st.getQuestItemsCount(items):
              count+=1
          if count:
            return l_just_pieces
          else:
            return l_no_tablet
      elif npcId==NPC[5]:
        if st.getQuestItemsCount(CARGO_BOX1):
          return m_box
        else:
          return m_no_box
          
  def onKill(self,npc,player,isPet):
    st = player.getQuestState(qn)
    if not st : return 
    if st.getState() != STARTED : return 

    npcId = npc.getNpcId()
    part,allowDrop,chancePartItem,chanceBox,partItem=DROPLIST[npcId]
    random1 = st.getRandom(101)
    random2 = st.getRandom(101)
    mobLevel = npc.getLevel()
    playerLevel = player.getLevel()
    if playerLevel - mobLevel > 8:
      chancePartItem/=3
      chanceBox/=3
    if allowDrop and st.getInt("part")==part :
      if random1<chancePartItem :
        st.giveItems(partItem,1)
        st.playSound("ItemSound.quest_itemget")
      if random2<chanceBox :
        st.giveItems(CARGO_BOX1,1)
        if not random1<chancePartItem:
          st.playSound("ItemSound.quest_itemget") 
    return


QUEST       = Quest(333,qn,"BlackLionHunt")
CREATED     = State('Start', QUEST)
STARTING    = State('Starting', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)

QUEST.setInitialState(CREATED)
QUEST.addStartNpc(NPC[0])

for npcId in NPC:
  QUEST.addTalkId(npcId)

for mobId in MOBS:
  QUEST.addKillId(mobId)