import graphene
from database import db_session, TableQuests
from graph_ql.typedefs import Quest, AddQuestFields


class AddQuest(graphene.Mutation):
    quest = graphene.Field(lambda: Quest)
    status = graphene.Boolean()

    class Arguments:
        input = AddQuestFields(required=True)

    @staticmethod
    def mutate(self, info, input):
        quest = TableQuests(**input)
        db_session.add(quest)
        db_session.commit()
        status = True
        return AddQuest(quest=quest, status=status)

class Mutation(graphene.ObjectType):
    addQuest = AddQuest.Field()
