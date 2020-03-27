from .serializers import Spost
from posts.models import Post
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response
# from rest_framework.Status import status
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from posts.api.serializers import Spost
from posts.models import Post
from posts.api.permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.db import close_old_connections
from rest_framework import filters
from rest_framework import status

# from rest_framework.responseim
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     # lookup_field="id"
#     serializer_class=Suser

class PostViewSet(viewsets.ModelViewSet):
    close_old_connections()
    queryset = Post.objects.all()
    # lookup_field="id"
    search_fields = ['url']
    filter_backends = (filters.SearchFilter,)


    serializer_class=Spost
    permission_classes =[IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]
    authentication_classes =(TokenAuthentication,JSONWebTokenAuthentication)
    def create(self, request):
        url = request.data.get('url')
        author = str(request.user)
        filtered_url = Post.objects.filter(url=url)
        already_exists = False
        for each_url in filtered_url:
            if each_url.author.username == author:
                already_exists = True
        if already_exists:
            return Response({"details" : "Review already exists ! "}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super(PostViewSet, self).create(request)             
    def perform_create(self,serializer):

        serializer.save(author=self.request.user)
    close_old_connections()
    # @action(detail=True,methods=['POST'])
    # def rate_post(self,request,pk=None):
    #     if 'stars' in request.data:
    #         post=Post.objects.get(id=pk)
    #         stars = request.data['stars']
    #         user=request.user
    #         # user = User.objects.get(id=1)
    #         print('hser title' ,user.username)
    #         response={'message':'ok this is working'}
            # try:
            #     rating=Rating.objects.get(user=user.id, Post=post.id)
            #     rating.stars=stars
            #     rating.save()
            #     serializer=Srating(rating,many=False)
            #     response={'message':'rating updated','result':serializer.data}
            #     return Response(response,status=status.HTTP_200_OK)
            # except:
            #     rating = Rating.objects.create(user=user,Post=post,stars=stars)
            #     serializer=Srating(rating,many=False)
            #     response={'message':'rating created','result':serializer.data}
            #     return Response(response,status=status.HTTP_200_OK)

            # return Response(response,status=status.HTTP_200_OK)
        # else:
        #     response={'message':'no stars'}
        #     return Response(response,status=status.HTTP_200_OK)

# class CommentsCreateAPIView(generics.CreateAPIView):
#     queryset=comments.objects.all()
#     serializer_class=Scomments
#     permission_classes=[IsAuthorOrReadOnly]
#     def perform_create(self,serializer):
#         request_user= self.request.user
#         kwarg_id=self.kwargs.get("id")
#         post=get_object_or_404(comments,id=kwarg_id)
#         serializer.save(author=request.user,post=post)
# class RatingViewSet(viewsets.ModelViewSet):
#     queryset=Rating.objects.all()
#     serializer_class=Srating
#     authentication_classes =(TokenAuthentication,)

# class PostRUDView(generics.RetrieveUpdateDestroyAPIView):

class PostRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=Spost
    permission_classes=[IsAuthorOrReadOnly,IsAuthenticatedOrReadOnly]
class PostLikeView(APIView):
    serializer_class=Spost
    permission_classes=[IsAuthenticatedOrReadOnly]
    def delete(self,request,pk):
        post=get_object_or_404(Post,pk=pk)
        user=request.user
        post.voters.remove(user)
        serializer_context={"request":request}
        serializer=self.serializer_class(post,context=serializer_context)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,pk):
        post=get_object_or_404(Post,pk=pk)
        user=request.user
        post.voters.add(user)
        serializer_context={"request":request}
        serializer=self.serializer_class(post,context=serializer_context)
        return Response(serializer.data,status=status.HTTP_200_OK)
class userView(mixins.RetrieveModelMixin,ListAPIView):
    """ this is to get the  all the objects created by a  indiviual user through id"""
    serializer_class=serializers.UserDetailSerializer
    # permission_classes=[IsOwnerOrReadOnly,permissions.IsAuthenticatedOrReadOnly]
    lookup_field='id'
    def get_queryset(self):
        if self.kwargs['id']:
            return Post.objects.all().filter(user=self.kwargs['id'])
###########
# class Postsnippet(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,Spost
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     serializer_class = Spost
#     lookup_field='id'
#     def get_queryset(self):
#         request = self.request
#         print(request.user)
#         qs = Post.objects.all()
#         query = request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
# class Postsnippet(viewsets.ModelViewSet):
#     serializer_class=Spost
#     queryset= Post.objects.all()
@api_view(["GET","POST"])
def api_get_create(request):


    if request.method == "GET":
        post=Post.objects.all()
        serializer= Spost(post,many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer= Spost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def api_delete(request,pk):
    # post=Post.objects.filter(pk=pk)
    try:
        post = Post.objects.get(pk=pk)  # Lookup a specific object
    except post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer= Spost(post,many=True)

        return Response(serializer.data)
    elif request.method == "PUT":
        # post=Post.objects.filter(pk=pk)
        serializer= Spost(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print("noot correct")
        return Response(serializer.data)
