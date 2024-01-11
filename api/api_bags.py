from fastapi import APIRouter
from pydantic import BaseModel, Field
import constants

router = APIRouter(
    prefix='/api/bags',
    tags=['API', 'Bags']
)


class NewBagData(BaseModel):
    title: str = Field(min_length=3, examples=['Plush bag'])
    color: str = Field(min_length=3, examples=['Red'])
    price: float = Field(default=0.1, gt=0.0, examples=[500])
    cover: str
    tags: list[constants.Gender] = []
    description: str = None


@router.post('/create')
def create_bag(bag: NewBagData) -> NewBagData:
    return bag


@router.get('/')
def get_bags() -> list[dict]:
    return [{'title': 'Bags', 'price': 100}]


@router.get('/')
def get_bags_by_title() -> list[dict]:
    pass


@router.put('/update/{bag_id}')
def update_bag():
    pass


@router.delete('/delete/{bag_id}')
def delete_bag():
    pass