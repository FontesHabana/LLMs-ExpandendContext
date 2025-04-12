import json



def results_evaluation():
    with open('data/results/results.json', 'r',encoding="utf-8" ) as archivo:
                results = json.load(archivo)
    
    correct_original=correct_answer(results, "original_story")
    results["metrics"]["correct_answer"]["original_story"]["llama_70B"]=correct_original
    correct_expanded=correct_answer(results, "expanded_story")
    results["metrics"]["correct_answer"]["expanded_story"]["llama_70B"]=correct_expanded
    
    results["metrics"]["percent_correct_answer"]["original_story"]["llama_70B"]=percent(results, correct_original)
    
    results["metrics"]["percent_correct_answer"]["expanded_story"]["llama_70B"]=percent(results, correct_expanded)
    
    match=match_answer(results)
    results["metrics"]["match_answer"]=match
    
    results["metrics"]["percent_match_answer"]=percent(results, match)
    
    
    if(correct_expanded-correct_original>0):
        results["metrics"]["answers_better_than_original"]=correct_expanded-correct_original
    else:
         results["metrics"]["answers_better_than_original"]=0
    
    
    if(correct_original-correct_expanded>0):
        results["metrics"]["answers_worse_than_original"]=correct_expanded-correct_original
    else:
         results["metrics"]["answers_worse_than_original"]=0
    
    
                
                
                
    with open("data/results/results.json","w",encoding="utf-8") as f:
                        json.dump(results, f, indent=4,ensure_ascii=False)
                        
def correct_answer(results, storytype, model="llama_70B_answer"):
    count=0
    for i in range(len(results["model_answer"])):
        if(results["model_answer"][f"story_{str(i+1).zfill(3)}"]["answer"]==results["model_answer"][f"story_{str(i+1).zfill(3)}"][storytype][model]):
            count+=1
    return count

def percent(results,total):
    percent=(total/len(results["model_answer"]))*100
    return percent

def match_answer(results):
    count=0
    for i in range(len(results["model_answer"])):
        if(results["model_answer"][f"story_{str(i+1).zfill(3)}"]["original_story"]["llama_70B_answer"]==results["model_answer"][f"story_{str(i+1).zfill(3)}"]["expanded_story"]["llama_70B_answer"]):
            count+=1
    return count