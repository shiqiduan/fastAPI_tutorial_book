class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"


import asyncio


async def test_run():
    user = User(id=1, name="John")
    print(str(user))


asyncio.run(test_run())
