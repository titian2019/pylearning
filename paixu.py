nu=[4,3,2,1,6]
nu1=[7,0,2,1,6]
'''for j in range(len(nu)-1):
    for i in range(j,len(nu)-1):
        if nu[j]>nu[i+1]:
            nu[j],nu[i+1]=nu[i+1],nu[j]
print(nu)
nu=[4,3,2,1,6]'''
'''for i in range(len(nu)-1):
    min=i
    for j in range(i,len(nu)-1):
        if nu[min]>nu[j+1]:
            min=j+1
    nu[i],nu[min]=nu[min],nu[i]
print(nu)
nu1=[7,0,2,1,6]
nu1=nu
for i in   range(len(nu1)-1):
    for j in    range(len(nu1)-1-i):
        change = False
        if nu1[j]>nu1[j+1]:
            nu1[j],nu1[j+1]=nu1[j+1],nu1[j]
            change = True
        if  change == False:
            break   #但不用交换时，减少排序次数
        print(nu1)
#print(nu1)

'''
nu1=[7,0,2,1,6]

def bijiao(num):
    l=[]
    r=[]
    for i in  num[1:]:
        if  i<num[0]:l.append(i)
        else:r.append(i)
    return [l,r]
def kuaipai(nu1):
    if  len(nu1)<2:
        return nu1
    else:
        p=nu1[0]
        res=bijiao(nu1)
        l=res[0]
        r=res[1]
        return kuaipai(l)+[p]+kuaipai(r)

print(kuaipai(nu1))
