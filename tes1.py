# Uncomment and complete this code - keep the names the same for testing purposes. 

def compute_heights(h_0=1.0, h_1=0.3, n=10):
    nlist=[h_0]
    for i in range(n):
        nlist.append(nlist[i]*0.9)
    hlist=[h_0]
    temp=h_0
    ind=temp*0.9
    while ind>=h_1:
        
        hlist.append(ind)
        temp=ind
        ind=temp*0.9
    if len(nlist)>len(hlist):
        return hlist
    else:
        return nlist
        

def main():
    print(compute_heights(0.5))
main()
    
    
