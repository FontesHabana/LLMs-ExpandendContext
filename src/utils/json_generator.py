import json
from src.utils import data_manager as data




def generate_dataset():
    original_dataset=data.data_list 

    dataset={}

    for i in range(len(original_dataset)):
        story_id=f"story_{str(i+1).zfill(3)}"
        
        dataset[story_id]={
            "original_text":{"text":original_dataset[i]["narrative"], "answer":None},
            "expanded_stories":[],
            "average_result":None,
            "most_common_result":None
        }


    #Save as json

    with open("data/processed/expanded_story.json","w",encoding="utf-8") as f:
        json.dump(dataset, f, indent=4,ensure_ascii=False)
        
    print("Diccionario guardado")
    return

def generate_result():
    
    result={}
    original_dataset=data.data_list 
    result={
        "model_answer":{},
        "metrics":{
                        "correct_answer":{
                "original_story":{
                    "llama_70B":None,
                    "DeepSeek":None,
                },
                "expanded_story":{
                    "llama_70B":None,
                    "DeepSeek":None,
                }
            },
            "percent_correct_answer":{
                "original_story":{
                    "llama_70B":None,
                    "DeepSeek":None,
                },
                "expanded_story":{
                    "llama_70B":None,
                    "DeepSeek":None,
                }
            },
            "match_answer":None,
            "answers_better_than_original":None,
            "answers_worse_than_original":None,
        }}
        
    
    for i in range(len(original_dataset)):
        story_id=f"story_{str(i+1).zfill(3)}"
        
        result["model_answer"][story_id]={
            "answer":original_dataset[i]["answer_index"],
            "original_story":{"llama_70B_answer":None,
            "DeepSeek_answer":None, },
            "expanded_story":{"llama_70B_answer":None,
            "DeepSeek_answer":None, },   
            }
    
    
 
        
 #Save as json

    with open("data/results/results.json","w",encoding="utf-8") as f:
        json.dump(result, f, indent=4,ensure_ascii=False)
        
    print("Diccionario guardado")
    return
