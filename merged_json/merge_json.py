import json


# f2data = "" 
# with open('sajhalinks.json') as f2: 
#   f2data = '\n' + f2.read()
    
# with open('full_sajha_descp.json','a+') as f1:
#     f1.write(f2data)
    
    
# print(f1.data)

f1data = f2data = "" 
 
with open('sajhalinks.json') as f1: 
  f1data = f1.read() 
with open('full_sajha_descp.json') as f2: 
  f2data = f2.read() 
 
f1data += "\n"
f1data += f2data
with open ('merged.json', 'a') as f3: 
  f3.write(f1data)