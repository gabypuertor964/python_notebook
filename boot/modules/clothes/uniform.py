import os
import sys

# Añadir el directorio principal al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from tools.display.text_align import left

# Imprimir camisa
def shirt():
    print(left("Camisa"))


