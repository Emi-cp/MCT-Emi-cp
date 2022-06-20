import random
insultos = ["Cuando naciste los doctores pensaban que tu mamá eataba haciendo popis", "Morro chancho culiao você dai asco pibe", "Te  falta calle pa'","No te la sabes","No que muy salsa morro? venga, dejese venir","Pi pupu pi pu","Ya te cargó el payaso carnal","Ya bailaste con la flaca carnal"]
gameOver = ["Bailaste con la flaca carnal","But ella no te quiere :'v","When subes tus momos en video (El futuro es hoy oiste viejo []v) but te terminan baneando (Ayyy mi lente de contacto :'v)","Ponte pilas carnalito ","Fuistes","Fin del juego"]

while True:
  jugador1=input("Elige tu nombre: ")
  print("(Tu mamá te despierta una mañana...)")
  print("...")
  input()
  print("despierta")
  input()
  print("...")
  input()
  print("DESPIERTA")
  print("ORALE MORRO, PÁRESE VAYASE POR LAS  TORTILLAS")
  print("(Tu mamá te entrega dinero para las tortillas y sales de la casa...)")
  input()
  print("(En el camino escuchas un ruido detrás tuyo...)")
  print("Orale compadre ya se la sabe mijo")
  asalto1=int(input("Qué quieres hacer? 1.-dejarte asaltar, 2.- salir corriendo, 3.- defenderte: "))
  
  if(asalto1==1):
    print("(Te has dejado asaltar y te quitaron todo tu dinero, no te queda más que regresar a casa...)")
    print("(Al regresar a casa tu mamá te ve sin dinero y sin tortillas)")
    print("ORALE MORRO Y LAS TORTILLAS?")
    pregunta1d1=int(input("Qué quieres hacer? 1.- Responder, 2.- Quedarte callao: "))
    if(pregunta1d1==1):
      print("(Decides responder)")
      print("Perdone jefa, me asaltaron en camino a la tie...")
      input()
      print("(Antes de que puedas terminar tu mamá te responde: )")
      print("AHHHHH, ME RESPONDES? AHORA SI TE CARGÓ EL PAYASO")
      print("(Tu mamá te pega con la chancla y terminas descuarajingao fuera de este mundo)")
      print(random.choice(gameOver))
      continue
    
    elif(pregunta1d1==2):
      print("(Te quedas callaito)")
      input()
      print("Tu jefa se enoja por no contestar")
      print("El ratoncito te como la lengua o por q no hablas chamaco tonto")
      print("(Tu mamá se enoja tanto q se le saca chorcha y te mete tremendo tortazo en el coco dejandote una gran contusión cerebral")
      print(random.choice(gameOver))
      continue
      
  elif(asalto1==2):
    print("(Huyes de la escena sin antes insultar al asaltante)")
    print(random.choice(insultos))
    print("(Pasas rapido a la tienda por las tortillas y regresas a casa...)")
    input()
    print("Al regresar a tu casa encuentras que entraron a tus aposentos y se llevaron a tu jefa")
    input()
    print("ijuesu betamax los setas estan afuera")
    print("Encuentras una notita de *Desconocido* encima de la mesa de la cocina")
    print("Muy buenas compare, hemos secuestrao a tu jefasa por actividades ilícitas en contra de la Armada Mexicana Loquitas Oaxaqueños, la mandaremos a Brazil en una semana, y si tienes lavadora, ahí la vemos")
    input()
    print("(Te quedas todo preocupadong por la jefasa)")
    pregunta1d2=int(input("Deseas ir a rescatarla? 1.- si, 2.- no"))

    if(pregunta1d2==1):
      print("(Decides ir a rescatar a tu jefasa pero buscas algo con que pelear de vuelta o defenderte)")
      print("(Recuerdas que hay una caja fuerte con una MP4 REX y un cuchillito de mariposa)")
      print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠾⠿⠀⠀
