#Este modelo amplia historias basandose en preguntas y respuestas generadas de manera aleatoria
import openai
import os
from src.utils import prompts
from src.key import Key
from pydantic import BaseModel
import json

class QResponse(BaseModel):
    """Esquema"""
    question: str

def text_generator(prompt, character, mytemperature=0.5, number=1):
    """Genera una lista de datos a partir de un prompt y un personaje"""
    #Pide información a la api
    response = Key.client.chat.completions.create(
        #Add system role for develop a character
        messages=[{"role": "system", "content": character},
            {"role": "user", "content": prompt}],
        model="accounts/fireworks/models/llama-v3p3-70b-instruct",
       
        temperature=mytemperature,
        n=number,
    )
    result=response.choices[0].message.content
    return result.split(",") #Devuelve una lista de preguntas separadas por comas

def amplied_history(prompt, character, mytemperature=0.5, number=1):
    """Genera una historia ampliada"""
    #Pide información a la api
    response = Key.client.chat.completions.create(
        #Add system role for develop a character
        messages=[{"role": "system", "content": character},
            {"role": "user", "content": prompt}],
        model="accounts/fireworks/models/llama-v3p3-70b-instruct",
       
        temperature=mytemperature,
        n=number,
    )
    result=response.choices[0].message.content
    return result


def qna_expander():
    """Genera una lista de preguntas y respuestas a partir de un texto"""
    #Crea una lista de preguntas a partir del texto
    questions=text_generator(prompts.generate_question_prompt(), prompts.detective_character)
    #Crea una lista de respuestas a partir del texto
    answers=text_generator(prompts.answer_question_prompt(questions), prompts.writing_assistant_character, 0.8)
    #Devuelve una lista de preguntas y respuestas
    
    return amplied_history(prompts.fusion_answerstory_prompt(answers), prompts.detective_character, 0.8)
    