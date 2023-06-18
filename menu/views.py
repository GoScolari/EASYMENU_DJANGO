from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context ={
            'posts': posts,
		
        }
        return render(request, 'menu_list.html',context)
    
class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {
            'form': form
            }
        return render(request, 'menu_create.html',context)
    
    def post(self, request, *args, **kwargs):
        if request.method =='POST':
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, create = Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect('menu:home')
        context = {
             
	    }
        
class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        posts = get_object_or_404(Post, pk=pk)
        context = {
            'post': posts,
        }
        return render(request, 'menu_detail.html' , context )

class BlogUpdateView(UpdateView):
    model = Post
    fields =['title', 'content']
    template_name = 'menu_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('menu:detail', kwargs={'pk': pk} )
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'menu_delete.html'
    success_url = reverse_lazy('menu:home')