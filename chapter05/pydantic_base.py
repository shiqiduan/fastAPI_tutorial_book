from datetime import date
from typing import List, Optional
from pydantic import (
    BaseModel,
    DirectoryPath,
    EmailStr,
    Field,
    FilePath,
    HttpUrl,
    IPvAnyAddress,
    Json,
    NameEmail,
    SecretBytes,
    SecretStr,
    field_validator,
    validator,
)


class Card(BaseModel):
    nums: str

    @field_validator("nums")
    def nums_rule(cls, nums):
        if len(nums) != 7:
            raise ValueError("长度不符合")
        return nums


class Person(BaseModel):
    name: str = Field(
        ...,
        title="姓名",
        description="长度大于 12",
        max_length=12,
        min_length=6,
        example="FooFooF",
    )
    age: Optional[int]
    enable: bool
    hobby: list
    address: dict
    birthday: date
    cards: Optional[List[Card]]

    # filePath: FilePath
    # dirPath: DirectoryPath
    # ip: IPvAnyAddress
    # email: EmailStr
    # nameEmail: NameEmail
    # secretStr: SecretStr
    # secretBytes: SecretBytes
    # website: HttpUrl
    # json_obj: Json


if __name__ == "__main__":
    person = Person(
        name="张三1235",
        age=18,
        enable=True,
        hobby=["篮球", "足球"],
        address={"province": "河北省", "city": "石家庄市"},
        birthday="2020-01-01",
        cards=[Card(nums="1234567")],
    )
    print(person.model_dump_json())

    new_person = person.model_copy(deep=True)

    person.cards[0].nums = "8888888"

    print("pid", person, id(person))
    print("new pid", new_person, id(new_person))
