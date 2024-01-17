from pydantic import BaseModel, Field
import constants


class NewRecipesData(BaseModel):
    title: str = Field(min_length=3, examples=["Recipe name"])
    cover: str
    tags: list[constants.TypesOfRecipes] = []
    description: str = None


class SavedRecipe(NewRecipesData):
    uuid: str = Field(examples=["9a7d8328-542d-437a-9ccb-fcff0eddd3b0"])