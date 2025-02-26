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

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api_views import (
    BlogCategoryViewSet,
    BlogViewSet,
    EventViewSet,
    MailViewSet,
    ProjetViewSet,
    ResumeViewSet,
    ServiceViewSet,
)

router = DefaultRouter()
router.register(r"life_events", EventViewSet)
router.register(r"services", ServiceViewSet)
router.register(r"resumes", ResumeViewSet)
router.register(r"projects", ProjetViewSet)
router.register(r"blog", BlogViewSet)
router.register(r"blog_categories", BlogCategoryViewSet)
router.register(r"mail", MailViewSet)

urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
