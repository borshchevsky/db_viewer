from sqlalchemy import create_engine, text, MetaData, insert
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, scoped_session


def get_data(mapping, dsn):
    engine = create_engine(dsn)
    connection = engine.connect()
    fields = ', '.join(f""""{s["fieldName"]}" {t["fieldName"]}""" for s, t in zip(mapping['source'], mapping['target']))
    sql_query = 'select ' + fields + f' from "{mapping["sourceSchema"]}"."{mapping["sourceTable"]}"'
    data = [item._asdict() for item in connection.execute(text(sql_query)).fetchall()]
    connection.close()
    return data


def load_data(mapping, data, dsn):
    engine = create_engine(dsn)
    session = scoped_session(sessionmaker(autoflush=False, bind=engine))
    metadata = MetaData(schema=mapping['targetSchema'])
    metadata.reflect(engine, only=[mapping['targetTable']])
    base = automap_base(metadata=metadata)
    base.prepare()
    tables = base.classes

    objects = [
        {
            **item
        } for item in data
    ]

    session.execute(insert(getattr(tables, mapping['targetTable'])), objects)
    session.commit()

    return objects


j = {
    "sourceServerId": 5,
    "targetServerId": 6,
    "sourceDb": "postgres",
    "targetDb": "postgres",
    "sourceSchema": "public",
    "targetSchema": "public",
    "sourceTable": "source_table",
    "targetTable": "target_table",
    "source": [
        {
            "schemaName": "public",
            "tableName": "source_table",
            "fieldName": "source_column",
            "id": 0
        }
    ],
    "target": [
        {
            "schemaName": "public",
            "tableName": "target_table",
            "fieldName": "target_column",
            "id": 1
        }
    ]
}

if __name__ == '__main__':
    data = get_data(j, 'postgresql://postgres:postgres@localhost:5432')
    print(load_data(j, data))
