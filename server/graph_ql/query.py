import graphene
from database import TableQuests
from graph_ql.typedefs import Quests


class Query(graphene.ObjectType):
    get_quests = graphene.List(Quests)
    quests_by_id = graphene.List(Quests, id=graphene.Int())

    @staticmethod
    def resolve_get_quests(parent, info, **args):
        return Quests.get_query(info).all()

    @staticmethod
    def resolve_quests_by_id(parent, info, **args):
        quests_query = Quests.get_query(info)
        return quests_query.filter(TableQuests.id == args.get("id")).all()
    