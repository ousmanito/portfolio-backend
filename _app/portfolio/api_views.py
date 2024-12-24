from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status

from .serializers import (
    BlogCategorySerializer,
    BlogSerializer,
    LifeEventSerializer,
    MailSerializer,
    ProjectSerializer,
    ResumeSerializer,
    SkillSerializer,
    ServiceSerializer,
)
from .models import (
    BlogPost,
    BlogCategory,
    LifeEvent,
    Mail,
    Project,
    Resume,
    Service,
    Skill,
)


class MailViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer


class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.prefetch_related("categories").all()
    serializer_class = BlogSerializer
    lookup_field = "url"


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = LifeEvent.objects.all().order_by("-date")
    serializer_class = LifeEventSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by("order")
    serializer_class = ServiceSerializer
    lookup_field = "url"


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    lookup_field = "url"


class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.prefetch_related("skills").order_by("order")
    serializer_class = ProjectSerializer