⠀⠀⣤⡀⠀⢠⠆⣰⣶⡶⠒⠒⠒⠒⠒⠂⢰⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆⠀
⠀⠀⠘⠿⢀⣾⠀⣿⣿⡿⠿⠿⠿⠿⠿⠇⢠⣤⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⣿⡆⠹⣿⣷⣶⣶⣶⣶⣶⡆⢠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣿⠿⠿⢿⣤⣤⣤⣤⣄⠀⠀⠀⣀⡼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⡇⠰⠶⢈⣿⡿⠁⠉⠛⠛⠓⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⣿⣶⣶⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣏⣸⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠉⠉⠉ ''')
      input()
      print("(BUT NO RECUERDAS LA CONTRASEÑA :'v")
      print("Recuerdas que la contraseña es de 4 digitos, suerte carnal")
      intento=int(input("Intenta adivinar la contraseña: "))
      
      while intento!=1234:
        print("Contraseña incorrecta carnal, intentele de nuevo")
     
      print("(Perfecto, conseguiste el arma y el cuchillo)")
      print('''   |^^^|
    }_{
    }_{
/|_/---\_|\\
I _|\_/|_ I
\| |   | |/
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   |   |
   \   /
    \ /
     Y ''')
      input()
      quote=int(input("Quieres ver tus habilidades manejando el cuchillo de mariposa? 1.-si 2.-no "))
      
      if(quote==1):
        print("A veces cuando sientes mariposas en el estómago no es amor...")
        input()
        print(random.choice(gameOver))
        continue

      elif(quote==2):
        print("no te distraes y sigues adelante en tu camino")
      print("Mientras vas buscando por la calle, vas preguntando a la gente... ")
      print("Muy buenas estimado caballero/dama ha visto usted una camioneta del Marina Oaxacos Revolucionario Estatal Nacionalmente Avestruz por estos lares?")
      input()
      print("(la gente te responde)")
      print("Ufala compadre por aqui no se ha visto ninguna de esas camionetas")
      print("(repentinamente se acerca un cholo y te dice...)")
      print("Buenas vato, te escuche hablar de mi diosito papucho tallado por los mismos ángeles cabeza de algodón, yo si vi una camioneta de M.O.R.E.N.A.")
      quote2=int(input("Tu eri fan de A.M.L.O.? 1.-simon 2.-nel"))
     
      if(quote2==1):
        print("(El señor responde...)")
        print("Ya sabía yo, eres uno de los nuestros, eres un cholo")
        input()
        print("(Le sigues la corriente y dices que si)")
        print("(El señor agarra y que te dice...)")
        input()
        print("Aquí a la esquina das vuelta a la derecha, te metes al callejón por 4 cuadras, giras a la izquierda agarrando la Av. Pipila y te metes en el entronque de Circumbalacion, ahí enfrente se encuentra")
        input()
        print("Tan en el palacio municipal, están a punto de dar una mañanera, metale turbo carnal o se la va a perder")
        print("(Te diriges a la dirección que te dijo el don)")
        input()
        print("(En el camino encuentras un tiangis)")
        print("(Decides ver si puedes abastecerte de algo y entras)")
        input()
        print("(Se te acercan 3 hombres misteriosos un poco despues de estar en el tiangis)")
        print("(Uno de los hombres se te acerca y en voz baja te dice...)")
        input()
        print("Ya te la sabes carnal, celular y cartera, y de pasadita cualquier tipo de objeto de valor")
        subquote=int(input("Qué quieres hace? 1.-Huir 2.-Defenderte"))
        
        if(subquote==1):
          print("(Decides huir de la escena e insultar a los asaltantes en el acto)")
          print(random.choice(insultos))
          print("(Llegas al palacio municipal de Ecatepec y justo se esta dando la mañanera)")
          input()
          print("(En lo que se da la mañanera decides escabullirte a buscar una entrada para poder entrar)")
          print("No mucho tiempo despues encuentras una entrada en la parte trasera del edificio y decides ver si puedes entrar")
          print("(Observas que necesitas 3 códigos diferentes de 8 digitos cada uno para poder accesar y que los codigos están en 3 partes diferentes de Ecatepec)")
          input()
          print("(Observas que en el muro hay un mapa para uno de los 3 códigos de acceso, el mapa te indica que te dirijas a el Centro Civico Río de Luz")
          print("(Te diriges a ese lugar a toda velocidad a buscar la primera clave de acceso")
          input()
          print("(Un buen rato pasa y por fin llegas a el Centro Civico Río de Luz)")
          input()
          print("(El lugar tiene guardias por todos lados por lo cual el entrar no va a ser tan facil)")
          print("(Decides esperar a que sea un poco más de noche a ver si encontrabas menos guardias de los que habia en el momento)")
          print("(Pasa un buen rato, ya son las 10:00pm")
          print("(Te das cuenta de que hay menos guardias por lo cual decides idear un plan)")
          print("(Rodeas el edificio en busca de otra entrada pero no encuentras ninguna)")
          print("(De repente se te ocurre la gran idea de hacer la Chapo classic y hacerte un tunel por el cual meterte al edificio sin que los guardias se den cuenta")
          input()
          print("(De rapidito te consigues una pala que estaba en una contrucción en progreso y regresas a el Centro Civico Río de Luz")
          print("(Buscas un punto por el cual empezar a hacer el tunel sin que se de cuenta la gente y empiezas a hacerlo)")
          input()
          print("(Por suerte el tunel lo terminas dentro de un closet de el edificio y nadie se da cuenta de que te escabulliste al edificio)")
          print("(Encuentras un cajón con traje de guardia y decides ponertela y hacerte pasar por guardia)")
          input()
          print("(Un guardia con placa de jefe te ve y se te acerca)")
          print("(Crees que te descubrieron hasta que el guardia te pregunta...)")
          print("Como va la guardia en el sector 2B Ramírez?")
          input()
          print("(Sigues la corriente haciendote pasar por ese tal 'Ramírez')")
          print("Perfecto patron, todo normal")
          input()
          print("(El guardia te responde...)")
          print("Tenga cuidado Ramírez, había un sujeto sospechoso afuera del sector 9S alrededor de las 10:00pm, si ve algo aviseme por favor")
          print("(Sorprendido de que tal vez ese 'sujeto sospechoso' se trate de ti le respondes de una manera ligeramente nerviosa)")
          print("Si patron, no se preocupe patron, yo le aviso de lo que vea")
          print("(El guardia te responde...)")
          print("Cuento con usted Ramírez, me voy a cuidar el sector 2A")
          input()
          print("(El guardia se aleja y cuando ya no esta a la vista empiezar a buscar el codigo en el edificio)")
          print("(Buscas cuarto tras cuarto pero no tienes suerte)")
          print("(Queda un ultimo cuarto pero hay 2 guardias en la entrada)")
          print("(No sabes que hacer pero decides acercate a la puerta)")
          input()
          print("(Uno de los guardias te advierte...)")
          print("Alejese mi chavo que el acercarse a esta puerta esta prohibido")
          input()
          subquote2=int(input("Qué deberías hacer? 1.-Distraer los guardias de alguna manera 2.-Intentar pelear con los guardias"))
          
          if(subquote2==1):
            print("(Se te ocurre hacer un ruido masivo el otro lado del edificio y distraer a los a todos los guardias del edificio)")
            print("(Detonas 7 disparos hacia una pared del otro lado del edificio para hacer que todos los guardias alertados vayan para esa parte)")
            print("(Cuidadosamente llegas al cuarto mientras esta sin guardia y entras)")
            print("(Te das cuenta de que dentro del cuarto hay algo de dinero, el primer codigo de acceso, un fusil COLT M4A1 y el mapa al siguiente codigo de acceso")
            print("(Rapidamente abandonas el edificio y decides buscar un lugar donde hospedarte ya que ya se hizo muy tarde y estas cansado despues de pasar un día tan agitado)")
            input()
            print("(Te quedas con el taje de guardia guardado por si te sirve en algún otro momento)")
            print("(Encuentras un motel con bajo precio y con una calidad agradable por lo cual decides hospearte ahí para el día siguiente ir a buscar el segundo codigo)")
            input()
            print("(Te despiertas a las 8:00am listo para desayunar y luego continuar con el rescate)")
            print("(Te diriges a unas kekas de doña pelos de la esquina para desayunar rapido e ir por el segundo codigo)")
            print("(Llegas a la garnachería y le dices a la señora q prepara las kekas)")
            print("Muy buenas seña me puede dar unas 5 kekas de queso sin queso porfa")
            print("(La señora te responde)")
            print("Claro jovenazo pereme un momentito")
            print("(Un cholo se acerca y te roba la comida)")
            decision=int(input("Qué quieres hacer? 1.-Recuperar tu comida 2.-Dejarlo ir y quedarte sin comer"))
            
            if(decision==1):
              print("(Lo persigues y recuperas tu comida)")
              print("(Comes tus garnachas y revisas la foto que le tomaste al mapa de el siguiente codigo de acceso)")
              input()
              print("Te dirijes al 'RÍO DE LOS REMEDIOS'")
              taxiono=int(input("Encuentras un taxi pero el conductor se ve sospechoso, 1.-Te vas en el taxi 2.-Te vas caminando"))

              if(taxiono==1):
                print("(Te subes al taxi)")
                print('''                   [\ ''')
                print('''              .----' `-----. ''')
                print('''             //^^^^;;^^^^^^`\ ''')
                print('''     _______//_____||_____()_\________''')
                print('''    /826    :      : ___              `\ ''')  
                print('''   |>   ____;      ;  |/\><|   ____   _<) ''')
                print('''  {____/    \_________________/    \____} ''')
                print('''       \ '' /                 \ '' / ''')
                print('''        '--'                   '--' ''')
                input()
                print("(Te das cuenta de que se va por otra ruta muy sospechosa)")
                input()
                print("(Empiezas a preocuparte mientras el taxi te lleva por una ruta demasiado sospechosa)")
                print("(Te empieza a preguntar preguntas personales)")
                print("(Le dices)")
                print("No joven, aquí ya me bajo, aquí estoy bien")
                print("(El taxista cierra las puertas dejandote encerrado)")
                input()
                print("(Se suben 2 warros y te noquean)")
                print("(Días despues encuentran tu cadaver a 50km de donde te agarraron en la costa de un río)")
                print(random.choice(gameOver))
                continue

                elif(taxiono==2):
                  print("(Te vas caminando a 'EL RÍO DE LOS REMEDIOS')")
                  input()
                  print("(Llegas a 'EL RÍO DE LOS REMEDIOS' y ves un agujero sospechoso ahí cerca pero debes nadar en aguas negras para acceder)")
                  print("(Te metes al río de aguas negras y entras por el agujero, entrando a un cuarto oculto con 8 guardias)")
                  print("(Uno de los guardias se te arcerca y te menciona)")
                  print("Qué pasó joven? esta es zona privada")
                  input()
                  print("(Tu le respondes mientras le entregas un quinienton)")
                  print("Y si la hacemos publica?")
                  print("(El guardia responde)")
                  print("Por ahí hubieras empezado joven")
                  input()
                  print("(Le respondes)")
                  print("Me puede dar el código de acceso chavo?")
                  print("(Te responde el guardia)")
                  print("Si joven, pero tiene que llamar a su amiga Sor Juana")
                  print("(Le entregas un billete de doscientos)")
                  print("(El guardia te dice)")
                  print("Le puedo dar 7 de los 8 dígitos por q si no, mi patroncito me corre, el último lo tendra que adivinar usted, le puedo decir que el último digito es uno de los siguientes 4: 3, 7, 8 o 0 y el resto del código es 1311195#")
                  livesGameOver=3
                  for x in range(3):
                    passw=int(input("Cuál es el último digito?"))
                    if(passw!=3):
                      print("(el guardia niegan con la cabeza)")
                    else:
                      break
                  if(livesGameOver<=0):
                    print(random.choice(gameOver))
                    continue
                  print("(Consigues el código y te retiras de esa zona)")
                  print("(Justo antes de salir el policia te dice)")
                  print("El último codigo se encuentra en el Oxxo, pregunta por recarga de datos, y cuando te digan que el sistema ha caido, les respondes: 'Nimodo, ya para la otra joven', te darán el codigo que necesitas.")
                  print("(Agradeces y sales de ahí con dirección a un Oxxo)")
                  print("(Más tarde llegas a un Oxxo y preguntas por recargas de saldo)")
                  print("(El trabajador te responde)")
                  print("Ufas perdone joven, se calló el sistema")
                  print("(Tu le respondes)")
                  print("Nimodo, ya para la otra joven")
                  print("(El joven te responde)")
                  print("Ah, entonces necesita el objeto?")
                  print("(Pues tome, aqui está")
                  print("(Te vas del Oxxo en direccion al palacio municipal)")
                  print("(Llegas a la puerta de atrás del palacio municipal un rato despues y sacas los 3 códigos)")
                  print("(Las tarjetas muestran los siguientes codigos (46592640) (13111953) (78323357)")
                  intentos=3
                  for x in range(3):
                    passwo=int(input("Introduce el primer codigo"))
                    if(passwo!=46592640):
                      print("(Codigo incorrecto)")
                    else:
                      break
                  if(intentos<=0):
                    print(random.choice(gameOver))
                    continue
                  print("Codigo correcto")
                  intentos2=3
                  for x in range(3):
                    passwo=int(input("Introduce el segundo codigo"))
                    if(passwo!=13111953):
                      print("(Codigo incorrecto)")
                    else:
                      break
                  if(intentos<=0):
                    print(random.choice(gameOver))
                    continue
                  print("Codigo correcto")
                  intentos3=3
                  for x in range(3):
                    passwo=int(input("Introduce el tercer codigo"))
                    if(passwo!=78323357):
                      print("(Codigo incorrecto)")
                    else:
                      break
                  if(intentos<=0):
                    print(random.choice(gameOver))
                    continue
                  print("Codigo correcto")
                  print("Acceso autorizado")
                  print("(Entraste con exito a el palacio municipal)")
                  print("(Entras con el traje de guardia y el arma que encontraste previamente en el centro cívico para que no te detecten con tanta facilidad)")
                  print("(Buscas el cuarto donde tienen atrapada a tu jefaza)")
                  print("(Despues de un momento encuentras una puerta que tiene unas escaleras hacia un piso subterráneo)")
                  print("(Con un poco de sospecha bajas a ese piso)")
                  print("(Al llegar al piso subterraneo encuentras un cuarto oscuro y amplio con una persona atada a una silla)")
                  print("(Con un mejor vistazo te das cuenta de que es tu mamá)")
                  print("(Corres hacia ella con la intencion de liberarla pero ella grita intentando advertirte de algo, pero tu no le entiendes debido a el paleacate atado en su boca)")
                  print("(Ves una figura grande frente a ti al llegar con tu mamá y te dice...)")
                  print("Te he estado esperando por un largo rato... He observado cada movimiento que haces, debo admitir que has llegado bastante lejos para llegar solo")
                  print("Pero, este es el fin de tu odisea, no hay escapatoria...")
                  print("(Cientos de televisiones mostrando grabaciones de cada uno de tus movimientos comienzan a prenderse iluminando el cuarto)")
                  print("(Con el cuarto iluminado te das cuenta de que la figura es el mismisimo AMLO)")
                  print("(Le dices a AMLO)")
                  print("DEJA IR A MI JEFAZA O VAS A VER")
                  print("(AMLO responde)")
                  print("Si quieres salir de aqui pelea por tu libertad, VEAMOS DE LO QUE ESTÁS HECHO...")
                  print("(AMLO rompe unos cables en el suelo causando una sobrecarga en si mismo causando que se vuelva como un superhumano)")
                  print("(Empieza una larga pelea)")
                  print("(Intentas dispararle a AMLO pero no sirve de nada, su cuerpo superhumano no le causan daño las balas)")
                  print("(Despues de un rato la pelea te deja cansado y AMLO deja de contenerse dejandote herido y a punto de rendirte)")
                  print("(Tu mamá te grita)")
                  print("HIJO POR FAVOR NO TE RINDAS, ENCUENTRA UNA MANERA SE QUE TU PUEDES, SI NO, HAY CHANCLA")
                  print("Esa frase te motiva a continuar la pelea, e ideas un plan")
                  print("(Atraerás a AMLO cerca de las teles y luego las tirarás sobre el)")
                  print("(Corres hacia donde están algunas de las teles y haces que AMLO te siga)")
                  print("(Una vez debajo de las teles le disparas a un soporte y sales corriendo)")
                  print("(Varias de las televisiones caen sobre AMLO causando que AMLO muera")
                  print("(Corres con tu madre para liberarla y salir de ese lugar)")
                  print("(Despues de salir son perseguidos por el gobierno así que deciden escapar hacia Europa en busca de una vida tranquila y segura)")
                  print("(Consigues un buen trabajo y estabilizarte economicamente en España viviendo una vida tranquila)")
                  print("Fin")
                  continue
                  
            elif(decision==2):
              print("(Te vas sin comer)")
              print("(Despues de un rato te desmayas de hambre y nadie viene a ayudarte, sino que te dejan tirado en la calle sin pertenencias")
              print(random.choice(gameOver))
              continue

          elif(subquote2==2):
            print("(Golpeas a los guardias repetidamente para poder acceder)")
            print("(Uno de los guardias sin dificultad alguna te devuelve un golpe que te deja noqueado en un instante)")
            print("(Eres capturado por el resto de tu vida y no pudiste rescatar a tu jefasa)")
            print(random.choice(gameOver))
            continue
          
          
        elif(subquote==2):
          print("(Decides defenderte de los asaltantes con las armas que encontraste previamente en la caja fuerte de tu casa)")
          print("(Logras derrotar a los asaltantes pero te caen 638,384,255 chapas y te meten 748 funas. Terminas en el bote por el resto de tu vida.")

      elif(quote2==2):
        print("(El señor responde...)")
        input()
        print("No eri cholo, no te voy a decir")
        print("Exterminen a los que no son cholos")
        print("(Te llegan 20 cholos y te empiezan a cargar de insultos)")
        print(random.choice(insultos))
        input()
        print(random.choice(insultos))
        input()
        print(random.choice(insultos))
        input()
        print(random.choice(insultos))
        print("(Los 20 cholos procede a apuñalarte 40 veces cada uno)")
        print(random.choice(gameOver))
        continue

    elif(pregunta1d2==2):
      print("(Te quedas toda tu vida pensando si tu jefasa logro sobrevivir en el mismísimo tercer mundo del fri fayer, Brazil)")
      print("(Le rezas a la virgencita por el bien de tu madresita)")
      input()
      print("(Años después llega un correo a tu casa de q tu jefasa murio, pero como todo mexicano que eres ya habias muerto en un secuestro hace 20 años)")
      print(random.choice(gameOver))
      continue
    
  elif(asalto1==3):
    print("Orale carnal, dejese venir")
    input()
    print("(El asaltante te pega un tiro a ver si muy salsa, tu quedas coajaito en el suelo y el asaltante termina feliz de tener dinero para pagar tortillas)") 
    print(random.choice(gameOver))
    continue