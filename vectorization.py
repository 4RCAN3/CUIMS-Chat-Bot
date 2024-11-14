from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
import pickle

'''with open('Data/Structured/processed', 'rb') as f:
    all_docs = pickle.load(f)'''

model_name = "hkunlp/instructor-large"
model_kwargs = {'device': 'cuda:0'}
encode_kwargs = {'normalize_embeddings': True}

hf_embedding = HuggingFaceInstructEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs,
    show_progress=True
)

'''db = FAISS.from_texts(all_docs, hf_embedding, verbose = 0)
db.save_local("vectors")'''