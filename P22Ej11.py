from numaleatorios import Aleatorio

random  = Aleatorio("series.txt")

class Evento():

    def __init__(self):
        super().__init__()
        self.tipo_evento = ""
        self.tiempo_creacion = 0
        self.tiempo_salida = 0

    def __str__(self):
        return str(self.tipo_evento) + " "  + str(self.tiempo_creacion) + " "  + str(self.tiempo_salida)

    def __repr__(self):
        return str(self)

#Simulacion en minutos

## Creacion de llegadas
tiempo = 0
tiempo_max = 6000 ## 100*60 2800 2760

p1,p2,p3 = 0,0,0

eventos = []

while(tiempo < tiempo_max):
    evento = Evento()
    llegada = random.exponencial(30)
    evento.tiempo_creacion = tiempo + llegada
    evento.tiempo_evento = evento.tiempo_creacion
    tiempo_creacion_pieza1= evento.tiempo_creacion
    evento.tipo_evento = "llegada_pieza1"
    tiempo = tiempo + llegada
    p1+=1
    eventos.append(evento)

tiempo =0
while(tiempo < tiempo_max):
    evento = Evento()
    llegada = random.exponencial(15)
    evento.tiempo_creacion = tiempo + llegada
    evento.tiempo_evento = evento.tiempo_creacion
    tiempo_creacion_pieza2= evento.tiempo_creacion
    evento.tipo_evento = "llegada_pieza2"
    tiempo = tiempo + llegada
    p2+=1
    eventos.append(evento)

tiempo =0
while(tiempo < tiempo_max):
    evento = Evento()
    llegada = random.exponencial(30)
    evento.tiempo_creacion = tiempo + llegada
    evento.tiempo_evento = evento.tiempo_creacion
    tiempo_creacion_pieza3= evento.tiempo_creacion
    evento.tipo_evento = "llegada_pieza3"
    tiempo = tiempo + llegada
    p3+=1
    eventos.append(evento)

tiempo=0
while(tiempo < tiempo_max):
    evento = Evento()
    llegada = 1
    evento.tiempo_creacion = tiempo + llegada
    evento.tiempo_evento = evento.tiempo_creacion
    evento.tipo_evento = "monitor"
    tiempo = tiempo + llegada
    eventos.append(evento)
    

## Inicio de la simulacion 
tiempo = 0
cola_de_espera = []
promedio_piezas= []
tiempo_pieza_en_espera=0
salidas = []
inspector_ocupado = False
piezas_max = 0
pieza1=0
pieza2=0
pieza3=0


