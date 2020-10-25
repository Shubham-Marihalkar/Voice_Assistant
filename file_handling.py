#function to wirte int list to file
def writelistint(lis_t,filename):
    tmp=[]
    try :
        tmp=readlistint(filename)
        lis_t=list(set(tmp+lis_t))#remove duplicates
    except:
    	del tmp
    fp=open(filename+'.txt', 'w+')
    with fp as filehandle:
        for listitem in lis_t:
            filehandle.write('%s\n' % listitem)
    fp.close()

def readlistint(filename):
    lis_t=[]
    fp=open(filename+'.txt', 'r')
    with fp as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            current = line[:-1]
            # add item to the list
            lis_t.append(int(current))
    fp.close()
    return (lis_t)



#function to wirte string (songs) list to file
def writelistString(lis_t,filename):
    tmp=[]
    try:
        tmp=readlistString(filename)
        lis_t=list(set(tmp+lis_t))#remove duplicates
    except:
    	del tmp
    fp=open(filename+'.txt', 'w+')
    with fp as filehandle:
        for listitem in lis_t:
            filehandle.write('%s\n' % listitem)
    fp.close()

def readlistString(filename):
    lis_t=[]
    fp=open(filename+'.txt', 'r')
    with fp as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            current = line[:-1]
            # add item to the list
            lis_t.append(current)
    fp.close()
    return (lis_t)
