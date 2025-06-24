from app.models import db
from sqlalchemy.orm import sessionmaker


def get_session():

    # Create a configured "Session" class
    Session = sessionmaker(bind=db)

    # Create a new session instance
    session = Session()

    try:
        yield session
    finally:
        session.close()
