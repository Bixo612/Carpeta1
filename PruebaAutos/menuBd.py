def leerEntero(txt):
    try:
        return int(input(txt))
    except:
        return None

#Menu

def printMenu():
    print("Menu")
    print("0 - Salir")
    print("1 - Listar Db")
    print("")

def menu():

    exit = True
    while exit:
        op = None
        printMenu()
        op = leerEntero("Ingrese una opcion:")
        if op == 0:
            exit = False
            print ("Hasta pronto")
            input ("")

        
#!/usr/bin/env python3

# Take an user input
name = input("What is your name? ")
# Check the input value

if(name != ""):
   # Print welcome message if the value is not empty
   print("Hello %s, welcome to our site" %name )
else:
   # Print empty message
   print("The name can't be empty.")

# Wait for the user input to terminate the program
input("Press any key to terminate the program")
# Print bye message
print("See you later.")




