import time
import os
import pygame
import random
import sys
import threading

equilibrio = 0
eventos = 0

def imprimir_letra_por_letra(texto): #0.05 original
    for letra in texto:
        print(letra, end='', flush=True)  # 'flush=True' asegura que se imprima inmediatamente
        time.sleep(0.05)  # Ajusta el valor según sea necesario para la velocidad deseada
    print()  # Imprime un salto de línea al final

def contador_noche():
    # Duración de la noche en segundos
    duracion_noche = 15 * 60  # 5 min

    # Obtén el tiempo actual en segundos
    tiempo_actual = time.time()

    # Calcula el tiempo de finalización de la noche
    tiempo_fin_noche = tiempo_actual + duracion_noche

    # Bucle del contador
    while True:
        # Calcula el tiempo restante
        tiempo_restante = max(0, tiempo_fin_noche - time.time())

        # Convierte el tiempo restante a minutos y segundos
        minutos_restantes, segundos_restantes = divmod(tiempo_restante, 60)

        # Espera un segundo antes de actualizar el contador
        time.sleep(1)

        if tiempo_restante == 0:
            limpiar_consola()
            print("¡La noche ha terminado!, has perdido...")
            break

def contiene_si(oracion):
    return oracion.lower() == "si"

def contiene_jose(oracion):
    return "jose" in oracion.lower()

def contiene_marco(oracion):
    return "marco" in oracion.lower()

def contiene_isaac(oracion):
    return "isaac" in oracion.lower()

def contiene_samir(oracion):
    return "samir" in oracion.lower()


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def reproducir_intro():
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/pablo/Desktop/ia/edd2/tercer parcia/champagne.mp3')
    pygame.mixer.music.play()

def reproducir_main():
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/pablo/Desktop/ia/edd2/tercer parcia/main.mp3')
    pygame.mixer.music.play()

def aceptado(player1):
    limpiar_consola()
    time.sleep(2)
    print(f"\n¡Hola, {player1.nombre}!\n")
    time.sleep(2)
    print(f"\nAhora comenzare a hacerte una serie de preguntas para saber si eres apto para el trabajo.")
    time.sleep(4)
    count = 0
    player1.pregunta_random(count)

    print(f"\nFelicidades, acabas de entrar al grupo de seguridad de CLUB CHAMPAGNE.")
    time.sleep(3)
    print(f"\nA continuacion te diremos el reglamento y algunas indicaciones que necesitas saber.")
    time.sleep(4)
    controles(player1)
    Noches(player1)

def Noches(player1):
    countn = 1
    reproducir_main()
    
    Nocheobj = Noche1(entrada=0, banos=0, barra=0, generalmesas=0, vip=0, administracion=0,
                  fotos=0, backstage=0, dj=0,
                  entradanum=0, banosnum=0, barranum=0, generalmesasnum=0, vipnum=0,
                  administracionnum=0, fotosnum=0, backstagenum=0, djnum=0)

    Nocheobj.random_lugar()
    countn=+1
    limpiar_consola()
    noche1(player1, Nocheobj)
    return


