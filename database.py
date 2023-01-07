from sqlalchemy import create_engine, MetaData
from clickhouse_sqlalchemy import get_declarative_base
from config import current_config as config

engine = create_engine(f'clickhouse://{config.db_username}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_name}', pool_size=1, max_overflow=0)
metadata = MetaData(bind=engine)

Base = get_declarative_base(metadata=metadata)
