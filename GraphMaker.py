#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kategosari
#
# Created:     04-11-2023
# Copyright:   (c) kategosari 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import spacy
from spacy import displacy
import matplotlib.pyplot as plt
NER = spacy.load("en_core_web_sm")

import pickle
novelname = "(Chronicle of the Fallers 2) Hamilton, Peter F. - A Night Without Stars.txt"
theNovel = open(novelname,"r")
theDic = open(novelname[:-4]+"LOCPERSON.txt","rb")
def prepareSample(file):
    sample = file.readlines()[500:]
    sampleText = "".join(sample).replace("\n","")
    sampleList = sampleText.split(".")
    return sampleList


def removeSmall(myDict,threshHold):
    myDict = {key:val for key, val in myDict.items() if len(val) > threshHold}
    return myDict
def scoreAdder(nerd,sDic,gajung,blacklist):

    for j in nerd.ents:
        if(j.label_ == 'PERSON' and j.text not in blacklist):

            try:
                sDic[j.text] += gajung
            except KeyError:
                sDic[j.text] = gajung

sample = prepareSample(theNovel)

location = removeSmall(pickle.load(theDic),1)
people = pickle.load(theDic)
def placeRunner(text,place,width=20):
    global  location
    XL = location[place]
    scoreDic = {}
    for j in XL:
        sampleSpace = text[j-1-width:j-1+width]

        for idx, k in enumerate(sampleSpace):
            k = NER(k)
            scoreAdder(k,scoreDic,0.8**abs(idx-width),location)
    return scoreDic

import networkx as nx

G = nx.Graph()
for l in location.keys():
    G.add_node(l,label = l,node_type = "blue")
for l in people.keys():
    G.add_node(l,label = l,node_type = "red")
for j in location.keys():
    tempdic = placeRunner(sample,j,20)

    for l in tempdic:
        G.add_edge(j,l,weight = tempdic[l])

big_graph = open("ExpGraph.pickle","wb")
pickle.dump(G,big_graph)
big_graph.close()