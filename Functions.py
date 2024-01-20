import os
import nltk
import collections
import nltk
import math
import re
import numpy as np
import pyqtgraph as pg
from numpy import dot
from numpy.linalg import norm


def replace_hyphen(text):
    # Split the text into words
    words = text.split()

    # Iterate over the words and replace hyphens between letters with space
    for i in range(len(words)):
        words[i] = re.sub(r'(?<=[a-zA-Z])-(?=[a-zA-Z])', ' ', words[i])

    # Join the modified words back into a string
    result = ' '.join(words)

    return result



def TermesSplit(f):
    file = open(f, 'r')
    text = file.read()
    #text=text.replace('.',' ')
    #text=replace_hyphen(text)
    file.close()
    termeSplit = text.split()
    #termeSplit = re.split(r'[ \.,:]+', text)
    MotsVides = nltk.corpus.stopwords.words('english')
    TermesSplitSansMotsVides = [terme for terme in termeSplit if terme.lower() not in MotsVides]
    return TermesSplitSansMotsVides

def TermesToken(f,exp):
    file = open(f, 'r')
    text = file.read()
    #text = text.replace('.', ' ')
    #text = replace_hyphen(text)
    file.close()
    ExpReg = nltk.RegexpTokenizer(exp)
    termeToken = ExpReg.tokenize(text)
    MotsVides = nltk.corpus.stopwords.words('english')
    TermesTokenSansMotsVides = [terme for terme in termeToken if terme.lower() not in MotsVides]
    return TermesTokenSansMotsVides

def SplitPorter_1(f):
    Porter = nltk.PorterStemmer()
    TermesSplitNormalisationPorter = [Porter.stem(terme) for terme in TermesSplit(f)]
    return TermesSplitNormalisationPorter

def SplitLancaster_1(f):
    Lancaster = nltk.LancasterStemmer()
    TermesSplitNormalisationLancaster = [Lancaster.stem(terme) for terme in TermesSplit(f)]
    return TermesSplitNormalisationLancaster

def TokenPorter_1(f,exp):
    Porter = nltk.PorterStemmer()
    TermesTokenNormalisationPorter = [Porter.stem(terme) for terme in TermesToken(f, exp)]
    return TermesTokenNormalisationPorter

def TokenLancaster_1(f,exp):
    Lancaster = nltk.LancasterStemmer()
    TermesTokenNormalisationLancaster = [Lancaster.stem(terme) for terme in TermesToken(f, exp)]
    return TermesTokenNormalisationLancaster
def SplitPorter(f):
    Porter = nltk.PorterStemmer()
    TermesSplitNormalisationPorter = [Porter.stem(terme) for terme in TermesSplit(f)]
    TermesFrequence = {}
    for terme in TermesSplitNormalisationPorter:
        if (terme in TermesFrequence.keys()):
            TermesFrequence[terme] += 1
        else:
            TermesFrequence[terme] = 1
    collections.OrderedDict(sorted(TermesFrequence.items()))
    return TermesFrequence


def SplitLancaster(f):
    Lancaster = nltk.LancasterStemmer()
    TermesSplitNormalisationLancaster = [Lancaster.stem(terme) for terme in TermesSplit(f)]
    TermesFrequence = {}
    for terme in TermesSplitNormalisationLancaster:
        if (terme in TermesFrequence.keys()):
            TermesFrequence[terme] += 1
        else:
            TermesFrequence[terme] = 1
    collections.OrderedDict(sorted(TermesFrequence.items()))
    return TermesFrequence


def TokenPorter(f,exp):
    Porter = nltk.PorterStemmer()
    TermesTokenNormalisationPorter = [Porter.stem(terme) for terme in TermesToken(f, exp)]
    TermesFrequence = {}
    for terme in TermesTokenNormalisationPorter:
        if (terme in TermesFrequence.keys()):
            TermesFrequence[terme] += 1
        else:
            TermesFrequence[terme] = 1
    collections.OrderedDict(sorted(TermesFrequence.items()))
    return TermesFrequence


