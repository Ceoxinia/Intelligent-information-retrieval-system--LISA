import collections
import math
import os
import tkinter as tk
import sys
import tkinter as tk
import tkinter.ttk as ttk
from builtins import int
from tkinter.constants import *
from tkinter import ttk
import os.path
import nltk
_script = sys.argv[0]
_location = os.path.dirname(_script)







def TermesSplit(f):
    file = open(f, 'r')
    text = file.read()
    file.close()
    termeSplit = text.split()
    MotsVides = nltk.corpus.stopwords.words('english')
    TermesSplitSansMotsVides = [terme for terme in termeSplit if terme.lower() not in MotsVides]
    return TermesSplitSansMotsVides

def TermesToken(f,exp):
    file = open(f, 'r')
    text = file.read()
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
                    file_out.write(filename[1]+' '+terme+' '+str(list_2.get(terme))+'\n')
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
                    file_out.write(filename[1] + ' ' + terme + ' ' + str(list_2.get(terme)) + '\n')
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
                    file_out.write(filename[1] + ' ' + terme + ' ' + str(list_2.get(terme)) + '\n')
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
                    file_out.write(filename[1] + ' ' + terme + ' ' + str(list_2.get(terme)) + '\n')

            file_out.close()

def Inverse(pathfiles,pathDesc,Type1,Type2,exp):

    global_list=[]

    for filename in os.listdir(pathfiles):
        f = os.path.join(pathfiles, filename)

        if os.path.isfile(f):
            if Type1 == 'split' and Type2 == 'Lanaster':
                list=SplitLancaster(f)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    global_list.append(terme+'_'+filename[1]+'_'+ str(list.get(terme)))
            elif Type1 == 'split' and Type2 == 'Porter':
                list = SplitPorter(f)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    global_list.append(terme+'_'+filename[1]+'_'+ str(list.get(terme)))
            elif Type1 == 'Token' and Type2 == 'Lanaster':
                list = TokenLancaster(f,exp)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    global_list.append(terme+'_'+filename[1]+'_'+ str(list.get(terme)))
            elif Type1 == 'Token' and Type2 == 'Porter':
                list = TokenPorter(f,exp)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    global_list.append(terme+'_'+filename[1]+'_'+ str(list.get(terme)))
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
    d = [];t= [];f = [];p=[]
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

    for i in range(nbr_ligne):
        freq_ti_di=f[i]
        max_freq_t_di=f[i]
        for j in range(nbr_ligne):
            if d[j]==d[i]:
                if f[j]>max_freq_t_di:
                    max_freq_t_di=f[j]
        poid=float(freq_ti_di)/float(max_freq_t_di)
        nb_docs=len(set(d))
        n=0
        for j in range(nbr_ligne):
            if t[j]==t[i]:
                n+=1
        poid=poid*math.log10(1+(nb_docs/n))
        poid = "{:.4f}".format(poid)
        p.insert(i,poid)
    ff= open(path, 'w')
    for i in range(nbr_ligne):
        st =str(t[i])+' '+str(int(d[i]))+' '+str(int(f[i]))+' '+str(p[i])+'\n'
        ff.write(st)
    ff.close()

def update_poids_descripteur(path):
    d = [];t= [];f = [];p=[]
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

    for i in range(nbr_ligne):
        freq_ti_di=f[i]
        max_freq_t_di=f[i]
        for j in range(nbr_ligne):
            if d[j]==d[i]:
                if f[j]>max_freq_t_di:
                    max_freq_t_di=f[j]
        poid=float(freq_ti_di)/float(max_freq_t_di)
        nb_docs=len(set(d))
        n=0
        for j in range(nbr_ligne):
            if t[j]==t[i]:
                n+=1
        poid=poid*math.log10(1+(nb_docs/n))
        poid = "{:.4f}".format(poid)
        p.insert(i,poid)
    ff= open(path, 'w')
    for i in range(nbr_ligne):
        st =str(int(d[i]))+' '+str(t[i])+' '+str(int(f[i]))+' '+str(p[i])+'\n'
        ff.write(st)
    ff.close()



_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black'
_tabfg2 = 'black'
_tabbg1 = 'grey75'
_tabbg2 = 'grey89'
_bgmode = 'light'

