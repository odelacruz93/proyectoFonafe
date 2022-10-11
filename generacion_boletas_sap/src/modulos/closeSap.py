import time
import pyautogui

def closeSap():
    # Teclear alt + f4 para cerrar SAP
    ruta_imagenes = "C:\\Users\\admrpa\\Documents\\Proyecto\\Fonafe\\generacion_boletas_sap\\src\\imagenes"
    time.sleep(4)
    pyautogui.hotkey('alt', 'f4')

    time.sleep(2)
    salir = pyautogui.locateCenterOnScreen(ruta_imagenes + "\\salir.png", confidence=0.9)
    print(salir)
    pyautogui.click(salir)

    time.sleep(2)
    cerrar_logon = pyautogui.locateCenterOnScreen(ruta_imagenes + "\\cerrar_logon.png", confidence=0.9)
    print(cerrar_logon)
    pyautogui.click(cerrar_logon)