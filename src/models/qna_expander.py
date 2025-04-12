#QuestionAnswer model
from src.utils import prompts
from src.request import request


def qna_expander(story_id, story):
    """QuestionAnswer model"""
    #Make questions
    questions=request.text_generator(prompts.generate_question_prompt(20,story_id, story), prompts.detective_character)
    #Make answer
    answers=request.text_generator(prompts.answer_question_prompt(questions, story_id, story), prompts.writing_assistant_character, 0.8)
    
    return request.expanded_story(prompts.fusion_story_prompt(answers, story), prompts.writing_assistant_character, 0.8)
    
def amplied_qna_expander(story_id, story):
    "Qna_expander repetido"
    for i in range (2):
        story=qna_expander(story_id, story)
    
    return story