import os

import nltk


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


def SplitPorter(f):
    Porter = nltk.PorterStemmer()
    TermesSplitNormalisationPorter = [Porter.stem(terme) for terme in TermesSplit(f)]
    return TermesSplitNormalisationPorter

def SplitLancaster(f):
    Lancaster = nltk.LancasterStemmer()
    TermesSplitNormalisationLancaster = [Lancaster.stem(terme) for terme in TermesSplit(f)]
    return TermesSplitNormalisationLancaster

def TokenPorter(f,exp):
    Porter = nltk.PorterStemmer()
    TermesTokenNormalisationPorter = [Porter.stem(terme) for terme in TermesToken(f, exp)]
    return TermesTokenNormalisationPorter

def TokenLancaster(f,exp):
    Lancaster = nltk.LancasterStemmer()
    TermesTokenNormalisationLancaster = [Lancaster.stem(terme) for terme in TermesToken(f, exp)]
    return TermesTokenNormalisationLancaster

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
                list=SplitLancaster(f)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    file_out = open(pathDesc + '/DescripteursSplitLancaster', "a")
                    file_out.write(filename[1]+' '+terme+'\n')
            elif Type1 == 'split' and Type2 == 'Porter':
                list = SplitPorter(f)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    file_out = open(pathDesc + '/DescripteursSplitPorter', "a")
                    file_out.write(filename[1]+' '+terme+'\n')
            elif Type1 == 'Token' and Type2 == 'Lanaster':
                list = TokenLancaster(f,exp)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    file_out = open(pathDesc + '/DescripteursTokenLancaster', "a")
                    file_out.write(filename[1]+' '+terme+'\n')
            elif Type1 == 'Token' and Type2 == 'Porter':
                list = TokenPorter(f,exp)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    file_out = open(pathDesc + '/DescripteursTokenPorter', "a")
                    file_out.write(filename[1]+' '+terme+'\n')
            file_out.close()

def Index(pathfiles,pathDesc,Type1,Type2,exp):

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
                    global_list.append(terme+'_'+filename[1])
            elif Type1 == 'split' and Type2 == 'Porter':
                list = SplitPorter(f)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    global_list.append(terme+'_'+filename[1])
            elif Type1 == 'Token' and Type2 == 'Lanaster':
                list = TokenLancaster(f,exp)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    global_list.append(terme+'_'+filename[1])
            elif Type1 == 'Token' and Type2 == 'Porter':
                list = TokenPorter(f,exp)
                list2 = []
                for i in list:
                    if i not in list2:
                        list2.append(i)
                list2.sort()
                for terme in list2:
                    global_list.append(terme+'_'+filename[1])
    global_list.sort()
    if Type1=='split' and Type2=='Lanaster':
        file_out=open(pathDesc+'/IndexSplitLancaster',"w")
        for term in global_list:
            t= term[:-2]
            d=term[-1]
            file_out.write(t+' '+d+'\n')
        file_out.close()
    elif Type1=='split' and Type2=='Porter':
        file_out = open(pathDesc + '/IndexSplitPorter', "w")
        for term in global_list:
            t= term[:-2]
            d=term[-1]
            file_out.write(t+' '+d+'\n')
        file_out.close()
    elif Type1=='Token' and Type2=='Lanaster':
        file_out=open(pathDesc+'/IndexTokenLancaster',"w")
        for term in global_list:
            t= term[:-2]
            d=term[-1]
            file_out.write(t+' '+d+'\n')
        file_out.close()
    elif Type1=='Token' and Type2=='Porter':
        file_out = open(pathDesc + '/IndexTokenPorter', "w")
        for term in global_list:
            t= term[:-2]
            d=term[-1]
            file_out.write(t+' '+d+'\n')
        file_out.close()





if __name__ == '__main__':
    path ="./Collection"
    path_out ="./Index"
    exp = '(?:[A-Z]\.)+|\d+(?:\.\d+)?DA?|\w+|\.{3}'
    Descripteur(path, path_out, 'split', 'Lanaster','')
    Descripteur(path, path_out, 'Token', 'Lanaster', exp)
    Descripteur(path, path_out, 'split', 'Porter','')
    Descripteur(path, path_out, 'Token', 'Porter', exp)

    Index(path, path_out, 'split', 'Lanaster', '')
    Index(path, path_out, 'Token', 'Lanaster', exp)
    Index(path, path_out, 'split', 'Porter', '')
    Index(path, path_out, 'Token', 'Porter', exp)