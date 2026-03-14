from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def build_vector_db():

    loader = TextLoader("Data/docs.txt")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embeddings)

    return vectorstore


def rag_search(vectorstore, question):

    results = vectorstore.similarity_search_with_score(question, k=2)

    best_doc, score = results[0]

    print("SIMILARITY SCORE:", score)

    if score < 0.8:
        return best_doc.page_content

    return None