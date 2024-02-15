# https://www.algoexpert.io/questions/generate-document

def generateDocument(characters, document):
    c = list(characters)
    d = list(document)

    for char in characters:
        if char in d:
            index = d.index(char)
            d.pop(index)

    return len(d) == 0
