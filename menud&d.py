import json
import requests
import os

try:
    #    resp = requests.get('http://www.dnd5eapi.co/api/')
    #    if resp.status_code==200:
    while True:

        os.system("cls")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("*-*Bienvenido al manual del Dungeon Master de D&D5*-*")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("¿Que quieres conocer, viajero?")
        print("\t1. Caracteristicas de personaje")
        print("\t2. Clases")
        print("\t3. Razas")
        print("\t4. Equipamiento")
        print("\t5. Hechizos")
        print("\t6. Monstruos")
        print("\t7. Cerrar manual")
        opcion = int(input())

# aqui empiezan las caracteristicas personales
        if opcion == 1:
            while True:
                os.system("cls")
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                print("*-*Caracteristicas de personaje*-*")
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                print("\t1. Puntos de experiencia")
                print("\t2. Habilidades")
                print("\t3. Conocimientos")
                print("\t4. Idiomas")
                print("\t5. Volver")
                opcion = int(input())

                if opcion == 1:
                    api_address = 'http://www.dnd5eapi.co/api/ability-scores'

                    os.system("cls")
                    resp = requests.get(api_address)

                    if resp.status_code == 200:
                        datos = json.loads(resp.content)
                        for dato in datos['results']:
                            print(dato['name'])

                    input("Pulse para continuar...")

                elif opcion == 2:
                    api_address = 'http://www.dnd5eapi.co/api/skills'
                    os.system("cls")
                    resp = requests.get(api_address)
                    if resp.status_code == 200:
                        datos = json.loads(resp.content)

                        for dato in datos['results']:
                            print(dato['name'])

                    input("Pulsa para continuar...")

                elif opcion == 3:
                    api_address = 'http://www.dnd5eapi.co/api/features'
                    os.system("cls")
                    resp = requests.get(api_address)
                    if resp.status_code == 200:
                        datos = json.loads(resp.content)

                        for dato in datos['results']:
                            print(dato['name'])

                    input("Pulse para continuar...")

                elif opcion == 4:
                    api_address = 'http://www.dnd5eapi.co/api/languages'
                    os.system("cls")
                    resp = requests.get(api_address)
                    if resp.status_code == 200:
                        datos = json.loads(resp.content)

                        for dato in datos['results']:
                            print(dato['name'])

                    input("Pulse para continuar...")
                elif opcion == 5:
                    break
                else:
                    print("Error, vuelve a introducir el numero")
                    input("Pulse para continuar...")

# aqui empiezan las clases
        elif opcion == 2:
            api_address = 'http://www.dnd5eapi.co/api/classes'

            os.system("cls")
            resp = requests.get(api_address)
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("*-*Clases de los personajes*-*")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            if resp.status_code == 200:
                datos = json.loads(resp.content)

                for dato in datos['results']:
                    print(dato['name'])

            input("pulse para continuar")

# las razas
        elif opcion == 3:
            api_address = 'http://www.dnd5eapi.co/api/races'

            os.system("cls")
            resp = requests.get(api_address)
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("*-*Razas de los personajes*-*")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            if resp.status_code == 200:

                datos = json.loads(resp.content)

                for dato in datos['results']:
                    print(dato['name'])

            input("pulse para continuar")

# el equipamiento
        elif opcion == 4:
            api_address = 'http://www.dnd5eapi.co/api/equipment'

            os.system("cls")
            resp = requests.get(api_address)
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("*-*Equipamiento de personajes*-*")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            if resp.status_code == 200:

                datos = json.loads(resp.content)

                for dato in datos['results']:
                    print(dato['name'])

            input("pulse para continuar")

# los hechizos
        elif opcion == 5:
            api_address = 'http://www.dnd5eapi.co/api/spells'

            os.system("cls")
            resp = requests.get(api_address)
            print("*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("*-*Hechizos existentes*-*")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*")
            if resp.status_code == 200:

                datos = json.loads(resp.content)

                for dato in datos['results']:
                    print(dato['name'])

            input("pulse para continuar")

# los monstruos
        elif opcion == 6:
            api_address = 'http://www.dnd5eapi.co/api/monsters'

            os.system("cls")
            resp = requests.get(api_address)
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("*-*Monstruos y villanos*-*")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-")
            if resp.status_code == 200:
                datos = json.loads(resp.content)

                for dato in datos['results']:
                    print(dato['name'])

            input("pulse para continuar")

# y salimos
        elif opcion == 7:
            break

        else:
            print("Error, por favor, vuelve a introducir eleccion")
            input("Pulse para continuar...")

except:
    print("Error, por favor, espere...")
