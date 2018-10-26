from sqlalchemy import Column, Integer, String


class UserModelMixin:
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, unique=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name