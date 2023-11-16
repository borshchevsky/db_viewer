from sqlalchemy import create_engine, text, MetaData, insert
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, scoped_session


def process(mapping, source_dsn, target_dsn):
    data = get_data(mapping, source_dsn)
    return load_data(mapping, data, target_dsn)


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
    session.execute(insert(getattr(tables, mapping['targetTable'])), data)
    session.commit()
    return len(data)
