---
output:
  bookdown::pdf_document2:
    latex_engine: xelatex
    toc: true
    toc_depth: 3
    number_sections: true
    fig_caption: true
    keep_md: true
    documentclass: report
    self_contained: true
author:  
- Air Force Civil Engineering Center (AFCEC)
- Geospatial Integration Office (GIO)
- Installation Geospatial Support (IGS)
params: 
    set_title: "My Title!"
date: "14 May, 2018"
link-citations: true
header-includes:
  - \usepackage {hyperref}
  - \hypersetup{linktocpage}
  - \hypersetup {colorlinks = true,linkcolor = blue, urlcolor = blue}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \usepackage{array}
  - \usepackage{multirow}
  - \usepackage[table]{xcolor}
  - \usepackage{wrapfig}
  - \usepackage{float}
  - \usepackage{colortbl}
  - \usepackage{pdflscape}
  - \usepackage{tabu}
  - \usepackage{threeparttable}
  - \usepackage[normalem]{ulem}
---

---
title: YoungstownJointARS_CIP Missing Data Report
---







\pagebreak


# Report Overview
The purpose of this report is to give  an overview of data missing from YoungstownJointARS_CIP's geodatabase when compared with the Air Force (AF) SDSFIE 3.101 geodatabase schema.

**The template geodatabase used for this report is the Full AF SDSFIE 3.101 geodatabase.**

A summary of findings may be found in Section \@ref(summary).

Upon receiving YoungstownJointARS_CIP's geodatabase, standard Feature Classes were migrated to standard Feature Datasets to match the Full AF SDSFIE 3.101 geodatabase, where required.  

This report first lists which AF SDSFIE standard Feature Datasets are missing from YoungstownJointARS_CIP's geodatabase in comparison with the Full geodatabase schema. This data can be found in the  Section \@ref(missFDS).

Then, for each of the AF SDSFIE standard Feature Datasets in the Full geodatabase schema that are included in YoungstownJointARS_CIP's geodatabase, this report lists which AF SDSFIE standard Feature Classes are missing from those Feature Datasets (Sections \@ref(missFCFDS) - \@ref(missFC)). Section \@ref(missFLDincFC) continues to identify the counts of Missing Fields per standard Feature Classes included. Of the included Feature Classes, empty Feature Classes are listed in the 'Empty Feature Classes' section (Section \@ref(emptFC)).  Further, Section \@ref(emptFLDneFC) identifies the counts of empty fields from non-empty, standard Feature Classes included in YoungstownJointARS_CIP's geodatabase.

Then, for each of the AF SDSFIE standard Feature Dataset/Feature Class combinations from Full schema that are included in YoungstownJointARS_CIP's geodatabase, this report then analyzes each AF SDSFIE standard Feature Class within YoungstownJointARS_CIP's geodatabase for indeterminant data at the Attribute level (Section \@ref(detindtVal)). For the purposes of this report, any data classified as 'Null', 'To be determined' (TBD), or 'Other' is considered 'indeterminant.' Section \@ref(pctindtFC) gives an overview of the percent of Attribute Table cells identified as 'Null', 'TBD', and 'Other' per Feature Class. The specific values that comprise 'Null', 'TBD', and 'Other' data are explicated in Sections \@ref(nullCnt), \@ref(tbdCnt), and \@ref(otherCnt), respectively, which give the counts of these indeterminent values by Feature Dataset and Feature Class within its subsections.

Finally, this report identifies noted discrepencies between the target Full schema and YoungstownJointARS_CIP's geodatabase (Section \@ref(diff)) for  (1) Fields with Incorrectly Populated Domains (Section \@ref(diffIncDom)) and (2) Fields Included in YoungstownJointARS_CIP's Geodatabase Not in the Full schema (Section \@ref(diffFLD)).

The data utilized to produce this report may be found within YoungstownJointARS_CIP's geodatabase in tables prepended with 'Full' (e.g.: 'Full_MissingData'). Specific references to these tables are found throughout the report where further details may be warranted.

\pagebreak

# Summary of Findings {#summary}
1. **22** : Total Number of Missing Feature Datasets   
2. **272** : Total Number of Missing Feature Classes within included Feature Datasets  
3. **12 **: Total Number of Empty Feature Classes within included Feature Datasets  
4. **451** : Total Number of Empty Fields from Empty Feature Classes  
5. **0** : Total Number of Empty Fields from non-Empty Feature Classes   
6. 67,136/140,864 **(47.66%)**: Total number of cells are populated with determinant data (i.e.: **not** 'Null', 'TBD', or 'Other')

7. 73,728/140,864 **(52.34%)**: Total number of cells are missing data (i.e.: 'Null', 'TBD', or 'Other')

    + 72,732/140,864 **(51.63%)**: Total number of cells are 'Null' data  
    
    + 914/140,864 **(0.65%)**: Total number of cells are 'TBD' data  
    
    + 82/140,864 **(0.06%)**: Total number of cells are 'Other' data    
8. **24** : Total Number of Fields with Incorrectly Populated Domains (within included standard Feature Classes)  
9. **0** : Total Number of Fields Included in YoungstownJointARS_CIP's Geodatabase **Not** Included in the Full Schema (within included standard Feature Classes)  


\pagebreak



# Missing Feature Datasets {#missFDS}
This section provides an overview of the AF SDSFIE standard Feature Datasets in the Full schema that are not also included in YoungstownJointARS_CIP's geodatabase. If YoungstownJointARS_CIP's geodatabase was delivered to AFCEC without Feature Datasets, 'loose' standard Feature Classes were first migrated to the respective Feature Dataset according to AF SDSFIE 3.101 standards.

Overall, YoungstownJointARS_CIP has 22 missing AF SDSFIE standard Feature Datasets.  

Please see Table \@ref(tab:cmissFDS) below for a complete listing of the AF SDSFIE standard Feature Datasets  missing from YoungstownJointARS_CIP's geodatabase, where applicable.  This information is also found in YoungstownJointARS_CIP's geodatabase under the 'Full_MissingFDS' table.


\rowcolors{2}{gray!6}{white}
\begin{table}[!h]

