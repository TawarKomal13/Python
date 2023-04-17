# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 12:33:13 2023

@author: Admin
"""

for x in range(1,11):
    for y in range(1,11):
        print('%d*%d=%d'%(x,y,x*y))
        
        
        
        
for i in "string": 
    print(i)
    if i == "r":
        break
print("the end")
        
        
for i in "string":
    if i=="i":
        continue
    print(i)
print("the end")


import os
os.getcwd()

os.chdir("C:\\Users\\Admin\\DATA ANALYSIS")
os.chdir("C:/Users/Admin//DATA ANALYSIS")
os.getcwd()



f=open("demofile.txt")
print(f.readline())
f.close()

f = open("demofile.txt")
for i in f:
    print(i)


f = open("demofile.txt", "a")
f.write("\nArtificial Intelligence")
f.close()


f = open("demofile.txt", "w")
f.write("AI")
f.close()

f = open("myfile.txt", "x")

print([1,2,3]+[4,5,6])

# repetition
a=["hi!"]*4

a.remove("hi!")


New_Data = [1,2,3,4,5,6,7]

print(max(New_Data))
print(min(New_Data))


alist = [123,"xyz", "abc", 123,"xyz"]
alist.count("xyz")


alist = [123,'xyz', "zara" 'abc', 123]
blist = [2009, "bulls"]
alist.extend(blist)
print("Extended List: ", alist)



alist = ["abc",123, "zara", "abc", 123]
alist.index("abc")



alist = [123,"xyz","zara", "abc"]
alist.insert(3,2009)
alist


alist = [123,"xyz","zara", "abc"]
alist.pop()



alist.pop(0)

players = {"virat","Rohit","Dhoni","Raina"}

players 
players.pop()   
        
 
phone = {"brand":"onepls","model":"9R","year":2021,"ram":"12GB"}
 
    
phones = {"brand":["oneplus","Xiaomi"],"model":["9R","Poco x3"], "year":[2021,2020]}
    
 
phones["brand"]
 
phones["model"]
 
    
phone = {"brand":"onepls","model":"9R","year":2021,"ram":"12GB", "year":2023}

phone    
 
    comprehensive
all_phones = {"brand":"One plus", "model":["9R","9"], "year": 2021.0, "Flagship":True}
all_phones    
 
phones["model"]    
 
phones.keys() 
 
phones.values()    
 
phones.items()    
 
phones["refresh_rate"] = "120Hz"
phones["model"]="9 Pro"
phones["model"]=["9R", "9 pro"] 
    
phones.update({"brand":["Apple","oneplus"]})
 
    
if "brand" in phones:
    print("Brand is present")
else:
    print("Brand is not present")
    
 
    
phones["brand_new"] = phones["brand"]
del phones["brand"]

phones["brand"] = phones.pop("brand_new")

del phones["brand"]
    
 
    
for i in all_phones:
    print(i)
    
for i in all_phones:
    print(all_phones[i])
    
 
for i, j in all_phones.items():
    print(i,":",j)
        
        
        