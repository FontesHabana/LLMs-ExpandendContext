from src.utils import data_manager
from src.request import request
from src.utils import prompts
import json
import time


def evaluator():
    with open('data/processed/expanded_story.json', 'r',encoding="utf-8" ) as archivo:
            dataset = json.load(archivo)  
    with open('data/results/results.json', 'r',encoding="utf-8" ) as archivo:
            results = json.load(archivo)  

    for i in range(11,50):
                story=dataset[f"story_{str(i+1).zfill(3)}"]["expanded_stories"][0]["qna_model"][0]["story"]
                answer=request.text_generator(prompts.solution_prompt(i,story),prompts.detective_character,1)
                results["model_answer"][f"story_{str(i+1).zfill(3)}"]["expanded_story"]["llama_70B_answer"]=answer[0]
                print(f"story_{str(i+1).zfill(3)} expanded")
                time.sleep(5)
                with open("data/results/results.json","w",encoding="utf-8") as f:
                    json.dump(results, f, indent=4,ensure_ascii=False)
                print(f"story_{str(i+1).zfill(3)} original")
                time.sleep(5)

    
    for i in range(11,50):
        
        results["model_answer"][f"story_{str(i+1).zfill(3)}"]["answer"]=data_manager.data_list[i]["answer_index"]
        
        story=dataset[f"story_{str(i+1).zfill(3)}"]["original_text"]["text"]
        answer=request.text_generator(prompts.solution_prompt(i,story),prompts.detective_character,1)
        results["model_answer"][f"story_{str(i+1).zfill(3)}"]["original_story"]["llama_70B_answer"]=answer[0]
        
        
        
        with open("data/results/results.json","w",encoding="utf-8") as f:
                    json.dump(results, f, indent=4,ensure_ascii=False)
        print(f"story_{str(i+1).zfill(3)} original")
        time.sleep(5)

   