#Laboratorio 6 Evelyn Feng Wu B82870


def get_user_input():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operacion = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
        return num1, num2, operacion
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        return get_user_input()

# Acá se define funciones lambda para cada operación
suma = lambda x, y: x + y
resta = lambda x, y: x - y
multiplicacion = lambda x, y: x * y
division = lambda x, y: x / y if y != 0 else "Division por cero"

# Utiliza un diccionario para mapear operaciones a funciones lambda
operaciones = {
    '+': suma,
    '-': resta,
    '*': multiplicacion,
    '/': division
}
# Acá se extiende el menu utilizando callbacks para invocar cada operación
def ejecutar_operacion(user_input, callback):
    num1, num2, operacion = user_input
    result = callback(num1, num2)
    print("Resultado:", result)

def main():
    while True:
        user_input = get_user_input()

        if user_input[2].lower() == 'exit':
            print("Salir.")
            break

        print("\nCalculando...")

        if user_input[2] in operaciones:
            ejecutar_operacion(user_input, operaciones[user_input[2]])
        else:
            print("Operacion invalida. Seleccione (+, -, *, /) o  escriba 'exit' para salir.")

if __name__ == "__main__":
    main()

