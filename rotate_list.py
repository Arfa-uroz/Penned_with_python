def rotatelist(l,k):
    if k<0:
        return(l)
    k = k % len(l)
    return (l[k:] + l[:k])

x= input("Enter a list of numbers space seprated  ").strip()
x=x.split(" ")
k= int(input("Rotations  "))
print(rotatelist(x,k))