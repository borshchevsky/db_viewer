from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from sqlalchemy import create_engine, inspect, text

from api.models import DB
from api.serializers import DBSerializer


class DBModelView(ModelViewSet):
    queryset = DB.objects.all()
    serializer_class = DBSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def serialize_db():
        data = {}
        engine = create_engine('postgresql://postgres:postgres@localhost:5432')
        connection = engine.connect()
        databases = [item[0] for item in connection.execute(text('SELECT datname FROM pg_database')).fetchall() if
                     'template' not in item[0]]
        connection.close()
        for db in databases:
            data[db] = {}
        for db in data:
            engine = create_engine(f'postgresql://postgres:postgres@localhost:5432/{db}')
            schemas = [schema for schema in inspect(engine).get_schema_names() if schema != 'information_schema']
            for schema in schemas:
                data[db][schema] = {}
                tables = inspect(engine).get_table_names(schema=schema)
                for table in tables:
                    data[db][schema][table] = {}
                    columns = inspect(engine).get_columns(schema=schema, table_name=table)
                    for column in columns:
                        data[db][schema][table][column['name']] = column['type']