\caption{(\#tab:cmissFDS)Missing Feature Datasets}
\centering
\begin{tabular}{l}
\hiderowcolors
\toprule
FDS\\
\midrule
\showrowcolors
Emergency\\
environmentalAirQuality\\
environmentalHazMat\\
environmentalHazWaste\\
environmentalIntegratedSolidWaste\\
environmentalStorageTanks\\
environmentalWaterQuality\\
GeneralMisc\\
Geodetic\\
Landform\\
MissileField\\
SpaceUtilization\\
ULUC2\\
utilitiesElectrical\\
utilitiesFuels\\
utilitiesGas\\
utilitiesMisc\\
utilitiesSewer\\
utilitiesStormwater\\
utilitiesThermal\\
utilitiesWater\\
WaterControl\\
\bottomrule
\multicolumn{1}{l}{\textbf{Note: } }\\
\multicolumn{1}{l}{22 Total Missing Feature Datasets}\\
\end{tabular}
\end{table}
\rowcolors{2}{white}{white}



# Missing and Empty Feature Classes {#miss-empFC}
## Missing Feature Classes by Feature Dataset {#missFCFDS}
Of the required Feature Datasets within the Full schema included in YoungstownJointARS_CIP's geodatabase, 272 of the standard Feature Classes are not present. Table \@ref(tab:cmissFCFDS) below gives the count of missing Feature Classes per Feature Dataset, sorted in ascending order, where applicable.  


\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}cc}
\caption{(\#tab:cmissFCFDS)Missing Feature Classes by Feature Dataset}\\
\hiderowcolors
\toprule
FDS & Missing\_FC\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cmissFCFDS)Missing Feature Classes by Feature Dataset \textit{(continued)}}\\
\toprule
FDS & Missing\_FC\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{2}{l}{\textbf{Note: } }\\
\multicolumn{2}{l}{272 Total Missing Feature Classes}\\
\endlastfoot
\showrowcolors
Pavements & 5\\
RealProperty & 7\\
Security & 7\\
Cadastre & 8\\
Auditory & 9\\
environmentalRestoration & 9\\
Planning & 16\\
environmentalCulturalResources & 20\\
Transportation & 28\\
Recreation & 29\\
MilitaryRangeTraining & 37\\
WaterWays & 48\\
environmentalNaturalResources & 49\\*
\end{longtable}
\rowcolors{2}{white}{white}



## Missing Feature Classes {#missFC}
Of the required Feature Datasets within the Full schema included in YoungstownJointARS_CIP's geodatabase, 272 of the required Feature Classes are not present. Table \@ref(tab:cmissFC) below gives a listing of all the Feature Classes missing, along with the associated Feature Dataset, where applicable. This information is also found in YoungstownJointARS_CIP's geodatabase under the 'Full_MissingFCs' table.  


