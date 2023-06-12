import os

# read the index.txt and preapre documents,vocab,idf
with open("index.txt", "r") as f:
    lines = f.readlines()
    # print(lines) 
    # here, we're just going through each line in index.txt i.e the question number and the question name and lines is a list of all question names as its elements


def preprocess(document_text):
    terms = [term.strip() for term in document_text.lower().split()[1:]]#here terms is a list of words which exist in a line i.e an element of 
    # terms=[term.lower() for term in document_text.strip().split()[1:]]
    # print(terms)#just printing all the terms in the document of array of lines
    return terms


vocab = {}
documents = []
for index, line in enumerate(lines):
    # print(index,end=" ")
    # read that problem statement and add it to the document string

    tokens = preprocess(line)
    documents.append(tokens)#we're appending each list of words of the questions to the documents list again,i.e now documents again is a list of lists

    
    tokens = set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1
# gives the frequency of "term" across all documents
# that is if the is present twice in same documents we count it only once not twice
# if the is present in doc-2 then we do frequency+=1
# print(documents[:5])

# reverse sort the vocab by the values
vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))

# print("Number of documnets: ",len(documents))
# print("Size of vocab: ",len(vocab))
# print("Sample document: ",documents[0])
# print(vocab)

# save the vocab in a text file

with open("tf-idf/vocab.txt", "w") as f:
    for key in vocab.keys():
        f.write("%s\n" % key)
        #we're just storing those words in descending order

with open("tf-idf/idf-values.txt", "w") as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])

# saving documents in text file
with open("tf-idf/documents.txt", "w") as f:
    for document in documents:
        f.write("%s\n" % " ".join(document))

# inverted index construction
inverted_index = {}
for index, document in enumerate(documents):
    for token in document:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else:
            inverted_index[token].append(index)

# save the inverted index in a text file
with open("tf-idf/inverted-index.txt", "w") as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % " ".join(str(doc_id) for doc_id in inverted_index[key]))
