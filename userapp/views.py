from django.shortcuts import render
from userapp.models import User
from userapp.forms import NewUserForm
# Create your views here.

def index(request):
    context_dict = {'text': 'Hello world', 'number': 100}
    return render(request, 'userapp/index.html', context=context_dict)
    
def user_list_view(request):
    user_list = User.objects.order_by('email')
    user_dict = {'user_list': user_list}
    return render(request, 'userapp/user_list.html', context=user_dict)
    
def user_form_view(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit= True)
            return index(request)
        else:
            print('Error')

    return render(request, 'userapp/user_form.html',{'form':form})
