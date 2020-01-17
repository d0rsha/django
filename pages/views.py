from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # Django templating
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "Look at me, I'm a context",
        "my_number": 123,
        "my_list": ['abc', 'def', 'ghi'],
        "my_html": "<h3>Look at me, I did html-injection</h3>"
    }
    return render(request, "contact.html", my_context)


def about_view(*args, **kwargs):
    return HttpResponse("<h1>Hello About</h1>")
