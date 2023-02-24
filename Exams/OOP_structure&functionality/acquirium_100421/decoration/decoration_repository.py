from acquirium_100421.decoration.base_decoration import BaseDecoration

class DecorationRepository:
    def __init__(self):
        self.decorations = []   #decorat. obj

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration
