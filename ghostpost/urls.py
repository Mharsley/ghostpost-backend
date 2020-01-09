"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin

from ghostpost.api.urls import urlpatterns as api_urls
# from ghostpost.views import index, boasturl, roasturl, add_post, add_author, add_like, remove_like, sorturl
# from ghostpost.models import Post, Author
from ghostpost.models import Post

admin.site.register(Post)
# admin.site.register(Author)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='homepage'),
    # path('boast/', boasturl),
    # path('roast/', roasturl),
    # path('addpost/', add_post),
    # path('addauthor/', add_author),
    # path('addlike/<int:post_id>', add_like),
    # path('removelike/<int:post_id>', remove_like),
    # path('sort/', sorturl)
]

urlpatterns += api_urls