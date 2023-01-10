import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from database import TableQuests


class Quests(SQLAlchemyObjectType):
    class Meta:
        model = TableQuests

class QuestFields:
    id = graphene.Int()
    type = graphene.String()
    title = graphene.String()
    description = graphene.String()
    parent_id = graphene.Int()
    share = graphene.Int()
    secret = graphene.Int()

class AddQuestFields(graphene.InputObjectType, QuestFields):
    pass
