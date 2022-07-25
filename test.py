import pandas as pd
emails = input("enter email :")
e = pd.read_excel("Email.xlsx")
x = e['Emails'].values

# print(emails)  
#  print(x)
k=0
for i in x:
    if emails == i:
        print('Email exists at row Number :',k+2)
        # print(k+2)
        # break
    k+= 1


