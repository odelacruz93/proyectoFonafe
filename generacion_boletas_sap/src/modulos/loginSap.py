import pyautogui
import time

def loginSAP():
    ruta_imagenes = "C:\\Users\\admrpa\\Documents\\Proyecto\\Fonafe\\generacion_boletas_sap\\src\\imagenes"

    # Click en el menu de optiones de ventana
    time.sleep(2)
    option = pyautogui.locateCenterOnScreen(ruta_imagenes + "\\options.png", confidence=0.9)
    print(option)
    pyautogui.click(option)

    # Maximizar menu princiapl SAP Easy Access (opcional) Puede que ya aparezca maximizado
    time.sleep(2)
    maximiza_sap = pyautogui.locateCenterOnScreen(ruta_imagenes + "\\maximiza_sap.png", confidence=0.9)
    print(maximiza_sap)
    pyautogui.click(maximiza_sap)

    # Ingresar Numero de transacción (Generacion Boletas de Pago)
    time.sleep(2)
    textbox_trx = pyautogui.locateCenterOnScreen(ruta_imagenes + "\\texbox_trx.png", confidence=0.9)
    print(textbox_trx)
    pyautogui.click(textbox_trx)
    time.sleep(1)
    pyautogui.write("ZHCM010")

    # Ubicarse y escribir el username
    time.sleep(2)
    print("ubica_usuario")
    x_user, y_user = pyautogui.locateCenterOnScreen(ruta_imagenes + "\\user.png", confidence=0.9)
    print(x_user, y_user)
    x_user = x_user + 60
    pyautogui.click(x_user, y_user)
    pyautogui.write("USER_RPA")

    # Ubicarse y escribir el password
    time.sleep(2)
    print("ubica pass")
    x_password, y_password = pyautogui.locateCenterOnScreen(ruta_imagenes + "\\password.png", confidence=0.9)
    print(x_password, y_password)
    x_password = x_password + 60
    pyautogui.click(x_password, y_password)
    pyautogui.write("Fonafe_rpa01$")
    time.sleep(1)
    pyautogui.hotkey("enter")

    # Minimiza ventana de conexion
    #time.sleep(2)
    #minimiza_cnx = pyautogui.locateCenterOnScreen("C:\\Users\\admrpa\\Documents\\fonafe\\generacion_boletas_sap\\src\\test\\elements\\minimiza_cnx.png", confidence=0.9)
    #print(minimiza_cnx)
    #pyautogui.click(minimiza_cnx)

