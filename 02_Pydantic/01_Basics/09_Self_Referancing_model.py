from pydantic import BaseModel, Field
from typing import Optional,List

class User(BaseModel):
    id: int
    name: str
    friends: Optional['User'] = None

user = User(
    id=1,
    name="Xitij"
)

user.friends = User(id=2, name="Aman")
print(user.model_dump_json())

# example 2
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()

comment = Comment(
    id=1,
    content="Great post!",
    replies=[
        Comment(id=2, content="Thanks for the comment!"),
        Comment(id=3, content="I agree!",replies=[
            Comment(id=1, content='nested reply')
        ])
    ]
)

print(comment.model_dump_json())