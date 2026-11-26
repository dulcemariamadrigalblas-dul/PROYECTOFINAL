print ("INICIO MAIN")

from clases.cultivo import Cultivo
from clases.gestor import GestorCultivos


def solicitar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un numero entero valido.")


def solicitar_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingrese un numero valido.")


def registrar_cultivo(gestor):

    numero = solicitar_entero(
        "Numero de caja: "
    )

    colonias = solicitar_entero(
        "Cantidad de colonias: "
    )

    dilucion = solicitar_decimal(
        "Dilucion: "
    )

    volumen = solicitar_decimal(
        "Volumen: "
    )

    medio = input(
        "Tipo de medio: "
    )

    cultivo = Cultivo(
    numero,
    medio,
    dilucion,
    volumen,
    colonias
    )
    gestor.agregar_cultivo(
        cultivo
    )

    print(
        "\nCultivo registrado."
    )


def mostrar_menu():

    print("\n" + "=" * 40)
    print("SISTEMA MICROBIOLOGICO")
    print("=" * 40)

    print("1. Registrar cultivo")
    print("2. Mostrar cultivos")
    print("3. Buscar cultivo")
    print("4. Estadisticas")
    print("5. Salir")


def main():

    gestor = GestorCultivos()

    while True:

        mostrar_menu()

        opcion = input(
            "\nSeleccione una opcion: "
        )

        if opcion == "1":

            registrar_cultivo(
                gestor
            )

        elif opcion == "2":

            gestor.mostrar_todos()

        elif opcion == "3":

            numero = solicitar_entero(
                "Numero de caja: "
            )

            gestor.buscar_cultivo(
                numero
            )

        elif opcion == "4":

            gestor.estadisticas()

        elif opcion == "5":

            print(
                "\nPrograma finalizado."
            )

            break

        else:

            print(
                "\nOpcion invalida."
            )


if __name__ == "__main__":
    main()