def TokenLancaster(f,exp):
    Lancaster = nltk.LancasterStemmer()
    TermesTokenNormalisationLancaster = [Lancaster.stem(terme) for terme in TermesToken(f, exp)]
    TermesFrequence = {}
    for terme in TermesTokenNormalisationLancaster:
        if (terme in TermesFrequence.keys()):
            TermesFrequence[terme] += 1
        else:
            TermesFrequence[terme] = 1
    collections.OrderedDict(sorted(TermesFrequence.items()))
    return TermesFrequence


def Descripteur(pathfiles,pathDesc,Type1,Type2,exp):
    if Type1=='split' and Type2=='Lanaster':
        file_out=open(pathDesc+'/DescripteursSplitLancaster',"w")
        file_out.close()
    elif Type1=='split' and Type2=='Porter':
        file_out = open(pathDesc + '/DescripteursSplitPorter', "w")
        file_out.close()
    elif Type1=='Token' and Type2=='Lanaster':
        file_out=open(pathDesc+'/DescripteursTokenLancaster',"w")
        file_out.close()
    elif Type1=='Token' and Type2=='Porter':
        file_out = open(pathDesc + '/DescripteursTokenPorter', "w")
        file_out.close()



    for filename in os.listdir(pathfiles):
        f = os.path.join(pathfiles, filename)
        dot_index = filename.rfind('.')
        nb_doc = filename[1:dot_index]
        if os.path.isfile(f):
            if Type1 == 'split' and Type2 == 'Lanaster':
                list_0=SplitLancaster_1(f)

                list = []
                for i in list_0:
                    if i not in list:
                        list.append(i)
                list.sort()
                list_2=SplitLancaster(f)

                for terme in list:
                    file_out = open(pathDesc + '/DescripteursSplitLancaster', "a")
                    file_out.write(nb_doc+' '+terme+' '+str(list_2.get(terme))+'\n')
            elif Type1 == 'split' and Type2 == 'Porter':
                list_0 = SplitPorter_1(f)
                list = []
                for i in list_0:
                    if i not in list:
                        list.append(i)
                list.sort()
                list_2 = SplitPorter(f)
                for terme in list:
                    file_out = open(pathDesc + '/DescripteursSplitPorter', "a")
                    file_out.write(nb_doc + ' ' + terme + ' ' + str(list_2.get(terme)) + '\n')
            elif Type1 == 'Token' and Type2 == 'Lanaster':
                list_0 = TokenLancaster_1(f,exp)
                list = []
                for i in list_0:
                    if i not in list:
                        list.append(i)
                list.sort()
                list_2 = TokenLancaster(f,exp)
                for terme in list:
                    file_out = open(pathDesc + '/DescripteursTokenLancaster', "a")
                    file_out.write(nb_doc+ ' ' + terme + ' ' + str(list_2.get(terme)) + '\n')
            elif Type1 == 'Token' and Type2 == 'Porter':
                list_0 = TokenPorter_1(f,exp)
                list = []
                for i in list_0:
                    if i not in list:
                        list.append(i)
                list.sort()
                list_2 = TokenPorter(f,exp)
                for terme in list:
                    file_out = open(pathDesc + '/DescripteursTokenPorter', "a")
                    file_out.write(nb_doc + ' ' + terme + ' ' + str(list_2.get(terme)) + '\n')
            file_out.close()

