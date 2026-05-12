Este proyecto explora el potencial de las Redes Neuronales aplicadas a la Visión por Computadora. Utiliza la librería DeepFace, que proporciona modelos pre-entrenados de última generación para resolver problemas complejos de reconocimiento facial con una API sencilla y potente.
El objetivo es transitar de la teoría de redes neuronales a la creación de un servicio o producto de usuario final que pueda integrarse en entornos del mundo real.

Capacidades del Sistema
Función DescripciónReconocimiento FacialIdentifica personas dentro de una base de datos de fotos Análisis de Atributos Detecta edad, género y emoción del rostro capturadoRegistro de AsistenciaGuarda automáticamente nombre y hora en un archivo CSV

Requisitos del Sistema

Sistema Operativo: Windows 10/11 (nativo)
Python: 3.9 o superior
Cámara web: conectada y funcional
Git: para clonar el repositorio


Nota sobre WSL: Este proyecto utiliza la ventana gráfica de OpenCV (cv2.imshow) y acceso directo a la cámara, por lo que no es compatible con WSL. Ejecutar en Windows nativo.


Instalación y Uso
1. Clonar el repositorio
bash
git clone : https://github.com/AlbertoHiru/Computer-Vision_HR.git
3. Crear entorno virtual
bash
python -m venv venv
.\venv\Scripts\Activate.ps1
4. Instalar dependencias
bash:
pip install -r requirements.txt

La primera ejecución descargará automáticamente los modelos de DeepFace Requiere conexión a internet.

4. Preparar la base de datos de rostros
Agrega fotos a la carpeta db/ con el nombre de cada persona como nombre de archivo:
db/
├── Messi.jpg
├── light_Yagami.jpg
└── Noel_Gallgher.jpg


Una foto por persona es suficiente
El nombre del archivo se usará como nombre en el registro de asistencia
Formatos soportados: .jpg, .jpeg, .png

5. Ejecutar
bash:
python main.py

Controles
Una vez abierta la ventana de la cámara, usa el teclado:
TeclaAcción1Seleccionar modo: Reconocimiento facial2Seleccionar modo: Análisis de atributos3Seleccionar modo: Reconocimiento + AtributosESPACIOCapturar frame y ejecutar el modo seleccionadoQSalir del programa

Archivos generados
ArchivoDescripciónasistencia.csvRegistro de personas identificadas con fecha y horaultimo_frame.jpgÚltima captura tomada por la cámara

Casos de Uso Implementados

Asistencia Automatizada: Registro de entrada en oficinas o aulas mediante detección en tiempo real.
Análisis de Audiencia: Detección de atributos demográficos para sistemas de personalización.
Hogar Inteligente: Identificación del usuario para personalizar el ambiente.


Lineamientos de Desarrollo

Las funcionalidades de visión implementan detección, reconocimiento y análisis de atributos con DeepFace.
Las acciones físicas (encender luz, reproducir música) se simulan con mensajes en consola para demostrar la lógica del servicio.


Créditos
Desarrollado como parte del módulo de Computer Vision, utilizando el framework DeepFace creado por Sefik Ilkin Serengil.
