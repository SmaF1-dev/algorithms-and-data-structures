def generate_max_input():
    with open("../txtf/input.txt", 'w') as f:
        n=5000
        lst = []
        st = 1000
        for i in range(1000):
            for i in range(5):
                lst.append(st)
            st-=1
        f.write(' '.join(list(map(str, lst))))

if __name__=="__main__":
    generate_max_input()