
1
edad= int(input("Cuantos años tienes?"))
if (edad>=65) or (edad<5):
    print("Con",edad,"años;te sale gratis")
else:
    print("Con",edad,"años,pagas 2.5")
    
    
    
    
2 
sexo=input("Que sexo eres?")
pelo=input("De que color es tu pelo")
edad=int(input("Cuantos años tienes?"))
if (edad<=65)and(sexo=="H"):
    print("Con",edad,"años y siendo",sexo,"te sale a 1")
if (edad>=65):
    print("Con",edad,"te sale gratis")
if (edad<=65)and(sexo=="M")and(pelo=="R"):
    print("Con",edad,"siendo",sexo,"y con el pelo",pelo,"te sale gratis")
else:
    print("Con",edad,"siendo",sexo,"y con el pelo",pelo,"pagas 0,5")
    
    
    
    
    3
    edad= int(input("Cuantos años tienes?"))
if (edad== 17 )or (edad<=23) or (edad>=18):
print("Con",edad,"años;tienes que ir a la sesión jóvenes")
