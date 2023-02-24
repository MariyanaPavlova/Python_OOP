from project.band_members.musician import Musician


class Drummer(Musician):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.valid_skills = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]
        self.skills = []

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.valid_skills:
            raise ValueError(f"{new_skill} is not a needed skill!")
        elif new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        elif new_skill in self.valid_skills and new_skill not in self.skills:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."