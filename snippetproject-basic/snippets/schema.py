import graphene
from graphene_django.types import DjangoObjectType
from .models import Snippet, HardCode


class SnippetType(DjangoObjectType):
    class Meta:
        model = Snippet


class HardCodeType(DjangoObjectType):
    class Meta:
        model = HardCode


class Query(graphene.ObjectType):
    all_snippets = graphene.List(SnippetType)
    all_hardcodes = graphene.List(HardCodeType)

    def resolve_all_snippets(self, info, **kwargs):
        return Snippet.objects.all()

    def resolve_all_hardcodes(self, info, **kwargs):
        return HardCode.objects.all()
