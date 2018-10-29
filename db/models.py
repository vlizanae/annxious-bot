from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr


class UserModelMixin:
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, unique=True)
    name = Column(String(32))

    @declared_attr
    def model_set(self):
        return relationship(
            'Network',
            order_by='Network.id',
            back_populates='user',
            cascade='all, delete, delete-orphan',
            lazy='dynamic'
        )

    def __repr__(self):
        return self.name


class NetworkModelMixin:
    __tablename__ = 'model'

    id = Column(Integer, primary_key=True)

    @declared_attr
    def user_id(self):
        return Column(Integer, ForeignKey('user.id'))

    name = Column(String(64), unique=True)
    created = Column(DateTime)
    train_ended = Column(DateTime, nullable=True)
    active = Column(Boolean, default=True)

    epoch = Column(Integer)
    train_loss = Column(Float, nullable=True)
    val_loss = Column(Float, nullable=True)

    best_train_epoch = Column(Integer, nullable=True)
    best_train_loss = Column(Float, nullable=True)
    best_val_epoch = Column(Integer, nullable=True)
    best_val_loss = Column(Float, nullable=True)

    @declared_attr
    def user(self):
        return relationship('User', back_populates='model_set')

    def __repr__(self):
        return self.name