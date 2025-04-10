#from src.extractors import extractor
from src.utils import prompts
from src.models import qna_expander as qna
from src.models import path_expander as path
from src.utils import data_manager


history = path.path_expander(0) 
print(history)

try:
    with open("original_history.txt", "w") as archivo:
        archivo.write(data_manager.data_list[0]['narrative'])
except Exception as e:
    print(f"Error al escribir en el archivo: {e}")

try:
    with open("history.txt", "w") as archivo:
        archivo.write(history)
except Exception as e:  
    print(f"Error al escribir en el archivo: {e}")