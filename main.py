import sys
from PyQt5 import QtWidgets, uic


app = QtWidgets.QApplication(sys.argv)

ventana = uic.loadUi("interfaces/seleccion_ingreso.ui")

ventana.show()

sys.exit(app.exec_())