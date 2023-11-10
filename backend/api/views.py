from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from sqlalchemy import create_engine, inspect, text

from api.models import DB
from api.serializers import DBSerializer


class DBModelView(ModelViewSet):
    queryset = DB.objects.all()
    serializer_class = DBSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data.get('name')
        if DB.objects.filter(name=name).exists():
            return Response({'error': 'Database with this name already exists.'}, status.HTTP_409_CONFLICT)
        data['schema'] = self.serialize_db(data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @staticmethod
    def serialize_db(data):
        host = data['host']
        port = data['port']
        username = data['username']
        password = data['password']
        data = {}
        dsn = f'postgresql://{username}:{password}@{host}:5432'
        engine = create_engine(dsn)
        connection = engine.connect()
        databases = [item[0] for item in connection.execute(text('SELECT datname FROM pg_database')).fetchall() if
                     'template' not in item[0]]
        connection.close()
        for db in databases:
            data[db] = {}
        for db in data:
            engine = create_engine(f'{dsn}/{db}')
            schemas = [schema for schema in inspect(engine).get_schema_names() if schema != 'information_schema']
            for schema in schemas:
                data[db][schema] = {}
                tables = inspect(engine).get_table_names(schema=schema)
                for table in tables:
                    data[db][schema][table] = {}
                    columns = inspect(engine).get_columns(schema=schema, table_name=table)
                    for column in columns:
                        data[db][schema][table][column['name']] = str(column['type'])
        return data
