from django.http import HttpResponse
from django.shortcuts import render

'''def home(request):
    return HttpResponse("<a href='https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'>click here</a>")


def index(request):
   return HttpResponse("<a href='https://www.facebook.com/'>click here</a>")


def index(request):
    return HttpResponse("""<!DOCTYPE html>
<html>
<head>
	<title>responsive webpage</title>
	<link rel="stylesheet" type="text/css" href="index1.css ">
	<style>
	*{
	padding: 0;
	margin:0;
}
body{
	background-color: pink;
}

.heading1{
	margin-left: 20px;
	width: 80%;
	height: 100px;
	background-color: black;
	color: white;
	opacity:;
}

.heading h1{
	float: left;
	margin-left: 60px;
	line-height: 100px;
}
	<style>
</head>
<body>
	<div class="heading">
		<div class="heading1">
			<h1>Home</h1>
			<h1>Services</h1>
			<h1>Gallery</h1>
			<h1>Contact</h1>
			<h1>Help</h1>
			<h1>Feedback</h1>
	    </div>
		
	</div>

</body>
</html>""")'''


def index(request):
    return render(request,'index.html')

 #return  HttpResponse("""I am home,
  #  <a href='http://127.0.0.1:8000/'>Home</a><br>
   # <a href='http://127.0.0.1:8000/removepunc'>removepunc</a><br>
    #<a href='http://127.0.0.1:8000/capitalise'>capitalise</a><br>
    #<a href='http://127.0.0.1:8000/newlineremover'>newlineremover</a><br>
    #<a href='http://127.0.0.1:8000/spaceremove'>spaceremove</a><br>
    #<a href='http://127.0.0.1:8000/charcount'>charcount</a><br> """)
'''def removepunc(request):
    djtext=(request.GET.get('text','default'))
    removepunc=(request.GET.get('removepunc','on'))
    punctuations="` ~ ! @ # $ % ^ & * ( ) _ -  ' < , . > / ?" 
    str=''
    for char in djtext:
        if char not in punctuations:
            str=str+char
    return render()  '''



'''def newlineremover(request):
    return  HttpResponse("""this is newlineremover,
    <a href='http://127.0.0.1:8000/'>go to home</a>""")

def spaceremove(request):
    return  HttpResponse("""this is spaceremove,
        <a href='http://127.0.0.1:8000/'>go to home</a>""")
 
def charcount(request):
    return  HttpResponse("""this is charcount,
        <a href='http://127.0.0.1:8000/'>go to home</a>""")'''

def analyze(request):
    #Get the text
    global analyzed
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcase = request.GET.get('fullcapsk', 'off')
    lowercase=request.GET.get('lowercase','off')

    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    if removepunc == "on" and fullcase=='off' and lowercase=='off':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcase=="on" and removepunc=='off' and lowercase=='off':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif lowercase=='on' and fullcase=="off" and removepunc=='off':
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.lower()

        kapil={'purpose':'text in lowercase','analyzed_text':analyzed}
        return render(request,'analyze.html',kapil)

    elif (removepunc=='on' and fullcase=='on' ) :
        analyzed=''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        analyzed1=analyzed
        final=''
        for char in analyzed1:
            final=final+char.upper()
        params = {'purpose': 'Removed Punctuations and uppercase', 'analyzed_text': final }
        return render(request, 'analyze.html', params)




