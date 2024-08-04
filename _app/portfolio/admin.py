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


class OrderedTitleModelAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    ordering = ("order", "id")

class OrderedSkillModelAdmin(admin.ModelAdmin):
    ordering = ("order", "id")


admin.site.register(ServiceDetail, OrderedTitleModelAdmin)
admin.site.register(Skill)
admin.site.register(Projet)
admin.site.register(SoftSkill, OrderedSkillModelAdmin)
admin.site.register(Experience, OrderedTitleModelAdmin)
admin.site.register(Education, OrderedTitleModelAdmin)
admin.site.register(Language, OrderedSkillModelAdmin)
admin.site.register(Expertise, OrderedSkillModelAdmin)
admin.site.register(Service, OrderedTitleModelAdmin)
admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(Comment)
