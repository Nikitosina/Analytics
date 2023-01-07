from clickhouse_sqlalchemy import engines
from clickhouse_sqlalchemy.types import UUID, Map, String, DateTime
from sqlalchemy import Column
from database import Base
from datetime import datetime

class Event(Base):
    __tablename__ = "events"

    id = Column(UUID, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    device_model = Column(String)
    analytics_user_id = Column(UUID, unique=True)
    platform = Column(String)
    parameters = Column(Map(String, String), nullable=False)
    timestamp = Column(DateTime, nullable=False)

    __table_args__ = (
        engines.MergeTree(),
    )

    def insert(self) -> str:
        # Use raw sql because sqlalchemy does not seem to support proper Map insertion
        return f'''
            INSERT INTO events (
                id, name, {'device_model, ' if self.device_model != None else ''}{'analytics_user_id, ' if self.analytics_user_id != None else ''}{'platform, ' if self.platform != None else ''}parameters, `timestamp`
            )
            VALUES (
                '{self.id}', '{self.name}', {f"'{self.device_model}', " if self.device_model != None else ''}{f"'{self.analytics_user_id}', " if self.analytics_user_id != None else ''}{f"'{self.platform}', " if self.platform != None else ''}{self.parameters}, '{datetime.strptime(self.timestamp, "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y-%m-%d %H:%M:%S")}'
            )
        '''
            

    def __repr__(self):
        return "<Event '{}'>".format(self.name)
