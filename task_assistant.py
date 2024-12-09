import os
import json
import csv
from datetime import datetime, timedelta

os.makedirs('data', exist_ok=True)

TASKS_FILE = 'data/tasks.json'

def load_tasks():
    """Cargar tareas desde un archivo JSON."""
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Guardar tareas en un archivo JSON."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def parse_date(input_date):
    """Intentar interpretar la fecha y convertirla a AAAA-MM-DD."""
    for fmt in ('%Y-%m-%d', '%Y.%m.%d', '%Y/%m/%d'):
        try:
            return datetime.strptime(input_date, fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    raise ValueError("Formato de fecha inválido. Usa AAAA-MM-DD.")

def add_task(tasks, name, priority, deadline):
    """Agregar una nueva tarea."""
    task = {
        "id": len(tasks) + 1,
        "name": name,
        "priority": priority,
        "deadline": deadline,
        "status": "Pendiente"
    }
    tasks.append(task)
    save_tasks(tasks)
    log_action("Agregada", task)
    print("¡Tarea agregada con éxito!")

def view_tasks(tasks):
    """Mostrar todas las tareas."""
    if not tasks:
        print("No hay tareas disponibles.")
    else:
        print("\nTareas:")
        for task in tasks:
            print(f"ID: {task['id']} | Nombre: {task['name']} | Prioridad: {task['priority']} | "
                  f"Fecha límite: {task['deadline']} | Estado: {task['status']}")

def update_task(tasks, task_id, status=None, name=None, priority=None, deadline=None):
    """Actualizar una tarea existente."""
    for task in tasks:
        if task["id"] == task_id:
            if name:
                task["name"] = name
            if priority:
                task["priority"] = priority
            if deadline:
                task["deadline"] = deadline
            if status:
                task["status"] = status
            save_tasks(tasks)
            log_action("Actualizada", task)
            print("¡Tarea actualizada con éxito!")
            return
    print("No se encontró la tarea.")

def delete_task(tasks, task_id):
    """Eliminar una tarea."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            log_action("Eliminada", task)
            print("¡Tarea eliminada con éxito!")
            return
    print("No se encontró la tarea.")

def search_tasks(tasks, keyword=None, priority=None):
    """Buscar tareas por palabra clave o prioridad."""
    results = [
        task for task in tasks
        if (keyword and keyword.lower() in task["name"].lower()) or
           (priority and priority.lower() == task["priority"].lower())
    ]
    if results:
        print("\nTareas encontradas:")
        for task in results:
            print(f"ID: {task['id']} | Nombre: {task['name']} | Prioridad: {task['priority']} | "
                  f"Fecha límite: {task['deadline']} | Estado: {task['status']}")
    else:
        print("No se encontraron tareas.")

def notify_upcoming_tasks(tasks):
    """Mostrar tareas cuya fecha límite está cerca."""
    today = datetime.today()
    upcoming = [
        task for task in tasks
        if datetime.strptime(task['deadline'], '%Y-%m-%d') - today <= timedelta(days=3) and
           task['status'] == 'Pendiente'
    ]
    if upcoming:
        print("\n⚠️ Tareas próximas al vencimiento:")
        for task in upcoming:
            print(f"ID: {task['id']} | Nombre: {task['name']} | Fecha límite: {task['deadline']}")
    else:
        print("\nNo hay tareas próximas al vencimiento.")

def export_tasks_to_csv(tasks, filename='tasks.csv'):
    """Exportar tareas a un archivo CSV."""
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'priority', 'deadline', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)
    print(f"Tareas exportadas a {filename} con éxito.")

def log_action(action, task):
    """Registrar acciones en un archivo log."""
    with open('data/log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()} - {action}: {task}\n")

def main():
    tasks = load_tasks()
    notify_upcoming_tasks(tasks) 

    while True:
        print("\nMenú del Asistente de Tareas:")
        print("1. Ver Tareas")
        print("2. Agregar Tarea")
        print("3. Actualizar Tarea")
        print("4. Eliminar Tarea")
        print("5. Exportar Tareas a CSV")
        print("6. Buscar Tareas")
        print("7. Salir")
        choice = input("Elige una opción: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            name = input("Introduce el nombre de la tarea: ")
            priority = input("Introduce la prioridad (Baja, Media, Alta): ")
            deadline = input("Introduce la fecha límite (AAAA-MM-DD): ")
            try:
                deadline = parse_date(deadline) 
                add_task(tasks, name, priority, deadline)
            except ValueError as e:
                print(e)
        elif choice == '3':
            task_id = int(input("Introduce el ID de la tarea a actualizar: "))
            print("Deja en blanco si no quieres cambiar un campo.")
            name = input("Nuevo nombre: ") or None
            priority = input("Nueva prioridad (Baja, Media, Alta): ") or None
            deadline = input("Nueva fecha límite (AAAA-MM-DD): ") or None
            try:
                if deadline:
                    deadline = parse_date(deadline)
                status = input("Nuevo estado (Pendiente, Completada): ") or None
                update_task(tasks, task_id, status, name, priority, deadline)
            except ValueError as e:
                print(e)
        elif choice == '4':
            task_id = int(input("Introduce el ID de la tarea a eliminar: "))
            delete_task(tasks, task_id)
        elif choice == '5':
            export_tasks_to_csv(tasks)
        elif choice == '6':
            print("Buscar tareas:")
            keyword = input("Introduce una palabra clave (o deja en blanco): ")
            priority = input("Introduce una prioridad (Baja, Media, Alta) o deja en blanco: ")
            search_tasks(tasks, keyword or None, priority or None)
        elif choice == '7':
            print("¡Adiós!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
