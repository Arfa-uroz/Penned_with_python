'''def matched(s):
    x=0
    y=0
    for i in s:
        if i == "(":
            x+=1
            for j in s[i+1:]:
                if j == ")":
                    y+=1
    if x == y:
        return(True)
    else:
        return(False)'''

def matched(x):
    ob=x.count("(")
    cb=x.count(")")
    l1=[]
    l2=[]
    if ob!=cb:
        return(False)

    for i in range(0,len(x)):
        if x[i]=="(":
                l1.append(i)
        if x[i]==")":
                l2.append(i)
    for i in range(0,len(l1)):
        if l1[i]>l2[i]:
            return(False)
    return(True)




x = input("Enter a string  ").strip()
print(matched(x))