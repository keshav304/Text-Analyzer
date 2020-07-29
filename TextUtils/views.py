# I have created this file
from django.http import HttpResponse
from django.shortcuts import render
import re


# def home(request): return HttpResponse(''' <h1><a href="https://www.linkedin.com/feed/">linkedin</a></h1> <h1><a
# href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Django
# playlist</a></h1> <h1><a href="https://github.com/">Github</a></h1> <h1><a
# href="https://www.instagram.com/">Instagram</a></h1> <h1><a
# href="https://www.freecodecamp.org/">freecodecamp</a></h1> ''')

def home(request):
    """
    # A template contains the static parts of the desired HTML output as well as some special syntax describing how
    dynamic content will be inserted
    #  second argument is the file which is being rendered by the function
    # render() can contain a third parameter which can send variable values to the fie being displayed (in this case index.html)
    """
    return render(request, 'index.html')


def analyze(request):
    # getting the text from home
    djtext = request.POST.get('text', 'default')


    # checking which checkboxes are on
    capitalizewholeparagraph = request.GET.get('capitalizewholeparagraph', 'off')
    removepunc = request.POST.get('removepunctuation', 'off')
    capitalize = request.POST.get('capitalizefirstletter', 'off')
    charcount = request.POST.get('countcharcters', 'off')
    spaceremove = request.POST.get('removespaces', 'off')



    if capitalizewholeparagraph == "on" and removepunc == 'off' \
            and capitalize == 'off' and spaceremove == 'off' and \
            charcount == 'off':
        params = {'para': djtext.upper()}
        return capitalizeWholepara(request, params)


    elif capitalizewholeparagraph == "off" and removepunc == 'off' \
            and capitalize == 'off' and spaceremove == 'off' and \
            charcount == 'on':
        params = {'para': len(djtext)}
        return capitalizeWholepara(request, params)


    elif capitalizewholeparagraph == "off" and removepunc == 'on' \
            and capitalize == 'off' and spaceremove == 'off' and \
            charcount == 'off':
        djtext_new = re.sub(r'[^\w\s]', '', djtext)
        params = {'para': djtext_new}
        return capitalizeWholepara(request, params)


    elif capitalizewholeparagraph == "off" and removepunc == 'off' \
            and capitalize == 'on' and spaceremove == 'off' and \
            charcount == 'off':
        wordArr = djtext.split(" ")
        newWordArr = []
        for word in wordArr:
            newWordArr.append(word.capitalize())
        word = " ".join(newWordArr)
        params = {'para': word}
        return capitalizeWholepara(request, params)


    elif capitalizewholeparagraph == "off" and removepunc == 'off' \
            and capitalize == 'off' and spaceremove == 'on' and \
            charcount == 'off':
        djtext_new = re.sub("  ", '', djtext)
        params = {'para': djtext_new}
        return capitalizeWholepara(request, params)
    else:
        return HttpResponse("<h1>Please select only one option!</h1>")


def removePunc(request, params):
    return render(request, 'removepunc.html', params)


def capitalize(request, params):
    return render(request, 'capitalize.html', params)


def spaceRemove(request, params):
    return render(request, 'spaceremove.html', params)


def charCount(request, params):
    return render(request, 'charcount.html', params)


def capitalizeWholepara(request, params):
    return render(request, 'capitalizeWholepara.html', params)
