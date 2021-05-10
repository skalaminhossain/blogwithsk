from django.shortcuts import render
from .models import Blog
from .models import Personalblog
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

def blog(request):
    blog = Blog.objects.all()
    context = {
        "blog":blog
    }
    return render(request, 'album/index.html', context)


def personalblog(request):
    personalblog = Personalblog.objects.all()
    paginator = Paginator(personalblog, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "personalblog":personalblog,
        "page_obj" : page_obj
    }
    return render(request, 'blueberry/index.html', context)


def blogDetails(request, slug):
    personalblog = Personalblog.objects.get(slug=slug)
    similar_post = personalblog.tags.similar_objects()[:4]
    comments = personalblog.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = personalblog
            new_comment.save()
            # messeges
            messages.success(request, 'Your comment Added.')
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()
    context = {
        "personalblog":personalblog,
        'similar_post': similar_post,
        'comments': comments
    }
    return render(request, 'blueberry/details.html', context)


def search_blog(request):
    
    queryset = Personalblog.objects.all()
    query = request.GET.get('q')
    
    paginator = Paginator(queryset, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if query:
        queryset = queryset.filter(
            Q(blogtitle__icontains=query) |  Q(description__icontains=query)


        ).distinct()
    context = {
        'queryset': queryset,
        'query': query


    }
    return render(request, 'blueberry/search.html', context)