class App:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("824x764+539+44")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0,  0)
        top.title("TP_RI")
        top.configure(background="#d9d9d9")

        self.top = top
        self.var_porter_stemmer = tk.IntVar()
        self.var_tokenization = tk.IntVar()
        self.che57 = tk.IntVar()
        self.selectedButton = tk.IntVar()
        self.che76 = tk.IntVar()
        self.term_per_doc = tk.IntVar()
        self.doc_per_term = tk.IntVar()

        self.che57.set(1)
        self.che76.set(0)

        self.Query = tk.Label(self.top)
        self.Query.place(x=49, y=53, height=26, width=61)
        self.Query.configure(anchor='w')
        self.Query.configure(background="#d9d9d9")
        self.Query.configure(compound='left')
        self.Query.configure(disabledforeground="#a3a3a3")
        self.Query.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Query.configure(foreground="#000000")
        self.Query.configure(text='''Query''')
        self.Entry = tk.Entry(self.top)
        self.Entry.place(x=126, y=53, height=30, width=384)
        self.Entry.configure(background="white")
        self.Entry.configure(disabledforeground="#a3a3a3")
        self.Entry.configure(font="TkFixedFont")
        self.Entry.configure(foreground="#000000")
        self.Entry.configure(insertbackground="black")
        self.Button1 = tk.Button(self.top)
        self.Button1.place(x=516, y=53, height=30, width=80)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=self.Commande_button_search)
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Search''')
        self.List_result = ttk.Treeview(self.top)
        self.List_result.place(x=50, y=190, height=558, width=554)



        self.List_result.heading(text="N°")
        self.List_result.heading(text="N°doc")
        self.List_result.heading(text="Terme")
        self.List_result.heading(text="Freq")
        self.List_result.heading(text="Poids")


        self.Spinbox1 = tk.Spinbox(self.top, from_=1.0, to=100.0)
        self.Spinbox1.place(x=730, y=50, height=31, width=59)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(justify='center')
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(state="disabled")
        self.Labelframe1 = tk.LabelFrame(self.top)
        self.Labelframe1.place(x=610, y=180, height=79, width=197)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Labelframe1.configure(foreground="#000000")
        self.Labelframe1.configure(text='''Matching''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe2 = tk.LabelFrame(self.top)
        self.Labelframe2.place(x=49, y=127, height=58, width=233)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Labelframe2.configure(foreground="#000000")
        self.Labelframe2.configure(text='''Processing''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Check_porter_stemmer = tk.Checkbutton(self.Labelframe2)
        self.Check_porter_stemmer.place(x=110, y=22, height=25, width=115
                , bordermode='ignore')
        self.Check_porter_stemmer.configure(activebackground="beige")
        self.Check_porter_stemmer.configure(activeforeground="black")
        self.Check_porter_stemmer.configure(anchor='w')
        self.Check_porter_stemmer.configure(background="#d9d9d9")
        self.Check_porter_stemmer.configure(compound='left')
        self.Check_porter_stemmer.configure(disabledforeground="#a3a3a3")
        self.Check_porter_stemmer.configure(foreground="#000000")
        self.Check_porter_stemmer.configure(highlightbackground="#d9d9d9")
        self.Check_porter_stemmer.configure(highlightcolor="black")
        self.Check_porter_stemmer.configure(justify='left')
        self.Check_porter_stemmer.configure(selectcolor="#d9d9d9")
        self.Check_porter_stemmer.configure(text='''Porter Stemmer''')
        self.Check_porter_stemmer.configure(variable=self.var_porter_stemmer)
        self.Check_porter_stemmer.configure(offvalue=0)
        self.Check_porter_stemmer.configure(onvalue=1)

        self.Check_tokenization = tk.Checkbutton(self.Labelframe2)
        self.Check_tokenization.place(x=10, y=21, height=27, width=98
                , bordermode='ignore')
        self.Check_tokenization.configure(activebackground="beige")
        self.Check_tokenization.configure(activeforeground="black")
        self.Check_tokenization.configure(anchor='w')
        self.Check_tokenization.configure(background="#d9d9d9")
        self.Check_tokenization.configure(compound='left')
        self.Check_tokenization.configure(disabledforeground="#a3a3a3")
        self.Check_tokenization.configure(foreground="#000000")
        self.Check_tokenization.configure(highlightbackground="#d9d9d9")
        self.Check_tokenization.configure(highlightcolor="black")
        self.Check_tokenization.configure(justify='left')
        self.Check_tokenization.configure(selectcolor="#d9d9d9")
        self.Check_tokenization.configure(text='''Tokenization''')
        self.Check_tokenization.configure(variable=self.var_tokenization)
        self.Check_tokenization.configure(offvalue=0)
        self.Check_tokenization.configure(onvalue=1)
        self.Labelframe3 = tk.LabelFrame(self.top)
        self.Labelframe3.place(x=292, y=127, height=58, width=310)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Labelframe3.configure(foreground="#000000")
        self.Labelframe3.configure(text='''Index''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Check_index = tk.Checkbutton(self.Labelframe3)
        self.Check_index.place(x=10, y=21, height=25, width=37
                , bordermode='ignore')
        self.Check_index.configure(activebackground="beige")
        self.Check_index.configure(activeforeground="black")
        self.Check_index.configure(anchor='w')
        self.Check_index.configure(background="#d9d9d9")
        self.Check_index.configure(compound='left')
        self.Check_index.configure(disabledforeground="#a3a3a3")
        self.Check_index.configure(foreground="#000000")
        self.Check_index.configure(highlightbackground="#d9d9d9")
        self.Check_index.configure(highlightcolor="black")
        self.Check_index.configure(justify='left')
        self.Check_index.configure(command=self.Commande_check_index)
        self.Check_index.configure(selectcolor="#d9d9d9")
        self.Check_index.configure(onvalue=1)
        self.Check_index.configure(offvalue=0)
        self.Check_index.configure(variable=self.che57)
        self.Radio_docs_per_term = tk.Radiobutton(self.Labelframe3)
        self.Radio_docs_per_term.place(x=68, y=21, height=25, width=106
                , bordermode='ignore')
        self.Radio_docs_per_term.configure(activebackground="beige")
        self.Radio_docs_per_term.configure(activeforeground="black")
        self.Radio_docs_per_term.configure(anchor='w')
        self.Radio_docs_per_term.configure(background="#d9d9d9")
        self.Radio_docs_per_term.configure(compound='left')
        self.Radio_docs_per_term.configure(disabledforeground="#a3a3a3")
        self.Radio_docs_per_term.configure(foreground="#000000")
        self.Radio_docs_per_term.configure(highlightbackground="#d9d9d9")
        self.Radio_docs_per_term.configure(highlightcolor="black")
        self.Radio_docs_per_term.configure(justify='left')
        self.Radio_docs_per_term.configure(selectcolor="#d9d9d9")
        self.Radio_docs_per_term.configure(text='''DOCS per Term''')
        self.Radio_docs_per_term.configure(variable=self.doc_per_term)
        self.Radio_docs_per_term.configure(value=1)

        self.Radio_terms_per_docs = tk.Radiobutton(self.Labelframe3)
        self.Radio_terms_per_docs.place(x=184, y=21, height=25, width=120
                , bordermode='ignore')
        self.Radio_terms_per_docs.configure(activebackground="beige")
        self.Radio_terms_per_docs.configure(activeforeground="black")
        self.Radio_terms_per_docs.configure(anchor='w')
        self.Radio_terms_per_docs.configure(background="#d9d9d9")
        self.Radio_terms_per_docs.configure(compound='left')
        self.Radio_terms_per_docs.configure(disabledforeground="#a3a3a3")
        self.Radio_terms_per_docs.configure(foreground="#000000")
        self.Radio_terms_per_docs.configure(highlightbackground="#d9d9d9")
        self.Radio_terms_per_docs.configure(highlightcolor="black")
        self.Radio_terms_per_docs.configure(justify='left')
        self.Radio_terms_per_docs.configure(selectcolor="#d9d9d9")
        self.Radio_terms_per_docs.configure(text='''Terms per DOCS''')
        self.Radio_terms_per_docs.configure(variable=self.term_per_doc)
        self.Radio_terms_per_docs.configure(value=1)

        self.Check_queries_dataset = tk.Checkbutton(self.top)
        self.Check_queries_dataset.place(x=610, y=50, height=29, width=111)
        self.Check_queries_dataset.configure(activebackground="beige")
        self.Check_queries_dataset.configure(activeforeground="black")
        self.Check_queries_dataset.configure(anchor='w')
        self.Check_queries_dataset.configure(background="#d9d9d9")
        self.Check_queries_dataset.configure(compound='left')
        self.Check_queries_dataset.configure(disabledforeground="#a3a3a3")
        self.Check_queries_dataset.configure(foreground="#000000")
        self.Check_queries_dataset.configure(highlightbackground="#d9d9d9")
        self.Check_queries_dataset.configure(highlightcolor="black")
        self.Check_queries_dataset.configure(justify='left')
        self.Check_queries_dataset.configure(selectcolor="#d9d9d9")
        self.Check_queries_dataset.configure(text='''Queries Dataset''')
        self.Check_queries_dataset.configure(variable=self.che76)
        self.Check_queries_dataset.configure(command=self.Commande_check_queries)
    def Commande_check_queries(self):
        if self.che76.get()==0:
            self.Spinbox1.config(state=DISABLED)
        else:
            self.Spinbox1.config(state=NORMAL)

    def Commande_check_index(self):
        if self.che57.get()==0:
            self.Radio_terms_per_docs.config(state=DISABLED)
            self.Radio_docs_per_term.config(state=DISABLED)
        else:
            self.Radio_terms_per_docs.config(state=NORMAL)
            self.Radio_docs_per_term.config(state=NORMAL)
    def Commande_button_search(self):
        l1=[];l2=[];l3=[];l4=[]

        if self.term_per_doc.get()==1 :
            if self.var_tokenization.get()==1:
                if self.var_porter_stemmer.get()==1:
                    file='./Index/DescripteursTokenPorter'
                    nbr_ligne=0
                    list=[]
                    with open(file) as file:
                        for line in file:
                            a1 = line.split(' ')[0]
                            l1.append(a1)
                            a2 = line.split(' ')[1]
                            l2.append(a2)
                            a3 = line.split(' ')[2]
                            l3.append(a3)
                            a4 = line.split(' ')[3]
                            l4.append(a4)

                            nbr_ligne = nbr_ligne + 1
                    j=0
                    for i in range(nbr_ligne):
                        if l1[i]==self.Entry.get():
                            j+=1
                            res=str(j)+' '+l1[i]+' '+l2[i]+' '+l3[i]+' '+l4[i]+'\n'
                            list.append(res)
                    self.List_result.curselection()
                    self.List_result.delete(0,'end')
                    r=0
                    list.reverse()
                    for a in list :
                        r+=1
                    for i in range(r):
                        self.List_result.insert(0, list[i])


        print("test")


if __name__ == '__main__':
    path = "./Collection"
    path_out = "./Index"
    exp = '(?:[A-Z]\.)+|\d+(?:\.\d+)?DA?|\w+|\.{3}'

    Descripteur(path, path_out, 'split', 'Lanaster', '')
    Descripteur(path, path_out, 'Token', 'Lanaster', exp)
    Descripteur(path, path_out, 'split', 'Porter', '')
    Descripteur(path, path_out, 'Token', 'Porter', exp)

    Inverse(path, path_out, 'split', 'Lanaster', '')
    Inverse(path, path_out, 'Token', 'Lanaster', exp)
    Inverse(path, path_out, 'split', 'Porter', '')
    Inverse(path, path_out, 'Token', 'Porter', exp)

    update_poids_descripteur("./Index/DescripteursSplitPorter")
    update_poids_descripteur("./Index/DescripteursTokenPorter")
    update_poids_descripteur("./Index/DescripteursSplitLancaster")
    update_poids_descripteur("./Index/DescripteursTokenLancaster")

    update_poids_inverse("./Index/InverseSplitPorter")
    update_poids_inverse("./Index/InverseTokenPorter")
    update_poids_inverse("./Index/InverseSplitLancaster")
    update_poids_inverse("./Index/InverseTokenLancaster")

    root=tk.Tk()
    app=App(root)
    root.mainloop()


