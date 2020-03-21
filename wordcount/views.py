from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,"home.html")

def aboutpage(request):
    return render(request,"about.html")
    
def count(request):
    fulltext = request.GET['fulltext']    
    wordlist = fulltext.split()
    wordlist = [w.lower() for w in wordlist]
    wordcountdict = {}
    for w in wordlist:
        if w in wordcountdict:
            wordcountdict[w] += 1
        else:
            wordcountdict[w] = 1
    sorted_wordcountdict = sorted(wordcountdict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,"count.html",{'fulltext':fulltext,'wordcount':len(wordlist),'wordcountdict':sorted_wordcountdict})