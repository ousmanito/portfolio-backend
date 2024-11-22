"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .api_views import (
    BlogViewSet,
    CommentViewSet,
    EducationViewSet,
    ExperienceViewSet,
    MailViewSet,
    ProjetViewSet,
    ServiceDetailViewSet,
    SkillViewSet,
    SoftSkillViewSet,
    ServiceViewSet,
    LanguageViewSet,
    BlogCategoryViewSet,
    decrement_comment_count,
    increment_comment_count,
)


router = DefaultRouter()
router.register(r"Experiences", ExperienceViewSet)
router.register(r"Education", EducationViewSet)
router.register(r"SoftSkills", SoftSkillViewSet)
router.register(r"Langages", LanguageViewSet)
router.register(r"Services", ServiceViewSet)
router.register(r"Skills", SkillViewSet)
router.register(r"Projets", ProjetViewSet)
router.register(r"ServiceDetails", ServiceDetailViewSet)
router.register(r"blog", BlogViewSet)
router.register(r"blog-details", BlogCategoryViewSet)
router.register(r"mail", MailViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/increment_comment_count/", increment_comment_count),
    path("api/decrement_comment_count/", decrement_comment_count),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
