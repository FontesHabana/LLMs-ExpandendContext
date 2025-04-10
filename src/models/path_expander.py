#Este modelo amplia historias basandose en preguntas y respuestas generadas de manera aleatoria
import openai
import os
from src.utils import prompts
from src.key import Key
from src.request import request

def path_expander(history_id):
    """Genera una lista de preguntas y respuestas a partir de un texto"""
    #Crea una lista de preguntas a partir del texto
    moments_list=request.text_generator(prompts.alone_moment_prompt(history_id), prompts.detective_character)
    #Completa los momentos
    completed_moments_list=request.text_generator(prompts.complete_alonemoment_prompt(history_id,moments_list), prompts.writing_assistant_character, 1)
    
    paragraph_list=[]
    for i in range(2):
         path_list=request.text_generator(prompts.path_history_prompt(history_id,i), prompts.detective_character)
         generated_par=request.text_generator(prompts.complete_path_prompt(history_id,i,path_list), prompts.writing_assistant_character, 1)
         
         for j in range(len(generated_par)):
            paragraph_list.append(generated_par[j])
    
    #Crea La historia ampliada
    amplied_history=request.amplied_history(prompts.fusion_history_prompt(completed_moments_list, history_id), prompts.writing_assistant_character, 0.8)
    
    amplied_history=request.amplied_history(prompts.fusion_history_prompt_string(paragraph_list, amplied_history), prompts.writing_assistant_character, 0.8)
    
    return amplied_history