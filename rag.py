from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceInstructEmbeddings

model_name = "hkunlp/instructor-large"
model_kwargs = {'device': 'cuda:0'}
encode_kwargs = {'normalize_embeddings': True}

hf_embedding = HuggingFaceInstructEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs,
    show_progress=True
)

db = FAISS.load_local("faiss_AiDoc", embeddings=hf_embedding)

