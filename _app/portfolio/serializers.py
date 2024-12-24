from rest_framework import serializers

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


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = "__all__"


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    categories = BlogCategorySerializer(many=True)

    class Meta:
        model = BlogPost
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class LifeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeEvent
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    details = SkillSerializer(many=True)

    class Meta:
        model = Service
        fields = [
            "id",
            "description",
            "details",
            "image",
            "title",
        ]


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "short_description",
            "description",
            "skills",
            "url",
            "github",
        ]
