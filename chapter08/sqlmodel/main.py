from sqlmodel import Field, Session, SQLModel, create_engine, select

engine = create_engine("sqlite:///database.db", echo=False)


class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str


SQLModel.metadata.create_all(engine)

user1 = Users(name="John", email="john@example.com", password="password")

user2 = Users(name="Jane", email="jane@example.com", password="password")


def add_user():
    with Session(engine) as session:
        session.add(user1)
        session.add(user2)
        session.commit()


def select_user():
    with Session(engine) as session:
        allusers = select(Users)

        results = session.exec(allusers)
        for user in results:
            print(user)


add_user()
select_user()
