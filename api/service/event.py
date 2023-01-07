import uuid
from database import engine
from sqlalchemy import text
from ..model.event import Event
from ..utils.response_helper import ResponseHelper
from typing import Dict, Tuple, List
from sqlalchemy.orm import scoped_session, sessionmaker


def save_events(data: List[Dict[str, str]]) -> Tuple[Dict[str, str], int]:
    with scoped_session(sessionmaker(bind=engine))() as session:
        try:
            for eventDict in data:
                parameters = eventDict['parameters']
                device_model = parameters.get('model', None)
                analytics_user_id = parameters.get('analytics_user_id', None)
                platform = parameters.get('platform', None)
                timestamp = parameters['timestamp']
                parameters.pop('model', None)
                parameters.pop('analytics_user_id', None)
                parameters.pop('platform', None)
                parameters.pop('timestamp', None)
                event = Event(id=str(uuid.uuid4()), name=eventDict['name'], device_model=device_model, \
                    analytics_user_id=analytics_user_id, platform=platform, parameters=parameters, timestamp=timestamp)

                # Preprocess parameters' strings before insert
                for key in event.parameters.keys():
                    value = str(event.parameters[key]).replace("'", "|")
                    event.parameters[key] = value

                session.execute(text(event.insert()))
                session.commit()

            return {'status': 'success'}, 200
        except Exception as e:
            session.rollback()
            return {'status': 'error', 'description': str(e)}, 500
