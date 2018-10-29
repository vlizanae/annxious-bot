from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from datetime import datetime

from config import psql_user, psql_pass
from .models import UserModelMixin, NetworkModelMixin


class Database:
    def __init__(self, session=False):
        self.engine = create_engine(
            'postgresql+psycopg2://{}:{}@localhost/annxious'
            .format(psql_user, psql_pass)
        )
        if session:
            self.session = sessionmaker(bind=self.engine)()

        self.User = None
        self.create_schema(commit=False)

    def create_schema(self, commit=True):
        Base = declarative_base()

        # Models
        class User(Base, UserModelMixin):
            pass
        self.User = User

        class Network(Base, NetworkModelMixin):
            pass
        self.Network = Network


        if commit:
            Base.metadata.create_all(self.engine)

    def drop_all(self):
        meta = MetaData(bind=self.engine)
        meta.reflect()
        meta.drop_all()

    def add_user(self, id, name):
        try:
            self.session.add(
                self.User(name=name, conversation_id=id)
            )
            self.session.commit()
        except Exception:
            self.session.rollback()

    def get_user(self, id):
        user = None
        try:
            user = (
                self.session.query(self.User)
                .filter(self.User.conversation_id == id)
                .one()
            )
        except:
            self.session.rollback()
        return user

    def add_network(self, user_cid, name):
        user = self.get_user(user_cid)
        try:
            self.session.add(
                self.Network(
                    user_id=user.id,
                    name=name,
                    created=datetime.now(),
                    epoch=-1
                )
            )
            self.session.commit()
        except Exception:
            self.session.rollback()

    def remove_network(self, id):
        try:
            network = (
                self.session.query(self.Network)
                .filter(self.Network.id == id)
                .one()
            )
            self.session.delete(network)
        except:
            self.session.rollback()

    def get_network(self, name):
        network = None
        try:
            network = (
                self.session.query(self.Network)
                .filter(self.Network.name == name)
                .one()
            )
        except:
            self.session.rollback()
        return network

    def update_network(self, **kwargs):
        try:
            network = self.get_network(kwargs['network_id'])
            network.epoch = kwargs['epoch']

            network.train_loss = kwargs['loss']
            if kwargs['epoch'] == 0 or kwargs['loss'] < network.best_train_loss:
                network.best_train_loss = kwargs['loss']
                network.best_train_epoch = kwargs['epoch']

            if 'val_loss' in kwargs.keys():
                network.val_loss = kwargs['val_loss']
                if kwargs['epoch'] == 0 or kwargs['val_loss'] < network.best_val_loss:
                    network.best_val_loss = kwargs['val_loss']
                    network.best_val_epoch = kwargs['epoch']

            self.session.commit()
        except:
            self.session.rollback()

    def deactivate_network(self, id):
        try:
            network = self.get_network(id)
            network.active = False
            network.train_ended = datetime.now()
            self.session.commit()
        except:
            self.session.rollback()

    def get_user_networks(self, id):
        models = []
        try:
            user = self.get_user(id)
            models = [
                network for network in user.model_set.filter(self.Network.active)
            ]
        except:
            self.session.rollback()
        return models