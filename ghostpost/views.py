# from django.shortcuts import render, HttpResponseRedirect, reverse

# from ghostpost.models import Author, Post
# from ghostpost.forms import PostForm, AuthorForm

# sort=True

# def sorturl(request, *args, **kwargs):
#     global sort
#     sort = not sort
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# def index(request,*args, **kwargs):
#     html = "main.html"
#     # items = Post.objects.order_by('date')
#     # items = Post.objects.all()
#     if sort == True:
#         items = Post.objects.order_by('date')
#     else:
#         items = Post.objects.order_by('likes')

#     return render(request, html, {'stories': items})

# def boasturl(request, *args, **kwargs):

#     html = "main.html"
#     if sort==True:
#         items = Post.objects.filter(boast=True).order_by('date')
#     else:
#         items = Post.objects.filter(boast=True).order_by('likes')

#     return render(request, html, {'stories': items})

# def roasturl(request, *args, **kwargs):

#     html = "main.html"
#     if sort==True:
#         items = Post.objects.filter(boast=False).order_by('date')
#     else:
#         items = Post.objects.filter(boast=False).order_by('likes')
#     return render(request, html, {'stories': items})

# def add_post(request, *args, **kwargs):
#     html = 'addpost.html'

#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Post.objects.create(
#                 title=data['title'],
#                 description=data['description'],
#                 author=data['author'],
#                 boast=data['boast']
#             )
#             return HttpResponseRedirect(reverse('homepage'))
#     form = PostForm()

#     return render(request,html,{'form': form})


# def add_author(request, *args, **kwargs):
#     html = 'addauthor.html'

#     if request.method == "POST":
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Author.objects.create(
#                 name=data['name'],
#             )
#             return HttpResponseRedirect(reverse('homepage'))
#     form = AuthorForm()

#     return render(request,html,{'form': form})

# def add_like(request, post_id, *args, **kwargs):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist():
#         return HttpResponseRedirect(reverse('homepage'))

#     post.likes +=1
#     post.save()
#     return HttpResponseRedirect(reverse('homepage'))

# def remove_like(request, post_id, *args, **kwargs):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist():
#         return HttpResponseRedirect(reverse('homepage'))

#     post.likes -=1
#     post.save()
#     return HttpResponseRedirect(reverse('homepage'))