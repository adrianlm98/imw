def add_contacts(phone_book, name, phone):
    phone_book[name] = phone

def show_contacts(phone_book):
    if phone_book == {}:
        print("No hay ningún número añadido")
    for name, number in phone_book.items():
        print("{}: {}".format(name, number))

def remove_contact(phone_book, name):
    del(phone_book[name])

def menu():
    phone_book = {}
    while True:
        print("1. Mostrarme los contactos")
        print("2. Añadir los contactos")
        print("3. Eliminar los contactos")
        print("4. Salir")
        option = input("Opción: ")
        if option == "1":
            show_contacts(phone_book)
        if option == "2":
            name = input("Introducir un nombre: ")
            if name in phone_book:
                print("El nombre ya existe")
            else:
                phone = input("Introduzca un número de teléfono: ")
                phone_numbers = len(phone)
                if phone_numbers == 9:
                    add_contacts(phone_book, name, phone)
                else:
                    print("Número incorrecto")
        if option == "3":
            name = input("Introduzca el nombre que quiera eliminar : ")
            if name not in phone_book:
                print("El nombre no existe")
            else:
                remove_contact(phone_book, name)
        if option == "4":
            print("Adiós")
            break

menu()

