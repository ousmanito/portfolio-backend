from django.contrib import admin

from .models import (
    BlogPost,
    BlogCategory,
    LifeEvent,
    Project,
    Resume,
    Service,
    Skill,
)
from modeltranslation.admin import TranslationAdmin


admin.site.register(Service, TranslationAdmin)
admin.site.register(Skill, TranslationAdmin)
admin.site.register(Project, TranslationAdmin)
admin.site.register(LifeEvent, TranslationAdmin)
admin.site.register(BlogPost, TranslationAdmin)
admin.site.register(BlogCategory, TranslationAdmin)
admin.site.register(Resume)
