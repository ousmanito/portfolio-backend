from django.contrib import admin
from .models import (
    Blog,
    BlogCategory,
    Comment,
    Education,
    Language,
    Projet,
    Service,
    Experience,
    ServiceDetail,
    Skill,
    SoftSkill,
)

admin.site.register(ServiceDetail)
admin.site.register(Skill)
admin.site.register(Projet)
admin.site.register(SoftSkill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Language)
admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(Comment)