def Inverse(pathfiles,pathDesc,Type1,Type2,exp):

    global_list=[]

    for filename in os.listdir(pathfiles):
        f = os.path.join(pathfiles, filename)
        dot_index = filename.rfind('.')
        nb_doc = filename[1:dot_index]
        if os.path.isfile(f):
            if Type1 == 'split' and Type2 == 'Lanaster':
                list=SplitLancaster(f)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    global_list.append(terme+'_'+nb_doc+'_'+ str(list.get(terme)))
            elif Type1 == 'split' and Type2 == 'Porter':
                list = SplitPorter(f)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    global_list.append(terme+'_'+nb_doc+'_'+ str(list.get(terme)))
            elif Type1 == 'Token' and Type2 == 'Lanaster':
                list = TokenLancaster(f,exp)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    global_list.append(terme+'_'+nb_doc+'_'+ str(list.get(terme)))
            elif Type1 == 'Token' and Type2 == 'Porter':
                list = TokenPorter(f,exp)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    global_list.append(terme+'_'+nb_doc+'_'+ str(list.get(terme)))
    global_list.sort()
    if Type1=='split' and Type2=='Lanaster':
        file_out=open(pathDesc+'/InverseSplitLancaster',"w")
        for term in global_list:
            t= term.split('_')[0]
            d=term.split('_')[1]
            f=term.split('_')[2]
            file_out.write(t+' '+d+' '+f+'\n')
        file_out.close()
    elif Type1=='split' and Type2=='Porter':
        file_out = open(pathDesc + '/InverseSplitPorter', "w")
        for term in global_list:
            t= term.split('_')[0]
            d=term.split('_')[1]
            f=term.split('_')[2]
            file_out.write(t+' '+d+' '+f+'\n')
        file_out.close()
    elif Type1=='Token' and Type2=='Lanaster':
        file_out=open(pathDesc+'/InverseTokenLancaster',"w")
        for term in global_list:
            t= term.split('_')[0]
            d=term.split('_')[1]
            f=term.split('_')[2]
            file_out.write(t+' '+d+' '+f+'\n')
        file_out.close()
    elif Type1=='Token' and Type2=='Porter':
        file_out = open(pathDesc + '/InverseTokenPorter', "w")
        for term in global_list:
            t= term.split('_')[0]
            d=term.split('_')[1]
            f=term.split('_')[2]
            file_out.write(t+' '+d+' '+f+'\n')
        file_out.close()


def update_poids_inverse(path):
    d = [];t= [];f = [];p=[];mx=dict();nb_cnt=dict()
    nbr_ligne = 0
    with open(path) as file:
        for line in file:
            a1 = line.split(' ')[1]
            d.append(float(a1))
            a2 = line.split(' ')[0]
            t.append(a2)
            a3 = line.split(' ')[2]
            f.append(float(a3))
            nbr_ligne = nbr_ligne + 1
            a1 = int(a1)
            if a1 not in mx:
                mx[int(a1)] = a3

            if a3 > mx[int(a1)]:
                mx[int(a1)] = a3
            try:
                nb_cnt[str(a2)] += 1
            except Exception as e:
                nb_cnt[str(a2)] = 1

        nb_docs = len(set(d))
    for i in range(nbr_ligne):
        freq_ti_di=f[i]
        max_freq_t_di=mx.get(d[i])

        poid=float(freq_ti_di)/float(max_freq_t_di)
        n=0
        n=nb_cnt[str(t[i])]
        poid=poid*math.log10(1+(nb_docs/n))
        poid = "{:.4f}".format(poid)
        p.insert(i,poid)
    ff= open(path, 'w')
    for i in range(nbr_ligne):
        st =str(t[i])+' '+str(int(d[i]))+' '+str(int(f[i]))+' '+str(p[i])+'\n'
        ff.write(st)
    ff.close()

