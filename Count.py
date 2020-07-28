import operator

def most_frequent(string):
    res={}
    for letter in string.lower():
        if not letter.isalpha():
            continue
        elif letter in res:
            res[letter]+=1
        else:
            res[letter]=1
    return res


string=str(input("Enter your string here : "))
op=most_frequent(string)
a=sorted(op.items(), key=operator.itemgetter(1), reverse=True)
print(a)
