import sys
print()

f = open(sys.argv[1], "r")
lines = f.readlines()
a = {}
for line in lines:
   a[line[0:12]] = 0
   
for line in lines:
    y = line.split()
    ab = y[8]
    if(int(ab) >= 400 and int(ab) <= 499):
        a[y[0]] += 1
        #print(ab)
for i in list(a):
    if(a[i] == 0):
        del a[i]

print("IP address \t #of 400 like errors")
for i in sorted(a, key=a.get, reverse = True):
    print(i + "\t\t" + str(a[i]))