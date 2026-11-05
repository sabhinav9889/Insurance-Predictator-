from pydantic import BaseModel, Field, computed_field
from typing import Annotated
from configs.constants import tier_1_cities, tier_2_cities, jobs


class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=150, description='Age of the user')]
    weight: Annotated[float, Field(..., gt=0, lt=200, description='Weight of the user')]
    height: Annotated[float, Field(..., gt=0, lt=250, description='Height of the user')]
    income_lpa: Annotated[float, Field(..., gt=0, description='Income of the user in LPA')]
    smoker: Annotated[bool, Field(..., description='Is user smoke ?')]
    city: Annotated[str, Field(..., description='The city of the user')]
    occupation: Annotated[jobs, Field(..., description='The occupation of the user')]

    @computed_field
    @property
    def bmi(self)->float:
        return round(self.weight/(self.height**2), 2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
