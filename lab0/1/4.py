inp_file = open('input.txt')
a,b = map(int, inp_file.readline().split())
inp_file.close()
out = str(a+b**2)
out_file = open('output.txt', 'w')
out_file.write(out)
out_file.close()