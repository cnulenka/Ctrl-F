def bmp1(m,s,f,p):
    i=m
    j=m+1
    f[i]=j
    while i>0:
        while (j<=m and p[i-1]!=p[j-1]):
            if(s[j]==0):
                s[j]=j-i
            j=f[j]

        i=i-1
        j=j-1
        f[i]=j
    return s,f

def bmp2(m,s,f):
    j=f[0]
    for i in range(0,m+1):
        if (s[i]==0):
            s[i]=j
        if(i==j):
            j=f[j]
    return s,f
def bmbad(p,m):
    occ=[-1]*256
    for i in range(0,m):
        occ[ord(p[i])]=i
    return occ    
def bmsearch(p,t,s,occ,m,res):
    i=0
    n=len(t)
    while i<=n-m:
        j=m-1
        while (j>=0 and p[j]==t[i+j]):
            j=j-1
        if(j<0):
            res.append(i)
            i=i+s[0]
        else:
            i+=max(s[j+1],j-occ[ord(t[i+j])])
    return res       
def Boyer_Moore(t,p):
    m=len(p)
    s=[0]*(m+1)
    f=[0]*(m+1)
    s,f=bmp1(m,s,f,p)

            
    s,f=bmp2(m,s,f)


    occ=(bmbad(p,m))
    res=[]
    res=bmsearch(p,t,s,occ,m,res)
    return res
    



