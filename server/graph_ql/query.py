import graphene
from database import TableQuests
from graph_ql.typedefs import Quest


class Query(graphene.ObjectType):
    quests = graphene.List(Quest, id=graphene.Int(required=False))
    get_journals = graphene.List(Quest)
    get_root = graphene.List(Quest)

    @staticmethod # this whole thing is the CLEANEST SHIT youve ever done seen
    def resolve_quests(parent, info, **kargs):
        pargs = ['id', 'type', 'parentId']
        quests_query = Quest.get_query(info) # rename to filtered or seomthing

        # check for the args
        for arg in pargs:
            if kargs.get(arg) is not None:
                quests_query = quests_query.filter(getattr(TableQuests, arg) == kargs.get(arg)).all()
        
        return quests_query
    
    @staticmethod # unneeded
    def resolve_get_journals(parent, info, **args):
        quests_query = Quest.get_query(info)
        return quests_query.filter(TableQuests.type == "journal").all()
    
    @staticmethod # unneeded
    def resolve_get_root(parent, info, **args):
        quests_query = Quest.get_query(info)
        return quests_query.filter(TableQuests.parent_id == 0).all()