def update_poids_descripteur(path):
    d = [];t= [];f = [];p=[];mx=dict();nb_cnt=dict()
    nbr_ligne = 0
    with open(path) as file:
        for line in file:
            a1 = line.split(' ')[0]
            d.append(float(a1))
            a2 = line.split(' ')[1]
            t.append(a2)
            a3 = line.split(' ')[2]
            f.append(float(a3))
            nbr_ligne = nbr_ligne + 1
            a1=int(a1)
            if a1 not in mx :
                mx[int(a1)] = a3
            if int(a3) > int(mx[int(a1)]):
                mx[int(a1)] = int(a3)

            try:
                nb_cnt[str(a2)]+=1
            except Exception as e:
                nb_cnt[str(a2)]=1

    nb_docs = len(set(d))
    for i in range(nbr_ligne):
        freq_ti_di=f[i]
        poid=float(freq_ti_di)/float(mx.get(d[i]))
        n=nb_cnt[str(t[i])]
        poid=poid*math.log10(1+(nb_docs/n))
        poid = "{:.4f}".format(poid)
        p.insert(i,poid)
    ff= open(path, 'w')
    for i in range(nbr_ligne):
        st =str(int(d[i]))+' '+str(t[i])+' '+str(int(f[i]))+' '+str(p[i])+'\n'
        ff.write(st)
    ff.close()

def get_docs_desc(path):
    l=[]
    with open(path,'r') as file:
        for line in file:
            a1 = int(line.split(' ')[0])
            if a1 not in l:
                l.append(a1)
    return l

def sentece_token(sentence,exp):
    ExpReg = nltk.RegexpTokenizer(exp)
    termeToken = ExpReg.tokenize(sentence)
    MotsVides = nltk.corpus.stopwords.words('english')
    TermesTokenSansMotsVides = [terme for terme in termeToken if terme.lower() not in MotsVides]
    ret_sentence = ' '.join(TermesTokenSansMotsVides)
    return ret_sentence

def sentence_porter_stemming(sentence):
    sentence=sentence.lower()

    words = sentence.split()
    porter_stemmer = nltk.PorterStemmer()

    stemmed_words = [porter_stemmer.stem(word) for word in words]
    stemmed_sentence = ' '.join(stemmed_words)
    return stemmed_sentence

def sentence_lancaster_stemming(sentence):
    sentence = sentence.lower()

    words = sentence.split()
    lancaster_stemmer = nltk.LancasterStemmer()

    stemmed_words = [lancaster_stemmer.stem(word) for word in words]
    stemmed_sentence = ' '.join(stemmed_words)
    return stemmed_sentence
