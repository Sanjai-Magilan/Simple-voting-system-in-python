# program for simple voting system
print("party: zero two, ippo, jojo")
print("1 for zero two\n2 for ippo\n3 for jojo")

h = []
i = []
e = []

z = int(input("Enter 1 for vote and 0 to exit: "))
while z == 1:
    a = int(input("Enter your choice: "))
    if a == 1:
        h.append(1)
    elif a == 2:
        i.append(1)
    elif a == 3:
        e.append(1)
    else:
        print("Invalid option")

    z = int(input("1 for continue 0 for exit: "))

s = len(h)
d = len(i)
f = len(e)

if s > d and s > f:
    print("zero two won")
elif d > f and d > s:
    print("ippo won")
elif f > d and f > s:
    print("jojo won")
elif s == d == f:
    print("All Tie")
elif s == d and s > f:
    print("zero two and ippo are tie")
elif s == f and s > d:
    print("zero two and jojo are tie")
elif f == d and f > s:
    print("ippo and jojo are tie")