class Noche1:
    def __init__(self, entrada, banos, barra, generalmesas, vip, administracion, fotos, backstage, dj,
                 entradanum, banosnum, barranum, generalmesasnum, vipnum, administracionnum, fotosnum, backstagenum, djnum):
        self.entrada = entrada
        self.banos = banos
        self.barra = barra
        self.generalmesas = generalmesas
        self.vip = vip
        self.administracion = administracion
        self.fotos = fotos
        self.backstage = backstage
        self.dj = dj
        self.entradanum = entradanum
        self.banosnum = banosnum
        self.barranum = barranum
        self.generalmesasnum = generalmesasnum
        self.vipnum = vipnum
        self.administracionnum = administracionnum
        self.fotosnum = fotosnum
        self.backstagenum = backstagenum
        self.djnum = djnum


    def random_lugar(self):
        numrand = random.randint(1, 3)
        if numrand == 1:
            numrandpor = random.randint(2, 4)
            numrandpor2 = random.randint(2, 4)
            self.entrada = f"La oscura entrada del antro revela una noche solitaria. En la fila, {numrandpor} hombres y {numrandpor2} mujeres esperan impacientes. Luces parpadeantes iluminan atuendos diversos, desde elegantes trajes hasta atuendos relajados."
            self.entradanum = numrand
        elif numrand == 2:
            self.entrada = "La noche se presenta sin sorpresas en el antro. La fila está compuesta por habituales hombres y mujeres. Luces suaves iluminan atuendos cotidianos. Como guardia, tu mirada revela una noche tranquila y sin complicaciones."
            self.entradanum = numrand
        elif numrand == 3:
            self.entrada = "La fila se extiende, indicando una noche concurrida. Luces parpadeantes iluminan a hombres y mujeres ansiosos. Conversaciones bulliciosas llenan el aire. Atuendos diversos reflejan la mezcla de estilos. Como guardia, sientes la presión de una noche más agitada."
            self.entradanum = numrand

        numrand1 = random.randint(1, 3)
        if numrand1 == 1:
            self.banos = "Una sorpresa desagradable espera en uno de los inodoros: alguien dejó una mierda gigante. El olor es suficiente razón para salir rápidamente de allí."
            self.banosnum = numrand1
        elif numrand1 == 2:
            self.banos = "Una bocanada de alivio te envuelve al entrar a los baños. Hoy es uno de esos raros días en los que no encuentras ningún rastro de desorden. La atmósfera es fresca, y la ausencia de problemas te llena de alegría. Un respiro bienvenido en medio del caos del antro."
            self.banosnum = numrand1
        elif numrand1 == 3:
            self.banos = "El baño no ofrece sorpresas; está como siempre, sucio y asqueroso. La desesperanza se cierne en el aire, ya que parece que no hay nada que puedas hacer para mejorar la situación. La sensación de impotencia te envuelve mientras enfrentas la cruda realidad de un espacio descuidado."
            self.banosnum = numrand1

        numrand2 = random.randint(1, 3)
        if numrand2 == 1:
            self.barra = "Hoy, la barra brilla con la presencia de lindas mujeres, creando un ambiente animado. Aunque la idea de disfrutar sin trabajar es tentadora, el agotamiento acumulado te recuerda la imposibilidad de escapar de tus responsabilidades como guardia."
            self.barranum = numrand2
        elif numrand2 == 2:
            self.barra = "Hoy, la barra está llena solo de hombres, dando al lugar una sensación monótona y deslucida. La experiencia en este antro asqueroso no cumple con las expectativas."
            self.barranum = numrand2
        elif numrand2 == 3:
            self.barra = "La barra rebosa de gente animada. Un coro de risas y conversaciones llena el aire. El deseo de tomarte un shot se intensifica, pero las responsabilidades como guardia lo impiden."
            self.barranum = numrand2

        numrand3 = random.randint(1, 3)
        if numrand3 == 1:
            self.generalmesas = "Un vistazo a la pista de baile revela una escena desoladora. La falta de movimiento y risas crea un ambiente similar al de un cementerio, con la ausencia de gente que normalmente daría vida a este espacio. La música resuena en un vacío, destacando la extraña quietud que envuelve la pista en esta noche."
            self.generalmesasnum = numrand3
        elif numrand3 == 2:
            self.generalmesas = "La atmósfera aquí es contagiosamente animada, con risas y la vibrante energía de la multitud. La tentación de sumergirse en esta bulliciosa escena te hace desear ser un nini, dejando atrás las responsabilidades para disfrutar plenamente del ambiente festivo."
            self.generalmesasnum = numrand3
        elif numrand3 == 3:
            self.generalmesas = "La observación revela un cambio en la dinámica: hoy, las mujeres parecen llegar con una energía festiva palpable. Su presencia promete animar la atmósfera y añadir un toque especial a la noche."
            self.generalmesasnum = numrand3

        numrand4 = random.randint(1, 3)
        if numrand4 == 1:
            self.vip = "Al observar el área VIP, la sensación de envidia se filtra. La gente allí parece tener la vida resuelta, disfrutando de lujos y comodidades que crean un aura de privilegio."
            self.vipnum = numrand4
        elif numrand4 == 2:
            self.vip = "La atmósfera del VIP irradia diversión y exclusividad. Desde la distancia, se percibe que la gente está teniendo un tiempo increíble, sumergida en una fiesta que parece estar en su propia dimensión de alegría y emoción."
            self.vipnum = numrand4
        elif numrand4 == 3:
            self.vip = "La vista al área VIP revela una impresión desfavorable. Las personas allí se ven odiosas, creando una atmósfera que aleja a cualquiera de querer compartir su espacio. La exclusividad parece venir con una dosis de actitud indeseable."
            self.vipnum = numrand4

        numrand5 = random.randint(1, 3)
        if numrand5 == 1:
            self.administracion = "Un saludo en la zona de administración confirma la soledad de Christopher. La sensación de estar solo en este espacio destinado a la gestión parece indicar que es mejor dejarlo en paz para que continúe con sus tareas."
            self.administracionnum = numrand5
        elif numrand5 == 2:
            self.administracion = "La escena en el área de administración revela un lugar vacío y silencioso. La ausencia de personas sugiere que hoy no hay nadie trabajando en este espacio, creando una sensación de tranquilidad inusual."
            self.administracionnum = numrand5
        elif numrand5 == 3:
            self.administracion = "Observando a la gente en este lugar, se percibe un aura de estrés que flota en el ambiente. Esta impresión refuerza la preferencia por tu rol como guardia, donde la presión puede ser diferente pero, al menos, conocida y manejable."
            self.administracionnum = numrand5

        numrand6 = random.randint(1, 3)
        if numrand6 == 1:
            self.fotos = "En un rincón, dos chicas capturan el momento tomándose fotos. La situación sugiere que solo se permite el paso de una persona a la vez, debería de hacer algo..."
            self.fotosnum = numrand6
        elif numrand6 == 2:
            self.fotos = "Una mirada a las fotos revela la presencia de un individuo que emana una actitud presumida en su imagen. La idea de que debería llamársele la atención flota en el aire, sugiriendo que su comportamiento puede no ser del agrado de todos."
            self.fotosnum = numrand6
        elif numrand6 == 3:
            self.fotos = "En una esquina, dos chicos se toman fotos, agregando una dosis juvenil al ambiente. La limitación de pasar uno por uno sugiere que el espacio está destinado a momentos individuales y no a multitudes."
            self.fotosnum = numrand6

        numrand7 = random.randint(1, 3)
        if numrand7 == 1:
            self.backstage = "Un vistazo al backstage revela una escena inquietante: el DJ parece estar consumiendo sustancias ilegales por la nariz. La situación plantea interrogantes sobre el trasfondo del evento y la conducta del personal detrás del escenario."
            self.backstagenum = numrand7
        elif numrand7 == 2:
            self.backstage = "Al observar el backstage, se nota una escena inusual: el DJ parece estar llorando. La emotividad de la situación añade un toque de melancolía, generando preguntas sobre qué podría estar sucediendo detrás de las cortinas del evento."
            self.backstagenum = numrand7
        elif numrand7 == 3:
            self.backstage = "La visión en el backstage revela una escena preocupante: el DJ yace en el suelo. La urgencia de ayudarlo se hace evidente, planteando interrogantes sobre su bienestar y generando la necesidad de intervenir."
            self.backstagenum = numrand7

        numrand8 = random.randint(1, 3)
        if numrand8 == 1:
            self.dj = f"La escena en el escenario revela una fiesta en pleno apogeo: el DJ tiene a cuatro chicas subidas a la plataforma. La dinámica festiva añade un toque de energía, sugiriendo que el DJ ha logrado involucrar a la audiencia de una manera única."
            self.djnum = numrand8
        elif numrand8 == 2:
            self.dj = "Una evaluación de la actuación del DJ sugiere que algo no está yendo bien. La falta de un rendimiento sólido puede generar inquietud en el ambiente, dejando preguntas sobre cómo afectará esto la experiencia de la audiencia."
            self.djnum = numrand8
        elif numrand8 == 3:
            self.dj = "Una observación en la barra del DJ revela una situación peculiar: dos individuos han subido al escenario. La escena añade una capa de intriga, planteando preguntas sobre su presencia y cómo podría afectar la dinámica del espectáculo."
            self.djnum = numrand8
        return


