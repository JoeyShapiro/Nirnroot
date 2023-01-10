FROM python

RUN python3 -m pip install flask flask_graphql sqlalchemy graphene graphene_sqlalchemy PyMySQL
RUN pip install flask flask_restful mysql-connector-python
ADD server/server.py ./
ADD server/database.py ./
ADD server/graph_ql ./graph_ql
ADD server/keys/ ./keys/

EXPOSE 5000
ENTRYPOINT [ "python", "server.py" ]
