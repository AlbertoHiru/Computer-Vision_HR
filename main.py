import cv2
import pandas as pd
from deepface import DeepFace
from datetime import datetime
import os

DB_PATH = "db"
ASISTENCIA_FILE = "asistencia.csv"


def registrar_asistencia(nombre):
    fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if not os.path.isfile(ASISTENCIA_FILE):
        df = pd.DataFrame(columns=['Nombre', 'Fecha_Hora'])
        df.to_csv(ASISTENCIA_FILE, index=False)

    df = pd.read_csv(ASISTENCIA_FILE)
    nueva_fila = pd.DataFrame({'Nombre': [nombre], 'Fecha_Hora': [fecha_hora]})
    df = pd.concat([df, nueva_fila], ignore_index=True)
    df.to_csv(ASISTENCIA_FILE, index=False)
    print(f"  Registro guardado: {nombre} a las {fecha_hora}")


def analizar_atributos(frame):
    print("\n  Analizando atributos del rostro...")
    try:
        resultado = DeepFace.analyze(
            img_path=frame,
            actions=['age', 'gender', 'emotion'],
            enforce_detection=False
        )
        r = resultado[0]
        print(f"  Edad estimada : {r['age']}")
        print(f"  Genero        : {r['dominant_gender']}")
        print(f"  Emocion       : {r['dominant_emotion']}")
    except Exception as e:
        print(f"  Error al analizar atributos: {e}")


def reconocer_rostro(frame):
    if not os.path.isdir(DB_PATH) or not os.listdir(DB_PATH):
        print(f"  La carpeta '{DB_PATH}' esta vacia o no existe.")
        print("  Agrega imagenes con el nombre de cada persona (ej: juan.jpg)")
        return

    print("\n  Buscando coincidencias en la base de datos...")
    try:
        resultados = DeepFace.find(
            img_path=frame,
            db_path=DB_PATH,
            enforce_detection=False,
            model_name='VGG-Face',
            distance_metric='cosine',
            silent=True
        )

        if len(resultados) > 0 and not resultados[0].empty:
            identity_path = resultados[0]['identity'][0]
            nombre = os.path.splitext(os.path.basename(identity_path))[0]
            print(f"  Persona identificada: {nombre}")
            registrar_asistencia(nombre)
        else:
            print("  No se encontro ninguna coincidencia en la base de datos.")

    except Exception as e:
        print(f"  Error en el reconocimiento: {e}")


def mostrar_menu():
    print("\n" + "="*45)
    print("   SISTEMA DE VISION - MENU PRINCIPAL")
    print("="*45)
    print("  [ESPACIO]  Capturar frame actual")
    print("  [1]        Reconocimiento facial (asistencia)")
    print("  [2]        Analizar atributos del rostro")
    print("  [3]        Reconocimiento + Atributos")
    print("  [Q]        Salir")
    print("="*45)
    print("  Ventana de camara activa. Presiona una tecla.")


def iniciar_sistema():
    if not os.path.isdir(DB_PATH):
        os.makedirs(DB_PATH)
        print(f"  Carpeta '{DB_PATH}' creada. Agrega fotos antes de usar reconocimiento.")

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("  Error: No se pudo abrir la camara.")
        print("  Verifica que este conectada y no este en uso por otra app.")
        return

    mostrar_menu()

    ultimo_modo = '1'  # modo por defecto

    while True:
        ret, frame = cap.read()
        if not ret:
            print("  Error: No se puede leer el video de la camara.")
            break

        cv2.imshow("Sistema de Vision - Presiona una tecla (ver consola)", frame)
        tecla = cv2.waitKey(1) & 0xFF

        if tecla == ord('q') or tecla == ord('Q'):
            print("\n  Cerrando sistema. Hasta luego!")
            break

        elif tecla in [ord('1'), ord('2'), ord('3')]:
            ultimo_modo = chr(tecla)
            print(f"\n  Modo seleccionado: {ultimo_modo}. Presiona ESPACIO para capturar.")

        elif tecla == ord(' '):
            print(f"\n  Capturando frame (modo {ultimo_modo})...")
            cv2.imwrite("ultimo_frame.jpg", frame)

            if ultimo_modo == '1':
                reconocer_rostro(frame)
            elif ultimo_modo == '2':
                analizar_atributos(frame)
            elif ultimo_modo == '3':
                reconocer_rostro(frame)
                analizar_atributos(frame)

            mostrar_menu()

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    iniciar_sistema()