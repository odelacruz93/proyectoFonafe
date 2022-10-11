import time

import modulos.openSap as open
import modulos.loginSap as login
import modulos.generarBoletaSap as boleta
import modulos.closeSap as close

open.openSAP()
login.loginSAP()
boleta.generarBoletaSAP()
close.closeSap()



