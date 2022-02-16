import os

def main():
    os.system("clear")

    print("AREA Y PERIMETRO DE UN CUADRADO")
    print("===============================")
    print("\n")

    lado=float(input("Lado del cuadrado:"))

    perimetro = 4 * lado
    area = lado ** 2

    print(f"El perimetro del cuadrado es: {perimetro:.2f}")
    print(f"El área del cuadrado es: {area:.2f}")

if __name__=='__main__':
    main()
