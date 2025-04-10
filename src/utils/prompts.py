
from src.utils import data_manager

#Agent character
detective_character = "Act as a murder detective"
writing_assistant_character="Act as creative writing assistant specializing in mystery and detective fiction"



    
#Question Model Prompt
# This prompt is used to generate a question based on the provided text. It instructs the model to create a question that is relevant to the content and context of the text.
def generate_question_prompt(number=20, history_id=0):
  "Genera el prompt para generar preguntas"
  return f"""Analyze the following detective story text. Your task is to generate exactly {number} questions based solely on the information presented.

These questions must adhere to the following strict rules:

1.  **Unanswered in Text:** Each question must address information that is **missing** or **not explicitly stated** within the provided story. Do not ask about things that are already explained.
2.  **Investigatively Useful:** The answer to each question should provide information that would be genuinely **useful or critical** for solving the central crime (e.g., establishing motive, opportunity, means, timeline, or identifying inconsistencies).
3.  **No Direct 'Whodunit':** Absolutely **none** of the questions should directly ask "Who is the murderer?", "Who committed the crime?", or implicitly target a specific person as the killer (e.g., avoid questions like "Why did [Character Name] kill the victim?").

Focus on identifying gaps in knowledge regarding evidence, timelines, alibis, motives, relationships, character backgrounds, unexplained occurrences, or missing procedural details.


Please list the 20 questions clearly.
    Text: {data_manager.data_list[history_id]['narrative']}    
    Suspect: {data_manager.data_list[history_id]['choices']}
 
 the output format is a text with the structure :
 1 string/ 2 string/ ... / 20 string/...
 Ignore any additional text or explanations and provide only the requested list.

"""

def answer_question_prompt(questions, history_id=0):
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
    TextStory: {data_manager.data_list[history_id]['narrative']}

    Suspect: {data_manager.data_list[history_id]['choices']}

    Question: {questions}



Answer:
 the output format is a text with the structure :
 1 string/ 2 string/ ... / 20 string,...
 Ignore any additional text or explanations and provide only the requested list.
"""


#History fusion
def fusion_history_prompt(answers, history_id=0):
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
    {data_manager.data_list[history_id]['narrative']}

**Story Fragments:**
    {answers}

Output:
 Generate a single string containing the complete story, ignoring any formatting or titles
  """

def fusion_history_prompt_string(answer, history):
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
    {history}
    

**Story Fragments:**
    {answer}

