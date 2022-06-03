while True:
  sn=0
  chiste=0
  sn=input("Quieres escuchar un chiste?si/no ")
  if (sn=="si"):
    chiste=int(input("Tengo 5 chistes, elige un número del 1 al 5 "))
    if (chiste==1):
      print("Habia un perro, llegó otro y son 2")
    if (chiste==2):
      print("Como se dice veterinario en ingles? Dogtor")
    if (chiste==3):
      print("Una madre le dijo a su hijo: hijo, me veo gorda y fea, que tengo hijo? el hijo le respondió: tienes toda la razón ")
    if (chiste==4):
      print("Un siego le dice a otro: Ojalá lloviera. El otro le respondió: ojalá yo también ")
    if (chiste==5):
      print("Un chico le pregunta a su padre: papá, puedo ir al cine? El padre le responde: si hijo, pero no entres")
  if (sn=="no"):
    print("ni modo")