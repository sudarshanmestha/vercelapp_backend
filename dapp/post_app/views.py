from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .models import Post
from .serializers import PostSerializer

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


