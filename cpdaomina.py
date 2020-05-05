cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

mydict = {}

for i in cpdomains:
    brk = i.split(" ")
    num = int(brk[0])
    mysite = brk[1].split(".")

    curr = mysite[-1]

    if curr in mydict:
        mydict[curr] += num
    else:
        mydict[curr] = num

    for i in range(len(mysite)-2,-1,-1):

        curr = mysite[i]+"."+curr
        if curr in mydict:
            mydict[curr] += num
        else:
            mydict[curr] = num


res = []

for i in mydict.keys():
    res.append(str(mydict[i])+" "+i)

print(res)