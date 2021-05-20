from django.shortcuts import render
from django.shortcuts import HttpResponse
import mysql.connector as mcdb
conn=mcdb.connect(host="127.0.0.1",user="root",password="root",database="samples")
print("successfully connected")
cur=conn.cursor()
val=None

def home(request):
    return render(request,"home.html")
def result(request):

    if request.method=="POST":
         url =request.POST['data']
         cur.execute("SELECT word,frequency FROM f_tables where url='{}'".format(url))
         myresult = cur.fetchall()
         dict={}
         flag="RESULTS OBTAINED FROM THE DATABASE"
         for x in myresult:
             dict[x[0]]=x[1]
         #print(dict)
         if len(dict)==0:
             flag="RESULTS ARE FRESHLY PROCESSED"
             import requests
             from bs4 import BeautifulSoup
             my_source_code = requests.get(url).text
             soup = BeautifulSoup(my_source_code, 'html.parser')
             content = (soup.get_text().strip())
             words = content.lower().split()

             clean_list = []
             common_words = ['the', 'he', 'at', 'but', 'there', 'of', 'was', 'be', 'not', 'use', 'and', 'for', 'this',
                             'what', 'an', 'a', 'on', 'have', 'all', 'each',
                             'to', 'are', 'from', 'were', 'which', 'in', 'as', 'or', 'we', 'she', 'is', 'with', 'when',
                             'do', 'you', 'his', 'had', 'your', 'how', 'that', 'they', 'by', 'can', 'their', 'it', 'I',
                             'word', 'said', 'if','--']
             for word in words:
                 symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/.,1234567890 "

                 for i in range(len(symbols)):
                     word = word.replace(symbols[i], '')

                 if len(word) > 0 and word not in common_words:
                     clean_list.append(word)

             word_count = {}
             for i in range(len(clean_list)):
                 for word in clean_list:
                     if word in word_count:
                         word_count[word] += 1
                     else:
                         word_count[word] = 1
             if '_' in word_count:
                 print("THERE")
                 word_count['-']=0

             a = sorted(word_count, key=word_count.get, reverse=True)[:10]
             dict = {}
             for i in a:
                 dict[i] = word_count[i]

                 cur.execute("INSERT INTO f_tables VALUES ('{}','{}','{}')".format(url,i,word_count[i]))
                 conn.commit()


    else:
        pass
    return render(request,"result.html", {'a':dict,"flag":flag})