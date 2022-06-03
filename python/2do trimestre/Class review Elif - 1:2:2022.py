import datetime
dia= datetime.date.today()
w=dia.weekday()+1

if (w==0):
  print("feliz domingo")

elif (w==1):
  print("es lunes *carita depresiva*")
  
elif (w==2):
  print("wuhu es martes")

elif (w==3):
  print("nais es miercoles")

elif (w==4):
  print("tremendo es jueves")

elif (w==5):
  print("banien a los macacos porq es viernes")
  
else:
  print("yahoo, es sabado")