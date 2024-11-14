import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pickle

data_dir = 'Data/Structured/'
chunk_size = 1200
chunk_overlap = 300
text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)


all_docs = []
for path in os.listdir(data_dir):
    if not path.endswith('txt'):
        continue

    with open(file=data_dir + path, encoding='utf-8') as f:
        file_data = f.read()
        
    docs = text_splitter.split_text(file_data)
    
    for i, chunk in enumerate(docs):
        chunk_data = f"File Name: {path.replace('.txt', '')}\nChunk Number: {i + 1}\n{chunk}"
        all_docs.append(chunk_data) 

    print(f'Processed: {path}')

print(all_docs[0])
print(len(all_docs))
with open('Data/Structured/processed', 'wb') as f:
    pickle.dump(all_docs, f)