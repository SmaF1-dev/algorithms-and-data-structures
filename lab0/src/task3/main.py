import time
t_start = time.perf_counter()

def calc_fib(n):
    a,b = 0,1
    s=0
    for i in range(n-1):
        s=(a+b)%10
        a,b = b,s
    return s

inp_file = open('input.txt')
inp = int(inp_file.readline())
inp_file.close()
if 0<=inp<=10**7:
    out = str(calc_fib(inp))
    out_file = open('output.txt', 'w')
    out_file.write(out)
    out_file.close()
else:
    print("Число должно быть от 0 до 10**7!")

print("Время работы: %s секунд " % (time.perf_counter()-t_start))