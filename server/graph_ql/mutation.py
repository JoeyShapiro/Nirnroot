import graphene
from database import db_session, TableQuests
from graph_ql.typedefs import Quest, SaveQuestFields
from sqlalchemy import update


class SaveQuest(graphene.Mutation):
    quest = graphene.Field(lambda: Quest)
    status = graphene.Boolean()
    updatable = [ 'type', 'title', 'description', 'parent_id', 'share', 'secret' ]

    class Arguments:
        input = SaveQuestFields(required=True)

    @staticmethod
    def mutate(self, info, input):
        quest = TableQuests(**input) # this is the new one
        if (dquest := db_session.get(TableQuests, quest.id)) is not None: # also checks if the id is valid
            vals = { col: input.get(col) or getattr(dquest, col) for col in SaveQuest.updatable } # dict for quest
            db_session.execute(
                update(TableQuests).where(TableQuests.id == dquest.id).values(vals)
            )
        else:
            db_session.add(quest) # should block task on root
        
        db_session.commit()

        status = True
        return SaveQuest(quest=quest, status=status) # returns either case

class Mutation(graphene.ObjectType):
    saveQuest = SaveQuest.Field()