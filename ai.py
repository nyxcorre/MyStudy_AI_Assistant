import google.generativeai as genai

import streamlit as st

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash-lite"
)



# AI CHAT

def ask_ai(question):

    try:

        prompt = f"""
        You are MyStudy AI assistant.

        Explain this topic simply:

        {question}
        """


        response = model.generate_content(
            prompt
        )


        return response.text


    except Exception as e:

        return str(e)


# STUDY PLANNER

def create_plan(subjects, days, hours):


    prompt=f"""

    Make a personalized study timetable.

    Subjects:
    {subjects}

    Days remaining:
    {days}

    Daily hours:
    {hours}

    Include breaks and revision.

    """


    response=model.generate_content(prompt)

    return response.text




# NOTES GENERATOR

def generate_notes(topic):


    prompt=f"""

    Create exam notes for:

    {topic}


    Include:
    - definition
    - important points
    - examples
    - exam questions

    """


    response=model.generate_content(prompt)


    return response.text




# FLASHCARDS

def make_flashcards(topic):


    prompt=f"""

    Create flashcards for:

    {topic}


    Format:

    Question:
    Answer:


    Make minimum 10 cards.

    """


    response=model.generate_content(prompt)


    return response.text
