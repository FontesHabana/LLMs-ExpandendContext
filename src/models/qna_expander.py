#Este modelo amplia historias basandose en preguntas y respuestas generadas de manera aleatoria
import openai
import os
from src.utils import prompts
from src.key import Key
from src.request import request


def qna_expander(history_id):
    """Genera una lista de preguntas y respuestas a partir de un texto"""
    #Crea una lista de preguntas a partir del texto
    questions=request.text_generator(prompts.generate_question_prompt(20,history_id), prompts.detective_character)
    #Crea una lista de respuestas a partir del texto
    answers=request.text_generator(prompts.answer_question_prompt(questions, history_id), prompts.writing_assistant_character, 0.8)
    #Devuelve una lista de preguntas y respuestas
    
    return request.amplied_history(prompts.fusion_history_prompt(answers, history_id), prompts.writing_assistant_character, 0.8)
    