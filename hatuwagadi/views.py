from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django_tables2 import SingleTableView
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
from plotly.offline import plot
from plotly.graph_objs import Bar, Pie
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine
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
    
from .tables import AccessToRoadnetworkTable


class HomePageView(TemplateView):
    template_name = 'index.html'


def AccessToRoadnetworkView(request):
    queryset = AccessToRoadnetwork.objects.all()
    
    alchemyEngine = create_engine('postgresql://postgres:PostGRE@127.0.0.1:5432/hatuwagadi')
    conn = alchemyEngine.connect()
    # conn = psycopg2.connect(database='hatuwagadi', user="postgres", password="PostGRE", host="127.0.0.1", port="5432")
    query1 = "select * from access_to_roadnetwork;"
    df1 = pd.read_sql_query(query1,con=conn)
    layout = go.Layout(barmode='group')
    # config = {'displayModeBar': False}
    config = {'displaylogo': False}
    fig1 = plot(px.bar(df1, x='road_infrastructure', y='road_infrastructure_condition',
           title='सडक सञ्जालमा पहुँच'), output_type='div', config=config, image_height=100)    
    # fig1 = plot(px.pie(df1, values='road_infrastructure', names='road_infrastructure_condition',title='सडक सञ्जालमा पहुँच', height=300),output_type='div', config=config)
    # fig1 = px.pie(df1, values='road_infrastructure', names='road_infrastructure_condition',title='सडक सञ्जालमा पहुँच', height=300)
    # piechart = fig1.to_html(full_html=False, include_plotlyjs=False)
    conn.close()    
    return render(request, "hatuwagadi/accesstoroadnetwork.html", context={'queryset':queryset, "fig1": fig1})    
    

def AgriLivstkCooperativesView(request):
    queryset = AgriLivstkCooperatives.objects.all()
    
    # alchemyEngine = create_engine('postgresql://postgres:PostGRE@127.0.0.1:5432/hatuwagadi')
    # conn = alchemyEngine.connect()
    # # conn = psycopg2.connect(database='hatuwagadi', user="postgres", password="PostGRE", host="127.0.0.1", port="5432")
    # query1 = "select * from agri_livstk_cooperatives;"
    # df1 = pd.read_sql_query(query1,con=conn)
    # layout = go.Layout(barmode='group')
    # # config = {'displayModeBar': False}
    # config = {'displaylogo': False}
    # fig1 = plot(px.bar(df1, x='road_infrastructure', y='road_infrastructure_condition',
    #        title='सडक सञ्जालमा पहुँच'), output_type='div', config=config, image_height=100)    
    # # fig1 = plot(px.pie(df1, values='road_infrastructure', names='road_infrastructure_condition',title='सडक सञ्जालमा पहुँच', height=300),output_type='div', config=config)
    # # fig1 = px.pie(df1, values='road_infrastructure', names='road_infrastructure_condition',title='सडक सञ्जालमा पहुँच', height=300)
    # # piechart = fig1.to_html(full_html=False, include_plotlyjs=False)
    # conn.close()    
    return render(request, "hatuwagadi/agrilivstkcooperative.html", context={'queryset':queryset})  
    
        
def AnimalHusbandryFirmsView(request):
    queryset = AnimalHusbandryFirms.objects.all()
    
    alchemyEngine = create_engine('postgresql://postgres:PostGRE@127.0.0.1:5432/hatuwagadi')
    conn = alchemyEngine.connect()
    # conn = psycopg2.connect(database='hatuwagadi', user="postgres", password="PostGRE", host="127.0.0.1", port="5432")
    query1 = "select * from animal_husbandry_firms;"
    df1 = pd.read_sql_query(query1,con=conn)
    layout = go.Layout(barmode='group')
    # config = {'displayModeBar': False}
    config = {'displaylogo': False}
    fig1 = plot(px.bar(df1, x='products', y='amount_produced',
           title='आधुनिक पशुपालन (फार्म) सम्बन्धी विवरण'), output_type='div', config=config, image_height=100)    
    # fig1 = plot(px.pie(df1, values='road_infrastructure', names='road_infrastructure_condition',title='सडक सञ्जालमा पहुँच', height=300),output_type='div', config=config)
    # fig1 = px.pie(df1, values='road_infrastructure', names='road_infrastructure_condition',title='सडक सञ्जालमा पहुँच', height=300)
    # piechart = fig1.to_html(full_html=False, include_plotlyjs=False)
    conn.close()    
    return render(request, "hatuwagadi/animalhusbandryfirms.html", context={'queryset':queryset, "fig1": fig1})   

