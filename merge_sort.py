def merge_sort(ar,l,mid,h):
    ll=[0]*(h-l+1)
    i,j,k=l,mid+1,0
    
    while i<=mid and j<=h:
        if ar[i]<=ar[j]:
            ll[k]=ar[i]
            k+=1
            i+=1
        else:
            ll[k]=ar[j]
            k+=1
            j+=1
    while i<=mid:
        ll[k]=ar[i]
        k+=1
        i+=1
    while j<=h:
        ll[k]=ar[j]
        k+=1
        j+=1
    for i in range(l,h+1):
        ar[i]=ll[i-l]
def sort(ar,l,h):
    if l<h:
        mid =(l+h)//2
        sort(ar,l,mid)
        sort(ar,mid+1,h)
        merge_sort(ar,l,mid,h)
ar=[4,5,3,1,2]
sort(ar,0,len(ar)-1)
print(ar)
