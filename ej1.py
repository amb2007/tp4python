def agregar_tarea(tareas, tarea, fecha_limite,propiedad, completada= False):
    nueva_tarea= {"tarea": tarea, "fecha limite": fecha_limite, "prioridad": propiedad, "completada" : completada}
    tareas.append(nueva_tarea)
    print("tarea agregada exitosamente")

def mostrar_tareas(tareas, completadas):
    tareas_filtradas = tareas
    if completadas is not None:
        tareas_filtradas = [t for t in tareas if t["completada"] == completadas]
    
    if not tareas_filtradas:
        print("No hay tareas para mostrar.")
    else:
        for i, tarea in enumerate(tareas_filtradas, 1):
            print(f"\nTarea {i}:")
            for clave, valor in tarea.items():
                print(f"{clave}: {valor}")

def marcar_completada(lista_tareas):
    ind = int(input("ingrese un indice de tarea: ")) - 1
    lista_tareas[ind]["completada"] = True
if __name__ == "__main__":
    lista_tareas= []
    while True:
        print("\n1. Agregar tarea")
        print("2. mostrar tarea")
        print("3. marcar tarea como completada")
        print("salir")
        opcion = input("seleccione una opcion")
        if opcion == "1":
            tarea_nueva = input("ingrese la descripcion de la tarea: ")
            fecha_limite_nueva = input("ingrese una fecha limite nueva en formato dd/mm/yyyy: ")
            prioridad_nueva = input("ingrese una prioridad: ")
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva)
        elif opcion == "2":
            comp= input("quiere solo ver las completas, las incompletas o todas? ")
            if comp == "completas":
                mostrar_tareas(lista_tareas, completadas = True)
            elif comp == "incompletas":
                mostrar_tareas(lista_tareas, completadas = False)
            else:
                mostrar_tareas(lista_tareas, completadas = None)
            
        elif opcion == "3":
            marcar_completada(lista_tareas)
        elif opcion == "4":
            break
        else:
            print("opcion no valida")