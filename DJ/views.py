from django.http import HttpResponse
from django.shortcuts import render
import operator
def noice(request):
	return render(request,"temp1.html")
def sparta(request):
	text = request.GET['text']
	wordlist = text.split()
	worddictionary = {}
	for word in wordlist:
		if word in worddictionary:
			#Increase
			worddictionary[word] += 1
		else:
			worddictionary[word]= 1
	sortedwords = sorted(worddictionary.items(),key = operator.itemgetter(1),reverse = True)
	return render (request,"sparta.html",{'yourtext':text,'count':len(wordlist),'sortedwords':sortedwords})
def about(request):
	return render(request,"About.html")