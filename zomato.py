from pyzomato import Pyzomato
import requests
import os
import csv
import numpy as np
import re
import pandas as pd

p = Pyzomato("caff8bcbc0929dd1a5eb05c467b9fc97")
estb=[41,21,23,1,20,4,31,16,7,71]
locaz=[74001,74002,74003,74004,74005]
nama,namaresto,namatype,ratescore,ratetext,cost,cuisines,lokasi,vtcount = [],[],[],[],[],[],[],[],[]
tes=0

"""
for i in range (0,len(locaz)):
    data = open("hasil-"+str(locaz[i])+".txt","r")
    temp = str(data.read()).replace(',','RETURNSPASIZING')
    temp = temp.replace(':','EQUALSTO')
    tempda = re.sub(r'[^\w\s]','',temp)
    tempda = tempda.replace('RETURNSPASIZING','\n')
    tempda = tempda.replace('EQUALSTO',':')
    wdata = open("hasil-"+str(locaz[i])+".txt","w")
    wdata.write(tempda)


temp = ''
for i in range(0,len(locaz)):
    for j in range(0,len(estb)):
        print(j)
        for x in range(1,3):
            temp = temp+str(p.search(entity_id=str(locaz[i]),entity_type="zone",start=str(1+((x-1)*20)),count=str(x*20),establishment_type=estb[j]))
    file = open("hasil-"+str(locaz[i])+".txt","w")
    file.write(temp)
    temp = ''

temp = ''
for j in range(0,len(estb)):
    print(j)
    for x in range(1,3):
        temp = temp+str(p.search(entity_id=str(74005),entity_type="zone",start=str(1+((x-1)*20)),count=str(x*20),establishment_type=estb[j]))
file = open("hasil-"+str(74005)+".txt","w",encoding='utf-8')
file.write(temp)
temp = ''

with open("hasil-74005.txt") as f:
    content = f.readlines()
    for line in content:
        if line.find("name")==1:
            ltemp = line.replace('\n','')
            nama.append(ltemp.replace('name: ',''))
            # print(line.replace('\n',''))
            #print(ltemp.replace('name: ',''))
        if line.find("cuisines") == 1:
            ltemp = line.replace('\n', '')
            cuisines.append(ltemp.replace('cuisines: ', ''))
        if line.find("average_cost_for_two:") == 1:
            ltemp = line.replace('\n', '')
            cost.append(ltemp.replace('average_cost_for_two: ', ''))
        if line.find("user_rating:") == 1:
            ltemp = line.replace('\n', '')
            ratescore.append(ltemp.replace('user_rating: aggregate_rating: ', ''))
        if line.find("rating_text:") == 1:
            ltemp = line.replace('\n', '')
            ratetext.append(ltemp.replace('rating_text: ', ''))
            lokasi.append("Jakarta Barat")
        if line.find("votes:") == 1:
            ltemp = line.replace('\n', '')
            vtcount.append(ltemp.replace('votes: ', ''))
    #print(content)

for i in range(0,len(nama)):
    if i%2==0:
        namaresto.append(nama[i])
    if i%2==1:
        namatype.append(nama[i])

print(len(namaresto))
print(len(namatype))
print(len(cuisines))
print(len(ratescore))
print(len(ratetext))
print(len(cost))


#data = list(*zip(np.asarray(nama), np.asarray(cuisines),np.asarray(ratescore),np.asarray(ratetext),np.asarray(cost),np.asarray(lokasi)))
data = np.column_stack((np.asarray(namaresto), np.asarray(cuisines),np.asarray(namatype),np.asarray(ratescore),np.asarray(ratetext),np.asarray(cost),np.asarray(lokasi),np.asarray(vtcount)))
item_length = len(data[0])
with open('clear74005.csv', 'w') as test_file:
  file_writer = csv.writer(test_file)
  for i in range(item_length):
    file_writer.writerow([x[i] for x in data])

label = ('namaresto','cuisines','namatype','ratescore','ratetext','cost','lokasi','votes')
df = pd.DataFrame(data,columns=label)
df.to_csv("clear74005.csv",index=False)
#np.savetxt("clearjakput.csv", data, delimiter=",")
print(data)

"""

data1 = pd.read_csv('clear74001.csv')
data2 = pd.read_csv('clear74002.csv')
data3 = pd.read_csv('clear74003.csv')
data4 = pd.read_csv('clear74004.csv')
data5 = pd.read_csv('clear74005.csv')

data = pd.concat([data1,data2,data3,data4,data5],ignore_index=True)
data.to_csv("Finalmaindata1.csv",index=False)
print(data)