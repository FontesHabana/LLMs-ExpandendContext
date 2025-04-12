import json
from src.request import request
from src.utils import prompts
from src.models import qna_expander as qna
from src.models import path_expander as path
from src.utils import data_manager
#from src.utils import dataset_generator as dg
from src.runners import story_maker as sm
from src.utils import json_generator as jg
from src.evaluators import evaluator, results_evaluator


"""with open('data/processed/expanded_story.json', 'r',encoding="utf-8" ) as archivo:
        dataset = json.load(archivo)  # Convierte el contenido del archivo en un diccionario

for i in range(50,100):
        story=dataset[f"story_{str(i+1).zfill(3)}"]["original_text"]["text"]
        story=qna.qna_expander(i,story)

        dataset[f"story_{str(i+1).zfill(3)}"]["expanded_stories"].append({"qna_model":[{"story":story,"answer":None}]})

        with open("data/processed/expanded_story.json","w",encoding="utf-8") as f:
                        json.dump(dataset, f, indent=4,ensure_ascii=False)
        print(f"story_{str(i+1).zfill(3)}")"""


results_evaluator.results_evaluation()
#evaluator.evaluator()
