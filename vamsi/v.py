from django.http import HttpResponse;
from django.shortcuts import render
import operator
'''
def ram(q):
    return HttpResponse("vamsi sai");

def song(r):
    return HttpResponse("<h1>hello guru prema kosamera jeevitham</h1>")

def t(r):
    return render(r,'ram.html',{'vlr': '8074179467'})'''

def ram(q):
    return render(q, "countwords.html");

def count(q):
    mess=q.GET['message'];
    l=mess.split();
    a=len(l);
    wlcount={};
    for word in l:
        if word in wlcount:
            wlcount[word] += 1;
            pass
        else:
            wlcount[word]=1;
    sort1=sorted(wlcount.items(),key=operator.itemgetter(1),reverse=True)
    return render(q,"count.html",{'msg':mess,"length":a, "abc":wlcount, "cba":sort1})
