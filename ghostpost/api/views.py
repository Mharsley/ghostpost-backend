from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
# from ghostpost.models import Author, Post
from ghostpost.models import Post
# from ghostpost.api.serializers import AuthoSerializer, PostSerializer
from ghostpost.api.serializers import PostSerializer

# class AuthorViewSet(ModelViewSet):
#     serializer_class = AuthoSerializer
#     basename = 'author'
#     queryset = Author.objects.all()

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    basename = 'post'
    
    def get_queryset(self):    
        return Post.objects.all().order_by('-date')

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            post.likes +=1
            post.save()
            return Response({
                "status": "Success "
            })
        return Response({
                "status": "Failure"
            })

    @action(detail=True, methods=['get'])
    def downvote(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            post.likes -=1
            post.save()
            return Response({
                "status": "Success "
            })
        return Response({
                "status": "Failure"
            })