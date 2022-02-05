data=[["manu130613","manu",1000000000],
  ["srividya13257","srividya",100000000000000],
  ["hssd3542534","harsha",100000000000000000]]

def checkingBalance(id):
    for s in data :
        if s[0]==id :
            print(s[2])
        

m=input("enter your id")
for h in data :
    if h[0]==m:
        print("hi"+h[1])

print("press 1 for checking balance")
print("press 2 for cash withdraw")
print("press 3 for cash deposit") 

n=int(input("enter your choice"))
if n==1:
    checkingBalance(m)
elif n==2:
    print("cash withdraw")
else :
    print("cash deposit")

    