from urllib import request
from django.http import HttpResponse
from django.contrib import messages
from django.http.request import HttpRequest as HttpRequest
from django.views.generic import TemplateView, DeleteView, FormView
from .models import Post
from .forms import PostForm

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context
    
class PostClassView(DeleteView):
    template_name = "detail.html"
    model = Post

class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    

    def form_valid(self, form):
        
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image'],
            condition = form.cleaned_data['condition'],
        )
        messages.add_message(self.request, messages.SUCCESS, 'Your Post Was Successfull')
        return super().form_valid(form)
    