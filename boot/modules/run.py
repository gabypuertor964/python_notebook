import os
import sys

# Añadir el directorio principal al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from tools.display.titles import title,bye
from tools.display.text_align import left
from tools.input.get import wait

from modules.calculator.operations import sum_custom
from modules.clothes.uniform import shirt

# ext.saludar()
title("Saludar")

# ext.hi()
print(left("Hola, como estas?"))

# print(ca.sumar(3,6,7,9))
print(left(str(sum_custom([3,6,7,9]))))

# uni.camisa()
shirt()

# ext.despedir()
bye("Despedir",False)

wait()