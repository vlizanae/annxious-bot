from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from secret import psql_user, psql_pass
from .models import UserModelMixin


class Database:
    def __init__(self, session=False):
        self.engine = create_engine(
            'postgresql+psycopg2://{}:{}@localhost/annxious'
            .format(psql_user, psql_pass)
        )
        self.Session = sessionmaker(bind=self.engine)

        self.User = None
        self.create_schema(commit=False)

    def create_schema(self, commit=True):
        Base = declarative_base()

        class User(Base, UserModelMixin):
            pass
        self.User = User

        if commit:
            Base.metadata.create_all(self.engine)

    def drop_all(self):
        meta = MetaData(bind=self.engine)
        meta.reflect()
        meta.drop_all()

    def add_user(self, id, name):
        session = self.Session()
        session.add(
            self.User(name=name, conversation_id=id)
        )
        session.commit()
        session.close()

    def get_user(self, id):
        session = self.Session()
        user = None
        try:
            user = (
                session.query(self.User)
                .filter(self.User.conversation_id == id)
                .one()
            )
        except NoResultFound:
            session.rollback()
        session.close()
        return user