def RSV(Q,path_file_desc,type):
    Q = Q.lower()
    words = Q.split()
    l=len(words)
    R = {}
    n = 0
    if type=='Scalar Product':
        with open(path_file_desc, 'r') as file:
            lines = file.readlines()
            prev_doc=int(lines[0].split()[0])
            for line in lines:
                if int(line.split()[0]) == prev_doc:
                    text=line.split()[1].lower()
                    if text in words:
                        p=float(line.split()[3])
                        n+=p
                else:
                    R[str(prev_doc)]=n
                    prev_doc=int(line.split()[0])
                    n=0
                    text = line.split()[1].lower()
                    if text in words:
                        p = float(line.split()[3])
                        n += p
        R[str(prev_doc)] = n
        R = dict(sorted(R.items(), key=lambda item: item[1], reverse=True))
        R = {key: value for key, value in R.items() if value != 0}
    elif type=='Cosine Measure':

        Qar=np.array([])
        Dar=np.array([])
        with open(path_file_desc, 'r') as file:
            lines = file.readlines()
            prev_doc=int(lines[0].split()[0])
            for line in lines:
                if int(line.split()[0]) == prev_doc:
                    text=line.split()[1].lower()
                    if text in words:
                        Qar=np.append(Qar,1)
                        Dar=np.append(Dar,float(line.split()[3]))
                    else:
                        Qar=np.append(Qar,0)
                        Dar=np.append(Dar,float(line.split()[3]))
                else:
                    n = dot(Qar, Dar) / ((l**0.5) * norm(Dar))
                    if math.isnan(n):
                        n = 0
                    R[str(prev_doc)] = n
                    prev_doc = int(line.split()[0])
                    n = 0
                    Qar = np.array([])
                    Dar = np.array([])
                    text = line.split()[1].lower()
                    if text in words:
                        Qar = np.append(Qar, 1)
                        Dar = np.append(Dar, float(line.split()[3]))
                    else:
                        Qar = np.append(Qar, 0)
                        Dar = np.append(Dar, float(line.split()[3]))
            n = dot(Qar, Dar) / ((l ** 0.5) * norm(Dar))
            R[str(prev_doc)] = n
            R = dict(sorted(R.items(), key=lambda item: item[1], reverse=True))
            R = {key: value for key, value in R.items() if value != 0}
    elif type=='Jaccard Measure':
        Qar=np.array([])
        Dar=np.array([])
        with open(path_file_desc, 'r') as file:
            lines = file.readlines()
            prev_doc=int(lines[0].split()[0])
            for line in lines:
                if int(line.split()[0]) == prev_doc:
                    text=line.split()[1].lower()
                    if text in words:
                        Qar = np.append(Qar, 1)
                        Dar = np.append(Dar, float(line.split()[3]))
                    else :
                        Qar = np.append(Qar, 0)
                        Dar = np.append(Dar, float(line.split()[3]))
                else:
                    Vi = sum(Qar[:] ** 2)
                    Wi = sum(Dar[:] ** 2)
                    P=dot(Qar, Dar)
                    a=l+Wi-P
                    if a!=0:
                        n=P/a
                    if math.isnan(n) :
                        n=0
                    R[str(prev_doc)] = n
                    prev_doc = int(line.split()[0])
                    n = 0
                    Qar = np.array([])
                    Dar = np.array([])
                    text = line.split()[1].lower()
                    if text in words:
                        Qar = np.append(Qar, 1)
                        Dar = np.append(Dar, float(line.split()[3]))
                    else:
                        Qar = np.append(Qar, 0)
                        Dar = np.append(Dar, float(line.split()[3]))
            Vi = sum(Qar[:] ** 2)
            Wi = sum(Dar[:] ** 2)
            P = dot(Qar, Dar)
            a = l + Wi - P
            if a != 0:
                n = P / a
            if math.isnan(n):
                n = 0
            R[str(prev_doc)] = n
            R = dict(sorted(R.items(), key=lambda item: item[1], reverse=True))
            R = {key: value for key, value in R.items() if value != 0}
    return R
def RSV_BM25(Q,path_file_desc,K,B):
    Q = Q.lower()
    words = Q.split()
    taille_docs =dict()
    avdl=0
    s=0
    R={}
    nb_doc_term={}
    with open(path_file_desc, 'r') as file:
        lines = file.readlines()
        for line in lines:
            i=int(line.split()[0])
            g=int(line.split()[2])
            try:
                nb_doc_term[str(line.split()[1].lower())]+=1
            except Exception as e:
                nb_doc_term[str(line.split()[1].lower())] = 1
            try:
                taille_docs[i]+=g
            except KeyError:
                taille_docs[i] = g

        N=len(taille_docs)
        for i in taille_docs.keys():
            avdl+=taille_docs[i]
        avdl=avdl/N
    with open(path_file_desc, 'r') as file:
        lines = file.readlines()
        prev_doc=int(lines[0].split()[0])
        dl = taille_docs[prev_doc]
        for line in lines:
            curr_d= int(line.split()[0])
            if curr_d==prev_doc :
                text=line.split()[1].lower()
                if text in words:
                    f=int(line.split()[2])

                    Ni=nb_doc_term[text]
                    c1=f+K*((1-B)+B*(dl/avdl))
                    b=math.log(((N - Ni + 0.5) / (Ni + 0.5)),10)
                    a=b*(f/c1)
                    s+=a
            else:
                R[str(prev_doc)] = s
                s=0
                prev_doc = int(line.split()[0])
                dl = taille_docs[prev_doc]
                text=line.split()[1].lower()
                if text in words:
                    f=int(line.split()[2])

                    Ni=nb_doc_term[text]
                    c1=f+K*((1-B)+B*(dl/avdl))
                    b=math.log(((N - Ni + 0.5) / (Ni + 0.5)),10)
                    a=b*(f/c1)
                    s+=a
        R[str(prev_doc)] = s
        R = dict(sorted(R.items(), key=lambda item: item[1], reverse=True))
        R = {key: value for key, value in R.items() if value != 0}
    return R

