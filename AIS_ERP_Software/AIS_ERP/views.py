#
# from django.http import HttpResponse
# from .models import AisErp
# from django.contrib.auth.models import User
# #  Create your views here.
################################################################
# from django.shortcuts import render
# from django.core.urlresolver import reverse_lazy
# from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = "AIS_ERP/signup.html"



#
# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth.models import User
# from django.views.generic import (
#     ListView,
#     DetailView,
#     CreateView,
#     UpdateView,
#     DeleteView
# )
# from .models import AisErp
# from .models import post
#
# def home(request):
#     ais_erp_objects = AisErp.objects.all()
#     context = {
#             'ais_erp_objects': ais_erp_objects
#     }
#     return render(request,'AIS_ERP/home.html', context)
#
#
# class AisErpListView(ListView):
#     model = AisErp
#     template_name = 'AIS_ERP/home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = 5
#
#
# class UserPostListView(ListView):
#     model = post
#     template_name = 'AIS_ERP/user_posts.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     paginate_by = 5
#
#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return post.objects.filter(author=user).order_by('-date_posted')
#
#
# class PostDetailView(DetailView):
#     model = post
#
#
# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = post
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#
# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = post
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
#
#
# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = post
#     success_url = '/'
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
#
#
# def about(request):
#     return render(request, 'AisErp/about.html', {'title': 'About'})
#
#
