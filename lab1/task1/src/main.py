def insertion_sort(n, lst):
    for i in range(1,n):
        elem = lst[i]
        j=i-1
        while j>=0 and lst[j]>elem:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=elem

    return lst

def main():
    file_inp = open("input.txt")
    n = int(file_inp.readline())
    lst = list(map(int, file_inp.readline().split()))
    file_inp.close()

    if len(lst)!= n:
        quit("Указанная длина списка не соответствует действительной!")

    if n>1000 or n<1 or max(lst)>10**9:
        quit("Входные данные не соответствуют условию задачи!")

    lst = list(map(str, insertion_sort(n, lst)))
    out = " ".join(lst)

    file_out = open("output.txt", 'w')
    file_out.write(out)
    file_out.close()

main()