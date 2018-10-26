from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from secret import psql_user, psql_pass
from .models import UserModelMixin


class Database:
    def __init__(self, session=False):
        self.engine = create_engine(
            'postgresql+psycopg2://{}:{}@localhost/annxious'
            .format(psql_user, psql_pass)
        )
        self.User = None
        self.session = None
        if session:
            self.start_session()

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

    def start_session(self):
        self.create_schema(commit=False)
        self.session = sessionmaker(bind=self.engine)()

    def close_session(self):
        self.session.close()

    def add_user(self, name):
        assert self.session is not None
        self.session.add(self.User(name=name))
        self.session.commit()

    def get_user(self, id):
        assert self.session is not None
        return (
            self.session.query(self.User)
                .filter(self.User.id == id)
                .one()
        )