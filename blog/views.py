from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.views.generic import ListView
from .models import Post


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'



"""
# Working with QuerySets and managers 

from django.contrib.auth.models import User
from blog.models import Post

user = User.objects.get(username='admin')
post = Post(title='Another post', slug='another-post', body='Post body.', author=user)
post.save()

# Updating objects

post.title = 'New title'
post.save()

# Retrieving objects

all_posts = Post.objects.all()
all_posts

# Using the filter() method

Post.objects.filter(publish__year=2020)
Post.objects.filter(publish__year=2020, author__username='admin')
Post.objects.filter(publish__year=2020).filter(author__username='admin')

# Using exclude()

Post.objects.filter(publish__year=2020).exclude(title__startswith='Why')

# Using order_by()

Post.objects.order_by('title')
Post.objects.order_by('-title')

# Deleting objects

post = Post.objects.get(id=1)
post.delete()

"""