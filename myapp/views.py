from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, JsonResponse

# Create your views here.

def test(request):
    # response = HttpResponse()
    html_content = """
    <html>
    <head>
        <title>Django Project</title>
    </head>
    <body>
    <h1>Django is a web framework</h1>
    </body>
    </html>
    """
    # response.content = html_content
    return HttpResponse(html_content)


def home(request):
    return render(request, "myapp/portfolio.html")


def index(request):
    # context = {"id":1, "name":"Shruti", "age":20, "title":"Student"}
    context = {"students": [
        {"id": 1, "name": "Ken", "age": 25, "is_active": True},
        {"id": 2, "name": "Jen", "age": 26, "is_active": False},
        {"id": 3, "name": "Aen", "age": 27, "is_active": True},
        {"id": 4, "name": "Ven", "age": 28, "is_active": False},
    ], "title": "Student"}
    return render(request, template_name="myapp/index.html", context=context)


def view_name_jon(request):
    return render(request, template_name="myapp/jon.html")


def view_name_jane(request):
    return render(request, template_name="myapp/jane.html")


def view_name(request, name):
    last_name = request.GET.get('last_name')
    print(last_name)
    if name.lower() == 'ram':
        full_name = "Ram Bahadur"
    elif name.lower() == 'harry':
        full_name = "Harry Krishna"
    elif name.lower() == 'jon':
        full_name = "Jon Prasad"
    else:
        # return HttpResponse("<h1>Name not found</h1>", status=404)
        return HttpResponseNotFound("<h1>Name not found</h1>")
    context = {
        "name": full_name,
    }
    if last_name:
        context.update(last_name=last_name)
    return render(request, template_name="myapp/name.html", context=context)

def json_view(request):
    response = {"id": 1, "name": "Ken","age": 25}
    students = [
        {"id": 1, "name": "Ken", "age": 25},
        {"id": 2, "name": "Jen", "age": 26},
        {"id": 3, "name": "Aen", "age": 27},
        {"id": 4, "name": "Ven", "age": 28}
    ]
    return JsonResponse(students, safe=False)

