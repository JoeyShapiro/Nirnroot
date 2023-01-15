import graphene
from database import TableQuests
from graph_ql.typedefs import Quest


class Query(graphene.ObjectType):
    pargs = {
        'id': graphene.Int(required=False),
        'parent_id': graphene.Int(required=False),
        'type': graphene.String()
    }

    quests = graphene.List(Quest, args=pargs)

    @staticmethod # this whole thing is the CLEANEST SHIT youve ever done seen
    def resolve_quests(parent, info, **kargs):
        quests_query = Quest.get_query(info) # rename to filtered or seomthing

        # check for the args
        for arg in list(Query.pargs.keys()):
            if kargs.get(arg) is not None:
                quests_query = quests_query.filter(getattr(TableQuests, arg) == kargs.get(arg)).all()
        
        return quests_query
