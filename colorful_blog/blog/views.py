from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostModelForm


@staff_member_required()
def blog_post_create_view(request):
    obj = BlogPost()
    title = 'Create a new Blog Post'
    template_name = 'create.html'
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        print("pasa por  despues de request user de create")
        post.save()
        print("pasa por post save")
        # post = BlogPost.objects.create(**form.cleaned_data)
        # forma  propia django para instanciar un nuevo objeto desempaquetando el diccionario en key value
        # utilizando un modelform se simplifica con form.save
        form = BlogPostModelForm()
    context = {'title': title, 'formulario': form}
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


@staff_member_required()
def blog_post_update_view(request, slug):
    print("pasa por el principio de update")
    obj = get_object_or_404(BlogPost, slug=slug)
    print("pasa por obj = get_object_or_404(BlogPost, slug=slug)")
    form = BlogPostModelForm(request.POST or None, instance=obj)
    print("pasa por form = BlogPostModelForm(request.POST or None, instance=obj)")
    if form.is_valid():
        print("pasa por if form.is_valid() comentado:")
        form.save()
        print("pasa por form.save()")

    template_name = 'update.html'
    title = f"Edit {obj.title}"
    context = {'form': form, 'title': title}
    return render(request, template_name, context)


@staff_member_required()
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog')
    title = 'Blogposts'
    template_name = 'delete.html'
    context = {'object': obj}
    return render(request, template_name, context)

