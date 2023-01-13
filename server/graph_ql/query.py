import graphene
from database import TableQuests
from graph_ql.typedefs import Quests


class Query(graphene.ObjectType):
    get_quests = graphene.List(Quests)
    quests_by_id = graphene.List(Quests, id=graphene.Int())
    get_journals = graphene.List(Quests)
    get_root = graphene.List(Quests)

    @staticmethod
    def resolve_get_quests(parent, info, **args):
        return Quests.get_query(info).all()

    @staticmethod
    def resolve_quests_by_id(parent, info, **args):
        quests_query = Quests.get_query(info)
        return quests_query.filter(TableQuests.id == args.get("id")).all()
    
    @staticmethod
    def resolve_get_journals(parent, info, **args):
        quests_query = Quests.get_query(info)
        return quests_query.filter(TableQuests.type == "journal").all()
    
    @staticmethod
    def resolve_get_root(parent, info, **args):
        quests_query = Quests.get_query(info)
        return quests_query.filter(TableQuests.parent_id == 0).all()
    
    # @staticmethod
    # def resolve_tasks(parent, info, **args):
    #     quests_query = Quests.get_query(info)
    #     return quests_query.filter(TableQuests.parent_id == args.get("id")).all()
