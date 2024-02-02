import csv

#Importa la identacion para el archivo csv
"""
with open('names.csv', 'r') as names:
    csv_reader = csv.reader(names) 
    
    # Si queremos saltearnos la primera linea de codigo entonces antes del bucle for voy a usar esto:
    
    next(csv_reader)
    
    for line in csv_reader:
       print(line)
       #print(line[2])"""
    
#indices empizan en 0 y suman consecutivamente
#Un archivo CSV esta indexado por lo tanto 
#si tenemos un indice de como estan ordenados los archivos csv por ejemplo tendriamos
#"Mary"   ,   "Smith-Robinson" , "maryjacobs@gmail.com"
#  0                1                     2     
#Por lo tanto si hacemos print(line[2]) en un bucle FOR esto nos va a devolver el mail de los mismos.
#Tambien podemos saltearnos la primera linea por ejemplo para no printear la palabra mail

#Ahora vamos a suponer que quiero guardar ciertos valores en un nuevo archivo CSV y, por ejemplo usar / 
#En lugar de comas es decir alterar el archivo y liberar otro archivo nuevo modificado.



"""with open('names.csv', 'r') as names:                           #abris el archivo
    csv_reader = csv.reader(names)                             #creas la nueva variable con el archivo original como reader en este caso
    
    with open('news.csv', 'w') as new_file:                 #abris un nuevo archivo para escritura (writer) y dentro del mismo estableces parametros
        csv_writer = csv.writer(new_file, delimiter= '\t')  #Este es la forma de escribir un nuevo archivo csv 
                                                            #\t es una tabulacion de python
                                                            #delimitador alterado con el segundo argumento de la funcion writer
    
        for line in csv_reader:
          csv_writer.writerow(line)                 # lo que vamos a sobre escribir en cada linea dentro del bucle for
                                                    #para que haga la operacion en cada una de las lineas
                                                    #Y sobreescriba sobre el READER es decir el archivo viejo usando las variables del writer}
                                                    
                                                    
#esto no nos va a generar ningun output pero nos va a crear en nuestra carpeta el nuevo archivo "news.csv"""

"""with open('names.csv', 'r') as names:                           #abris el archivo
    csv_reader = csv.DictReader(names)                     #Esto hace que sea un diccionario es decir un nombre y un valor
    for line in csv_reader:
        print(line['last_name'])                                  #Esto hace que la informacion sea mas facil de extrear
                                                            #podemos hacer uso de las palabras clave del diccionario
        
        """



with open('names.csv', 'r') as names:                          
    csv_reader = csv.DictReader(names)                    
    
    with open('news.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', ]    #podemos skipear el email por ejemplo pero despues hay que del
        csv_writer= csv.DictWriter(new_file, fieldnames= fieldnames, delimiter = '\t')         #cuando usamos el writer hay que aclarar los fields
        csv_writer.writeheader()           #escribe el header/encabezado
        for line in csv_reader:
            del line['email ']
            csv_writer.writerow(line)
            


