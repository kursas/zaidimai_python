# -*- coding: utf-8 -*-
import io
print("Zaidimas-Victorina,atsakyk teisingai i uzduota klausima tik mažomis raidemis!.Is viso 3 klausimai su 3 teisingais atsakymais "
      "\nfaila vopr.txt,galima papildyti klausimais ir atsakymais."
      "\nKad atvazduotu lietuviškas raides PyCharm programoje "
      "\natlikite sekanti veiksmą:File-->Settings-->Editor-->File Encoding-->Global Encoding::UTF-8-->Project Encoding::UTF-8-->Apply-->Ok.")
kol = 0

f = io.open('D://DUMENYS//DARIUS//Desktop//vopr.txt',encoding='utf-8')
vopr_f = f.readlines()
f.close()

vsego = int(len(vopr_f) / 2)

vopr = []
st = 1
for i in vopr_f:
    if st == 1:
        newi = i.replace("\n", "");
        q = []
        q.append(newi)
        st = 2
    else:
        newi = i.replace("\n", "");
        q.append(newi)
        vopr.append(q)
        st = 1

for i in vopr:
    otv = input(i[0])
    if otv.lower() == i[1]:
        print("Teisingai")
        kol = kol + 1
    else:
        print("Neteisingai")

print(kol," klausimai, ir is viso teisingu atsakymu: ", vsego)

#Atsakymai
#1945
#lygiakraštis


#output
Zaidimas-Victorina,atsakyk teisingai i uzduota klausima!.Is viso 3 klausimai su 3 teisingais atsakymais 
faila vopr.txt,galima papildyti klausimais ir atsakymais.
Kad atvazduotu lietuviškas raides PyCharm programoje 
atlikite sekanti veiksmą:File-->Settings-->Editor-->File Encoding-->Global Encoding::UTF-8-->Project Encoding::UTF-8-->Apply-->Ok.
Istorija. Kokiais metais baigėsi Antrasis pasaulinis karas?1945
Teisingai
Geometrija. Kaip vadinasi trikampis, kurio visos kraštinės yra lygios?lygiakraštis
Teisingai
Biologija. Kaip vadinamas angliavandenių sintezės iš neorganinių medžiagų dėl saulės energijos procesas?fotosintezė
Teisingai
3  klausimai, ir is viso teisingu atsakymu:  3

Process finished with exit code 0
#fotosintezė
