bits=input("Enter the string: ")
row=[]
if(len(bits)%8!=0):
    bits="0"*(8-len(bits)%8)+bits

for i in range(8,len(bits)+1,8):
    row.append(bits[i-8:i])

string=''
for i in range(0,8):
    count=0
    for j in range(0,len(row)):
        if(row[j][i]=='1'):
            count+=1
    if(count%2):
        string+='1'
    else:
        string+='0'

row.append(string)    

for i in row:
    if(i.count("1")%2):
        print(i+'1')
    else:
        print(i+'0')
    

rev=input("Enter the recieved: ")
row=[]

for i in range(9,len(rev)+1,9):
    row.append(rev[i-9:i])
flag=0
for i in range(0,8):
    count=0
    for j in range(0,len(row)-1):
        if(row[j][i]=='1'):
            count+=1
    if(count%2):
        if(row[-1][i]!='1'):
            flag=1
    else:
        if(row[-1][i]!='0'):
            flag=1
print(flag)
print(row)

for i in row:
    print(i)
    if(i[:-1].count("1")%2):
        if(i[-1]!='1'):
            flag=1
    else:
        if(i[-1]!='0'):
            flag=1
if(flag):
    print("error")
else:
    print("correct")
