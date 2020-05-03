def bottles(a,x):
    t=dict()
    s=0
    for i in range(x):
        t[a[i]]=t.get(a[i],0)+1
        s=max(s,t[a[i]])
    print("mini no. of","visi bottle are:",s)
x=int(input())
a=list(map(int,input().split(" ")))
bottles(a,x)