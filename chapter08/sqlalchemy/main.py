from sqlalchemy import Integer, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:")

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    nikename = Column(String)
    password = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, nikename={self.nikename}, password={self.password}, email={self.email})>"


Base.metadata.create_all(engine, checkfirst=True)

session = sessionmaker(bind=engine)
session = session()


def add_user():
    for x in range(10):
        _user = User(name=f"a{x}", nikename=f"a{x}", password=f"a{x}", email=f"a{x}")
        session.add(_user)
    session.commit()


def find_user():
    ret = session.query(User).filter(User.name.like("a%")).all()
    for item in ret:
        print(item)


def update_user():
    update = session.query(User).filter(User.id == 1).first()
    update.name = "new_name"
    session.commit()


def delete_user():
    delete = session.query(User).filter(User.id == 2).first()
    if delete:
        session.delete(delete)
        session.commit()


def select_all():
    users = session.query(User).all()
    for user in users:
        print(user)


add_user()
select_all()
print()
find_user()
print()
update_user()
select_all()
print()
delete_user()
select_all()
session.close()