Output:
 Generate a single string containing the complete story, ignoring any formatting or titles
  """
#Path Expander Prompt

def alone_moment_prompt(history_id):
  
  
  "Genera el prompt para determinar momentos solitarios"
  return f"""**Detailed Prompt: Extract and Format Suspect Solitary Moments**

    **Objective:**
    Analyze the provided 'Story Text' to identify every instance where any individual named in the 'List of Suspects' is explicitly stated or strongly implied to be alone. Consolidate these findings into a single, comma-separated string, with each identified instance represented by a specifically formatted value.

    **Inputs:**
    1.  **Story Text:** The narrative, witness statements, case file, or other relevant text to be analyzed.
    2.  **List of Suspects:** A list containing the exact names of the suspects whose solitary moments need to be tracked.

    **Detailed Instructions:**

    1.  **Initialization:** Create an empty list variable to store the formatted strings representing identified solitary moments.
    2.  **Iterate Through Suspects:** Process each name provided in the 'List of Suspects' one by one.
    3.  **Analyze Text for Current Suspect:** For the suspect currently being processed, meticulously scan the *entire* 'Story Text' from beginning to end. Your goal is to locate all distinct segments describing moments where this *specific suspect* was alone.
        * Look for **explicit statements**: Phrases like "was alone," "by himself," "by herself," "on his own," "on her own," "no one else was there," "the room was empty except for him/her."
        * Look for **strong contextual implications**: Situations where the narrative strongly suggests solitude, such as "He locked the door to his study," "She drove back unaccompanied," "After everyone else left, he remained," "He spent the hour in his private workshop." Evaluate context carefully – only include if the implication of being alone is clear and unambiguous within the narrative description.
    4.  **Extract and Format Each Instance:** For *every separate instance* you identify for the current suspect:
        * Identify the **Suspect Name** (the one you are currently processing).
        * Determine the **Time Reference**: Extract the most precise time indicator associated with this moment from the text (e.g., "9:15 PM," "around midnight," "Tuesday afternoon," "during the coffee break"). If no exact time is given, use a contextual marker (e.g., "after the argument," "before dinner," "upon returning"). If no usable time reference exists for that specific moment, use the placeholder "Time Unknown".
        * Determine the **Location Reference**: Extract the location where the suspect was alone, if mentioned (e.g., "in the office," "at home," "walking in the park," "in his car"). If no location is specified or clearly inferable for that moment, use the placeholder "Location Unknown".
        * **Create the Value String:** Format this extracted information into a single string precisely as follows: `"Suspect Name (Time Reference, Location)"`.
            * *Example 1:* `"Dr. Aris Thorne (9:15 PM, In the office)"`
            * *Example 2:* `"Eleanor Vance (After the argument, Location Unknown)"`
            * *Example 3:* `"Sam Bridges (Time Unknown, Walking in the park)"`
        * Add this newly created value string to the list you initialized in step 1.
    5.  **Generate Final Output:** Once you have iterated through *all* suspects in the list and analyzed the *entire* text for each one, take the list of collected value strings:
        * Join all the strings in the list together into one single string, using a comma followed by a space ("/ ") as the separator between each value.
        * **This final, single, comma-separated string is the required output.**
        * If, after analyzing the text for all suspects, *no instances* of anyone being alone were found, output the specific string: `"No solitary moments identified for the listed suspects."`

    **Input Story Text:**
        TextStory: {data_manager.data_list[history_id]['narrative']}

        Suspect: {data_manager.data_list[history_id]['choices']}
    [Paste the full story text, statements, or relevant documents here]"""
    
def complete_alonemoment_prompt(history_id, moments_list):
  "Prompt para completar momentos en blanco"
  return f"""**Detailed Prompt: Creative Development of Solitary Moments (Police Novel Writer Persona)**

    **Your Role:**
    Assume the persona of a seasoned police novel writer. Your strength lies in creating atmospheric scenes, delving into character psychology, and subtly weaving intrigue and doubt. You write with an evocative style and pay close attention to details that may (or may not) be significant.

    **Objective:**
    Based on the provided 'Story Text' and 'List of Suspects', your first task is to identify the key moments when each listed suspect was alone. Following that, your main task is to *creatively expand* upon each of those solitary moments. You will write a detailed narrative paragraph for each instance, describing the character's actions, thoughts, feelings, or surroundings from your writer's perspective, enriching the plot and mystery without solving it.

    **Inputs:**
    1.  **Story Text:** The base narrative, statements, case notes, or other relevant text to be analyzed.
    2.  **List of Suspects:** The names of the individuals whose solitary actions you need to develop.

    **Detailed Instructions:**

    1.  **Phase 1: Precise Identification:**
        * Meticulously analyze the provided 'Story Text'.
        * For each name in the 'List of Suspects', identify and note all distinct instances where the text confirms (explicitly or through strong implication) that the suspect was alone. Try to associate each instance with a time and place, if available in the original text.
    2.  **Phase 2: Creative Narrative Development (Your Primary Focus):**
        * For **each** solitary instance identified in Phase 1 for a suspect:
        * Step into your writer role. Craft a **vivid and detailed narrative paragraph** (roughly 50-150 words per paragraph, as a guideline) describing that specific moment.
        * **Focus on Character Experience:** What were they doing physically (gestures, movements, tasks)? What was crossing their mind (memories, worries, plans - related or unrelated to the case)? What sensations were they perceiving (a chill, a particular scent, a distant sound)? What was the atmosphere like (claustrophobic, calm, tense)? Were they interacting with any objects meaningfully?
        * **Maintain Coherence:** Ensure your additions are consistent with the character as presented in the original story, their likely emotional state, and the overall tone of the police procedural narrative.
        * **CRITICAL CONSTRAINT:** Your writing must add layers of intrigue, depth, or potential misdirection (subtle red herrings are acceptable), but it **must NEVER directly or indirectly reveal the culprit of the main crime.** Do not include confessional thoughts, clearly incriminating actions related to the murder, or anything that removes ambiguity about the killer's identity. The reader must keep guessing. You may reveal other minor secrets or concerns of the character if it fits creatively.
    3.  **Mandatory Output Format:**
        * The final output must be a sequence of the creative paragraphs you have generated.
        * Each paragraph must correspond to a single instance of a suspect being alone.
        * Separate **each paragraph** from the next using **exactly one forward slash character (`/`)**. There should be no spaces before or after the separating slash.
        * If, after the initial analysis, you find no instances where any of the listed suspects were alone, return only the text: `No solitary moments identified for the listed suspects requiring narrative development.`

    **Story Text:**
        TextStory: {data_manager.data_list[history_id]['narrative']}

        Suspect: {data_manager.data_list[history_id]['choices']}

        List of moments:{moments_list} """
         
def path_history_prompt(history_id, suspect_id):
    "Genera el camino de los sospechozos"
    return f""" **Prompt: Generate Detailed Log of Character Actions and Conversations**

        **Objective:**
        Analyze the provided 'Story Text' to identify and compile a comprehensive, detailed list documenting every specific action taken by, and every conversation involving, the designated 'Target Character'. The list should be organized chronologically according to the narrative sequence.

        **Inputs:**
        1.  **Story Text:** The narrative, chapter, scene, transcript, or document to be analyzed.
        2.  **Target Character:** The exact name of the character whose activities are to be logged.

        **Detailed Instructions:**

        1.  **Character Focus:** Read the 'Story Text' meticulously from beginning to end, paying close attention to every sentence and paragraph involving the 'Target Character'.
        2.  **Identify Actions:** Locate and record every instance where the Target Character performs a discernible physical action or interacts significantly with their environment or objects. Examples include, but are not limited to:
            * **Movement:** Walking, running, driving, entering, exiting, sitting, standing, gesturing (nodding, pointing, waving).
            * **Object Interaction:** Picking up, putting down, using (a tool, phone, computer), opening, closing (doors, drawers, books), writing, reading, eating, drinking.
            * **Observable Tasks:** Searching, examining, hiding, preparing something, waiting.
            * Record *what* the action is and any relevant qualifiers mentioned (e.g., "walked *quickly*", "picked up the *letter*", "looked *nervously*").
        3.  **Identify Conversations:** Locate and record every instance where the Target Character communicates verbally with others, or where their speech is reported. Examples include:
            * **Direct Dialogue:** Any text enclosed in quotation marks attributed to the character.
            * **Reported Speech:** Summaries or indirect quotes of what the character said (e.g., "She explained her alibi," "He denied knowing anything," "Character asked about the time").
            * **Participation Mention:** Notes that the character was part of a discussion, argument, or conversation, even if their specific words aren't provided (e.g., "They discussed the plan," "He argued with Maria").
            * For each conversational instance, note *who* they were speaking to (if mentioned) and *what* was said (quote or summary).
        4.  **Chronological Compilation:** As you identify each action and conversation instance, mentally (or actually) note its place in the narrative sequence.
        5.  **Output Generation:** Create a single, detailed list summarizing these findings in chronological order as they appear in the text.
            * Use bullet points (`- `) or numbered items for each distinct entry.
            * Each entry should clearly state the action or describe the conversation segment.
            * Provide enough detail from the text to make the entry informative.

        **Story Text:**
         TextStory: {data_manager.data_list[history_id]['narrative']}

        Suspect: {data_manager.data_list[history_id]['choices'][suspect_id]}
       """

def complete_path_prompt(history_id, suspect_id, path_list):
    "Prompt para completar el camino"
    return f""" Role: Act as a seasoned crime fiction writer, specializing in adding depth and tension to scenes.

            Task: I will provide you with two pieces of information:

            [Story Snippet]: A paragraph or section from an ongoing crime story.
            [Character Actions]: A list of specific actions performed by one character relevant to that story snippet.
            Your goal is to write one or more new paragraphs that seamlessly weave the specified [Character Actions] into the provided [Story Snippet]. You should:

            Integrate the actions naturally into the flow of the narrative.
            Feel free to expand on the scene by adding relevant details, internal thoughts of the character (if appropriate), dialogue with other characters present (or implied), descriptions of the environment, and minor related actions to make the scene feel complete and believable.
            Maintain the established tone and style of the [Story Snippet].
            Crucially, under no circumstances should you explicitly state or implicitly hint at the identity of the killer. The mystery must be preserved.
            Output: Provide only the newly written paragraph(s) that incorporate the character's actions, ready to be inserted into or appended to the original story snippet. Separate each paragraph with "/" return only the text of the new paragraph(s) without any additional commentary or formatting.
            **Story Text:**
        TextStory: {data_manager.data_list[history_id]['narrative']}

        Suspect: {data_manager.data_list[history_id]['choices']}

        List of moments:{path_list}
            
            """
                