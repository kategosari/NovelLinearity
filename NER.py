
import pickle
novelname = "(Chronicle of the Fallers 2) Hamilton, Peter F. - A Night Without Stars.txt"
aaa = open(novelname,"r")


sample = aaa.readlines()[500:]
sampleText = "".join(sample).replace("\n","")
sampleList = sampleText.split(".")
import spacy
from spacy import displacy

NER = spacy.load("en_core_web_sm")


locdic = {}
orgdic = {}
sCounter = 0
def saveFromSentence(text1):
    global locdic,orgdic,sCounter
    sCounter += 1
    text1= NER(text1)
    for word in text1.ents:

        if(word.label_ == "LOC"):
            try:
                locdic[word.text].append(sCounter)
            except KeyError:
                locdic[word.text]= [sCounter]
        if(word.label_ == "GPE"):
            try:
                locdic[word.text].append(sCounter)
            except KeyError:
                locdic[word.text]= [sCounter]
        if(word.label_ == "PERSON"):
            try:
                orgdic[word.text].append(sCounter)
            except KeyError:
                orgdic[word.text]= [sCounter]
counter = 0
print(len(sampleList))
for k in sampleList:
    counter += 1
    if(counter % 100 == 0):
        print(counter)
    saveFromSentence(k)

locationFile = open(novelname[:-4]+"LOCPERSON.txt","wb")
pickle.dump(locdic,locationFile)
pickle.dump(orgdic,locationFile)

locationFile.close()
aaa.close()