from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
#    worddictionary.items()
    for word in wordlist:
        if word in worddictionary:
            #Increase the count by 1
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    print('Sorted list : ', type(sortedwords))
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
    return render(request,'about.html')
