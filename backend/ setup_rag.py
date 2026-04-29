from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
import os
from dotenv import load_dotenv

load_dotenv()

my_key = os.getenv("GEMINI_EMBEDDING_API_KEY")


## load document

file_path = "/home/Mr.nobody_3000/Desktop/Code/AI/Mark_1/backend/Company_Docs/skills-and-behaviours-for-customer-care-entry-3.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

# Splitting just the first page to save memory
texts = text_splitter.split_documents([docs[0]])



# --- 3. Embedding ---


embeddings_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001", google_api_key=my_key
)

vector_store = Chroma.from_documents(
    documents=texts,
    embedding=embeddings_model,
    persist_directory="./Vector"
)





