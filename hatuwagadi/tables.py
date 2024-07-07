import django_tables2 as tables
from .models import AccessToRoadnetwork, AgriLivstkCooperatives,\
    AnimalHusbandryFirms,AnimalProducts,AvailabilityOfIrrigationFacilities,\
    BuildingSlumHousingForUnderprivileged, CitizenAwarenessVillageDevelpmtOrg,\
    CommunityInstitutionDetails, DeadFamilyMembers,DescriptionOfBridges,\
    DescriptionOfCommunityForests,DescriptionOfDiseaseTreatment,\
    DescriptionOfGovernmentBuilding,DetailsOfNgo,DisasterManagement,\
    EnvironmentAndHygiene,FarmersEntrepreneursAndSavingsGroups,\
    FinancialInstutionsDetails,ForestDescription,ForestInLocalLevel,\
    ForestryAndEnvironment, GenderEqualtiyNSocialInclusion,\
    GhattaMillsAndCollectionProcessingCenters, GovernmentOfficesAndAgencies,\
    HealthNNutritionInformation,HotelsLodgesResturantsHomestay,HrRelatedToAgricultureAndAnimalHusbandry,\
    InvestmentInformation, LandUseCondition, LoanInformation, MajorFestivalsAndFairs, MappingOfNaturalResources,\
    MotherWomenGroupAndTraditionalGroup, NaturalCalamity,PersonalEventDetails, ProjectsOfPride,\
    PublicAndCommunityBuildings, PublicPondsAndFisheries, PublicServiceDelivery, Roadways,\
    SavingsInformation, SocialSecurityProgramDetails, SolidWasteManagement, SourceOfAirPollution,YearlyCultivation

class AccessToRoadnetworkTable(tables.Table):
    class Meta:
        model = AccessToRoadnetwork
        template_name = "django_tables2/bootstrap.html"
        