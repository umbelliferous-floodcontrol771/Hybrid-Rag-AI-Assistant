import streamlit as st
from groq import Groq

from rag_pipeline import build_vector_db, rag_search
from router import route_question
from tools import wikipedia_tool


client = Groq(
    api_key="api key here"
)


class GroqLLM:

    def invoke(self, prompt):

        chat = client.chat.completions.create(
            model="openai/gpt-oss-120b", 
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return type("obj", (object,), {
            "content": chat.choices[0].message.content
        })


llm = GroqLLM()


#vector db building can be time consuming,
#so we do it once at the start and reuse the same vectorstore for all questions
vectorstore = build_vector_db()


#Streamlit UI
st.title("Hybrid AI Assistant")

question = st.text_input("Ask anything")


if question:

    # Try RAG first
    vector_answer = rag_search(vectorstore, question)

    if vector_answer:

        prompt = f"""
Use the context to answer the question.

Context:
{vector_answer}

Question:
{question}
"""

        response = llm.invoke(prompt)

        answer = response.content

        tool_used = "RAG (Vector DB)"

    else:

        tool = route_question(llm, question)

        if tool == "wiki":

            answer = wikipedia_tool(question)

            tool_used = "Wikipedia"

        else:

            response = llm.invoke(question)

            answer = response.content

            tool_used = "LLM"


    st.subheader("Answer")

    st.write(answer)

    st.caption(f"Tool used: {tool_used}")