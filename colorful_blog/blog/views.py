from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm


def blog_post_create_view(request):
    obj = BlogPost()
    title = 'Create a new Blog Post'
    template_name = 'create.html'
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        post = BlogPost.objects.create(**form.cleaned_data)
        # forma propia django para instanciar un nuevo objeto desempaquetando el diccionario en key value
        form = BlogPostForm()
    context = { 'title': title, 'formulario': form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    title = 'Blogposts'
    template_name = 'detail.html'
    context = {'object': obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    title = 'Blogposts'
    template_name = 'list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    title = 'Blogposts'
    template_name = 'update.html'
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    title = 'Blogposts'
    template_name = 'delete.html'
    context = {'object': obj}
    return render(request, template_name, context)
