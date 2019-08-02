from FTV.Objects.Feature import Feature


class FeaturesManager:
    next_id = 0

    def __init__(self, *args: Feature):
        self.features = {}

    def add(self, feature: Feature, id_number: int):
        if feature.enabled:
            self.features[id_number] = feature
            self.next_id += 1

    def add_multiple(self, *args: Feature):
        for feature in args:
            self.add(feature, self.next_id)

    def get(self, index) -> Feature:
        return self.features[index]
