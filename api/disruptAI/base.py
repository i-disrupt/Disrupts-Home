import os
import openai as DisruptAI
from .setting import key

DisruptAI.api_key = key

class BaseTools():
    def __init__():
        return "Initialization Function"

    def Query(qpt, m='text-davinci-002', t=0, mt=100, tp=1, fp=0.0, pp=0.0, s=["\n"]):
        r"""
        Query a response from the AI
        usage: `Query(qpt='This is what the AI is being prompted')`

        Query:
            m / Model (text-davinci-002, text-ada-001, text-curie-001)
            t / Temperature
            mt / Max amount of tokens to spend
            tp / top p
            fp / frequency penalty
            pp / presence_penalty
            s / what character makes the ai stop

        """
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: Where is the Valley of Kings?\nA:",
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
        )

    def Request(query):
        Query(query)