def RSV_Bool(Q,path_file_desc):
    Q = Q.lower()
    words = Q.split()
    doc=[]
    result_str=''
    R={}
    for word in words:
        if word not in ('and', 'or', 'not'):
            new_word = f" \"{word}\" in doc"
        else:
            new_word = ' ' + word
        result_str = result_str + new_word

    try:
        result = eval(result_str)
        if isinstance(result, bool):
            with open(path_file_desc, 'r') as file:
                lines = file.readlines()
                prev_d = int(lines[0].split()[0])
                for line in lines:
                    curr_d= int(line.split()[0])
                    if curr_d==prev_d :
                        j=str(line.split()[1])
                        j=j.lower()
                        doc.append(j)
                    else:
                        result = eval(result_str)
                        if result :
                            R[str(prev_d)]='YES'
                        else:
                            R[str(prev_d)]='NO'

                        doc.clear()
                        j = str(line.split()[1])
                        j = j.lower()
                        doc.append(j)
                        prev_d=curr_d
                result = eval(result_str)
                if result:
                    R[str(prev_d)] = 'YES'
                else:
                    R[str(prev_d)] = 'NO'
    except Exception as e:
        print(e)
        R['1'] = 'Error syntax'
    return R

def judgments_load(path):
    judgfile = {}
    lines = open(path, "r").read().split("\n")
    for line in lines:
        line = line.split()
        if line[0] in judgfile.keys():
            judgfile[line[0]].append(line[1])
        else:
            judgfile[line[0]] = []
            judgfile[line[0]].append(line[1])
    return judgfile

def MPrecision(judg_load, RSV_list,p5,p10,precision,recall,fscore,widget):


    RSV_list = np.array(list(RSV_list.keys()))

    P = {}
    R = {}
    Fscore = {}
    doc_perSelected = 0
    NBRDocSelected = len(RSV_list)

    for i in range(NBRDocSelected):
        if str(RSV_list[i]) in judg_load:
            doc_perSelected += 1
        P[i] = round(doc_perSelected / (i + 1), 5)
        R[i] = round(doc_perSelected / len(judg_load), 5)
        if i == 4:
            p5.setText(str(doc_perSelected / 5))
        if i == 9:
            print('ok')
            p10.setText(str(doc_perSelected / 10))
        if not (P[i] + R[i]) == 0:
            Fscore[i] = round(2 * P[i] * R[i] / (P[i] + R[i]), 5)
        else:
            Fscore[i] = 0

    precision.setText(str(P[NBRDocSelected - 1]))

    recall.setText(str(R[NBRDocSelected - 1]))

    fscore.setText(str(Fscore[NBRDocSelected - 1]))


    Rj = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    Pj = []
    R = list(R.values())

    for i in range(len(Rj)):
        l = []
        for j in range(len(R)):
            if (R[j] >= Rj[i]):
                l.append(P[j])
        if len(l) > 0:
            Pj.append(max(l))
        else:
            Pj.append(0)
    widget.clear()
    widget.setBackground("w")
    pen = pg.mkPen(color=(255, 0, 0))
    widget.setTitle("Curve Recall/Precision", color="b", size="20pt")
    styles = {"color": "red", "font-size": "18px"}
    widget.setLabel("left", "Precision", **styles)
    widget.setLabel("bottom", "Recall", **styles)
    widget.plot(Rj, Pj, symbol="+", pen=pen)

if __name__ == '__main__':
    Q='Documents AND NOT ranking OR queries OR GPT-3.5'
    Q = sentence_porter_stemming(Q)
    print(Q)
    #print(RSV_BM25(Q,'./Index/DescripteursTokenPorter',2,1.5))
    print(RSV_Bool(Q,'./Index/DescripteursTokenPorter'))




