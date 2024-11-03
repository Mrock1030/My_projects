#this program is for generator password for diferente web site

#importamos la libreria de random
import random
#importamos la nueva libreria que nos permita crear los QR
import qrcode
#importamos el OS para que guarde los archivos en una ruta especifica
import os 
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
        print("Input to number correct")
        
#creamos un for para generar la contraseña
password = ""
for pwd in range(lenght):
    password += random.choice(characters)
    
#imprimimos la contraseña        
#print("Here is your password: " + password)
qr = qrcode.make(password)

#Creamos el path para que se guarden los archivos
save_path = "/home/juanka/Documents/qr_passwords"

#en caso de que no existe el path
if not os.path.exists(save_path):
    os.makedirs(save_path)
    
# Guardamos el código QR en la ruta especificada
qr.save(os.path.join(save_path, "password_qr.png"))

print("Generate your QR \n") 
print("Here is your password: " + password)
