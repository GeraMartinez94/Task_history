Descripción
El Asistente de Tareas es una aplicación en línea de comandos para gestionar tus tareas diarias. Permite agregar, visualizar, actualizar, eliminar y exportar tareas. Además, incluye funcionalidades como notificaciones de tareas próximas al vencimiento y búsquedas personalizadas por palabras clave o prioridad.

Funcionalidades
Ver Tareas: Muestra todas las tareas almacenadas con su información detallada.
Agregar Tareas: Permite añadir una nueva tarea con nombre, prioridad y fecha límite.
Actualizar Tareas: Modifica los detalles de una tarea existente (nombre, prioridad, fecha límite o estado).
Eliminar Tareas: Elimina una tarea específica por su ID.
Exportar Tareas a CSV: Genera un archivo CSV con las tareas existentes.
Buscar Tareas: Encuentra tareas por palabra clave en el nombre o por prioridad.
Notificaciones: Muestra tareas próximas al vencimiento (dentro de 3 días).
Historial de Acciones: Registra las operaciones realizadas en un archivo de log.
Requisitos
Python 3.6 o superior.
Bibliotecas estándar: os, json, csv, y datetime.
Instalación
Clona este repositorio o descarga el archivo principal.
Asegúrate de tener Python 3 instalado en tu sistema.
Ejecuta el script directamente desde la terminal.
Uso
Ejecutar el programa:
bash
Copiar código
python nombre_del_script.py
Seleccionar una opción del menú:
Sigue las instrucciones en pantalla para gestionar tus tareas.
Estructura del Proyecto
bash
Copiar código
data/
│   ├── tasks.json      # Archivo donde se almacenan las tareas.
│   ├── log.txt         # Registro de acciones realizadas.
├── nombre_del_script.py  # Código principal.
Exportar Tareas
Las tareas se pueden exportar a un archivo CSV ejecutando la opción correspondiente en el menú. El archivo resultante (tasks.csv) estará disponible en el directorio raíz del proyecto.

Ejemplo de Uso
Agregar una tarea
Selecciona la opción 2. Agregar Tarea.
Ingresa el nombre, prioridad (Baja, Media, Alta) y fecha límite en el formato AAAA-MM-DD.
Ver las tareas
Selecciona la opción 1. Ver Tareas para ver la lista completa.
Actualizar una tarea
Selecciona la opción 3. Actualizar Tarea.
Ingresa el ID de la tarea a modificar y los nuevos valores. Deja los campos en blanco si no deseas cambiar algo.
Eliminar una tarea
Selecciona la opción 4. Eliminar Tarea.
Proporciona el ID de la tarea a eliminar.
Exportar a CSV
Selecciona la opción 5. Exportar Tareas a CSV.
El archivo tasks.csv será creado automáticamente.
Registro de Cambios
Cada acción (agregar, actualizar o eliminar) queda registrada en el archivo data/log.txt con la fecha y hora correspondiente.

Contribuciones
Contribuciones, reportes de errores y sugerencias son bienvenidos. Por favor, abre un issue o realiza un pull request.

Licencia
Este proyecto está licenciado bajo la MIT License.

