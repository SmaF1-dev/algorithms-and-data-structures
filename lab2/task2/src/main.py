import sys
def merge(lst, p, q, r):
    n1 = q-p+1
    n2 = r-q
    left = [0]*n1
    for j in range(0,n1):
        left[j]=lst[p+j]
    right = [0]*n2
    for j in range(0,n2):
        right[j]=lst[q+j+1]

    i, j = 0, 0
    k=p
    while i<n1 and j<n2:
        if left[i]<=right[j]:
            lst[k]=left[i]
            i+=1
        else:
            lst[k]=right[j]
            j+=1
        k+=1

    while i<n1:
        lst[k]=left[i]
        i+=1
        k+=1
    while j<n2:
        lst[k]=right[j]
        j+=1
        k+=1

sys.setrecursionlimit(100000000)
def merge_sort(lst, p,r,lst_act):
    if p<r:
        q = (r+p)//2
        merge_sort(lst,p,q, lst_act)
        merge_sort(lst,q+1,r, lst_act)
        merge(lst,p,q,r)
        lst_act.append((p,lst[p],r,lst[r]))

def main():
    with open("input.txt") as f:
        n = int(f.readline())
        lst = list(map(int, f.readline().split()))
    max_n = 2*10**4
    max_el=10**9
    lst_act = []
    if n>max_n or n==0 or max(lst)>max_el or len(lst)!=n:
        quit("Incorrect input")
    merge_sort(lst,0,n-1, lst_act)
    with open("output.txt","w") as f:
        for i in range(len(lst_act)):
            f.write(str(lst_act[i][0]+1)+", "+str(lst_act[i][2]+1)+", "+str(lst_act[i][1])+", "+str(lst_act[i][3])+"\n")
        f.write(' '.join(map(str,lst)))

main()