while(tiempo < tiempo_max):
    eventos.sort(key=lambda x:x.tiempo_evento)
    evento = eventos.pop(0) ## Evento proximo
    tiempo = evento.tiempo_evento
    piezas_max = max(piezas_max, len(cola_de_espera))
    print(evento)

    ##simulacion pieza1
    if(evento.tipo_evento == "monitor"):
        promedio_piezas.append(len(cola_de_espera))
    elif(evento.tipo_evento == "llegada_pieza1"):
    
        
        if(len(cola_de_espera) == 0 and inspector_ocupado == False):
            inspector_ocupado = True
            evento.tiempo_inspeccion = tiempo
            tiempo_inspeccion_p1=evento.tiempo_inspeccion
            evento.tiempo_evento = tiempo + random.exponencial(3)##Tiempo de maquinado 
            evento.tipo_evento ="salida_inspeccion_pieza1"
            evento.tiempo_salida = evento.tiempo_evento
            eventos.append(evento)
        else:
            cola_de_espera.append(evento)
    elif( evento.tipo_evento == "salida_inspeccion_pieza1"):
        pieza1+=1
        inspector_ocupado = False
        evento.tiempo_salida = tiempo
        salidas.append(evento)
        if(len(cola_de_espera)>0):
            pieza = cola_de_espera.pop(0)
            inspector_ocupado = True
            pieza.tiempo_inspeccion = tiempo
            if pieza.tipo_evento == "llegada_pieza1":
                pieza.tiempo_evento = tiempo + random.exponencial(3)##Tiempo de maquinado
                pieza.tiempo_salida = pieza.tiempo_evento
                pieza.tipo_evento ="salida_inspeccion_pieza1"
            elif pieza.tipo_evento == "llegada_pieza2":
                pieza.tiempo_evento = tiempo + random.exponencial(5)##Tiempo de maquinado
                pieza.tiempo_salida = pieza.tiempo_evento
                pieza.tipo_evento ="salida_inspeccion_pieza2"
            elif pieza.tipo_evento == "llegada_pieza3":
                pieza.tiempo_evento = tiempo + random.exponencial(10)##Tiempo de maquinado
                pieza.tiempo_salida = pieza.tiempo_evento
                pieza.tipo_evento ="salida_inspeccion_pieza3"
            eventos.append(pieza)
    
    ##simulacion pieza2
    elif(evento.tipo_evento == "llegada_pieza2"):
        
        if(len(cola_de_espera) == 0 and inspector_ocupado == False):
            inspector_ocupado = True
            evento.tiempo_inspeccion = tiempo
            tiempo_inspeccion_p2=evento.tiempo_inspeccion
            evento.tiempo_evento = tiempo + random.exponencial(5)##Tiempo de maquinado 
            evento.tipo_evento ="salida_inspeccion_pieza2"
            evento.tiempo_salida = evento.tiempo_evento
            eventos.append(evento)
        else:
            cola_de_espera.append(evento)
    elif( evento.tipo_evento == "salida_inspeccion_pieza2"):
        pieza2+=1
        inspector_ocupado = False
        evento.tiempo_salida = tiempo
        salidas.append(evento)
        if(len(cola_de_espera)>0):
            pieza = cola_de_espera.pop(0)
            inspector_ocupado = True
            pieza.tiempo_inspeccion = tiempo
            if pieza.tipo_evento == "llegada_pieza1":
                pieza.tiempo_evento = tiempo + random.exponencial(3)##Tiempo de maquinado
                pieza.tiempo_salida = pieza.tiempo_evento
                pieza.tipo_evento ="salida_inspeccion_pieza1"
            elif pieza.tipo_evento == "llegada_pieza2":
                pieza.tiempo_evento = tiempo + random.exponencial(5)##Tiempo de maquinado
                pieza.tiempo_salida = pieza.tiempo_evento
                pieza.tipo_evento ="salida_inspeccion_pieza2"
            elif pieza.tipo_evento == "llegada_pieza3":
                pieza.tiempo_evento = tiempo + random.exponencial(10)##Tiempo de maquinado
                pieza.tiempo_salida = pieza.tiempo_evento
                pieza.tipo_evento ="salida_inspeccion_pieza3"
            eventos.append(pieza)

    ##simulacion pieza3
    elif(evento.tipo_evento == "llegada_pieza3"):
        if(len(cola_de_espera) == 0 and inspector_ocupado == False):
            inspector_ocupado = True
            evento.tiempo_inspeccion = tiempo
            tiempo_inspeccion_p3=evento.tiempo_inspeccion
            evento.tiempo_evento = tiempo + random.exponencial(10)##Tiempo de maquinado 
            evento.tipo_evento ="salida_inspeccion_pieza3"
            evento.tiempo_salida = evento.tiempo_evento
            eventos.append(evento)
        else:
            cola_de_espera.append(evento)
    elif( evento.tipo_evento == "salida_inspeccion_pieza3"):
        pieza3+=1
        inspector_ocupado = False
        evento.tiempo_salida = tiempo
        salidas.append(evento)
        if(len(cola_de_espera)>0):
            pieza = cola_de_espera.pop(0)
            inspector_ocupado = True
            pieza.tiempo_inspeccion = tiempo

            if pieza.tipo_evento == "llegada_pieza1":
                pieza.tiempo_evento = tiempo + random.exponencial(3)##Tiempo de maquinado
                pieza.tiempo_salida = pieza.tiempo_evento
                pieza.tipo_evento ="salida_inspeccion_pieza1"
            elif pieza.tipo_evento == "llegada_pieza2":
                pieza.tiempo_evento = tiempo + random.exponencial(5)##Tiempo de maquinado
                pieza.tiempo_salida = pieza.tiempo_evento
                pieza.tipo_evento ="salida_inspeccion_pieza2"
            elif pieza.tipo_evento == "llegada_pieza3":
                pieza.tiempo_evento = tiempo + random.exponencial(10)##Tiempo de maquinado
                pieza.tiempo_salida = pieza.tiempo_evento
                pieza.tipo_evento ="salida_inspeccion_pieza3"
            eventos.append(pieza)

######### a) Utilizacion del centro de maquinado ########
tiempo_total_inspeccion = 0
for pieza in salidas:
    tiempo_total_inspeccion += pieza.tiempo_salida-pieza.tiempo_inspeccion
print("tiempo_total de inspeccion",tiempo_total_inspeccion)
    
print("a) la utilizacion del centro de maquinado es ",(tiempo_total_inspeccion/tiempo_max)*100,"%") ## a) Utilizacion del centro de maquinado

######### b) el número total de piezas producidas #######
total=0
for evento in salidas:
    total+=1
print("b) el número total de piezas producidas son",total, " piezas") ## b) el número total de piezas producidas

print(pieza1, " ", pieza2, " ", pieza3, " ")

##### c) ) El tiempo promedio de espera de las piezas en el almacén/llegadas
tiempos_espera = 0
for pieza in salidas:
    tiempo_diff = pieza.tiempo_inspeccion - pieza.tiempo_creacion
    tiempos_espera +=  tiempo_diff
    
print("c) tiempo promedio de espera de las piezas en almacen ",tiempos_espera/len(salidas)) ## c)

######### d)el número promedio de piezas en el almacén/llegadas ########

print("d) el número promedio de piezas en el almacén ",sum(promedio_piezas)/len(promedio_piezas)) ##d)
