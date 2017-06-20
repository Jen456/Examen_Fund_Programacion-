numero= int(input('Ingrese numero:\n'))
contador =0 
lista_mul= []
lista_sum=[]
mul=1
suma=0
while (): 
    numero= numero /10
    if contador==1 or contador ==3: 
        lista_mul.append(numero)
        contador= contador+1
    else: 
        lista_sum.append(numero)
        contador= contador+1

for i in lista_mul:
   
    mul= mul*i 

for j in lista_sum:
    
    suma+=j 

result= mul+suma
result= result%10
print ("Codigo valido\n")
print(result)