\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}cc}
\caption{(\#tab:cmissFC)Missing Feature Classes}\\
\hiderowcolors
\toprule
FDS & FC\_MISSING\\
\midrule
\endfirsthead
\caption[]{(\#tab:cmissFC)Missing Feature Classes \textit{(continued)}}\\
\toprule
FDS & FC\_MISSING\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{2}{l}{\textbf{Note: } }\\
\multicolumn{2}{l}{272 Total Missing Feature Classes}\\
\endlastfoot
\showrowcolors
Auditory & MilFlightTrack\_L\\
Auditory & NoiseAbatementFeature\_A\\
Auditory & NoiseAbatementFeature\_L\\
Auditory & NoiseAbatementFeature\_P\\
Auditory & NoiseIncident\_P\\
Auditory & NoiseReceiver\_P\\
Auditory & NoiseSource\_L\\
Auditory & NoiseSource\_P\\
Auditory & NoiseZone\_L\\
Cadastre & Disposal\_A\\
Cadastre & DisposalRODParcel\_A\\
Cadastre & DoDFormerlyUsedDefense\_A\\
Cadastre & DoDFormerlyUsedDefense\_P\\
Cadastre & ExternalPropertyInterest\_A\\
Cadastre & ExternalPropertyInterest\_P\\
Cadastre & Installation\_P\\
Cadastre & Outgrant\_P\\
environmentalCulturalResources & ArchaeologicalSite\_A\\
environmentalCulturalResources & ArchaeologicalSite\_L\\
environmentalCulturalResources & ArchaeologicalSite\_P\\
environmentalCulturalResources & CemeteryOrBurialSite\_A\\
environmentalCulturalResources & CemeteryOrBurialSite\_P\\
environmentalCulturalResources & CulResPotentialArea\_A\\
environmentalCulturalResources & CulRestrictedAccess\_A\\
environmentalCulturalResources & CulSurveyArea\_A\\
environmentalCulturalResources & HistoricBuilding\_A\\
environmentalCulturalResources & HistoricBuilding\_P\\
environmentalCulturalResources & HistoricLandscape\_A\\
environmentalCulturalResources & HistoricObject\_A\\
environmentalCulturalResources & HistoricObject\_P\\
environmentalCulturalResources & NativeAffiliation\_A\\
environmentalCulturalResources & SacredSite\_A\\
environmentalCulturalResources & SacredSite\_L\\
environmentalCulturalResources & SacredSite\_P\\
environmentalCulturalResources & TraditionalCulRes\_A\\
environmentalCulturalResources & TraditionalCulRes\_L\\
environmentalCulturalResources & TraditionalCulRes\_P\\
environmentalNaturalResources & AgriculturalTract\_A\\
environmentalNaturalResources & CoastalZoneMgtArea\_A\\
environmentalNaturalResources & DispersedRecArea\_A\\
environmentalNaturalResources & EssentialFishHabitat\_A\\
environmentalNaturalResources & FaunaIncidentPoint\_P\\
environmentalNaturalResources & FireArea\_A\\
environmentalNaturalResources & FireBreakLine\_L\\
environmentalNaturalResources & FloodPlainArea\_A\\
environmentalNaturalResources & ForestCompartment\_A\\
environmentalNaturalResources & ForestMgtArea\_A\\
environmentalNaturalResources & ForestProductHarvest\_A\\
environmentalNaturalResources & ForestStand\_A\\
environmentalNaturalResources & FuelBreakLine\_L\\
environmentalNaturalResources & FuelMgtArea\_A\\
environmentalNaturalResources & HabitatProtectiveZone\_A\\
environmentalNaturalResources & HazSuppressionArea\_A\\
environmentalNaturalResources & HistoricRiverAlignment\_L\\
environmentalNaturalResources & LandCover\_A\\
environmentalNaturalResources & NatResRecFeature\_P\\
environmentalNaturalResources & NatResRestReclProj\_A\\
environmentalNaturalResources & NatResRestReclProj\_P\\
environmentalNaturalResources & NatResSurvey\_A\\
environmentalNaturalResources & NatResSurvey\_L\\
environmentalNaturalResources & NatResSurvey\_P\\
environmentalNaturalResources & NoxiousOrInvasiveSpecies\_A\\
environmentalNaturalResources & NoxiousOrInvasiveSpecies\_L\\
environmentalNaturalResources & NoxiousOrInvasiveSpecies\_P\\
environmentalNaturalResources & PrescribedBurnUnit\_A\\
environmentalNaturalResources & RecNatureTrail\_L\\
environmentalNaturalResources & SoilSurveyArea\_A\\
environmentalNaturalResources & SpecialMgtArea\_A\\
environmentalNaturalResources & SpecialStatusSpecies\_A\\
environmentalNaturalResources & SpecialStatusSpecies\_L\\
environmentalNaturalResources & SpecialStatusSpecies\_P\\
environmentalNaturalResources & SpeciesArea\_A\\
environmentalNaturalResources & SpeciesPoint\_P\\
environmentalNaturalResources & SpeciesSpecificHabitat\_A\\
environmentalNaturalResources & SpeciesSpecificHabitat\_L\\
environmentalNaturalResources & SpeciesSpecificHabitat\_P\\
environmentalNaturalResources & SurfaceRiparianArea\_A\\
environmentalNaturalResources & Vegetation\_A\\
environmentalNaturalResources & WaterBody\_A\\
environmentalNaturalResources & WatercourseLine\_L\\
environmentalNaturalResources & WaterFeature\_A\\
environmentalNaturalResources & Watershed\_A\\
environmentalNaturalResources & Wetland\_L\\
environmentalNaturalResources & Wetland\_P\\
environmentalNaturalResources & WildlandUrbanInterfaceArea\_A\\
environmentalNaturalResources & WildlifeMgtArea\_A\\
environmentalRestoration & EnvOperableUnit\_A\\
environmentalRestoration & EnvRemediationArea\_A\\
environmentalRestoration & EnvRestorSampLoc\_P\\
environmentalRestoration & LandUseControl\_A\\
environmentalRestoration & PollutionArea\_A\\
environmentalRestoration & PotentialEnvSite\_A\\
environmentalRestoration & RestTreatmentSysComp\_L\\
environmentalRestoration & RestTreatmentSysComp\_P\\
environmentalRestoration & RestTreatmentSystem\_A\\
MilitaryRangeTraining & AirfieldLighting\_P\\
MilitaryRangeTraining & AmmunitionStorage\_A\\
MilitaryRangeTraining & FiringSite\_A\\
MilitaryRangeTraining & FiringSite\_L\\
MilitaryRangeTraining & FiringSite\_P\\
MilitaryRangeTraining & ImpactArea\_P\\
MilitaryRangeTraining & MilDropZone\_A\\
MilitaryRangeTraining & MilDropZone\_P\\
MilitaryRangeTraining & MilLandingZone\_A\\
MilitaryRangeTraining & MilLandingZone\_P\\
MilitaryRangeTraining & MilLocalFlying\_A\\
MilitaryRangeTraining & MilObsvPosition\_A\\
MilitaryRangeTraining & MilObsvPosition\_P\\
MilitaryRangeTraining & MilQuantityDistArc\_A\\
MilitaryRangeTraining & MilRange\_P\\
MilitaryRangeTraining & MilRangeEquipment\_P\\
MilitaryRangeTraining & MilRangeLighting\_P\\
MilitaryRangeTraining & MilSpecialUseAirSpace\_A\\
MilitaryRangeTraining & MilTarget\_A\\
MilitaryRangeTraining & MilTarget\_L\\
MilitaryRangeTraining & MilTarget\_P\\
MilitaryRangeTraining & MilTrainingLoc\_L\\
MilitaryRangeTraining & MilTrainingLoc\_P\\
MilitaryRangeTraining & MilTrainingRoute\_A\\
MilitaryRangeTraining & MilTrainingRoute\_L\\
MilitaryRangeTraining & MilTrainingRoute\_P\\
MilitaryRangeTraining & MunitionsStorage\_A\\
MilitaryRangeTraining & MunitionsStorage\_P\\
MilitaryRangeTraining & MunitionWasteDisposal\_A\\
MilitaryRangeTraining & RadarEquipment\_A\\
MilitaryRangeTraining & RadarEquipment\_P\\
MilitaryRangeTraining & RangeControllerPosition\_P\\
MilitaryRangeTraining & SmallArmsRangeDangerZone\_A\\
MilitaryRangeTraining & SpecialOperatingProcedure\_A\\
MilitaryRangeTraining & SpecialOperatingProcedure\_L\\
MilitaryRangeTraining & SpecialOperatingProcedure\_P\\
MilitaryRangeTraining & SurfaceDangerZone\_A\\
Pavements & PavementLinearStructure\_A\\
Pavements & PavementPhoto\_P\\
Pavements & PavementSampleUnit\_A\\
Pavements & PavementSlab\_A\\
Pavements & PavementTest\_P\\
Planning & AdministrativeBoundary\_A\\
Planning & AirfieldFrangibleZone\_A\\
Planning & AirfieldImaginarySurface\_A\\
Planning & AirfieldObst\_P\\
Planning & AssetUseOpportunities\_A\\
Planning & EncroachmentMgtAction\_P\\
Planning & FutureProjects\_A\\
Planning & FutureProjects\_P\\
Planning & FutureProjectsLandUse\_A\\
Planning & IncompatibleLandUse\_A\\
Planning & LandMgtZone\_A\\
Planning & LegacyBuildingHazard\_A\\
Planning & NatResAcquisitionBoundary\_A\\
Planning & SpeciesHazard\_A\\
Planning & SpeciesHazardIncident\_P\\
Planning & StandoffDistArc\_A\\
RealProperty & Building\_P\\
RealProperty & FlagPole\_P\\
RealProperty & Roof\_A\\
RealProperty & Structure\_A\\
RealProperty & Structure\_L\\
RealProperty & Structure\_P\\
RealProperty & Tower\_A\\
Recreation & BoatRamp\_P\\
Recreation & Campground\_A\\
Recreation & Campground\_P\\
Recreation & Campsite\_A\\
Recreation & Campsite\_P\\
Recreation & FeeCollection\_A\\
Recreation & FeeCollection\_P\\
Recreation & FishHatchery\_A\\
Recreation & FishHatchery\_P\\
Recreation & FishHaven\_A\\
Recreation & FishHaven\_P\\
Recreation & FishingLoc\_A\\
Recreation & FishingLoc\_P\\
Recreation & GolfCourseFeature\_A\\
Recreation & GolfCourseFeature\_L\\
Recreation & GolfCourseFeature\_P\\
Recreation & GroundsMaintenance\_A\\
Recreation & GroundsMaintenance\_L\\
Recreation & ObsvLocation\_A\\
Recreation & ObsvLocation\_P\\
Recreation & Playground\_A\\
Recreation & Playground\_P\\
Recreation & RecArea\_P\\
Recreation & RecFeature\_A\\
Recreation & RecFeature\_P\\
Recreation & RecFirearmsRange\_A\\
Recreation & RecFirearmsRange\_P\\
Recreation & RecTrail\_L\\
Recreation & RecTrailFeature\_P\\
Security & AccessControl\_A\\
Security & Barricade\_A\\
Security & Barricade\_L\\
Security & Barricade\_P\\
Security & RestrictedArea\_A\\
Security & SectorZone\_A\\
Security & TransitionPoint\_P\\
Transportation & AircraftParking\_P\\
Transportation & AirfieldSurface\_A\\
Transportation & AirfieldSurface\_L\\
Transportation & Bridge\_P\\
Transportation & Guardrail\_L\\
Transportation & NavigationalAid\_P\\
Transportation & PavementMarkings\_A\\
Transportation & PavementMarkings\_L\\
Transportation & PavementMarkings\_P\\
Transportation & RailroadFeature\_P\\
Transportation & RailroadStation\_A\\
Transportation & RailroadStation\_P\\
Transportation & RailroadTurntable\_P\\
Transportation & RailroadYard\_A\\
Transportation & RoadArea\_A\\
Transportation & RoadPoint\_P\\
Transportation & RoadPosition\_P\\
Transportation & Sidewalk\_A\\
Transportation & TrafficControlPolePostMast\_P\\
Transportation & TrafficControlSign\_P\\
Transportation & TrafficControlSignPost\_P\\
Transportation & TrafficControlTrafficLight\_P\\
Transportation & TrafficCounter\_P\\
Transportation & TransportationRoute\_L\\
Transportation & TransportationRoute\_P\\
Transportation & TransportationTunnel\_A\\
Transportation & Vehicle\_A\\
Transportation & WindSock\_P\\
WaterWays & ArrivalPoint\_L\\
WaterWays & ArrivalPoint\_P\\
WaterWays & BankArmoring\_A\\
WaterWays & BankArmoring\_L\\
WaterWays & ChannelLine\_L\\
WaterWays & DischargeFlowStructure\_A\\
WaterWays & DischargeFlowStructure\_L\\
WaterWays & DischargeFlowStructure\_P\\
WaterWays & DistMarker\_P\\
WaterWays & DocksAndWharfs\_L\\
WaterWays & DocksAndWharfs\_P\\
WaterWays & DredgingEvent\_A\\
WaterWays & Fender\_A\\
WaterWays & Fender\_L\\
WaterWays & Hulk\_A\\
WaterWays & Hulk\_P\\
WaterWays & Lock\_A\\
WaterWays & Lock\_L\\
WaterWays & Marina\_A\\
WaterWays & Marina\_L\\
WaterWays & Marina\_P\\
WaterWays & MarineCable\_L\\
WaterWays & MarineCaution\_A\\
WaterWays & MarineNavigationAid\_P\\
WaterWays & MarinePipe\_L\\
WaterWays & MooringStructure\_A\\
WaterWays & MooringStructure\_P\\
WaterWays & NavigationLandmark\_A\\
WaterWays & NavigationLandmark\_P\\
WaterWays & PlacementArea\_A\\
WaterWays & PlacementArea\_L\\
WaterWays & PlacementArea\_P\\
WaterWays & PlacementImpactArea\_A\\
WaterWays & PrecautionaryArea\_A\\
WaterWays & ProjectDimension\_A\\
WaterWays & RiverineFlowStructure\_L\\
WaterWays & ShallowDepthOrDryingHeight\_A\\
WaterWays & ShoreEntryLoc\_A\\
WaterWays & ShoreEntryLoc\_L\\
WaterWays & ShoreEntryLoc\_P\\
WaterWays & SupportStructure\_A\\
WaterWays & SupportStructure\_L\\
WaterWays & SupportStructure\_P\\
WaterWays & UnderwaterObstacle\_L\\
WaterWays & VesselHoldingArea\_A\\
WaterWays & VesselRepairFacility\_A\\
WaterWays & WrecksAndObstructions\_A\\
WaterWays & WrecksAndObstructions\_P\\*
\end{longtable}
\rowcolors{2}{white}{white}


## Missing Field Counts from Included Feature Classes {#missFLDincFC}
Of the standard Feature Classes included, 0 standard fields for said Feature Classes in Full schema are missing in YoungstownJointARS_CIP's geodatabase. Table \@ref(tab:cmissFLDincFC) gives a count of the *fields* missing from each standard Feature Class in YoungstownJointARS_CIP's geodatabase.  

Across AF Installations overall, if the Feature Class was included, Missing Fields derived largely from fields such as "editor" or "dateEdited." In this regard, it is recommended that you compare these fields with those counted in the Section \@ref(diffFLD).


For a more detailed breakdown of the individual missing fields from standard Feature Classes, see the 'Full_MissingFields' table in YoungstownJointARS_CIP's geodatabase.  


\begin{table}[!h]

\caption{(\#tab:cmissFLDincFC)Missing Field Counts by Feature Class}
\centering
\begin{tabular}{l|l|r}
\hline
FDS & FC & Missing\_Field\_Count\\


\hline
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{0 Total Missing Fields}\\
\end{tabular}
\end{table}




## Empty Feature Classes {#emptFC}


Of the Feature Classes within the Full schema included in YoungstownJointARS_CIP's geodatabase, 12 standard Feature Classes are empty. Table \@ref(tab:cemptFC2) gives a listing of all the empty Feature Classes in YoungstownJointARS_CIP's geodatabase. In total, 451 empty Fields are present due to empty Feature Classes. This information is also found in YoungstownJointARS_CIP's geodatabase under the 'Full_EmptyFeatureClasses' table. 

\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}ccc}
\caption{(\#tab:cemptFC2)Empty Feature Classes}\\
\hiderowcolors
\toprule
FDS & FC & Empty\_Field\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cemptFC2)Empty Feature Classes \textit{(continued)}}\\
\toprule
FDS & FC & Empty\_Field\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{451 Total Empty Fields}\\
\endlastfoot
\showrowcolors
Cadastre & Outgrant\_A & 33\\
Cadastre & Site\_A & 34\\
MilitaryRangeTraining & ImpactArea\_A & 33\\
MilitaryRangeTraining & MilTrainingLoc\_A & 32\\
Recreation & GolfCourse\_A & 33\\
Transportation & Bridge\_A & 48\\
Transportation & Bridge\_L & 50\\
Transportation & RailSegment\_L & 46\\
Transportation & RailTrack\_L & 37\\
Transportation & RoadPath\_L & 33\\
WaterWays & DocksAndWharfs\_A & 35\\
environmentalCulturalResources & HistoricDistrict\_A & 37\\*
\end{longtable}
\rowcolors{2}{white}{white}





## Empty Fields from Non-Empty Feature Classes {#emptFLDneFC}
Of the Feature Classes within the Full schema included in YoungstownJointARS_CIP's geodatabase, 0 empty fields are present due to non-empty Feature Classes. Table \@ref(tab:cemptFLDneFC) below gives the count of empty fields by non-empty feature classes.  


For a more detailed breakdown of the individual empty fields from non-empty feature classes, see the 'Full_MissingData' table in YoungstownJointARS_CIP's geodatabase where rows are 'F' for the 'EMPTY_FC' column *and* rows are '0' for the 'POP_VALS_COUNT' column.  


\begin{table}[!h]

\caption{(\#tab:cemptFLDneFC)Empty Fields from Non-Empty Feature Classes}
\centering
\begin{tabular}{l|l|r}
\hline
FDS & FC & Empty\_Fields\_Counts\\


\hline
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{0 Total Empty Fields}\\
\end{tabular}
\end{table}



# Determinant and Indeterminant Values {#detindtVal}

YoungstownJointARS_CIP's geodatabase was analyzed for potential gaps in data at the Attribute level. Gaps in data were determined for each standard Feature Class' Attribute Table where cell values are 'Null', 'TBD' or 'Other.'  


Within the standard Feature Dataset/Feature Class combinations included in YoungstownJointARS_CIP's geodatabase, the percentage of data populated with determinant values (i.e.: data **not** classified as 'Null', 'TBD', or 'Other') are recorded in Table \@ref(tab:cdetindtVal2) below by Feature Class.  

The 'EnvRemediationSite_A' Feature class had the minimum data determined percentage of 34.2%, while the 'RecArea_A' Feature class had the maximum data determined percentage of 73.1%. On average, not including empty, standard Feature Classes, 59.6% of values are populated with determinant data for YoungstownJointARS_CIP's geodatabase *when averaged across standard Feature Classes included*. This information is also found in YoungstownJointARS_CIP's geodatabase under the 'Full_Determinant_Values_by_FC' table. 



\rowcolors{2}{white}{gray!6}

\begin{longtable}{l>{\bfseries}ccc}
\caption{(\#tab:cdetindtVal2)Determinant Value Percentage by Feature Class}\\
\hiderowcolors
\toprule
  & FDS & FC & Values\_Determined(\%)\\
\midrule
\endfirsthead
\caption[]{(\#tab:cdetindtVal2)Determinant Value Percentage by Feature Class \textit{(continued)}}\\
\toprule
  & FDS & FC & Values\_Determined(\%)\\
\midrule
\endhead
\
\endfoot
\bottomrule
\endlastfoot
\showrowcolors
1 & Auditory & NoiseZone\_A & 57.1\\
2 & Cadastre & Site\_P & 59.4\\
3 & Cadastre & Installation\_A & 68.3\\
4 & Cadastre & LandParcel\_A & 71.2\\
8 & environmentalNaturalResources & Wetland\_A & 40.9\\
9 & environmentalRestoration & EnvRemediationSite\_A & 34.2\\
10 & MilitaryRangeTraining & MilRange\_A & 64.7\\
11 & MilitaryRangeTraining & MilQuantityDistCombinedArc\_A & 67.3\\
14 & Pavements & PavementSection\_A & 34.6\\
15 & Pavements & PavementBranch\_A & 59.0\\
16 & Planning & LandUse\_A & 62.2\\
17 & Planning & AirAccidentZone\_A & 67.6\\
18 & RealProperty & Tower\_P & 57.3\\
19 & RealProperty & Building\_A & 67.5\\
20 & Recreation & RecArea\_A & 73.1\\
22 & Security & AccessControl\_P & 54.5\\
23 & Security & Fence\_L & 63.8\\
24 & Security & AccessControl\_L & 64.5\\
25 & Transportation & RoadCenterline\_L & 52.3\\
26 & Transportation & VehicleParking\_A & 72.5\\*
\end{longtable}
\rowcolors{2}{white}{white}



## Percent of Values 'Null', 'TBD' or 'Other' by Feature Class {#pctindtFC}


Within the standard Feature Dataset/Feature Class combinations included, the percentage of data populated with indeterminant values are recorded in Table \@ref(tab:cpctindtFC2) below.  

 

For YoungstownJointARS_CIP's geodatabase, 0.1% of cells are populated with 'Other' values, 3.1% of cells are populated with values 'To be determined,' and 37.2 of cells are populated with 'Null' cells, *when averaged across standard Feature Classes* included in YoungstownJointARS_CIP's geodatabase.  This information is also found in YoungstownJointARS_CIP's geodatabase under the 'Full_Summary_Cell_Pct_by_FC' table. 




\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}ccccc}
\caption{(\#tab:cpctindtFC2)Percent Other, TBD, and Null Cells by Feature Class}\\
\hiderowcolors
\toprule
FDS & FC & \%\_Other & \%\_TBD & \%\_Null\\
\midrule
\endfirsthead
\caption[]{(\#tab:cpctindtFC2)Percent Other, TBD, and Null Cells by Feature Class \textit{(continued)}}\\
\toprule
FDS & FC & \%\_Other & \%\_TBD & \%\_Null\\
\midrule
\endhead
\
\endfoot
\bottomrule
\endlastfoot
\showrowcolors
Auditory & NoiseZone\_A & 0.0 & 0.0 & 42.9\\
Cadastre & LandParcel\_A & 0.0 & 0.0 & 28.8\\
Cadastre & Installation\_A & 0.0 & 0.0 & 31.7\\
Cadastre & Site\_P & 0.0 & 0.0 & 40.6\\
environmentalNaturalResources & Wetland\_A & 0.0 & 15.9 & 43.2\\
environmentalRestoration & EnvRemediationSite\_A & 0.0 & 5.3 & 60.5\\
MilitaryRangeTraining & MilQuantityDistCombinedArc\_A & 0.0 & 2.2 & 30.5\\
MilitaryRangeTraining & MilRange\_A & 0.0 & 5.9 & 29.4\\
Pavements & PavementBranch\_A & 0.0 & 0.2 & 40.7\\
Pavements & PavementSection\_A & 0.0 & 0.1 & 65.3\\
Planning & AirAccidentZone\_A & 0.0 & 0.0 & 32.4\\
Planning & LandUse\_A & 0.0 & 3.8 & 34.0\\
RealProperty & Building\_A & 0.0 & 0.1 & 32.4\\
RealProperty & Tower\_P & 0.0 & 0.0 & 42.7\\
Recreation & RecArea\_A & 0.0 & 1.1 & 25.8\\
Security & AccessControl\_L & 1.1 & 4.7 & 29.7\\
Security & Fence\_L & 0.1 & 2.6 & 33.5\\
Security & AccessControl\_P & 0.0 & 9.1 & 36.4\\
Transportation & VehicleParking\_A & 0.2 & 0.6 & 26.7\\
Transportation & RoadCenterline\_L & 0.0 & 11.0 & 36.7\\*
\end{longtable}
\rowcolors{2}{white}{white}




## 'Null' Value Counts {#nullCnt}
YoungstownJointARS_CIP's geodatabase was analyzed for data with attributes 'Null' data at the Feature Class Attribute level.  72,732/140,864 (51.63%) *null* cells exist within standard Feature Classes in YoungstownJointARS_CIP's geodatabase. 
 
 For the purposes of this report, 'Null' data is classified as any cell within a Feature Class' Attribute Table  that contains any one of the following values:

1.  "NULL"
2.  "None"
3.  "none"
4.  "NONE"
6.  "-99999"
7.  "77777"
8.  "NA"
9.  "N/A"
10. "n/a"
11. "Null"

Please see Tables \@ref(tab:cnullCntFDS) & \@ref(tab:cnullCntFC) for a count of Null cells by Feature Dataset and Feature Class, respectively.

A more detailed breakdown of the individual values and counts of values for each *field* may be found in the YoungstownJointARS_CIP's geodatabase in the 'Full_MissingData' Table under the 'NULL_VALUE_COUNTS' column. Further, you may see the counts of 'Null' cells by standard Feature Class in the 'Full_NullCellCountbyFC' Table, or by Field in the 'Full_NullCellCountbyFLD' Table, in YoungstownJointARS_CIP's geodatabase.


###  'Null' Count by Feature Dataset {#nullCntFDS}
\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}cc}
\caption{(\#tab:cnullCntFDS)Count of Null Cells by Feature Dataset}\\
\hiderowcolors
\toprule
FDS & Total\_Null\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cnullCntFDS)Count of Null Cells by Feature Dataset \textit{(continued)}}\\
\toprule
FDS & Total\_Null\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{2}{l}{\textbf{Note: } }\\
\multicolumn{2}{l}{72732 Total 'Null' Cells}\\
\endlastfoot
\showrowcolors
Auditory & 54\\
Cadastre & 196\\
environmentalNaturalResources & 513\\
environmentalRestoration & 115\\
MilitaryRangeTraining & 93\\
Pavements & 63,729\\
Planning & 576\\
RealProperty & 1,879\\
Recreation & 24\\
Security & 3,468\\
Transportation & 2,085\\*
\end{longtable}
\rowcolors{2}{white}{white}


###  'Null' Count by Feature Class {#nullCntFC}
\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}ccc}
\caption{(\#tab:cnullCntFC)Count of Null Cells by Feature Class}\\
\hiderowcolors
\toprule
FDS & FC & Total\_Null\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cnullCntFC)Count of Null Cells by Feature Class \textit{(continued)}}\\
\toprule
FDS & FC & Total\_Null\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{72732 Total 'Null' Cells}\\
\endlastfoot
\showrowcolors
Auditory & NoiseZone\_A & 54\\
Cadastre & Installation\_A & 52\\
Cadastre & LandParcel\_A & 131\\
Cadastre & Site\_P & 13\\
MilitaryRangeTraining & MilQuantityDistCombinedArc\_A & 83\\
MilitaryRangeTraining & MilRange\_A & 10\\
Pavements & PavementBranch\_A & 16,513\\
Pavements & PavementSection\_A & 47,216\\
Planning & AirAccidentZone\_A & 22\\
Planning & LandUse\_A & 554\\
RealProperty & Building\_A & 1,640\\
RealProperty & Tower\_P & 239\\
Recreation & RecArea\_A & 24\\
Security & AccessControl\_L & 1,012\\
Security & AccessControl\_P & 36\\
Security & Fence\_L & 2,420\\
Transportation & RoadCenterline\_L & 347\\
Transportation & VehicleParking\_A & 1,738\\
environmentalNaturalResources & Wetland\_A & 513\\
environmentalRestoration & EnvRemediationSite\_A & 115\\*
\end{longtable}
\rowcolors{2}{white}{white}


                           

## 'TBD' Value Counts {#tbdCnt}
YoungstownJointARS_CIP's geodatabase was analyzed for data with attributes 'to be determined ' (TBD) at the Feature Class Attribute level. 914/140,864 (0.65%) *TBD* cells exist within standard Feature Classes in YoungstownJointARS_CIP's geodatabase. 

For the purposes of this report, TBD data is classified as any Feature Class Attribute Table cell that contains one of the following values:

1. 'To be determined'
2. 'TBD'
3. 'Tbd'
4. 'tbd'
5. '99999'

Please see Tables \@ref(tab:ctbdCntFDS) & \@ref(tab:ctbdCntFC) for a count of 'TBD' cells by Feature Dataset and Feature Class, respectively.

A more detailed breakdown of the individual values and counts of values found for each *field* may be found in the YoungstownJointARS_CIP's geodatabase in the 'Full_MissingData' Table under the 'TBD_VALUE_COUNTS' column. Further, you may see the counts of 'Null' cells by standard Feature Class in the 'Full_TBDCellCountbyFC' Table, or by Field in the 'Full_TBDCellCountbyFLD' Table, in YoungstownJointARS_CIP's geodatabase.


###  'TBD' Count by Feature Dataset {#tbdCntFDS}
\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}cc}
\caption{(\#tab:ctbdCntFDS)Count of TBD Cells by Feature Dataset}\\
\hiderowcolors
\toprule
FDS & Total\_TBD\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:ctbdCntFDS)Count of TBD Cells by Feature Dataset \textit{(continued)}}\\
\toprule
FDS & Total\_TBD\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{2}{l}{\textbf{Note: } }\\
\multicolumn{2}{l}{914 Total 'TBD' Cells}\\
\endlastfoot
\showrowcolors
environmentalNaturalResources & 189\\
environmentalRestoration & 10\\
MilitaryRangeTraining & 8\\
Pavements & 139\\
Planning & 62\\
RealProperty & 7\\
Recreation & 1\\
Security & 357\\
Transportation & 141\\*
\end{longtable}
\rowcolors{2}{white}{white}


###  'TBD' Count by Feature Class {#tbdCntFC}
\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}ccc}
\caption{(\#tab:ctbdCntFC)Count of TBD Cells by Feature Class}\\
\hiderowcolors
\toprule
FDS & FC & Total\_TBD\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:ctbdCntFC)Count of TBD Cells by Feature Class \textit{(continued)}}\\
\toprule
FDS & FC & Total\_TBD\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{914 Total 'TBD' Cells}\\
\endlastfoot
\showrowcolors
MilitaryRangeTraining & MilQuantityDistCombinedArc\_A & 6\\
MilitaryRangeTraining & MilRange\_A & 2\\
Pavements & PavementBranch\_A & 98\\
Pavements & PavementSection\_A & 41\\
Planning & LandUse\_A & 62\\
RealProperty & Building\_A & 7\\
Recreation & RecArea\_A & 1\\
Security & AccessControl\_L & 160\\
Security & AccessControl\_P & 9\\
Security & Fence\_L & 188\\
Transportation & RoadCenterline\_L & 104\\
Transportation & VehicleParking\_A & 37\\
environmentalNaturalResources & Wetland\_A & 189\\
environmentalRestoration & EnvRemediationSite\_A & 10\\*
\end{longtable}
\rowcolors{2}{white}{white}



## 'Other' Value Counts {#otherCnt}
YoungstownJointARS_CIP's geodatabase was analyzed for data with attributes classified as 'Other' at the Feature Class Attribute level. Overall, 82/140,864 (0.06%) *Other* cells exist within standard Feature Classes in YoungstownJointARS_CIP's geodatabase.  


For the purposes of this report, 'Other' data is classified as any Feature Class Attribute Table cell that contains one of the following values:

1. 'Other'
2. 'other'
3. 'OTHER'
4. '88888'

Please see Tables \@ref(tab:cotherCntFDS) & \@ref(tab:cotherCntFC) for a count of 'Other' cells by Feature Dataset and Feature Class, respectively.


A more detailed breakdown of the individual values and counts of values for each *field* may be found in the YoungstownJointARS_CIP's geodatabase in the 'Full_MissingData' Table under the 'OTHER_VALUE_COUNTS' column.   Further, you may see the counts of 'Null' cells by standard Feature Class in the 'Full_OtherCellCountbyFC' Table, or by Field in the 'Full_OtherCellCountbyFLD' Table, in YoungstownJointARS_CIP's geodatabase.

###  'Other' Count by Feature Dataset {#otherCntFDS}
\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}cc}
\caption{(\#tab:cotherCntFDS)Count of Other Cells by Feature Dataset}\\
\hiderowcolors
\toprule
FDS & Total\_Other\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cotherCntFDS)Count of Other Cells by Feature Dataset \textit{(continued)}}\\
\toprule
FDS & Total\_Other\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{2}{l}{\textbf{Note: } }\\
\multicolumn{2}{l}{82 Total 'Other' Cells}\\
\endlastfoot
\showrowcolors
Pavements & 25\\
Security & 41\\
Transportation & 16\\*
\end{longtable}
\rowcolors{2}{white}{white}

###  'Other' Count by Feature Class {#otherCntFC}

\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}ccc}
\caption{(\#tab:cotherCntFC)Count of Other Cells by Feature Class}\\
\hiderowcolors
\toprule
FDS & FC & Total\_Other\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cotherCntFC)Count of Other Cells by Feature Class \textit{(continued)}}\\
\toprule
FDS & FC & Total\_Other\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{82 Total 'Other' Cells}\\
\endlastfoot
\showrowcolors
Pavements & PavementSection\_A & 25\\
Security & AccessControl\_L & 37\\
Security & Fence\_L & 4\\
Transportation & VehicleParking\_A & 16\\*
\end{longtable}
\rowcolors{2}{white}{white}


