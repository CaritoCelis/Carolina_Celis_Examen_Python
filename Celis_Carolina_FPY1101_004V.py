import random
import csv

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez",
                "Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def asignar_sueldos_aleatorios():
    sueldos = []
    for _ in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    return sueldos

def clasificar_sueldos(sueldos):
    print("\nSueldos menores a $800.000")
    print("TOTAL:", len([s for s in sueldos if s < 800000]))
    print("Nombre empleado\t-\tSueldo")
    for nombre, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            print(f"{nombre}\t-\t${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000")
    print("Total:", len([s for s in sueldos if 800000 <= s <= 2000000]))
    print("Nombre empleado\t-\tSueldo")
    for nombre, sueldo in zip(trabajadores, sueldos):
        if 800000 <= sueldo <= 2000000:
            print(f"{nombre}\t-\t${sueldo}")
    
    print("\nSueldos superiores a $2.000.000")
    print("Total:", len([s for s in sueldos if s > 2000000]))
    print("Nombre empleado\t-\tSueldo")
    for nombre, sueldo in zip(trabajadores, sueldos):
        if sueldo > 2000000:
            print(f"{nombre}\t-\t${sueldo}")
    
    total_sueldos = sum(sueldos)
    print(f"\nTotal sueldos: ${total_sueldos}")

def ver_estadisticas(sueldos):
    sueldo_mas_alto = max(sueldos)
    sueldo_mas_bajo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)
    
    media_geom = 1
    for sueldo in sueldos:
        media_geom *= sueldo
    media_geom = media_geom ** (1 / len(sueldos))
    
    print("\n--- Estadísticas de Sueldos: ---")
    print(f"Sueldo más alto:\t${sueldo_mas_alto}")
    print(f"Sueldo más bajo:\t${sueldo_mas_bajo}")
    print(f"Promedio de sueldos:\t${promedio_sueldos:.2f}")
    print(f"Media geométrica:\t${media_geom:.2f}")

def reporte_sueldos(sueldos):
    descuento_salud = 0.07
    descuento_afp = 0.12
    
    print("\n--- Reporte de Sueldos: ---")
    print("Nombre empleado\t-\tSueldo Base\t-\tDescuento Salud\t-\tDescuento AFP\t-\tSueldo Líquido")
    for nombre, sueldo in zip(trabajadores, sueldos):
        desc_salud = sueldo * descuento_salud
        desc_afp = sueldo * descuento_afp
        sueldo_liquido = sueldo - desc_salud - desc_afp
        print(f"{nombre}\t\t${sueldo}\t\t${desc_salud:.2f}\t\t${desc_afp:.2f}\t\t${sueldo_liquido:.2f}")
    
    
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])
        for nombre, sueldo in zip(trabajadores, sueldos):
            desc_salud = sueldo * descuento_salud
            desc_afp = sueldo * descuento_afp
            sueldo_liquido = sueldo - desc_salud - desc_afp
            writer.writerow([nombre, sueldo, desc_salud, desc_afp, sueldo_liquido])

# Menú principal
if __name__ == "__main__":
    sueldos = []
    while True:
        print("\n--- Menú Principal ---")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opc = input("Seleccione una opción (1-5): ")
        
        if opc == "1":
            sueldos = asignar_sueldos_aleatorios()
            print("\nSueldos asignados aleatoriamente.")
        elif opc == "2":
            if not sueldos:
                print("Primero debe asignar los sueldos aleatorios (opción 1).")
            else:
                clasificar_sueldos(sueldos)
        elif opc == "3":
            if not sueldos:
                print("Primero debe asignar los sueldos aleatorios (opción 1).")
            else:
                ver_estadisticas(sueldos)
        elif opc == "4":
            if not sueldos:
                print("Primero debe asignar los sueldos aleatorios (opción 1).")
            else:
                reporte_sueldos(sueldos)
                print("\nReporte de sueldos generado en 'reporte_sueldos.csv'.")
        elif opc == "5":
            print("\nFinalizando programa...\nDesarrollado por Carolina Celis Ahumada\nRUT: 18.424.822-0.\n")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1-5).")
