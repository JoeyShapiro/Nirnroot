import graphene
from database import TableQuests
from graph_ql.typedefs import Quest


class Query(graphene.ObjectType):
    quests = graphene.List(Quest, id=graphene.Int(required=False))
    get_journals = graphene.List(Quest)
    get_root = graphene.List(Quest)

    @staticmethod
    def resolve_quests(parent, info, **kargs):
        pargs = ['id', 'type', 'parentId']
        quests_query = Quest.get_query(info) # rename to filtered or seomthing

        # check for the args
        if kargs.get('id') is not None:
            quests_query = quests_query.filter(TableQuests.id == kargs.get('id')).all()
        
        return quests_query
    
    @staticmethod
    def resolve_get_journals(parent, info, **args):
        quests_query = Quest.get_query(info)
        return quests_query.filter(TableQuests.type == "journal").all()
    
    @staticmethod
    def resolve_get_root(parent, info, **args):
        quests_query = Quest.get_query(info)
        return quests_query.filter(TableQuests.parent_id == 0).all()
