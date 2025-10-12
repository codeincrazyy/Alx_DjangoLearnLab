from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import PermissionDenied
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import Post, Comment, Like
from notifications.models import Notification

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only authors to edit or delete their own posts/comments.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    search_fields = ['title', 'content']  # Allows search by title or content
    ordering_fields = ['created_at', 'updated_at']
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get users that the current user follows
        following_users = self.request.user.following.all()
        # Return posts authored by followed users, newest first
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if Like.objects.filter(post=post, user=request.user).exists():
        return Response({'detail': 'You have already liked this post.'}, status=400)

    Like.objects.create(post=post, user=request.user)

    # Create notification for the post author
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked',
            content_type=ContentType.objects.get_for_model(Post),
            object_id=post.id
        )

    return Response({'detail': f'You liked the post "{post.title}".'}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(post=post, user=request.user).first()

    if not like:
        return Response({'detail': 'You have not liked this post yet.'}, status=400)

    like.delete()
    return Response({'detail': f'You unliked the post "{post.title}".'}, status=200)