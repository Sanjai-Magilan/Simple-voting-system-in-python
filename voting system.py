#program for simple voting system
print("party: zero two,ippo,jojo")
print("1 for zero two\n2 for ippo\n3 for jojo")
h=[ ]
i=[ ]
e=[ ]
z=int(input("enter 1 for vote and 0 to exit : "))
while(z==1):
    a = int(input("Enter your choice : "))
    if (a == 1):

            h.append(1)

    elif (a == 2):

            i.append(1)

    elif (a == 3):  # how use the while loop perfectly

            e.append(1)

    else:

            print("Invalid option")

    s = (len(h))
    d = (len(i))
    f = (len(e))
    z = int(input("1 for countio 0 for exit : ")) # here is the probleme
if (s > d and s > f):

    print("zero two won")

elif (d > f and d > s):

    print("ippo is won")

elif (f > d and f > s):

    print("jojo is won")

elif (s == d and f == d and a == 1 and a == 2 and a == 3):

    print("All Tie")

elif (s == d and a == 1 and a == 2 and a == 3):

    print("zero two and ippo are Tie")

elif (s == f and a == 1 and a == 2 and a == 3):

    print("zero two and jojo are tie")

elif (f == d and a == 1 and a == 2 and a == 3):

    print("ippo and jojo are tie")
