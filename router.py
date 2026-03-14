def route_question(llm, question):

    prompt = f"""
You are an AI router deciding which tool should answer a question.

Tools:

wiki → factual knowledge about people, places, history
llm → reasoning, explanations, opinions

Question: {question}

Answer ONLY one word:
wiki
llm
"""

    response = llm.invoke(prompt)

    tool = response.content.strip().lower()

    print("ROUTER SELECTED:", tool)

    return tool