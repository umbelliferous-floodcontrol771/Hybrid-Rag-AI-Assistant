                Hybrid AI Assistant chatbot

Features:
 Can answer to your personal documents with,
 RAG with FAISS vector DB

 it also have,
 Similarity threshold routing which handles question out of the box of private documents so we added,
 Wikipedia tool integration
 LLM fallback reasoning

 Just a simple ,Streamlit interface



 Decission Architecture of the Assistant 

User Query  
→ Vector Similarity Search  
→ If match → RAG   (for grounded answering of personal documents)
→ Else → Router  
→ Wikipedia / LLM


#Data folder having doc.txt contains only my information for grouding answer checking, User can use and modify with their own .txt document for their downstream task perpous chatbot as per their need !