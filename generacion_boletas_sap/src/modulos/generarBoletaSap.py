import pyautogui
import time
from datetime import datetime
import os

def generarBoletaSAP():
    ruta_imagenes = "C:\\Users\\admrpa\\Documents\\Proyecto\\Fonafe\\generacion_boletas_sap\\src\\imagenes"
    # Ingresar Sociedad
    time.sleep(4)
    x_sociedad, y_sociedad = pyautogui.locateCenterOnScreen(
        ruta_imagenes + "\\texbox_sociedad.png",
        confidence=0.9)
    print(x_sociedad, y_sociedad)
    x_sociedad += 100
    print(x_sociedad, y_sociedad)
    pyautogui.click(x_sociedad, y_sociedad)
    pyautogui.write("0600")
    pyautogui.hotkey("enter")

    # Ingresar Nomina
    time.sleep(2)
    x_nomina, y_nomina = pyautogui.locateCenterOnScreen(
        ruta_imagenes + "\\textbox_nomina.png",
        confidence=0.9)
    print(x_nomina, y_nomina)
    x_nomina += 105
    print(x_nomina, y_nomina)
    pyautogui.click(x_nomina, y_nomina)
    pyautogui.write("U1")

    # Obtener e ingresar periodo
    month = str(datetime.now().month)
    year = str(datetime.now().year)
    carpeta_mes = "SIN ASIGNAR"
    # Asignar nombre del mes para crear carpeta donde se guardaran las boletas.
    if month == '01':
        carpeta_mes = "ENERO"
    elif month == '02':
        carpeta_mes = "FEBRERO"
    elif month == '03':
        carpeta_mes = "MARZO"
    elif month == '04':
        carpeta_mes = "ABRIL"
    elif month == '05':
        carpeta_mes = "MAYO"
    elif month == '06':
        carpeta_mes = "JUNIO"
    elif month == '07':
        carpeta_mes = "JULIO"
    elif month == '08':
        carpeta_mes = "AGOSTO"
    elif month == '09':
        carpeta_mes = "SETIEMBRE"
    elif month == '10':
        carpeta_mes = "OCTUBRE"
    elif month == '11':
        carpeta_mes = "NOVIEMBRE"
    elif month == '12':
        carpeta_mes = "DICIEMBRE"
    else:
        carpeta_mes = "SIN ASIGNAR"

    time.sleep(2)
    # Ingresar mes
    x_periodo, y_periodo = pyautogui.locateCenterOnScreen(
        ruta_imagenes + "\\textbox_periodo.png",
        confidence=0.9)
    print(x_periodo, x_periodo)
    mes = x_periodo + 56
    pyautogui.click(mes, y_periodo)
    pyautogui.write(month)

    # Ingresar año
    año = x_periodo + 90
    pyautogui.click(año, y_periodo)
    pyautogui.write(year)


    # Ingresar calidad nomina.
    time.sleep(2)
    x_calidad_nomina, y_calidad_nomina = pyautogui.locateCenterOnScreen(
        ruta_imagenes + "\\calidad_nomina.png",
        confidence=0.9)
    print(x_calidad_nomina, y_calidad_nomina)
    nomina = x_calidad_nomina - 19
    pyautogui.click(nomina, y_calidad_nomina)
    pyautogui.write("U1")
    pyautogui.hotkey("enter")

    # Seleccionar radio button "Archivo pdf" y desactivar checkbox "PDF Unico"
    time.sleep(2)
    archivo_pdf = pyautogui.locateCenterOnScreen(
        ruta_imagenes + "\\archivo_pdf.png",
        confidence=0.9)
    print(archivo_pdf)
    pyautogui.click(archivo_pdf)

    time.sleep(2)
    pdf_unico = pyautogui.locateCenterOnScreen(
        ruta_imagenes + "\\pdf_unico.png",
        confidence=0.9)
    print(pdf_unico)
    pyautogui.click(pdf_unico)


    #Crear y validar si existe carpeta del MES actual donde se descargaran las boletas
    ruta_descarga = "C:\\Users\\admrpa\\Documents\\SAP\\SAP GUI\\BOLETAS_SIN_FIRMAR\\"+year+"\\"+carpeta_mes+"\\"
    os.makedirs(ruta_descarga, exist_ok=True)

    #colocar ruta de descarga boletas y ejecutar proceso con f8
    time.sleep(2)
    x_ruta_descarga, y_ruta_descarga = pyautogui.locateCenterOnScreen(
        ruta_imagenes + "\\ruta_descarga.png",
        confidence=0.9)
    print(x_ruta_descarga, y_ruta_descarga)
    x_ruta_descarga = x_ruta_descarga + 109
    pyautogui.click(x_ruta_descarga, y_ruta_descarga)
    pyautogui.write(ruta_descarga)
    time.sleep(5)
    pyautogui.hotkey('f8')
    pyautogui.screenshot()
    time.sleep(60)

    # Reconocer icono OK de culminación del proceso de descarga
    msg = pyautogui.locateCenterOnScreen(ruta_imagenes + "\\mensaje_final.png", confidence=0.9)
    print(msg)
    if msg == None:
        print("Las boletas NO se descargaron correctamente, por favor revisar el log")
    else:
        print("Las boletas se descargaron correctamente en " + ruta_descarga)