# Differences Between YoungstownJointARS_CIP's Geodatabase and the Full Standard Schema {#diff}

## Fields with Incorrectly Populated Domains {#diffIncDom}


Within the standard Feature Classes included in YoungstownJointARS_CIP's geodatabaase from the Full schema, this section identifies the count of domain-contrained fields that have values outside of the domain values. In total, 24 fields have values that are not included in a field's domain.  

Please see Table \@ref(tab:cdiffIncDom2) below for the counts of incorrectly populated domains/fields by feature class.


A more detailed breakdown of the individual incorrectly-populated values and counts of these values may be found in the YoungstownJointARS_CIP's geodatabase within the 'Full_MissingData' Table under the 'INC_POP_VALS' column.   




\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}ccc}
\caption{(\#tab:cdiffIncDom2)Count of Incorrectly Populated Domains by Feature Class}\\
\hiderowcolors
\toprule
FDS & FC & Incorrectly\_Populated\_Field\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cdiffIncDom2)Count of Incorrectly Populated Domains by Feature Class \textit{(continued)}}\\
\toprule
FDS & FC & Incorrectly\_Populated\_Field\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{24 Total Count of Fields}\\
\endlastfoot
\showrowcolors
Auditory & NoiseZone\_A & 1\\
Cadastre & Installation\_A & 1\\
Cadastre & LandParcel\_A & 1\\
Cadastre & Site\_P & 2\\
environmentalNaturalResources & Wetland\_A & 1\\
environmentalRestoration & EnvRemediationSite\_A & 1\\
MilitaryRangeTraining & MilQuantityDistCombinedArc\_A & 1\\
MilitaryRangeTraining & MilRange\_A & 1\\
Pavements & PavementBranch\_A & 1\\
Pavements & PavementSection\_A & 1\\
Planning & AirAccidentZone\_A & 1\\
Planning & LandUse\_A & 1\\
RealProperty & Building\_A & 3\\
RealProperty & Tower\_P & 2\\
Recreation & RecArea\_A & 1\\
Security & AccessControl\_L & 1\\
Security & AccessControl\_P & 1\\
Security & Fence\_L & 1\\
Transportation & RoadCenterline\_L & 1\\
Transportation & VehicleParking\_A & 1\\*
\end{longtable}
\rowcolors{2}{white}{white}



