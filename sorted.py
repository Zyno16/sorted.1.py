c={"a":3,"b":4,"g":8}
tmp=list()
for k,v in c.items():
    tmp.append( (v,k) )
print(tmp)
tmp = sorted(tmp,reverse=True)
print(tmp)