import os
import csv
#Para revisar donde empieza el programa
print("corriendo......")
#Ruta del archivo
budget_data=os.path.join("../PyBank/Resources/budget_data.csv")
#Archivo donde se escribira en txt
financial_analysis=os.path.join("../PyBank/analysis/financial_analysis.txt")
#Abre el archivo

with open(budget_data) as my_file:
#    #separa por comas
    csv_reader=csv.reader(my_file,delimiter=",")
    #Se salta el primero
    next(csv_reader,None)
    nomon=0
    netpl=0
    sumcha=0
    #Apuntadores para saber en que fila esta el cambio
    aptri=0
    aptrd=0
    my_list=[]
    my_list_date=[]
    
    for each_line in csv_reader:
        #Guarda el valor de las fechas
        datebud=each_line[0]
        #Guarda el valor de profit or loss
        PrL=int(each_line[1])
        #Va sumando los valores de profit or loss
        netpl=netpl+PrL
        #print("profit/loss",{PrL},"Date",{datebud})
        #Agrega los valores a una lista
        my_list.append(PrL)
        #agregan las fechas a una lista 
        my_list_date.append(datebud)
        

"imprime numero de meses y net pl"
print("Financial Analysis")
print("-------------------------------------------")
print("Total Months:  ",len(my_list_date))
print("Total:  $",netpl)
#---------------------- change average calculation------------------"
#Contador
contav=0
mx=0
for i in range (len(my_list_date)):
    #Si es cero no resta el valor anterior
    if i==0:
        sumcha=0
        GIPe=0
        GDPe=0
    #Apartir de uno va restandom el valor anterior
    else:
        #variable que indica el numero anterior de lalista
        x=i-1
        #guarda solo el valor de la resta
        deltare=my_list[i]-my_list[x]
        #Va acumulando la resta del varior anterior
        sumcha=sumcha+my_list[i]-my_list[x]
        #cuenta para obtener average
        contav=contav+1
        #Calculo del numero mas graande
        if deltare>GIPe:
            GIPe=deltare
            #Guarda el lugar donde ocurrió el cambio
            aptri=i
        else:
            GIPe=GIPe
        #calculo del numero mas pequeño
        if deltare<GDPe:
            GDPe=deltare
            #Guarda el lugar donde ocurrió el cambio
            aptrd=i
        else:
            GDPe=GDPe
       
#obtiene el promedio de change
mx=sumcha/contav
#Redondea dos
avercha=round(mx,2)
#Impresion de resultados
totam=str(contav)
print("Average change: $",avercha)
print("Greatest Increase In Profits:",my_list_date[aptri],"(%",GIPe,")")
print("Greatest Decrease In Profits:",my_list_date[aptrd],"(%",GDPe,")")
#-------------------------------------------Impresion en txt-------------------------
with open(financial_analysis,"w") as txt_file:
    impresion=(f"Financial Analysis\n\n"
               f"-----------------------------------\n\n"
               f"Total Months: {str(len(my_list_date))}\n\n"
               f"Total: ${str(netpl)}\n\n"
               f"Average change: ${str(avercha)}\n\n"
               f"Greatest Increase in Profits: {str(my_list_date[aptri])} (${str(GIPe)})\n\n"
               f"Greatest Decrease in Profits: {str(my_list_date[aptrd])} (${str(GDPe)})\n\n"
               )
    txt_file.write(impresion)






