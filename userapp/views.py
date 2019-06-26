from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'userapp/index.html')
    
def user_list_view(request):
    my_dict = {'insert_me': 'Hello I am from views.py'}
    return render(request, 'userapp/user_list.html', context=my_dict)