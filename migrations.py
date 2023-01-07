from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


conn_str = 'clickhouse://default:@localhost/default'
engine = create_engine(conn_str)
session = sessionmaker(bind=engine)()

create_events_table_script = '''
CREATE TABLE IF NOT EXISTS events (
    id UUID,
    name String,
    device_model Nullable(String),
    analytics_user_id Nullable(UUID),
    platform Nullable(String),
    parameters Map(String, String),
    timestamp Datetime('Europe/Moscow')
) 
ENGINE = MergeTree() ORDER BY id
'''

# add_device_id_column_script = '''
# ALTER TABLE events ADD COLUMN IF NOT EXISTS device_id Nullable(String)
# '''

with engine.connect() as connection:
    result = connection.execute(text(create_events_table_script))
    print(result)
