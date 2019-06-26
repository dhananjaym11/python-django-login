from django.shortcuts import render
from userapp.models import User

# Create your views here.

def index(request):
    return render(request, 'userapp/index.html')
    
def user_list_view(request):
    user_list = User.objects.order_by('email')
    user_dict = {'user_list': user_list}
    return render(request, 'userapp/user_list.html', context=user_dict)