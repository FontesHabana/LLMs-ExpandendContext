#from src.extractors import extractor
from src.utils import prompts
from src.models import qna_expander as qna
from src.models import path_expander as path
from src.utils import data_manager
from src.utils import json_generator as dg
import json




def story_maker():
    with open('data/processed/expanded_story.json', 'r',encoding="utf-8" ) as archivo:
        dataset = json.load(archivo)  # Convierte el contenido del archivo en un diccionario
    for i in range(10):
        
        story=qna.amplied_qna_expander(i,dataset[f"story_{str(i+1).zfill(3)}"]["original_text"]["text"])
        
        dataset[f"story_{str(i+1).zfill(3)}"]["expanded_stories"].append({"qna_model":[{"story":story,"answer":None}]})
        print(f"Add history {i}.1 ")
        story=path.path_expander(i,dataset[f"story_{str(i+1).zfill(3)}"]["original_text"]["text"])
        
        dataset[f"story_{str(i+1).zfill(3)}"]["expanded_stories"].append({"path_model":[{"story":story,"answer":None}]})
        print(f"Add history {i}.2 ")
        
        
    with open("data/processed/expanded_story.json","w",encoding="utf-8") as f:
        json.dump(dataset, f, indent=4,ensure_ascii=False)
    print("Historias ampliadas guardadas con  exito")






