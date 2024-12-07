from modeltranslation.translator import translator, TranslationOptions
from .models import BlogCategory, BlogPost, LifeEvent, Project, Service, Skill


class ServiceTranslationOptions(TranslationOptions):
    fields = ("title", "description")


class SkillTranslationOptions(TranslationOptions):
    fields = ("title",)


class ProjectTranslationOptions(TranslationOptions):
    fields = ("title", "short_description", "description")


class BlogPostTranslationOptions(TranslationOptions):
    fields = ("title", "resume", "body")


class LifeEventTranslationOptions(TranslationOptions):
    fields = ("title", "entity", "description")


class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(Skill, SkillTranslationOptions)

translator.register(Service, ServiceTranslationOptions)

translator.register(Project, ProjectTranslationOptions)

translator.register(BlogPost, BlogPostTranslationOptions)
translator.register(BlogCategory, BlogCategoryTranslationOptions)

translator.register(LifeEvent, LifeEventTranslationOptions)
