import graphene
from graph_ql.query import Query
from graph_ql.mutation import Mutation
from graph_ql.typedefs import Quest


schema = graphene.Schema(
    query=Query, mutation=Mutation, types=[Quest]
)