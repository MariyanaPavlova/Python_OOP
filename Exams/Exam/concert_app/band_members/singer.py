from project.band_members.musician import Musician


class Singer(Musician):


    def __init__(self, name, age):
        super().__init__(name, age)
        self. valid_skills = ["sing high pitch notes", "sing low pitch notes"]
        self.skills = []

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.valid_skills:
            raise ValueError(f"{new_skill} is not a needed skill!")
        elif new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        elif new_skill in self.valid_skills and new_skill not in self.skills:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."