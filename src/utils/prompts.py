
from src.utils import data_manager
from src.extractors import blacklist

#Agent character
detective_character = "Act as a murder detective"
writing_assistant_character="Act as creative writing assistant specializing in mystery and detective fiction"


extract_places=f"""Read the following text and extract all the physical places or locations mentioned in it. List them clearly, including buildings, streets, and natural landmarks. Do not include locations like the locations including in the blacklist. Provide only the actual places mentioned in the text Output them in a list separated by , 
     Texto: {data_manager.data_list[0]['narrative']}
     BlackList={blacklist.BLACKLIST_LOCATIONS}
    Output: place1, place2, place3
    
    Return ONLY the list, without additional text."
    """
    
    
#Question Model Prompt
# This prompt is used to generate a question based on the provided text. It instructs the model to create a question that is relevant to the content and context of the text.
def generate_question_prompt(number=20):
  "Genera el prompt para generar preguntas"
  return f"""Analyze the following detective story text. Your task is to generate exactly {number} questions based solely on the information presented.

These questions must adhere to the following strict rules:

1.  **Unanswered in Text:** Each question must address information that is **missing** or **not explicitly stated** within the provided story. Do not ask about things that are already explained.
2.  **Investigatively Useful:** The answer to each question should provide information that would be genuinely **useful or critical** for solving the central crime (e.g., establishing motive, opportunity, means, timeline, or identifying inconsistencies).
3.  **No Direct 'Whodunit':** Absolutely **none** of the questions should directly ask "Who is the murderer?", "Who committed the crime?", or implicitly target a specific person as the killer (e.g., avoid questions like "Why did [Character Name] kill the victim?").

Focus on identifying gaps in knowledge regarding evidence, timelines, alibis, motives, relationships, character backgrounds, unexplained occurrences, or missing procedural details.


Please list the 20 questions clearly.
    Text: {data_manager.data_list[0]['narrative']}   
    Suspect: {data_manager.data_list[0]['choices']}
 
 the output format is a text with the structure :
 1 string, 2 string, ... , 20 string,...
 Ignore any additional text or explanations and provide only the requested list.

"""

def answer_question_prompt(questions):
  """Genera las respuestas"""
  return f"""```
You are a creative writing assistant specializing in mystery and detective fiction. Your task is to expand upon an existing story by generating new sections that address specific unanswered questions, while carefully preserving the central mystery.

**Inputs:**
1.  **Original Story Text:** The base narrative provided below.
2.  **Unanswered Questions:** A list of questions about information missing from the original story.
3. **Suspicious Characters:** A list of characters who are suspected of being involved in the crime.

**Task:**
For **each** question in the provided list:
1.  Generate a **new, creative story section**.
2.  This section must **directly address and provide an answer or significant clarification** to the corresponding question (e.g., revealing a character's previously unknown action, explaining the origin of an object, clarifying a relationship detail).
3.  Maintain **stylistic consistency** with the original story (match the tone, character voices, vocabulary, atmosphere, and narrative perspective).
4.  The section should feel like a natural addition, written so it could be **plausibly inserted** into the existing narrative flow or add valuable context as a flashback, dialogue, or discovered note/document.
5.  **CRITICAL CONSTRAINT:** None of the generated sections must **explicitly reveal the identity of the murderer** or make direct, unambiguous accusations. They can provide clues, deepen context, introduce complications, add atmospheric detail, or offer misdirection, but the ultimate 'whodunit' must remain unresolved within these additions. Focus on answering the *specific question asked* without solving the entire case. Ensure that for the {len(questions)} provided questions, there are exactly {len(questions)} corresponding generated text fragments in the output

**Input Story:**
    TextStory: {data_manager.data_list[0]['narrative']}

    Suspect: {data_manager.data_list[0]['choices']}

    Question: {questions}



Answer:
 the output format is a text with the structure :
 1 string, 2 string, ... , 20 string,...
 Ignore any additional text or explanations and provide only the requested list.
"""

def fusion_answerstory_prompt(answers):
  "fusion a history"
  return f"""
You are a creative writing assistant specializing in seamless narrative integration. Your task is to merge a given original story with a set of supplementary story fragments into a cohesive and expanded single narrative.

**Inputs:**
1.  **Original Story:** The initial narrative text.
2.  **Story Fragments:** A collection of text snippets designed to add to or elaborate on the original story.

**Task:**
1.  **Integrate** each of the provided story fragments into the original story.
2.  Ensure that the integration is **chronologically consistent** within the overall narrative.
3.  The transitions between the original text and the added fragments must be **smooth and natural**, such that the reader cannot discern where the original story ends and a fragment begins. This requires careful attention to pacing, tone, character voice, and narrative flow.
4.  The resulting output should be a **single, unified, and longer story** where the added fragments feel organically woven into the existing narrative.

**Input Story:**
    {data_manager.data_list[0]['narrative']}

**Story Fragments:**
    {answers}

Output:
 Generate a single string containing the complete story, ignoring any formatting or titles
  """
