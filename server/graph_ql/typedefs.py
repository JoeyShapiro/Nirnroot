import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from database import TableQuests

class Quest(SQLAlchemyObjectType):
    class Meta:
        model = TableQuests

# these are the fields for mutation
class QuestFields:
    id = graphene.Int(required=False)
    type = graphene.String(required=True)
    title = graphene.String(required=True)
    description = graphene.String(required=False)
    parent_id = graphene.Int(required=True)
    share = graphene.Int(required=False)
    secret = graphene.Int(required=True)

class SaveQuestFields(graphene.InputObjectType, QuestFields):
    pass
