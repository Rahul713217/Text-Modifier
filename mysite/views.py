
# I create this file
'''
def index(request):
    return H('<h1>hello<h1> <a href="https://practice.geeksforgeeks.org/">GFG Portal</a>')

def about(request):
    return H('dfs - bfs')

'''
# For practice purpose
###################################

from django.http import HttpResponse as H

from django.shortcuts import render as r

def index(request):
    return r(request, 'index.html')
    # return H('Home')

def analyze(request):

    djtext = request.POST.get('text','default')
    
    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    removenewlines = request.POST.get('removenewlines','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    # countchar = request.POST.get('countchar','off')

    # print(removepunc)
    # print(djtext)

    if removepunc == 'on':
        punctuations = '''!()-[]{};:\,<>'"./?@#$%^&*_~'''
        analyzed = ''
        for i in djtext:
            if i not in punctuations:
                analyzed += i
        param = {'analyzed_text': analyzed }
        djtext = analyzed

    if uppercase == 'on':
        analyzed = ''
        for i in djtext:
            analyzed += i.upper()
        param = {'analyzed_text': analyzed }
        djtext = analyzed

    if removenewlines == 'on':
        analyzed = ''
        for i in djtext:
            if i != '\n' and i != '\r':
                analyzed += i
            # else:
            #     print('no')
        # print ('pre', analyzed)
        param = {'analyzed_text': analyzed }
        djtext = analyzed
    
    if extraspaceremover == 'on':
        analyzed = ''
        for i,e in enumerate(djtext):                  
            if not (djtext[i] == ' ' and djtext[i-1] == ' '):
                analyzed += e
        param = {'analyzed_text': analyzed }
        djtext = analyzed

    # if countchar == 'on':
    #     k = 0
    #     for i in djtext:
    #         if i != ' ':
    #             k += 1
    #     param = {'analyzed_text': f'\n Character Count {k}'}
    
    if removepunc=='off' and uppercase=='off' and removenewlines=='off' and extraspaceremover=='off':
        return H('Please Check Atleast One Box')

    return r(request, 'analyze.html', param)



















