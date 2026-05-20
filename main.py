
import requests

BASE_URL = "https://api-colombia.com/api/v1"

#Información general de Colombia
def info_pais():
    url = f"{BASE_URL}/Country/Colombia"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n--- Información de Colombia ---")
        print(f"Nombre: {data['name']}")
        print(f"Descripción: {data['description']}")
        print(f"Moneda: {data['currency']}")
    else:
        print("Error al consultar la API")

#Departamentos y capitales
def departamentos():
    url = f"{BASE_URL}/Department"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n--- Departamentos ---")
        for dep in data:
            print(f"{dep['name']} - Capital: {dep['cityCapital']}")
    else:
        print("Error al consultar la API")

#Regiones y su descripción
def regiones():
    url = f"{BASE_URL}/Region"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n--- Regiones ---")
        for reg in data:
            print(f"{reg['name']} - {reg['description']}")
    else:
        print("Error al consultar la API")

#Atracciones turísticas
def atracciones():
    url = f"{BASE_URL}/TouristicAttraction"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n--- Atracciones Turísticas ---")
        for a in data:
            print(f"{a['name']} - Ciudad: {a['city']['name']}")
    else:
        print("Error al consultar la API")

#Menú interactivo
def menu():
    while True:
        print("\n===== MENÚ =====")
        print("1. Información del país")
        print("2. Departamentos")
        print("3. Regiones")
        print("4. Atracciones turísticas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            info_pais()
        elif opcion == "2":
            departamentos()
        elif opcion == "3":
            regiones()
        elif opcion == "4":
            atracciones()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()