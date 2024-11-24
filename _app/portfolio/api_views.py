from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status

from .serializers import (
    BlogCategorySerializer,
    BlogSerializer,
    EventSerializer,
    MailSerializer,
    ProjetSerializer,
    ServiceDetailSerializer,
    SkillSerializer,
    SoftSkillSerializer,
    LanguageSerializer,
    ServiceSerializer,
    CommentSerializer,
)
from .models import (
    Blog,
    BlogCategory,
    Comment,
    Event,
    Mail,
    Projet,
    Service,
    ServiceDetail,
    Skill,
    SoftSkill,
    Language,
)


@api_view(["POST"])
def increment_comment_count(request):
    comment_id = request.data.get("comment_id")
    try:
        comment = Comment.objects.get(id=comment_id)
        comment.increment_count()
        return Response({"count": comment.count}, status=status.HTTP_200_OK)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def decrement_comment_count(request):
    comment_id = request.data.get("comment_id")
    try:
        comment = Comment.objects.get(id=comment_id)
        if comment.count > 0:
            comment.decrement_count()
        return Response({"count": comment.count}, status=status.HTTP_200_OK)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)


class MailViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-creation_date")
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        blog_id = request.query_params.get("blog_id")
        if blog_id is not None:
            queryset = queryset.filter(blog_id=blog_id, parent=None)
        else:
            queryset = queryset.filter(parent=None)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.prefetch_related("category").all()
    serializer_class = BlogSerializer
    lookup_field = "url"


class SoftSkillViewSet(viewsets.ModelViewSet):
    queryset = SoftSkill.objects.prefetch_related("skill").all().order_by("order")
    serializer_class = SoftSkillSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all().prefetch_related("skill").order_by("order")
    serializer_class = LanguageSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("-date")
    serializer_class = EventSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by("order")
    serializer_class = ServiceSerializer
    lookup_field = "url"


class ServiceDetailViewSet(viewsets.ModelViewSet):
    queryset = ServiceDetail.objects.all().order_by("order")
    serializer_class = ServiceDetailSerializer


class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.prefetch_related("skill").order_by("order")
    serializer_class = ProjetSerializer