class Player1:
    def __init__(self, nombre, skin, atractivo, labia, dinero, fuerza, inteligencia, lugar, inventario):
        self.nombre = nombre
        self.skin = skin
        self.atractivo = atractivo
        self.labia = labia
        self.dinero = dinero
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.lugar = lugar
        self.inventario = inventario

    def elegir_personaje(self):
        limpiar_consola()
        print(self.skin)
        print(f"\nEstadísticas de {self.nombre}:")
        print(f"Atractivo: {self.atractivo}")
        print(f"Labia: {self.labia}")
        print(f"Dinero: {self.dinero}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        oracion = input("Quieres elegir este personaje? No podras cambiarlo durante la partida...")
        limpiar_consola()
        if (contiene_si(oracion)):
            aceptado(self)
        self.elegir_deci()


    def elegir_deci(self):
        print("--Elige tu personaje--\n")
        print("*Escribe un nombre para ver sus estadisticas y su skin\n")
        print("Marco Calvillo")
        print("Samir Marquez")
        print("Isaac Arriaga")
        print("Jose Cerna")
        oracion = input("")
        if(contiene_jose(oracion)):
            self.nombre = "Jose Cerna"
            self.skin = '''                                                                                                                            
                                  *%%%%%%%%%%.                                  
                               %#####%%%  ## %* #                               
                             ########%%%  #, (#%%%%%%%%%                        
                            #########%%%%%(%%&&&%%%%%%%%%                       
                           #########%%%%%&&&&&&&&&%%%%%%                        
                          (####%#%%%%%&&%(((///%@@&%%%%                         
                          #####%%%%%((////*******@@@&                           
                         #%#%%%%&@@(/,. ## &  ##    ...                          
                        #%%%%&((&%(&         .   ...,,,                         
                        .%%%%(**, %%        ..,,****,                           
                          %&&      .........,****,                              
                              *&&@&%/*** .//**/%.                               
                                     %####%%%%%%%%%                             
                                      %%&&%%&&&&%&/,                            
                                     .((((((((((####                            
                                     ((((((((((#####.                           
                                     #((((######%%%,                            
                                        *#/ (//*                                
                                       .,/##(//////(                            
                                 /**///((* *      .,                            
                                                                   '''
            self.atractivo = 7
            self.labia = 2
            self.dinero = 6
            self.fuerza = 3
            self. inteligencia = 9
            self.elegir_personaje()
        if(contiene_marco(oracion)):
            self.nombre = "Marco Calvillo"
            self.skin = '''                                                
                        ,...,,,,,,.,.                                           
                 ..  ..**###/((#(((//****,.    ,(%                              
                ,...,/#%%%%&%%%%##########*(  /###%@@@@..                       
                ,,,,,//((##%             /       ..,(%&@@. .                    
                .,,,,,**,..*(            .,     .,,*/(#@@@*.      .             
                 ,,,**,,. .,*/(        .  .*. *(%##*##%&@@%,.       ..,         
                  **,,*....**/#(      .     .((/*(%##%&#@%#  .         ./       
                   */(/,.,,*/#%(//         ,#%#,**/##%&%      .      ./#((      
                     ((/,,,/(%,..,,/  . . ,*(&**(###%#&%.     .     ,##((,      
                       //,,/(   .,*/(* . . .**((###( *         .  ,/(###,       
                        .,//    .,,/(    ((#####%%*            .,,*(##(         
                         ...    .,*/.   .*/(((##%% ...   .    ..,/((((          
                          ..   ..,,/. ......,/#.     ......  .,*((((/           
                        ...........*,....,*.       .*..,**,.,*/(((/             
                        ...........,,. .      ...,,/(**/((*,/((/.               
                          .......... ...  ...,,*/((##//**((/(/*                 
                          *.......     ...,,**/####*..,*/((/*                   
                         ......... .....,,,*/(####*.,*/((/                      
                       .......,,.......,**%%#%##%*,**((((                       
                      .......,/*,....,,*/((#####/*,*/(((                        
                      ....,,,,,..,,,,**///////*****((((                         
                      ....   .    ...,**((////////(#(,                          
                      ........   ...,,,*/((####((##(                            
                     .......... ...,,*,**/(#%%####(                             
                      ...........,***/((#####%%##                               
                     .... .....,*//(((#####%%%##                                
                    ......... ...,*****,*/(##%#                                 
                   ............,**,...,,,,**/((                                 
                   .,,...*,..........,,,*//((#(                                 
                  ,,,,,,.......,,,,,,***/(((##/                                 
                  ,,,,,,,,,,,,,**,**/((#(#####.                                 
                 (#&/**,,*,,,,***/(####&%@@&@%                                  
                ##&&&%&%&#&#&%&&%&&(@&&@&&#&&&&                                 
               /%@%%&&#&@@@&&&@&%&&#&@#&%%&&@%%(                                
              ,%%#%#@%(%##%#&%&%%%#&##&%%&#&%&&/                                '''
            self.atractivo = 6
            self.labia = 7
            self.dinero = 5
            self.fuerza = 9
            self. inteligencia = 4
            self.elegir_personaje()
        if(contiene_isaac(oracion)):
            self.nombre = "Isaac Arriaga"
            self.skin = '''                                                                                
                                    %,....%                                     
                                   .......,%                                    
                                   %.....,,%                                    
                                     (%%%%                                      
                               %%%%%%%%%%%%%%%%%                                
                              %//////////////////%                              
                            %*////////////////////%                             
                           .///////////////////////%                            
                          %/////%%///////////%%//////%                          
                        %//////% %///////////% %//////%                         
                       %//////%  %///////////%   %/%%%%%%%%                     
                      %%%///%    %///////////%    %///%%%/%                     
                      .%...%     %....,%....,#     %%..%%/%                     
                                 %....,%....,#          %/%                     
                                 %....,%....,#     %////%/%                     
                                 %....,%....,#          %/%                     
                                 %....,%....,#          %/%                     
                                 %....,%%%%%%%          %/%                     
                                 %....,%     #          %/%                     
                                 %....,%   ..%          %/%                     
                                 %....,%                %/%                     
                                 %....,%                %/%                     
                                 %....,%                %/%                     
                                 %////(%                %/%                     
                                  %%%%%                 %/%                     '''
            self.atractivo = 2
            self.labia = 7
            self.dinero = 1
            self.fuerza = 5
            self. inteligencia = 7
            self.elegir_personaje()
        if(contiene_samir(oracion)):
            self.nombre = "Samir Marquez"
            self.skin = '''    *(/(///(/((##/#/,                              
                          .*((%#%#%#&#((&%%#%%#%%(#%/*,,,                       
       .              .//#//(%/##%(%%#%##%&%#%%%(%%#%(*(((/..                   
                     */(,**/##(###%%###%%&%&&&%%&%%##(&#%(((//.                 
                  ,,*//%*((/*(////(#%%%%%%%%##%%%%%%&%%%(#%(/(/*.               
                ,*////**////,,,,.,*(*#%&&%%#(#/(%#####(####**(((**,             
               ,,/*%**((/**,*,,...,**//#%%%#*/,.*##/(#(///*(*/((/*/,,           
              ,//,((#//*,,.,.,......*,,*((//*,,.,,**//,*,****(*/////*.          
             ,,*(/((**,,,.,.............,****,........*/**,/(*(/.*,/(/          
             ,.(((/*,,,,..........,......,,,.,......,*..,*/,*/##(/*/(#.         
             *.(#/*,,,,,..................,,,,.,...........,,*/#%#*,((          
             ,.((/*,,,,,*,,....,,..... ...........,,,,*****/*,**###/#(          
              ,,//,,.,*//,............ . .   ..............,,/(*/%%((           
              ,./(,.,,...................... .......,,.,,,...,**,##//           
              ,./,,.,.,..,,*////*,,,,,.. ........,,*,..,.,,,,,****(*,           
        . ..,*/.*..,,,,,,,%#(&&&(/,*,,,......,,,,,*,%&%%,##/,,,,*,***,((        
          ***,*,,...,,**/*,.%&@&#../.,,.........,,.,%@&%/.,**,,,,,,***//,       
          ,/,,,,.........,*,,,,.,.....,,..............,,..,,....,,,*,*,/,       
           ,,,*,.....................,,.........................,,,/**/.        
            *,/,. ...................,,......,,... .............,*./*,,         
             *,,**..................,*,.......,,...  .........,.,*,,**          
              ,,,,.............   .,............,.  ..........,,,,,,,           
               ,,,...,........    .,,./(*,,*,/,,,.  .........,,,,,*             
                   ...,,,.......... ..... . ..............,,,,,,,      .        
         . .        ....,,.................. ............,,,,,,,,               
                    ..,,,,,,..........,,**.**,,........,,,,,*,*,  .             
                      .,,,,,,,....,./(#%&@@@&&&(/,,,..,,,,,,**,                 
    .              *,/.,,,,,,,,,,,*/#@@%##%%##&&&(*,.,,,,,,*** .                
                 (#(#&&,,,,,,,,,,,,,/%%@#/,*/#@@#*,,,,,,,**,*@%%,               
                //,,##%&*,,,,,,,.,,,,*/##@##%@#/*,,,.,,,*,,*@(*#(#              
              .(/(#/#(///&/,,,,,,..,,*//*//*/,,//,,.,,**,,%%%%&#%%#             
             ./#*/%&#(#%%*/@/***,,,,,*///**///(*,.,,,**,*,./(#&##,(/            
###((####%/**#/#%#%%(**%@%&&%%&//*,,,,..........,,,**,*#%(((%%**.,#(*%&&((/#((##
%//&%%(#%/*(,(#,(#/*&%,(#*%&%%&%%%/*,,,,.......,,**,(/(/%#%%&&%%%##%#,%#%/(/(#%&
.,##/ ((%%&*.#/*(#&%//#.*&@%(/%&#&%@%***,,,,*,**/&@%%#.,(##&%&&&##*##,#&&%#//,%%
 ,##.,/,*#(%##&%%,,#.(,(%##&##(#(#,./*,**//(*/%(%%(&@@@@#%#&%&#%%&%,/.,%,,..,,%.
(%,*/#,(%#%%%%&&&&%&&%*%&%%,(*.*,.%%%/*,/(**%(#//#%%%&%&@@@/.%../#(#/,#*..,/(.%(
(#/,..,*.*./,#((%.,,.* *%&#*/.(*#&%%%&.#&%&#&%%###&%%%%&&&&&#&%&@%/###%#,#(,.#@%
. .,  ,**.*/,.%(./../. ,,*#,(/,/ &%&,.%&%// .,(. %#%##%&(.%###.#...*(.,#,..((*,,'''
            self.atractivo = 5
            self.labia = 3
            self.dinero = 7
            self.fuerza = 3
            self. inteligencia = 8
            self.elegir_personaje()
        print("ESE PERSONAJE NO EXISTE, elige otro :)")
        self.elegir_deci()
        

    def mostrar_estadisticas(self):
        limpiar_consola()
        print(f"\nEstadísticas de {self.nombre}:")
        print(f"Atractivo: {self.atractivo}")
        print(f"Labia: {self.labia}")
        print(f"Dinero: {self.dinero}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Lugar: {self.lugar}")
    
    def pregunta_random(self, count):
        preguntas_realizadas = []
        
        while count < 3:  # Modificado para que se realicen preguntas hasta que count sea 3
            numrand = random.randint(1, 9)
            
            # Verificar si la pregunta ya se hizo
            if numrand in preguntas_realizadas:
                continue

            preguntas_realizadas.append(numrand)

            if numrand == 1:
                res = input("¿Tienes experiencia previa en seguridad?\n")
                if contiene_si(res):
                    self.fuerza += 1
                    count += 1

            elif numrand == 2:
                res = input("¿Está familiarizado con el uso de sistemas de vigilancia y cámaras de seguridad?\n")
                if contiene_si(res):
                    self.inteligencia += 1
                    count += 1

            elif numrand == 3:
                res = input("¿Posee entrenamiento en primeros auxilios?\n")
                if contiene_si(res):
                    self.inteligencia += 1
                    count += 1

            elif numrand == 4:
                res = input("¿Está dispuesto a trabajar en turnos nocturnos y fines de semana?\n")
                if contiene_si(res):
                    self.labia += 1
                    count += 1

            elif numrand == 5:
                res = input("¿Tiene conocimientos en el uso de equipo de seguridad, como detectores de metales?\n")
                if contiene_si(res):
                    self.atractivo -= 1
                    count += 1

            elif numrand == 6:
                res = input("¿Puede seguir procedimientos y protocolos establecidos en caso de emergencias?\n")
                if contiene_si(res):
                    self.atractivo -= 1
                    count += 1

            elif numrand == 7:
                res = input("¿Está dispuesto a someterse a pruebas de drogas y verificación de antecedentes?\n")
                if contiene_si(res):
                    self.atractivo += 1
                    count += 1

            elif numrand == 8:
                res = input("¿Tiene habilidades de comunicación efectiva para tratar con el personal y los clientes?\n")
                if contiene_si(res):
                    self.atractivo -= 1
                    count += 1
                    self.labia -= 1

            elif numrand == 9:
                res = input("¿Puede mantener la confidencialidad en situaciones sensibles?\n")
                if contiene_si(res):
                    self.inteligencia += 1
                    count += 1
        if(count>3):
                time.sleep(1)
                print(f"\n Felicidades, NO ENTRASTE AL EQUIPO, favor de retirarte...\n Te acuchillaron al salir de la entrevista. \n FIN, BAD ENDING")
                time.sleep(4)
                sys.exit()
        return

def intro():
    
    limpiar_consola()
    print(''' ___    _      _   _  ___       ___    _   _  _____         ___    _____  ___    _   _  ___   
(  _`\ ( )    ( ) ( )(  _`\    (  _`\ ( ) ( )(  _  )/'\_/`\(  _`\ (  _  )(  _`\ ( ) ( )(  _`\ 
| ( (_)| |    | | | || (_) )   | ( (_)| |_| || (_) ||     || |_) )| (_) || ( (_)| `\| || (_(_)
| |  _ | |  _ | | | ||  _ <'   | |  _ |  _  ||  _  || (_) || ,__/'|  _  || |___ | , ` ||  _)_ 
| (_( )| |_( )| (_) || (_) )   | (_( )| | | || | | || | | || |    | | | || (_, )| |`\ || (_( )
(____/'(____/'(_____)(____/'   (____/'(_) (_)(_) (_)(_) (_)(_)    (_) (_)(____/'(_) (_)(____/'
    ''')
    reproducir_intro()
    input("Presiona ENTER para comenzar.")
    player1 = Player1(nombre="None", skin = 0, atractivo=0, labia=0, dinero=0, fuerza=0, inteligencia=0, lugar=0, inventario={})
    pygame.mixer.music.stop()
    limpiar_consola()
    print("Hola.")
    time.sleep(1)
    limpiar_consola()
    print("Hola..")
    time.sleep(0.5)
    limpiar_consola()
    print("Hola...")
    time.sleep(0.5)
    limpiar_consola()
    print("Bienvenido a la entrevista para poder ser guardia")
    print("de seguridad del 'Club Champagne', el antro más prestigioso de Aguascalientes.")
    time.sleep(4)
    print("Primero, comenzaremos con tu nombre.\n")
    time.sleep(2)
    print("Como te llamas?\n")
    player1.elegir_deci()

def controles(player1):
    limpiar_consola()
    print(f"\n ----------INDICACIONES----------")
    print(f"\n - Cada noche tendras que vigilar la entrada e instalaciones del antro, tendras que")
    print(f"\n estar en 3 eventos por noche, tienes 5 horas(5 minutos en la vida real)")
    print(f"\n para hacerlo, de lo contrario seras despedido y no obtendras ninguna paga por ningun dia trabajado.")
    print(f"\n ")
    print(f"\n ----------CONTROLES----------\n")
    print(f' - Puedes usar "VER" para saber lo que esta pasando a tu alrededor, te recomendamos usarlo despues de moverte de posicion.\n')
    print(f' - Puedes usar "MOVER" para elegir donde moverte hacia las direcciones posibles.\n')
    print(f' - Puedes usar "HABLAR" para poder hablar con las personas que se encuentren cerca de la zona.\n')
    print(f' - Puedes usar "CONTROLES" para poder ver la ventana de controles e indicaciones \n')
    input(f'Presiona enter para iniciar el juego y adentrarte en tu mision, recuerda, tienes 5 minutos.\n')
    Noches(player1)
    return
     
def perder():
    input(f'Presiona enter.\n')
    limpiar_consola()
    print("PERDISTE!")
    perder()


def final(player1, Nocheobj):
    global eventos
    global equilibrio
    limpiar_consola()
    if equilibrio == 0:
        imprimir_letra_por_letra("Terminas la noche con un equilibrio neutral. Aunque no hubo grandes problemas, tampoco destacaste en resolver situaciones críticas. El antro sigue funcionando, pero tu impacto fue limitado.")
        imprimir_letra_por_letra("Al final de la noche, te retiras del antro reflexionando sobre las decisiones que tomaste y cómo podrías mejorar en el futuro.")

    elif equilibrio > 0:
        imprimir_letra_por_letra("¡Felicidades! Has mantenido un buen equilibrio durante toda la noche. Tu habilidad para tomar decisiones ha contribuido a un ambiente positivo en el antro.")
        imprimir_letra_por_letra("Los clientes están contentos, el personal te agradece y, al final de la noche, el jefe te felicita por tu desempeño. Tu reputación como guardia de seguridad sigue creciendo.")
        
    elif equilibrio < 0:
        imprimir_letra_por_letra("La noche termina con un equilibrio negativo. Las decisiones tomadas han generado más problemas de los que resolviste, y el antro enfrenta desafíos crecientes.")
        imprimir_letra_por_letra("Al final de la noche, el jefe te hace saber su insatisfacción y considera tomar medidas. Tu reputación como guardia de seguridad puede verse afectada negativamente.")
    respuesta = input()
    final(player1, Nocheobj)


def eleccion(player1, Nocheobj):
    global eventos
    global equilibrio
    if(eventos==3):
        final(player1, Nocheobj)
    respuestaon = False
    while(not respuestaon):
        respuesta = input("")
        if(respuesta=="ver"):
            ver(player1, Nocheobj)
        elif(respuesta=="mover"):
            mover(player1, Nocheobj)
        elif(respuesta=="hablar"):
            hablar(player1, Nocheobj)
        elif(respuesta=="controles"):
            controles(player1)
        else: imprimir_letra_por_letra("\nNo puedes hacer eso ahora...")


def ver(player1, Nocheobj):
    global eventos
    global equilibrio
    if(player1.lugar == "entrada"):
        imprimir_letra_por_letra(Nocheobj.entrada + "\n")
    if(player1.lugar == "banos"):
        imprimir_letra_por_letra(Nocheobj.banos + "\n")
    if(player1.lugar == "barra"):
        imprimir_letra_por_letra(Nocheobj.barra + "\n")
    if(player1.lugar == "generalmesas"):
        imprimir_letra_por_letra(Nocheobj.generalmesas + "\n")
    if(player1.lugar == "vip"):
        imprimir_letra_por_letra(Nocheobj.vip + "\n")
    if(player1.lugar == "administracion"):
        imprimir_letra_por_letra(Nocheobj.administracion + "\n")
    if(player1.lugar == "fotos"):
        imprimir_letra_por_letra(Nocheobj.fotos + "\n")
    if(player1.lugar == "backstage"):
        imprimir_letra_por_letra(Nocheobj.backstage + "\n")
    if(player1.lugar == "dj"):
        imprimir_letra_por_letra(Nocheobj.dj + "\n")
    return

def mover(player1, Nocheobj):
    global eventos
    global equilibrio
    imprimir_letra_por_letra("\nA donde te quieres mover? (Lugares del antro segun el mapa: Entrada, Banos, Generalmesas, Vip, Barra, Administracion, Fotos, Dj y Backstage.)")
    respuesta = input("").lower()

    if respuesta == player1.lugar:
        imprimir_letra_por_letra("\nYa estás en ese lugar...")
        eleccion(player1, Nocheobj)

    if respuesta == "entrada":
        if player1.lugar in ["banos", "generalmesas", "vip"]:
            imprimir_letra_por_letra("\nTe moviste a la entrada.")
            player1.lugar = "entrada"
            eleccion(player1, Nocheobj)
        else:
            imprimir_letra_por_letra("\nNo te puedes mover a ese lugar...")
    elif respuesta == "banos":
        if player1.lugar in ["entrada", "barra"]:
            imprimir_letra_por_letra("\nTe moviste a los baños.")
            player1.lugar = "banos"
        else:
            imprimir_letra_por_letra("\nNo te puedes mover a ese lugar...")
    elif respuesta == "barra":
        if player1.lugar in ["administracion", "generalmesas", "banos"]:
            imprimir_letra_por_letra("\nTe moviste a la barra.")
            player1.lugar = "barra"
        else:
            imprimir_letra_por_letra("\nNo te puedes mover a ese lugar...")
    elif respuesta == "generalmesas":
        if player1.lugar in ["vip", "entrada", "barra", "fotos"]:
            imprimir_letra_por_letra("\nTe moviste a las mesas de general.")
            player1.lugar = "generalmesas"
        else:
            imprimir_letra_por_letra("\nNo te puedes mover a ese lugar...")
    elif respuesta == "vip":
        if player1.lugar in ["dj", "entrada", "generalmesas"]:
            imprimir_letra_por_letra("\nTe moviste al VIP.")
            player1.lugar = "vip"
        else:
            imprimir_letra_por_letra("\nNo te puedes mover a ese lugar...")
    elif respuesta == "administracion":
        if player1.lugar in ["fotos", "barra"]:
            imprimir_letra_por_letra("\nTe moviste a la administración.")
            player1.lugar = "administracion"
        else:
            imprimir_letra_por_letra("\nNo te puedes mover a ese lugar...")
    elif respuesta == "fotos":
        if player1.lugar in ["dj", "administracion", "generalmesas"]:
            imprimir_letra_por_letra("\nTe moviste a la zona de fotos.")
            player1.lugar = "fotos"
        else:
            imprimir_letra_por_letra("\nNo te puedes mover a ese lugar...")
    elif respuesta == "backstage":
        if player1.lugar == "dj":
            imprimir_letra_por_letra("\nTe moviste al backstage.")
            player1.lugar = "backstage"
        else:
            imprimir_letra_por_letra("\nNo te puedes mover a ese lugar...")
    elif respuesta == "dj":
        if player1.lugar in ["vip", "backstage", "fotos"]:
            imprimir_letra_por_letra("\nTe moviste a la zona del DJ.")
            player1.lugar = "dj"
        else:
            imprimir_letra_por_letra("\nNo te puedes mover a ese lugar...")
    else:
        imprimir_letra_por_letra("\nEse lugar no existe...")

    eleccion(player1, Nocheobj)

def hablar(player1, Nocheobj):
    global eventos
    global equilibrio
    if player1.lugar == "entrada":
        if Nocheobj.entradanum == 1:
            imprimir_letra_por_letra("\nLa gente parece no notar tu presencia y te ignoran...")
            eleccion(player1, Nocheobj)
        elif Nocheobj.entradanum == 2:
            imprimir_letra_por_letra("\nNo eres lo suficientemente atractivo para que la gente te tome enserio, te ignoran todos en la fila...")
            eleccion(player1, Nocheobj)
        elif Nocheobj.entradanum == 3:
            imprimir_letra_por_letra("\nHay tanta gente en el lugar, intentas hablar pero el ruido del ambiente silencia tus palabras, nadie te escucha...")
            eleccion(player1, Nocheobj)
    elif player1.lugar == "banos":
        if Nocheobj.banosnum == 1:
            imprimir_letra_por_letra("\nA quien piensas hablarle? No hay nadie en esta habitacion, a menos que quieras hablar con la mierda... O incluso agarrala...")
            eleccion(player1, Nocheobj)
        elif Nocheobj.banosnum == 2:
            imprimir_letra_por_letra("\nA quien piensas hablarle? No hay nadie en esta habitacion...")
            eleccion(player1, Nocheobj)
        elif Nocheobj.banosnum == 3:
            imprimir_letra_por_letra("A quien piensas hablarle? No hay nadie en esta habitacion...")
            eleccion(player1, Nocheobj)
    elif player1.lugar == "barra":
        if Nocheobj.barranum == 1:
            imprimir_letra_por_letra("Te acercas a una mujer solitaria posada en la barra, a pesar de su belleza y gran confianza que se tiene en si misma, te armas de valor y decides hablarle.")
            imprimir_letra_por_letra(player1.nombre + ": Hola linda, como te llamas?")
            if(player1.atractivo + player1.labia < 10):
                imprimir_letra_por_letra("Mujer: No me hables porfavor, prefiriria salir con shrek que con un horrible hombre como tu.\n")
                imprimir_letra_por_letra("Avergonzado y triste, te pones nervioso, dejas que tus emociones te sobrepasen y piensas en que la mujer fue grosera contigo, quieres sacarla del antro? (si/no)")
                respuesta = input().lower()
                if(respuesta =="si"):
                    imprimir_letra_por_letra("Agarras a la mujer desconocida por el brazo, la arrastras por todo el bar y la dejas tirada en la calle...")
                    equilibrio = equilibrio + 1
                    eventos += 1
                    eleccion(player1, Nocheobj)
                else:
                    imprimir_letra_por_letra("Aguitado y con ganas de no vivir, te alejas de la mujer...")
                    eventos += 1
                    equilibrio = equilibrio - 1
                    eleccion(player1, Nocheobj)
            else:
                imprimir_letra_por_letra("Diana: Hola, me llamo Diana, tu guapote como te llamas?")
                imprimir_letra_por_letra(player1.nombre + ": Me llamo" + player1.nombre + ", Mucho gusto princesa, queria saber si podrias darme tu numero, ya sabes, para cuando salga de aca, vernos?")
                imprimir_letra_por_letra("Diana: Claro guapote, aqui esta mi numero...")
                imprimir_letra_por_letra("Diana te entrega su numero, lo agarras y lo metes en tu bolsillo... Te retiras de la mesa...")
                equilibrio = equilibrio - 1
                eventos += 1
                eleccion(player1, Nocheobj)
        elif Nocheobj.barranum == 2:
            imprimir_letra_por_letra("Te acercas a una hombre sentado en un silla de una mesa central del antro.")
            imprimir_letra_por_letra(player1.nombre + ": Hola guapote, que haces aqui sentado tan solitario...")
            imprimir_letra_por_letra("El hombre se levanta y procede a intentar tirarte un golpe.")
            if(player1.fuerza > 5):
                imprimir_letra_por_letra("Esquivas el golpe y le metes un vergazote al cabron, lo levantas y lo sacas del bar.")
                equilibrio = equilibrio + 1
                eventos += 1
                eleccion(player1, Nocheobj)
            else:
                imprimir_letra_por_letra("Eres menos fuerte que el, su golpe hace contacto con tu cabeza, caes al suelo desangrandote, empiezas lentamente a ver la luz, y........ pierdes")
                perder()
        elif Nocheobj.barranum == 3:
            imprimir_letra_por_letra("Te acercas a una hombre sentado en un silla dela barra del antro.")
            imprimir_letra_por_letra("Te tomas un shot y le hablas al sujeto de al lado")
            imprimir_letra_por_letra(player1.nombre + ": Hoy la noche esta como para celebrarse, que tal estas hombre?")
            imprimir_letra_por_letra("Hombre Desconocido: Increible brother, hoy la noche esta super animada. Oye, me caiste bien, aqui entre nos, no quieres un poco de co###na?")
            respuesta = input().lower()
            if(respuesta == "si"):
                imprimir_letra_por_letra("Te acercas al hombre desconocido, el saca una pequena bolsa con un polvo blanco, la vierte en la mesa, te acercas y la espiras...")
                imprimir_letra_por_letra("Te sientes mareado pero al mismo tiempo con mucha adrenalina, le agradeces al sujeto y te alejas de el...")
                player1.fuerza = player1.fuerza + 1
                player1.intelgencia = player1.inteligencia -2
                equilibrio = equilibrio - 1
                eventos += 1
                eleccion(player1, Nocheobj)
            else: 
                imprimir_letra_por_letra("Agarras al hombre desconocido por el brazo, lo arrastras por todo el bar y lo dejas tirado en la calle...")
                eleccion(player1, Nocheobj)
    elif player1.lugar == "vip":
        if Nocheobj.vipnum == 1:
            imprimir_letra_por_letra(player1.nombre + ": Hola senores, necesitan de algo o hay algo que pueda hacer por ustedes el dia de hoy?")
            imprimir_letra_por_letra("Hombre VIP1: ???, perdon, me estas hablando a mi? Que poco respeto tienen estos sucios empleados para que me terminen hablando.")
            if(player1.fuerza + player1.dinero > 14):
                imprimir_letra_por_letra(player1.nombre + ": A ver cabron, a mi no me vas a estar faltando al respeto en mi trabajo, no me importa quien seas ni cuanto dinero tengas. Me respetas o te sales.")
                imprimir_letra_por_letra("Hombre VIP2: Mis amigos y yo hacemos lo que queremos, no vas a estar aqui diciendonos que hacer, o vas a hacer algo debilucho?")
                imprimir_letra_por_letra("Que quieres hacer? -)Pelear -)Disculparse")
                respuesta = input().lower
                if(respuesta=="pelear"):
                    if(player1.fuerza > 7):
                        imprimir_letra_por_letra("En un rincón del antro, la tensión aumenta. Tres hombres del VIP, aparentemente en desacuerdo, se enfrentan al guardia de seguridad. La pelea estalla, pero el guardia, con habilidades bien entrenadas, logra vencer a los tres individuos. Después de una serie de movimientos rápidos y precisos, el guardia logra controlar la situación. Con determinación, arroja a los agresores fuera del antro, restaurando la calma en el interior y demostrando su habilidad para mantener el orden.")
                        player1.fuerza = player1.fuerza + 1
                        equilibrio = equilibrio + 1
                        eventos += 1
                        eleccion(player1, Nocheobj)
                    else:
                        imprimir_letra_por_letra("En un rincón del antro, surge un enfrentamiento inesperado. Tres hombres del VIP desafían al guardia de seguridad, y a pesar de su valiente resistencia, se ven superados en número y habilidad. La pelea termina con el guardia siendo vencido, y los tres individuos se retiran, dejando una sensación de agitación en el aire y planteando interrogantes sobre la seguridad del lugar.")
                        perder()
            else: 
                imprimir_letra_por_letra(player1.nombre + ": Perdoneme senor, no pasa nada, los dejare aqui tranquilos, me retiro.")
                player1.inteligencia = player1.inteligencia + 1
                equilibrio = equilibrio - 1
                eventos += 1
                eleccion(player1 , Nocheobj)

        elif Nocheobj.vipnum == 2:
            imprimir_letra_por_letra("Te acercas a la mesa vip con mucha emocion, quieres hablar con la gente privilegiada de ahi, pero al acercarte a ellos te miran de manera fea, te sientes mal contigo mismo y mejor te alejas...")
        elif Nocheobj.vipnum == 3:
            imprimir_letra_por_letra("Enojado y con envidia por la gente que se encuentra en la zona vip, te acercas hacia la zona, despues de empezar tu paso, uno de los otros trabajadores te ve, se acerca a ti y te dice:")
            imprimir_letra_por_letra("Tony Trabajador: No vale la pena" + player1.nombre + ", no dejare que te acerques asi de enojado, no quiero problemas.")
            imprimir_letra_por_letra("Tony te llama la atencion, decides alejarte de la mesa vip...")
            equilibrio = equilibrio - 1
            eventos += 1
            eleccion(player1, Nocheobj)
    elif player1.lugar == "generalmesas":
        if Nocheobj.generalmesasnum == 1:
            imprimir_letra_por_letra("No hay nadie aqui, ni modo que le hables a la pared...")
            player1.inteligencia == player1.inteligencia - 1
            eleccion(player1, Nocheobj)
        elif Nocheobj.generalmesasnum == 2:
            imprimir_letra_por_letra("La musica y el ambiente estan tan llenos de ondas y emociones que no puedes hablar con nadie, nadie te escucha...")
            player1.inteligencia == player1.inteligencia + 1
            eleccion(player1, Nocheobj)
        elif Nocheobj.generalmesasnum == 3:
            imprimir_letra_por_letra("Te acercas a una mujer solitaria posada en una mesa, a pesar de su belleza y gran confianza que se tiene en si misma, te armas de valor y decides hablarle.")
            imprimir_letra_por_letra(player1.nombre + ": Hola linda, como te llamas?")
            if(player1.atractivo + player1.labia > 6):
                imprimir_letra_por_letra("Mujer: No me hables porfavor, prefiriria salir con shrek que con un horrible hombre como tu.\n")
                imprimir_letra_por_letra("Avergonzado y triste, te pones nervioso, dejas que tus emociones te sobrepasen y piensas en que la mujer fue grosera contigo, quieres sacarla del antro? (si/no)")
                respuesta = input().lower()
                if(respuesta =="si"):
                    imprimir_letra_por_letra("Agarras a la mujer desconocida por el brazo, la arrastras por todo el bar y la dejas tirada en la calle...")
                    equilibrio = equilibrio + 1
                    eventos += 1
                    eleccion(player1, Nocheobj)
                else:
                    imprimir_letra_por_letra("Aguitado y con ganas de no vivir, te alejas de la mujer...")
                    equilibrio = equilibrio - 1
                    eventos += 1
                    eleccion(player1, Nocheobj)
            else:
                imprimir_letra_por_letra("Andrea: Hola, me llamo Diana, tu guapote como te llamas?")
                imprimir_letra_por_letra(player1.nombre + ": Me llamo" + player1.nombre + ", Mucho gusto princesa, queria saber si podrias darme tu numero, ya sabes, para cuando salga de aca, vernos?")
                imprimir_letra_por_letra("Diana: Claro guapote, aqui esta mi numero...")
                imprimir_letra_por_letra("Andrea te entrega su numero, lo agarras y lo metes en tu bolsillo... Te retiras de la mesa...")
                equilibrio = equilibrio - 1
                eventos += 1
                eleccion(player1, Nocheobj)
    elif player1.lugar == "administracion":
        if Nocheobj.administracionnum == 1:
            imprimir_letra_por_letra(player1.nombre + ": Hola Cristopher, como estas brother? Te veo muy serio y desolado aqui, por cierto, Porque tienes las luces apagadas y tienes esa cara de enojado???")
            imprimir_letra_por_letra("Cristopher se acerca a ti, la luz alcanza su cara, puedes ver que ha estado llorando, se acerca a ti con un cuchillo, tienes que actuar rapido, que haces? (Correr/Pelear)")
            respuesta = input().lower()
            if (respuesta == "correr"):
                if(player1.inteligencia > 6):
                    imprimir_letra_por_letra("Esquivas el cuchillazo que te lanza cristopher, te haces para atras, cristopher se calma y vuelve a su asiento...")
                    eventos += 1
                    eleccion(player1, Nocheobj)
                else:
                    imprimir_letra_por_letra("El cuchillazo que te lanza cristopher te da directamente en el corazon, lo miras directamente y se rie de ti...")
                    perder()
            else:   
                if(player1.fuerza>8):
                    imprimir_letra_por_letra("Le metes un golpe bien metido al cristopher en la cabeza, cae al suelo, aliviado por su caida, comienzas a relajarte...")
                    eventos += 1
                    eleccion(player1, Nocheobj)
                else:  
                    imprimir_letra_por_letra("Le metes un golpe bien metido al cristopher en la cabeza, el ni se inmuta y admira tu valentia y decide dejarte vivir...")
                    player1.inteligencia = player1.inteligencia + 1
                    player1.fuerza = player1.fuerza + 1
                    eventos += 1
                    eleccion(player1, Nocheobj)
        elif Nocheobj.administracionnum == 2:
            imprimir_letra_por_letra("No hay nadie en esta habitacion, no le puede hablar a nadie bro...")
            eleccion(player1, Nocheobj)
        elif Nocheobj.administracionnum == 3:
            imprimir_letra_por_letra("Tienes demasiado miedo como para hablarle a alguien de la sala ya por la tension del ambiente.")
            eleccion(player1, Nocheobj)
    elif player1.lugar == "fotos":
        if Nocheobj.fotosnum == 1:
            imprimir_letra_por_letra(player1.nombre + ": Hola chicas, una disculpa, solo se puede una por una, no las dos a la vez.")
            imprimir_letra_por_letra("Mujer Desconocida: MMMMmm hola??? Tu quien eres perdon? No te conozco. Mi papa es el dueno de este antro, deberias de checar con quien hablas primero, digo, si no quieres que te despidan...")
            imprimir_letra_por_letra("Entras en duda si creerle a la chica o no, le crees y la dejas o la sacas?(sacar/dejar)")        
            respuesta = input().lower()
            if(respuesta == "sacar"):
                imprimir_letra_por_letra("Agarras a la mujer desconocida por el brazo, la arrastras por todo el bar y la dejas tirada en la calle...")
                eventos += 1
                equilibrio  = equilibrio + 1
                eleccion(player1, Nocheobj)
            else:
                imprimir_letra_por_letra("Pides disculpas y  te alejas de la mujer...")
        elif Nocheobj.fotosnum == 2:
            imprimir_letra_por_letra(player1.nombre + ": Hola vato, disculpa, no puedes estar tirando tanto flow aqui en la de fotos, haznos el favor de retirarte del area...")
            imprimir_letra_por_letra("Hombre Desconocido: Ah, perdon hermanito, no sabia que no se podia tirar tanta facha aca en las fotos.")
            player1.inteligencia = player1.inteligencia + 1
            eventos += 1
            eleccion(player1, Nocheobj)
        elif Nocheobj.fotosnum == 3:
            imprimir_letra_por_letra(player1.nombre + ": Hola chicos, una disculpa, solo se puede uno por uno, no los dos a la vez.")
            imprimir_letra_por_letra("Hombre1: Ah, perdoneme guardia. Te dije Carlos, te dije que solo podia pasar uno! Siempre te tengo que andar cuidando cabron.")
            imprimir_letra_por_letra("Carlos: Ay wey, neta ya me tienes harto, si no te callas a la verga, te voy a meter unos vergazos ahorita mismo...")
            imprimir_letra_por_letra("Sientes que la situacion esta escalando, debes de hacer algo... (Interrumpir/Dejarlos pelear)")
            respuesta = input().lower()
            if(respuesta == "interrumpir"):
                imprimir_letra_por_letra("Detienes la pelea que iba a surgir, sacas a los dos hombres arrastrandolos por el antro, vuelves al lugar de las fotos...")
                equilibrio = equilibrio + 1
                eventos += 1
                player1.inteligencia = player1.inteligencia + 1
                player1.labia = player1.labia + 1
                eleccion(player1, Nocheobj)
            else: 
                imprimir_letra_por_letra("Se desata una pelea por no haber ayudado a detenerla, los dos hombres terminan noqueados, los sacas a la entrada y vuelves al lugar de las fotos...")
                eventos += 1
                equilibrio = equilibrio -1
                eleccion(player1, Nocheobj)
    elif player1.lugar == "dj":
        if Nocheobj.djnum == 1:
            imprimir_letra_por_letra("Decides no interrumpirlo ya que sientes una presencia extrana...")
            eleccion(player1, Nocheobj)
        elif Nocheobj.djnum == 2:
            imprimir_letra_por_letra(player1.nombre + ": Oye cabron, hechale ganas que si no haces que la gente se anime, te van a correr.")
            imprimir_letra_por_letra("Dj: Perdoname bro, porfavor no le digas al jefe, es que mi novia me acaba de dejar y ando medio aguitado...")
            imprimir_letra_por_letra("El Dj parece estar triste, deberia de animarlo o reganarlo? (animarlo/reganarlo)")
            respuesta = input().lower()
            if(respuesta == "animarlo"):
                imprimir_letra_por_letra(player1.nombre + ": Venga bro, te voy a hacer el paro, nada mas trata de disimularlo e intenta subir mas el ambiente...")
                imprimir_letra_por_letra("El dj se mira mas feliz y se contenta con el hecho de que lo hayas ayudado.")
                eventos += 1
                equilibrio = equilibrio + 1
                eleccion(player1, Nocheobj)
            else:
                imprimir_letra_por_letra(player1.nombre + ": No me importa como te sientas, si dentro de 30 min no hay mas ambiente, te voy a reportar con el jefe...")
                imprimir_letra_por_letra("El dj se mira mas triste de lo que se veia antes, pero continua con su trabajo.")
                eventos += 1
                equilibrio = equilibrio + 1
                eleccion(player1, Nocheobj)

            eleccion(player1, Nocheobj)
        elif Nocheobj.djnum == 3:
            imprimir_letra_por_letra("Observas al DJ manipulando los controles, pero algo no parece estar bien. Decides acercarte para investigar.")
            imprimir_letra_por_letra("Al llegar más cerca, notas que el DJ está en problemas técnicos. Las luces parpadean y la música se detiene. ¿Cómo abordas la situación?")
            
            imprimir_letra_por_letra("Ayuda o Ignorar")
            
            respuesta = input().lower()
            if respuesta == "ayuda":
                imprimir_letra_por_letra(player1.nombre + ": Hey, ¿necesitas ayuda con eso? Puedo conocer un poco sobre equipos de sonido.")
                imprimir_letra_por_letra("DJ: ¡Oh, gracias! Estoy atrapado aquí y la gente se impacienta. Si puedes ayudar, sería genial.")
                # Aquí puedes añadir una sub-trama donde el jugador intenta solucionar los problemas técnicos del DJ.
                imprimir_letra_por_letra("Después de unos minutos, logras solucionar el problema y la música vuelve. El DJ te agradece y la gente aplaude.")
                eventos += 1
                equilibrio = equilibrio + 1
                eleccion(player1, Nocheobj)
            else:
                imprimir_letra_por_letra("Prefieres no involucrarte y regresas a tu área.")
                # Puedes añadir consecuencias basadas en esta decisión.
                eventos += 1
                equilibrio = equilibrio - 1
                eleccion(player1, Nocheobj)

    elif player1.lugar == "backstage":
        if Nocheobj.backstagenum == 1:
            imprimir_letra_por_letra(player1.nombre +": Oye cabron, que estas consumiendo? No puedes estar haciendo esto.")
            imprimir_letra_por_letra("Dj:Ho-ho-hola, pe-perdona, eS QueEEE noO mmmmEeeeeE zienTO biEEENnn...")
            imprimir_letra_por_letra("El dj parece estar en un estado muy critico, que haces? (Ayudar/Reportar)")
            respuesta = input().lower()
            if(respuesta=="ayudar"):
                imprimir_letra_por_letra("Lo ayudas a levantarse, lo llevas a los banos a que vomite, se mejora y te agradece...")
                eventos += 1
                equilibrio = equilibrio - 1 
                eleccion(player1, Nocheobj)
            else:
                imprimir_letra_por_letra("Te enojas con el dj, lo llevas a administracion, llega el jefe, gracias a que lo llevaste lo despiden...")
                eventos += 1
                equilibrio = equilibrio + 1
                eleccion(player1, Nocheobj)
        elif Nocheobj.backstagenum == 2:
            imprimir_letra_por_letra(player1.nombre + ": Oye cabron, hechale ganas que si no haces que la gente se anime, te van a correr.")
            imprimir_letra_por_letra("Dj: Perdoname bro, porfavor no le digas al jefe, es que mi novia me acaba de dejar y ando medio aguitado...")
            imprimir_letra_por_letra("El Dj parece estar triste, deberia de animarlo o reganarlo? (animarlo/reganarlo)")
            respuesta = input().lower()
            if(respuesta == "animarlo"):
                imprimir_letra_por_letra(player1.nombre + ": Venga bro, te voy a hacer el paro, nada mas trata de disimularlo e intenta subir mas el ambiente...")
                imprimir_letra_por_letra("El dj se mira mas feliz y se contenta con el hecho de que lo hayas ayudado.")
                eventos += 1
                equilibrio = equilibrio + 1
                eleccion(player1, Nocheobj)
            else:
                imprimir_letra_por_letra(player1.nombre + ": No me importa como te sientas, si dentro de 30 min no hay mas ambiente, te voy a reportar con el jefe...")
                imprimir_letra_por_letra("El dj se mira mas triste de lo que se veia antes, pero continua con su trabajo.")
                eventos += 1
                equilibrio = equilibrio + 1
                eleccion(player1, Nocheobj)
            eleccion(player1, Nocheobj)
        elif Nocheobj.backstagenum == 3:
            imprimir_letra_por_letra(player1.nombre +": Oye cabron, estas bien? ")
            imprimir_letra_por_letra("Dj:Ho-ho-hola, pe-perdona, eS QueEEE noO mmmmEeeeeE zienTO biEEENnn...")
            imprimir_letra_por_letra("El dj parece estar en un estado muy critico, que haces? (Ayudar/Reportar)")
            respuesta = input().lower()
            if(respuesta=="ayudar"):
                imprimir_letra_por_letra("Lo ayudas a levantarse, lo llevas a los banos a que vomite, se mejora y te agradece...")
                eventos += 1
                equilibrio = equilibrio - 1 
                eleccion(player1, Nocheobj)
            else:
                imprimir_letra_por_letra("Te enojas con el dj, lo llevas a administracion, llega el jefe, gracias a que lo llevaste lo despiden...")
                eventos += 1
                equilibrio = equilibrio + 1
                eleccion(player1, Nocheobj)
            eleccion(player1, Nocheobj)
    
    eleccion(player1, Nocheobj)


def noche1(player1, Nocheobj):
    
    # Crea un hilo para el contador
    hilo_contador = threading.Thread(target=contador_noche)

    player1.lugar = "entrada"
    imprimir_letra_por_letra('*Son las 9:00 pm, te diriges a la entrada del antro, vas a la oficina y dejas tus cosas. Sientes la música pulsante y la energía vibrante del lugar mientras te preparas para tu turno como guardia de seguridad. Regresas a la entrada, donde la fila de personas ansiosas por entrar ya comienza a formarse. El sonido de risas y la música envuelven el ambiente, creando una atmósfera emocionante.\n')
    imprimir_letra_por_letra('*Tomas tu posición junto a la puerta, te colocas el auricular y ajustas el micrófono. Observas a las personas que esperan ansiosas su turno para entrar. Algunas lucen elegantes con atuendos brillantes y glamorosos, mientras que otras optan por un estilo más relajado pero igualmente a la moda.\n')
    # Inicia el hilo del contador
    hilo_contador.start()
    imprimir_letra_por_letra(Nocheobj.entrada + "\n")
    imprimir_letra_por_letra('Que haces?\n')
    eleccion(player1, Nocheobj)
    # Espera a que el hilo del contador termine antes de salir del programa principal
    hilo_contador.join()
    
def main():
    intro()

if __name__ == "__main__":
    main()
