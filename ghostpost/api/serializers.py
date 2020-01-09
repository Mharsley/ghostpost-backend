from rest_framework.serializers import HyperlinkedModelSerializer
# from ghostpost.models import Author, Post
from ghostpost.models import Post

# class AuthoSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Author
#         fields = (
#             'name',
#         )

class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description',
            'boast',
            'date',
            'likes',
        )