## Fields Included in YoungstownJointARS_CIP's Geodatabase Not in Full {#diffFLD}
In total, 0 fields are included in YoungstownJointARS_CIP's geodatabase that are not included in the Full schema for each standard Feature Class included. Tables \@ref(tab:cdiffFLDnotFDS) & \@ref(tab:cdiffFLDnotFC) below lists counts of these fields by Feature Dataset and by Feature Class, respectively.  

In general, across AF Installations, if the Feature Class was included, Non-standard fields derived largely from fields such as "LAST_EDITED_DATE", "LAST_EDITED_USER", or "CREATED_DATE", therefore it is recommended that you cross-reference this sections with Section \@ref(missFLDincFC), where applicable. Further, for a more detailed listing of the individual non-standard *fields* included in YoungstownJointARS_CIP's geodatabase, see the 'Full_MissingData' Table under the 'NON_SDS' column. Fields that are not included the Full geodatabase will have the 'NON_SDS' column equal to 'T' (for 'True').  


### Fields Included in YoungstownJointARS_CIP's Geodatabase Not in Full Schema by Feature Dataset {#diffFLDnotFDS}

\begin{table}[!h]

\caption{(\#tab:cdiffFLDnotFDS)Count of Fields not in Target Geodatabase  by Feature Dataset}
\centering
\begin{tabular}{l|r}
\hline
FDS & NON\_SDS\_FIELD\_COUNT\\


\hline
\multicolumn{2}{l}{\textbf{Note: } }\\
\multicolumn{2}{l}{0 Total Count of Fields}\\
\end{tabular}
\end{table}


### Fields Included in YoungstownJointARS_CIP's Geodatabase Not in Full Schema by Feature Class {#diffFLDnot}

\begin{table}[!h]

\caption{(\#tab:cdiffFLDnotFC)Count of Fields not in Target Geodatabase by Feature Class}
\centering
\begin{tabular}{l|l|r}
\hline
FDS & FC & NON\_SDS\_FIELD\_COUNT\\


\hline
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{0 Total Count of Fields}\\
\end{tabular}
\end{table}




\pagebreak




# Production Info
For posterity, development information used to compile this report is listed below. .  



```
## R version 3.4.1 (2017-06-30)
## Platform: x86_64-w64-mingw32/x64 (64-bit)
## Running under: Windows >= 8 x64 (build 9200)
## 
## Matrix products: default
## 
## locale:
## [1] LC_COLLATE=English_United States.1252 
## [2] LC_CTYPE=English_United States.1252   
## [3] LC_MONETARY=English_United States.1252
## [4] LC_NUMERIC=C                          
## [5] LC_TIME=English_United States.1252    
## 
## attached base packages:
## [1] stats     graphics  grDevices utils     datasets  methods   base     
## 
## other attached packages:
##  [1] bindrcpp_0.2.2        tinytex_0.5           kableExtra_0.7.0.9000
##  [4] yaml_2.1.19           devtools_1.13.4       backports_1.1.2      
##  [7] digest_0.6.15         anchors_3.0-8         MASS_7.3-49          
## [10] rgenoud_5.8-1.0       bibtex_0.4.2          purrr_0.2.4          
## [13] bookdown_0.7          Rcpp_0.12.16          ggmap_2.6.1          
## [16] sf_0.6-1              rmarkdown_1.9.10      markdown_0.8         
## [19] knitr_1.20            stringr_1.3.0         DT_0.4               
## [22] leaflet_1.1.0         dplyr_0.7.4           ggplot2_2.2.1        
## [25] rprojroot_1.3-2       packrat_0.4.9-1      
## 
## loaded via a namespace (and not attached):
##  [1] httr_1.3.1        maps_3.3.0        viridisLite_0.3.0
##  [4] shiny_1.0.5       assertthat_0.2.0  sp_1.2-7         
##  [7] pillar_1.2.1      lattice_0.20-35   glue_1.2.0       
## [10] rvest_0.3.2       colorspace_1.3-2  htmltools_0.3.6  
## [13] httpuv_1.3.6.2    plyr_1.8.4        pkgconfig_2.0.1  
## [16] xtable_1.8-2      scales_0.5.0      jpeg_0.1-8       
## [19] git2r_0.21.0      tibble_1.4.2      withr_2.1.2      
## [22] lazyeval_0.2.1    proto_1.0.0       magrittr_1.5     
## [25] mime_0.5          memoise_1.1.0     evaluate_0.10.1  
## [28] xml2_1.2.0        class_7.3-14      tools_3.4.1      
## [31] hms_0.4.2         geosphere_1.5-7   RgoogleMaps_1.4.1
## [34] munsell_0.4.3     compiler_3.4.1    e1071_1.6-8      
## [37] rlang_0.2.0       classInt_0.1-24   units_0.5-1      
## [40] grid_3.4.1        rstudioapi_0.7    rjson_0.2.15     
## [43] htmlwidgets_1.0   crosstalk_1.0.0   gtable_0.2.0     
## [46] DBI_0.8           curl_3.2          reshape2_1.4.3   
## [49] R6_2.2.2          udunits2_0.13     bindr_0.1.1      
## [52] readr_1.1.1       stringi_1.1.7     mapproj_1.2.6    
## [55] png_0.1-7         xfun_0.1
```

