from AppPackage.Experiments.Examples.BackgroundLoadingApp.Features.SubFeaturesLoader.AbstractFeature import \
    AbstractFeature


class Feature2(AbstractFeature):
    def setupSettings(self):
        pass
        # self.settings.setDisabled()

    def setupManagers(self):
        pass

    def setupFeatures(self):
        from AppPackage.Experiments.Examples.BackgroundLoadingApp.Features.SubFeaturesLoader.SubFeature2.Feature2_1 import \
            Feature2_1
        from AppPackage.Experiments.Examples.BackgroundLoadingApp.Features.SubFeaturesLoader.SubFeature2.Feature2_2 import \
            Feature2_2
        from AppPackage.Experiments.Examples.BackgroundLoadingApp.Features.SubFeaturesLoader.SubFeature2.Feature2_3 import \
            Feature2_3
        from AppPackage.Experiments.Examples.BackgroundLoadingApp.Features.SubFeaturesLoader.SubFeature2.Feature2_4 import \
            Feature2_4

        self.addFeatures(
            Feature2_1,
            Feature2_2,
            Feature2_3,
            Feature2_4
        )
