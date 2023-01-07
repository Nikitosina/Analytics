from sqlalchemy import create_engine, MetaData
from clickhouse_sqlalchemy import get_declarative_base

engine = create_engine('clickhouse://default:@localhost/default', pool_size=1, max_overflow=0)
metadata = MetaData(bind=engine)

Base = get_declarative_base(metadata=metadata)
