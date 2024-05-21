from django.contrib import admin
from .models import (
    Blog,
    BlogCategory,
    Comment,
    Education,
    Expertise,
    Language,
    Projet,
    Service,
    Experience,
    ServiceDetail,
    Skill,
    SoftSkill,
)


class ModelAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    ordering = ("order", "id")


admin.site.register(ServiceDetail, ModelAdmin)
admin.site.register(Skill)
admin.site.register(Projet)
admin.site.register(SoftSkill, ModelAdmin)
admin.site.register(Experience, ModelAdmin)
admin.site.register(Education, ModelAdmin)
admin.site.register(Language, ModelAdmin)
admin.site.register(Expertise, ModelAdmin)
admin.site.register(Service, ModelAdmin)
admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(Comment)
