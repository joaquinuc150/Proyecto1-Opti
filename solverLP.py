from random import randint

#Lectura de Parametros
plantas = int(input("Ingresar la cantidad de plantas de produccion: "))
centros = int(input("Ingresar la cantidad de centros de distribucion: "))
plantas_capacidad_inf = int(input("Ingrese el limite inferior de la capacidad de las plantas: "))
plantas_capacidad_sup = int(input("Ingrese el limite superior de la capacidad de las plantas: "))
centros_demanda_inf = int(input("Ingrese el limite inferior de la demanda de los centros: "))
centros_demanda_sup = int(input("Ingrese el limite superior de la demanda de los centros: "))
costo_transporte_inf = int(input("Ingrese el limite inferior para el costo de transporte: "))
costo_transporte_sup = int(input("Ingrese el limite superior para el costo de transporte: "))
print("0)Caso Balanceado")
print("1)Caso Desbalanceado")
caso = int(input("Elegir Caso:"))
if(caso == 1):
    print("1)Demandas satisfechas exactamente")
    print("2)Demandas sobresatisfechas")
    print("3)Demandas sobresatisfechas y oferta total despachada")
    caso_desbalanceado = int(input("Si el caso es desbalanceado, cual es el criterio a elegir: "))


print()
plantas_capacidades = []
oferta_total = 0
for x in range(plantas):
    capacidad = randint(plantas_capacidad_inf,plantas_capacidad_sup)
    oferta_total += capacidad 
    #print("Planta de produccion "+str(x+1)+" tiene una capacidad de "+str(capacidad)+" productos")
    plantas_capacidades.append(capacidad)
print()
centros_demandas = []
demanda_total = 0
for x in range(centros):
    demanda = randint(centros_demanda_inf,centros_demanda_sup)
    demanda_total += demanda
    #print("Centro de distribucion "+str(x+1)+" tiene una demanda de "+str(demanda)+" productos")
    centros_demandas.append(demanda)
print()
costos_transporte = []
for x in range(plantas):
    costos_planta_i= []
    for y in range(centros):
        costo = randint(costo_transporte_inf,costo_transporte_sup)
        costos_planta_i.append(costo)
    #print("Costo de transporte de Planta "+str(x+1)+" :",costos_planta_i)
    costos_transporte.append(costos_planta_i)
print()
#print("Oferta total =",oferta_total)
#print("Demanda total =",demanda_total)

if(oferta_total >= demanda_total):
    if(caso == 0):
        centros_demandas[0] += oferta_total - demanda_total
    factible = "factible"
else:
    factible = "infactible"
#Generador LP
#print("\nSolver para LP")
#Funcion Objetivo
fo = "min: "
for i in range(plantas):
    for j in range(centros):
        fo += str(costos_transporte[i][j])+" x"+str(i+1)+"_"+str(j+1)
        if i != (plantas-1):
            fo += " + "
        elif j != (centros-1):
            fo += " + "
        else:
            fo += ';\n'
#print(fo)
#Restricciones
signo_oferta = ''
signo_demanda = ''
if caso == 1:
    if caso_desbalanceado == 1:
        signo_oferta = ' <= '
        signo_demanda = ' = '
    elif caso_desbalanceado == 2:
        signo_oferta = ' <= '
        signo_demanda = ' >= '
    elif caso_desbalanceado == 3:
        signo_oferta = ' = '
        signo_demanda = ' >= '
else:
    caso_desbalanceado = 0
    signo_oferta = ' = '
    signo_demanda = ' = '


const = ""
for i in range(plantas):
    for j in range(centros):
        const += "x"+str(i+1)+"_"+str(j+1)
        if j < (centros - 1):
            const += " + "
        else:
            const += signo_oferta
    const += str(plantas_capacidades[i])+';\n'

const += '\n'

for j in range(centros):
    for i in range(plantas):
        const += "x"+str(i+1)+"_"+str(j+1)
        if i < (plantas - 1):
            const += " + "
        else:
            const += signo_demanda
    const += str(centros_demandas[j])+';\n'

enteros = 'int '
for i in range(plantas):
    for j in range(centros):
        if i != (plantas-1):
            enteros += "x"+str(i+1)+"_"+str(j+1)+", "
        elif j != (centros-1):
            enteros += "x"+str(i+1)+"_"+str(j+1)+", "
        else:
            enteros += "x"+str(i+1)+"_"+str(j+1)+';'

if caso == 1:
    solver = open("not_balanced_instances/"+str(caso_desbalanceado)+"/modeloLP_"+str(plantas)+"_"+str(centros)+"_"+str(caso_desbalanceado)+"_"+factible+".lp","w")
    solver.write(fo)
    solver.write("\n")
    solver.write(const)
    solver.write("\n")
    solver.write(enteros)
    solver.close()
elif caso == 0:
    solver = open("balanced_instances/modeloLP_"+str(plantas)+"_"+str(centros)+"_"+factible+".lp","w")
    solver.write(fo)
    solver.write("\n")
    solver.write(const)
    solver.write("\n")
    solver.write(enteros)
    solver.close()