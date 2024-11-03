#this program is for generator password for diferente web site

#importamos la libreria de random
import random 
print(" Welcome to your Password Generator")

#creamos una variable de caracteres
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@!#$%&()?¿¡'
##anotherchartes = 
#añadimos una varibale para saber de cuantos caracteres quieres la contraseña
while True:
    try :
        lenght = int(input("Input your password lenght: "))
        print("\n"*20)
        break
    except ValueError:
        print("\n"*50)
        print("Ingrese un numero correcto")
        
#creamos un for para generar la contraseña
password = ""
for pwd in range(lenght):
    password += random.choice(characters)
    
#imprimimos la contraseña        
print("Here is your password: " + password)

        
