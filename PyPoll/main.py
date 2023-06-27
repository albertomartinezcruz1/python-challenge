import os
import csv
#Para revisar donde empieza el programa
print("corriendo......")
#Ruta del archivo
election_data=os.path.join("../PyPoll/Resources/election_data.csv")
#Archivo donde se escribira en txt
election_analysis=os.path.join("../PyPoll/analysis/election_analysis.txt")
#Abre el archivo
with open(election_data) as my_file:
#    #separa por comas
    csv_reader=csv.reader(my_file,delimiter=",")
    #Se salta el primero
    next(csv_reader,None)
    #inicializa variables
    novot=0
    my_list_id=[]
    my_list_county=[]
    my_list_vote=[]
    counts_dic={}
    for each_line in csv_reader:
        #Guarda el valor de los id
        ballotid=int(each_line[0])
        #Guarda el valor de county
        County=each_line[1]
        #Guarda el valor del voto
        candidate=each_line[2]
        #Agrega los valores a una lista
        my_list_id.append(ballotid)
        #agregan county a una lista 
        my_list_county.append(County)
        #agregan los votos a una lista
        my_list_vote.append(candidate)
#Guarda el valor de numero de votante
novot=len(my_list_vote)
#inicializa lista donde se almacena el nombre, porcentaje y numero de votos obtenidos respectivamente
my_list_of_candidates=[]
percentages=[]
number_of_votes=[]
#inicia contador
i=1
#cuenta los votos para cdaa candidato se guarda en keys con el nombre del candidato
for each_element in my_list_vote:
    if each_element in counts_dic:
        counts_dic[each_element]+=1
        i+=1
    else:
        counts_dic[each_element]=1
        #Guarda los nombres en my_list_of_candidates
        my_list_of_candidates.append(my_list_vote[i+1])

for each_elemen in counts_dic:
    #crea lista donde vienen los numeros de votos por cada candidato
    number_of_votes.append(int(counts_dic[each_elemen]))
j=0
mx=0
#Guarda ne la lista porcentajes el calculo de los porcentajes
for j in range(len(number_of_votes)):
    mx=number_of_votes[j]/novot*100
    percentages.append(round(mx,3))

print("Election Results")
print("---------------------------------------------")
print("Total votes: ",novot)
print("---------------------------------------------")
k=0
contav=0
ganador=0
#Impresión de nombre de candidatp+ porcentake+ numero de votos
for k in range(len(number_of_votes)):
    print (my_list_of_candidates[k],":",percentages[k],"%","(",number_of_votes[k],")")
    #valor para ser comparado
    deltare=number_of_votes[k]
    if k==0:
        #Guarda valor para comparar
        ganador=number_of_votes[k]
    else:
        #Calculo del numero mas graande
        if deltare>ganador:
            #si es mayor cambia el valor por el mayor
            ganador=deltare
            #Guarda el lugar donde ocurrió el cambio
            contav=k
        else:
            #sino ganador se queda igual
            ganador=ganador
print("---------------------------------------------")
print("Winner: ", my_list_of_candidates[contav])
print("---------------------------------------------")
#--------------------------txt file-----------------------------
z=0
with open(election_analysis,"w") as txt_file:
    impresion= (f"Election Results\n\n"
               f"-----------------------------------\n\n"
               f"Total Votes:{str(novot)}\n\n"
               f"-----------------------------------\n\n")
               #f"Total Months:{str(len(my_list_date))}\n"
               #f"Total: $ {str(netpl)}\n"
               #f"Average change: $ {str(avercha)}\n"
               #f"Greatest Increase in Profits: {str(my_list_date[aptri])}(%{str(GIPe)})\n"
               #f"Greatest Decrease in Profits: {str(my_list_date[aptrd])}(%{str(GDPe)})\n"
    txt_file.write(impresion)
    for k in range(len(number_of_votes)):
        txt_file.write (my_list_of_candidates[k])
        txt_file.write(": ")
        txt_file.write (str(percentages[k]))
        txt_file.write("% (")
        txt_file.write (str(number_of_votes[k]))
        txt_file.write(")\n\n")
    impresion2=(f"---------------------------------------------\n\n"
               f"Winner: {(my_list_of_candidates[contav])}\n\n"
               f"---------------------------------------------\n")
    txt_file.write(impresion2)
#print (my_list_of_candidates[k],":",percentages[k],"%","(",number_of_votes[k],")")
#":",percentages[k],"%","(",number_of_votes[k],")")

        