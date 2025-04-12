
from src.utils import prompts
from src.request import request

def path_expander(story_id, story):
    
    
    moments_list=request.text_generator(prompts.alone_moment_prompt(story_id,story), prompts.detective_character,0.7)
  
    completed_moments_list=request.text_generator(prompts.complete_alonemoment_prompt(story_id,moments_list, story), prompts.writing_assistant_character, 1)
    
    paragraph_list=[]
    for i in range(2):
         path_list=request.text_generator(prompts.path_story_prompt(story_id,i, story),prompts.writing_assistant_character,1)
         generated_par=request.text_generator(prompts.complete_path_prompt(story_id,i,path_list,story),  1)
         
         for j in range(len(generated_par)):
            paragraph_list.append(generated_par[j])
    
    #Crea La historia ampliada
    expanded_story=request.expanded_story(prompts.fusion_story_prompt(completed_moments_list,story),prompts.writing_assistant_character, 1)
    
    return expanded_story