from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse
from .models import Entry
from .forms import UserRegisterForm ,moodForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView , DetailView ,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def cover(request):
    return render (request , 'diary/cover.html')

@login_required
def Profile(request):
    current_user = request.user

    return render (request , 'diary/profile.html' , {'current_user':current_user})
@login_required
def home(request):

    current_user_id = request.user
    if request.method == "POST":
        form = moodForm(request.POST)
        if form.is_valid:
            return redirect('homepage')

    else :
        form = moodForm()
    context = {
        'diarys' : Entry.objects.filter(author=current_user_id).order_by('-date_posted'),
        'form' : form
    }
    
    return render(request , 'diary/base.html', context)
class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(LoginRequiredMixin,CreateView):
    model = Entry
    fields = ['mood','title', 'text']
                                            
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EntryUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Entry
    fields = ['mood','title', 'text']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        entry = self.get_object()
        if self.request.user == entry.author:
            return True
        return False

class EntryDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Entry
    success_url = '/home'

    def test_func(self):
        entry = self.get_object()
        if self.request.user == entry.author:
            return True
        return False


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f'Account Created For {username}')
            return redirect('login')

    else :
        form = UserRegisterForm()
    return render(request , 'diary/register.html' , {'form' : form})