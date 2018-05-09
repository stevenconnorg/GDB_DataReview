# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 07:53:08 2018
@author: stevenconnorg
"""



import arcpy, os
from arcpy import env
env.overwriteOutput = True

# usps suffix data from https://github.com/allanbreyes/udacity-data-science/tree/master/p2/data
     
fc =  arcpy.GetParameterAsText(0)
prefixFld =  arcpy.GetParameterAsText(1)
nameFld =  arcpy.GetParameterAsText(2)
suffixFld =  arcpy.GetParameterAsText(3)

# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# fc =  r"C:\Users\stevenconnorg\Documents\knight-federal-solutions\GDB_DataReview\GDB_DataReview\dat\gdbs-cleaned\Example.gdb\Transportation\RoadCenterline_L"
# prefixFld =  "roadPrefix"
# nameFld =  "roadName"
# suffixFld =  "roadSuffix"
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================


def get_geodatabase_path(input_table):
  '''Return the Geodatabase path from the input table or feature class.
  :param input_table: path to the input table or feature class 
  '''
  workspace = os.path.dirname(input_table)
  if [any(ext) for ext in ('.gdb', '.mdb', '.sde') if ext in os.path.splitext(workspace)]:
    return workspace
  else:
    return os.path.dirname(workspace)

gdbPath = get_geodatabase_path(fc[0])


arcpy.env.workspace=gdbPath
# column names: 
# PrimaryStreetSuffixName
# CommonlyUsed
# PostalServiceStandardSuffixAbbreviation
suffixes = [['ALLEY', 'ALLEE', 'ALY'],
 ['ALLEY', 'ALLEY', 'ALY'],
 ['ALLEY', 'ALLY', 'ALY'],
 ['ALLEY', 'ALY', 'ALY'],
 ['ANNEX', 'ANEX ', 'ANX'],
 ['ANNEX', 'ANNEX', 'ANX'],
 ['ANNEX', 'ANNX', 'ANX'],
 ['ANNEX ', 'ANX', 'ANX'],
 ['ARCADE', 'ARC', 'ARC'],
 ['ARCADE', 'ARCADE', 'ARC'],
 ['AVENUE', 'AV', 'AVE'],
 ['AVENUE', 'AVE', 'AVE'],
 ['AVENUE', 'AVEN', 'AVE'],
 ['AVENUE', 'AVENU', 'AVE'],
 ['AVENUE', 'AVENUE', 'AVE'],
 ['AVENUE', 'AVN', 'AVE'],
 ['AVENUE', 'AVNUE', 'AVE'],
 ['BAYOO', 'BAYOO', 'BYU'],
 ['BAYOO', 'BAYOU', 'BYU'],
 ['BEACH', 'BCH', 'BCH'],
 ['BEACH', 'BEACH', 'BCH'],
 ['BEND', 'BEND', 'BND'],
 ['BEND', 'BND', 'BND'],
 ['BLUFF', 'BLF', 'BLF'],
 ['BLUFF', 'BLUF', 'BLF'],
 ['BLUFF', 'BLUFF', 'BLF'],
 ['BLUFFS', 'BLUFFS', 'BLFS'],
 ['BOTTOM', 'BOT', 'BTM'],
 ['BOTTOM', 'BOTTM', 'BTM'],
 ['BOTTOM', 'BOTTOM', 'BTM'],
 ['BOTTOM ', 'BTM', 'BTM'],
 ['BOULEVARD', 'BLVD', 'BLVD'],
 ['BOULEVARD', 'BOUL', 'BLVD'],
 ['BOULEVARD', 'BOULEVARD', 'BLVD'],
 ['BOULEVARD', 'BOULV', 'BLVD'],
 ['BRANCH', 'BR', 'BR'],
 ['BRANCH', 'BRANCH', 'BR'],
 ['BRANCH', 'BRNCH', 'BR'],
 ['BRIDGE', 'BRDGE', 'BRG'],
 ['BRIDGE', 'BRG', 'BRG'],
 ['BRIDGE', 'BRIDGE', 'BRG'],
 ['BROOK', 'BRK', 'BRK'],
 ['BROOK', 'BROOK', 'BRK'],
 ['BROOKS', 'BROOKS', 'BRKS'],
 ['BURG', 'BURG', 'BG'],
 ['BURGS', 'BURGS', 'BGS'],
 ['BYPASS', 'BYP', 'BYP'],
 ['BYPASS', 'BYPA', 'BYP'],
 ['BYPASS', 'BYPAS', 'BYP'],
 ['BYPASS', 'BYPASS', 'BYP'],
 ['BYPASS', 'BYPS', 'BYP'],
 ['CAMP ', 'CAMP', 'CP'],
 ['CAMP ', 'CMP', 'CP'],
 ['CAMP ', 'CP', 'CP'],
 ['CANYON ', 'CANYN', 'CYN'],
 ['CANYON ', 'CANYON', 'CYN'],
 ['CANYON ', 'CNYN', 'CYN'],
 ['CANYON ', 'CYN', 'CYN'],
 ['CAPE ', 'CAPE', 'CPE'],
 ['CAPE ', 'CPE', 'CPE'],
 ['CAUSEWAY ', 'CAUSEWAY', 'CSWY'],
 ['CAUSEWAY ', 'CAUSWAY', 'CSWY'],
 ['CAUSEWAY ', 'CSWY', 'CSWY'],
 ['CENTER ', 'CEN', 'CTR'],
 ['CENTER ', 'CENT', 'CTR'],
 ['CENTER ', 'CENTER ', 'CTR'],
 ['CENTER ', 'CENTR ', 'CTR'],
 ['CENTER ', 'CENTRE', 'CTR'],
 ['CENTER ', 'CNTER ', 'CTR'],
 ['CENTER ', 'CNTR ', 'CTR'],
 ['CENTER ', 'CTR ', 'CTR'],
 ['CENTERS ', 'CENTERS ', 'CTRS'],
 ['CIRCLE ', 'CIR ', 'CIR'],
 ['CIRCLE ', 'CIRC ', 'CIR'],
 ['CIRCLE ', 'CIRCL ', 'CIR'],
 ['CIRCLE ', 'CIRCLE ', 'CIR'],
 ['CIRCLE ', 'CRCL ', 'CIR'],
 ['CIRCLE ', 'CRCLE ', 'CIR'],
 ['CIRCLES ', 'CIRCLES ', 'CIRS'],
 ['CLIFF ', 'CLF ', 'CLF'],
 ['CLIFF ', 'CLIFF ', 'CLF'],
 ['CLIFFS ', 'CLFS ', 'CLFS'],
 ['CLIFFS ', 'CLIFFS ', 'CLFS'],
 ['CLUB ', 'CLB ', 'CLB'],
 ['CLUB ', 'CLUB ', 'CLB'],
 ['COMMON ', 'COMMON ', 'CMN'],
 ['CORNER ', 'COR ', 'COR'],
 ['CORNER ', 'CORNER ', 'COR'],
 ['CORNERS ', 'CORNERS ', 'CORS'],
 ['CORNERS ', 'CORS ', 'CORS'],
 ['COURSE ', 'COURSE ', 'CRSE'],
 ['COURSE ', 'CRSE ', 'CRSE'],
 ['COURT ', 'COURT ', 'CT'],
 ['COURT ', 'CRT ', 'CT'],
 ['COURT ', 'CT ', 'CT'],
 ['COURTS ', 'COURTS ', 'CTS'],
 ['COURTS ', 'CT ', 'CTS'],
 ['COVE ', 'COVE ', 'CV'],
 ['COVE ', 'CV ', 'CV'],
 ['COVES ', 'COVES ', 'CVS'],
 ['CREEK ', 'CK ', 'CRK'],
 ['CREEK ', 'CR ', 'CRK'],
 ['CREEK ', 'CREEK ', 'CRK'],
 ['CREEK ', 'CRK ', 'CRK'],
 ['CRESCENT ', 'CRECENT ', 'CRES'],
 ['CRESCENT ', 'CRES ', 'CRES'],
 ['CRESCENT ', 'CRESCENT ', 'CRES'],
 ['CRESCENT ', 'CRESENT ', 'CRES'],
 ['CRESCENT ', 'CRSCNT ', 'CRES'],
 ['CRESCENT ', 'CRSENT ', 'CRES'],
 ['CRESCENT ', 'CRSNT ', 'CRES'],
 ['CREST ', 'CREST ', 'CRST'],
 ['CROSSING ', 'CROSSING ', 'XING'],
 ['CROSSING ', 'CRSSING ', 'XING'],
 ['CROSSING ', 'CRSSNG ', 'XING'],
 ['CROSSING ', 'XING ', 'XING'],
 ['CROSSROAD ', 'CROSSROAD ', 'XRD'],
 ['CURVE ', 'CURVE ', 'CURV'],
 ['DALE', 'DALE', 'DL'],
 ['DALE', 'DL', 'DL'],
 ['DAM', 'DAM', 'DM'],
 ['DAM', 'DM ', 'DM'],
 ['DIVIDE', 'DIV', 'DV'],
 ['DIVIDE', 'DIVIDE', 'DV'],
 ['DIVIDE', 'DV', 'DV'],
 ['DIVIDE', 'DVD', 'DV'],
 ['DRIVE', 'DRIV', 'DR'],
 ['DRIVE', 'DRIVE', 'DR'],
 ['DRIVE', 'DRV', 'DR'],
 ['DRIVE ', 'DR', 'DR'],
 ['DRIVES', 'DRIVES', 'DRS'],
 ['ESTATE', 'EST', 'EST'],
 ['ESTATE', 'ESTATE', 'EST'],
 ['ESTATES', 'ESTATES', 'ESTS'],
 ['ESTATES', 'ESTS', 'ESTS'],
 ['EXPRESSWAY', 'EXP', 'EXPY'],
 ['EXPRESSWAY', 'EXPR', 'EXPY'],
 ['EXPRESSWAY', 'EXPRESS', 'EXPY'],
 ['EXPRESSWAY', 'EXPRESSWAY', 'EXPY'],
 ['EXPRESSWAY', 'EXPW', 'EXPY'],
 ['EXPRESSWAY', 'EXPY', 'EXPY'],
 ['EXTENSION', 'EXT', 'EXT'],
 ['EXTENSION', 'EXTENSION', 'EXT'],
 ['EXTENSION', 'EXTN', 'EXT'],
 ['EXTENSION', 'EXTNSN', 'EXT'],
 ['EXTENSIONS', 'EXTENSIONS', 'EXTS'],
 ['EXTENSIONS', 'EXTS', 'EXTS'],
 ['FALL', 'FALL', 'FALL'],
 ['FALLS', 'FALLS', 'FLS'],
 ['FALLS', 'FLS', 'FLS'],
 ['FERRY', 'FERRY', 'FRY'],
 ['FERRY', 'FRRY', 'FRY'],
 ['FERRY', 'FRY', 'FRY'],
 ['FIELD', 'FIELD', 'FLD'],
 ['FIELD', 'FLD', 'FLD'],
 ['FIELDS', 'FIELDS', 'FLDS'],
 ['FIELDS', 'FLDS', 'FLDS'],
 ['FLAT', 'FLAT', 'FLT'],
 ['FLAT', 'FLT', 'FLT'],
 ['FLATS', 'FLATS', 'FLTS'],
 ['FLATS', 'FLTS', 'FLTS'],
 ['FORD', 'FORD', 'FRD'],
 ['FORD', 'FRD', 'FRD'],
 ['FORDS', 'FORDS', 'FRDS'],
 ['FOREST', 'FOREST', 'FRST'],
 ['FOREST', 'FORESTS', 'FRST'],
 ['FOREST', 'FRST', 'FRST'],
 ['FORGE', 'FORG', 'FRG'],
 ['FORGE', 'FORGE', 'FRG'],
 ['FORGE', 'FRG', 'FRG'],
 ['FORGES', 'FORGES', 'FRGS'],
 ['FORK', 'FORK', 'FRK'],
 ['FORK', 'FRK', 'FRK'],
 ['FORKS', 'FORKS', 'FRKS'],
 ['FORKS', 'FRKS', 'FRKS'],
 ['FORT', 'FORT', 'FT'],
 ['FORT', 'FRT', 'FT'],
 ['FORT', 'FT', 'FT'],
 ['FREEWAY', 'FREEWAY', 'FWY'],
 ['FREEWAY', 'FREEWY', 'FWY'],
 ['FREEWAY', 'FRWAY', 'FWY'],
 ['FREEWAY', 'FRWY', 'FWY'],
 ['FREEWAY', 'FWY', 'FWY'],
 ['GARDEN', 'GARDEN', 'GDN'],
 ['GARDEN', 'GARDN', 'GDN'],
 ['GARDEN', 'GDN', 'GDN'],
 ['GARDEN', 'GRDEN', 'GDN'],
 ['GARDEN', 'GRDN', 'GDN'],
 ['GARDENS', 'GARDENS', 'GDNS'],
 ['GARDENS', 'GDNS', 'GDNS'],
 ['GARDENS', 'GRDNS', 'GDNS'],
 ['GATEWAY', 'GATEWAY', 'GTWY'],
 ['GATEWAY', 'GATEWY', 'GTWY'],
 ['GATEWAY', 'GATWAY', 'GTWY'],
 ['GATEWAY', 'GTWAY', 'GTWY'],
 ['GATEWAY', 'GTWY', 'GTWY'],
 ['GLEN', 'GLEN', 'GLN'],
 ['GLEN', 'GLN', 'GLN'],
 ['GLENS', 'GLENS', 'GLNS'],
 ['GREEN', 'GREEN', 'GRN'],
 ['GREEN', 'GRN', 'GRN'],
 ['GREENS', 'GREENS', 'GRNS'],
 ['GROVE', 'GROV', 'GRV'],
 ['GROVE', 'GROVE', 'GRV'],
 ['GROVE', 'GRV', 'GRV'],
 ['GROVES', 'GROVES', 'GRVS'],
 ['HARBOR', 'HARB', 'HBR'],
 ['HARBOR', 'HARBOR', 'HBR'],
 ['HARBOR', 'HARBR', 'HBR'],
 ['HARBOR', 'HBR', 'HBR'],
 ['HARBOR', 'HRBOR', 'HBR'],
 ['HARBORS', 'HARBORS', 'HBRS'],
 ['HAVEN', 'HAVEN', 'HVN'],
 ['HAVEN', 'HAVN', 'HVN'],
 ['HAVEN', 'HVN', 'HVN'],
 ['HEIGHTS', 'HEIGHT', 'HTS'],
 ['HEIGHTS', 'HEIGHTS', 'HTS'],
 ['HEIGHTS', 'HGTS', 'HTS'],
 ['HEIGHTS', 'HT', 'HTS'],
 ['HEIGHTS', 'HTS', 'HTS'],
 ['HIGHWAY', 'HIGHWAY', 'HWY'],
 ['HIGHWAY', 'HIGHWY', 'HWY'],
 ['HIGHWAY', 'HIWAY', 'HWY'],
 ['HIGHWAY', 'HIWY', 'HWY'],
 ['HIGHWAY', 'HWAY', 'HWY'],
 ['HIGHWAY', 'HWY', 'HWY'],
 ['HILL', 'HILL', 'HL'],
 ['HILL', 'HL', 'HL'],
 ['HILLS', 'HILLS', 'HLS'],
 ['HILLS', 'HLS', 'HLS'],
 ['HOLLOW ', 'HLLW', 'HOLW'],
 ['HOLLOW ', 'HOLLOW', 'HOLW'],
 ['HOLLOW ', 'HOLLOWS', 'HOLW'],
 ['HOLLOW ', 'HOLW', 'HOLW'],
 ['HOLLOW ', 'HOLWS', 'HOLW'],
 ['INLET', 'INLET', 'INLT'],
 ['INLET ', 'INLT', 'INLT'],
 ['ISLAND', 'IS', 'IS'],
 ['ISLAND ', 'ISLAND', 'IS'],
 ['ISLAND ', 'ISLND', 'IS'],
 ['ISLANDS', 'ISS', 'ISS'],
 ['ISLANDS ', 'ISLANDS', 'ISS'],
 ['ISLANDS ', 'ISLNDS', 'ISS'],
 ['ISLE', 'ISLE', 'ISLE'],
 ['ISLE ', 'ISLES', 'ISLE'],
 ['JUNCTION', 'JCT', 'JCT'],
 ['JUNCTION', 'JCTION', 'JCT'],
 ['JUNCTION', 'JCTN', 'JCT'],
 ['JUNCTION', 'JUNCTION', 'JCT'],
 ['JUNCTION', 'JUNCTN', 'JCT'],
 ['JUNCTION', 'JUNCTON', 'JCT'],
 ['JUNCTIONS', 'JCTNS', 'JCTS'],
 ['JUNCTIONS', 'JCTS', 'JCTS'],
 ['JUNCTIONS', 'JUNCTIONS', 'JCTS'],
 ['KEY', 'KEY', 'KY'],
 ['KEY', 'KY', 'KY'],
 ['KEYS', 'KEYS', 'KYS'],
 ['KEYS', 'KYS', 'KYS'],
 ['KNOLL', 'KNL', 'KNL'],
 ['KNOLL', 'KNOL', 'KNL'],
 ['KNOLL', 'KNOLL', 'KNL'],
 ['KNOLLS', 'KNLS', 'KNLS'],
 ['KNOLLS', 'KNOLLS', 'KNLS'],
 ['LAKE', 'LAKE', 'LK'],
 ['LAKE', 'LK', 'LK'],
 ['LAKES', 'LAKES', 'LKS'],
 ['LAKES', 'LKS', 'LKS'],
 ['LAND', 'LAND', 'LAND'],
 ['LANDING', 'LANDING', 'LNDG'],
 ['LANDING', 'LNDG', 'LNDG'],
 ['LANDING', 'LNDNG', 'LNDG'],
 ['LANE', 'LA', 'LN'],
 ['LANE', 'LANE', 'LN'],
 ['LANE', 'LANES', 'LN'],
 ['LANE', 'LN', 'LN'],
 ['LIGHT', 'LGT', 'LGT'],
 ['LIGHT', 'LIGHT', 'LGT'],
 ['LIGHTS', 'LIGHTS', 'LGTS'],
 ['LOAF ', 'LF', 'LF'],
 ['LOAF ', 'LOAF', 'LF'],
 ['LOCK ', 'LCK', 'LCK'],
 ['LOCK ', 'LOCK', 'LCK'],
 ['LOCKS', 'LOCKS', 'LCKS'],
 ['LOCKS ', 'LCKS', 'LCKS'],
 ['LODGE', 'LDGE', 'LDG'],
 ['LODGE ', 'LDG', 'LDG'],
 ['LODGE ', 'LODG', 'LDG'],
 ['LODGE ', 'LODGE', 'LDG'],
 ['LOOP ', 'LOOP', 'LOOP'],
 ['LOOP ', 'LOOPS', 'LOOP'],
 ['MALL', 'MALL', 'MALL'],
 ['MANOR', 'MANOR', 'MNR'],
 ['MANOR', 'MNR', 'MNR'],
 ['MANORS', 'MANORS', 'MNRS'],
 ['MANORS', 'MNRS', 'MNRS'],
 ['MEADOW', 'MDW', 'MDW'],
 ['MEADOW', 'MEADOW', 'MDW'],
 ['MEADOWS', 'MDWS', 'MDWS'],
 ['MEADOWS', 'MEADOWS', 'MDWS'],
 ['MEADOWS', 'MEDOWS', 'MDWS'],
 ['MEWS', 'MEWS', 'MEWS'],
 ['MILL', 'MILL', 'ML'],
 ['MILL', 'ML', 'ML'],
 ['MILLS', 'MILLS', 'MLS'],
 ['MILLS', 'MLS', 'MLS'],
 ['MISSION', 'MISSION', 'MSN'],
 ['MISSION', 'MSN', 'MSN'],
 ['MISSION', 'MSSN', 'MSN'],
 ['MISSION ', 'MISSN', 'MSN'],
 ['MOTORWAY', 'MOTORWAY', 'MTWY'],
 ['MOUNT', 'MNT', 'MT'],
 ['MOUNT', 'MOUNT', 'MT'],
 ['MOUNT', 'MT', 'MT'],
 ['MOUNTAIN', 'MNTAIN', 'MTN'],
 ['MOUNTAIN', 'MNTN', 'MTN'],
 ['MOUNTAIN', 'MOUNTIN', 'MTN'],
 ['MOUNTAIN', 'MTIN', 'MTN'],
 ['MOUNTAIN ', 'MOUNTAIN', 'MTN'],
 ['MOUNTAIN ', 'MTN', 'MTN'],
 ['MOUNTAINS', 'MOUNTAINS', 'MTNS'],
 ['MOUNTAINS ', 'MNTNS', 'MTNS'],
 ['NECK', 'NCK', 'NCK'],
 ['NECK', 'NECK', 'NCK'],
 ['ORCHARD', 'ORCH', 'ORCH'],
 ['ORCHARD', 'ORCHARD', 'ORCH'],
 ['ORCHARD', 'ORCHRD', 'ORCH'],
 ['OVAL', 'OVAL', 'OVAL'],
 ['OVAL', 'OVL', 'OVAL'],
 ['OVERPASS', 'OVERPASS', 'OPAS'],
 ['PARK', 'PARK', 'PARK'],
 ['PARK', 'PK', 'PARK'],
 ['PARK', 'PRK', 'PARK'],
 ['PARKS', 'PARKS', 'PARK'],
 ['PARKWAY', 'PARKWAY', 'PKWY'],
 ['PARKWAY', 'PARKWY', 'PKWY'],
 ['PARKWAY', 'PKWAY', 'PKWY'],
 ['PARKWAY', 'PKWY', 'PKWY'],
 ['PARKWAY', 'PKY', 'PKWY'],
 ['PARKWAYS', 'PARKWAYS', 'PKWY'],
 ['PARKWAYS', 'PKWYS', 'PKWY'],
 ['PASS', 'PASS', 'PASS'],
 ['PASSAGE', 'PASSAGE', 'PSGE'],
 ['PATH', 'PATH', 'PATH'],
 ['PATH', 'PATHS', 'PATH'],
 ['PIKE', 'PIKE', 'PIKE'],
 ['PIKE', 'PIKES', 'PIKE'],
 ['PINE', 'PINE', 'PNE'],
 ['PINES', 'PINES', 'PNES'],
 ['PINES', 'PNES', 'PNES'],
 ['PLACE', 'PL', 'PL'],
 ['PLACE', 'PLACE', 'PL'],
 ['PLAIN', 'PLAIN', 'PLN'],
 ['PLAIN', 'PLN', 'PLN'],
 ['PLAINS', 'PLAINES', 'PLNS'],
 ['PLAINS', 'PLAINS', 'PLNS'],
 ['PLAINS ', 'PLNS', 'PLNS'],
 ['PLAZA', 'PLAZA', 'PLZ'],
 ['PLAZA', 'PLZA', 'PLZ'],
 ['PLAZA ', 'PLZ', 'PLZ'],
 ['POINT ', 'POINT', 'PT'],
 ['POINT ', 'PT', 'PT'],
 ['POINTS', 'POINTS', 'PTS'],
 ['POINTS', 'PTS', 'PTS'],
 ['PORT', 'PRT', 'PRT'],
 ['PORT ', 'PORT', 'PRT'],
 ['PORTS', 'PRTS', 'PRTS'],
 ['PORTS ', 'PORTS', 'PRTS'],
 ['PRAIRIE', 'PR', 'PR'],
 ['PRAIRIE', 'PRR', 'PR'],
 ['PRAIRIE ', 'PRAIRIE', 'PR'],
 ['PRAIRIE ', 'PRARIE', 'PR'],
 ['RADIAL', 'RAD', 'RADL'],
 ['RADIAL', 'RADIAL', 'RADL'],
 ['RADIAL', 'RADIEL', 'RADL'],
 ['RADIAL', 'RADL', 'RADL'],
 ['RAMP', 'RAMP', 'RAMP'],
 ['RANCH', 'RANCH', 'RNCH'],
 ['RANCH', 'RANCHES', 'RNCH'],
 ['RANCH', 'RNCH', 'RNCH'],
 ['RANCH', 'RNCHS', 'RNCH'],
 ['RAPID', 'RAPID', 'RPD'],
 ['RAPID', 'RPD', 'RPD'],
 ['RAPIDS', 'RAPIDS', 'RPDS'],
 ['RAPIDS', 'RPDS', 'RPDS'],
 ['REST', 'REST', 'RST'],
 ['REST', 'RST', 'RST'],
 ['RIDGE', 'RDG', 'RDG'],
 ['RIDGE', 'RDGE', 'RDG'],
 ['RIDGE', 'RIDGE', 'RDG'],
 ['RIDGES', 'RDGS', 'RDGS'],
 ['RIDGES', 'RIDGES', 'RDGS'],
 ['RIVER', 'RIV', 'RIV'],
 ['RIVER', 'RIVER', 'RIV'],
 ['RIVER', 'RIVR', 'RIV'],
 ['RIVER', 'RVR', 'RIV'],
 ['ROAD', 'RD', 'RD'],
 ['ROAD ', 'ROAD', 'RD'],
 ['ROADS', 'RDS', 'RDS'],
 ['ROADS ', 'ROADS', 'RDS'],
 ['ROUTE', 'ROUTE', 'RTE'],
 ['ROW ', 'ROW', 'ROW'],
 ['RUE ', 'RUE', 'RUE'],
 ['RUN', 'RUN', 'RUN'],
 ['SHOAL', 'SHL', 'SHL'],
 ['SHOAL', 'SHOAL', 'SHL'],
 ['SHOALS', 'SHLS', 'SHLS'],
 ['SHOALS', 'SHOALS', 'SHLS'],
 ['SHORE', 'SHOAR', 'SHR'],
 ['SHORE', 'SHORE', 'SHR'],
 ['SHORE', 'SHR', 'SHR'],
 ['SHORES', 'SHOARS', 'SHRS'],
 ['SHORES', 'SHORES', 'SHRS'],
 ['SHORES', 'SHRS', 'SHRS'],
 ['SKYWAY', 'SKYWAY', 'SKWY'],
 ['SPRING', 'SPG', 'SPG'],
 ['SPRING', 'SPNG', 'SPG'],
 ['SPRING', 'SPRING', 'SPG'],
 ['SPRING', 'SPRNG', 'SPG'],
 ['SPRINGS', 'SPNGS', 'SPGS'],
 ['SPRINGS', 'SPRINGS', 'SPGS'],
 ['SPRINGS', 'SPRNGS', 'SPGS'],
 ['SPRINGS ', 'SPGS', 'SPGS'],
 ['SPUR', 'SPUR', 'SPUR'],
 ['SPURS', 'SPURS', 'SPUR'],
 ['SQUARE', 'SQ', 'SQ'],
 ['SQUARE', 'SQR', 'SQ'],
 ['SQUARE', 'SQRE', 'SQ'],
 ['SQUARE', 'SQUARE', 'SQ'],
 ['SQUARE ', 'SQU', 'SQ'],
 ['SQUARES', 'SQRS', 'SQS'],
 ['SQUARES ', 'SQUARES', 'SQS'],
 ['STATION', 'STATION', 'STA'],
 ['STATION', 'STATN', 'STA'],
 ['STATION ', 'STA', 'STA'],
 ['STATION ', 'STN', 'STA'],
 ['STRAVENUE', 'STRAV', 'STRA'],
 ['STRAVENUE', 'STRAVE', 'STRA'],
 ['STRAVENUE', 'STRAVN', 'STRA'],
 ['STRAVENUE', 'STRVN', 'STRA'],
 ['STRAVENUE ', 'STRA', 'STRA'],
 ['STRAVENUE ', 'STRAVEN', 'STRA'],
 ['STRAVENUE ', 'STRAVENUE', 'STRA'],
 ['STRAVENUE ', 'STRVNUE', 'STRA'],
 ['STREAM', 'STREME', 'STRM'],
 ['STREAM ', 'STREAM', 'STRM'],
 ['STREAM ', 'STRM', 'STRM'],
 ['STREET', 'ST', 'ST'],
 ['STREET', 'STRT', 'ST'],
 ['STREET ', 'STR', 'ST'],
 ['STREET ', 'STREET', 'ST'],
 ['STREETS', 'STREETS', 'STS'],
 ['SUMMIT', 'SUMIT', 'SMT'],
 ['SUMMIT', 'SUMMIT', 'SMT'],
 ['SUMMIT ', 'SMT', 'SMT'],
 ['SUMMIT ', 'SUMITT', 'SMT'],
 ['TERRACE', 'TER', 'TER'],
 ['TERRACE', 'TERR', 'TER'],
 ['TERRACE', 'TERRACE', 'TER'],
 ['THROUGHWAY', 'THROUGHWAY', 'TRWY'],
 ['TRACE', 'TRACE', 'TRCE'],
 ['TRACE', 'TRACES', 'TRCE'],
 ['TRACE', 'TRCE', 'TRCE'],
 ['TRACK', 'TRACK', 'TRAK'],
 ['TRACK', 'TRACKS', 'TRAK'],
 ['TRACK', 'TRAK', 'TRAK'],
 ['TRACK', 'TRK', 'TRAK'],
 ['TRACK', 'TRKS', 'TRAK'],
 ['TRAFFICWAY', 'TRAFFICWAY', 'TRFY'],
 ['TRAFFICWAY', 'TRFY', 'TRFY'],
 ['TRAIL', 'TR', 'TRL'],
 ['TRAIL', 'TRAILS', 'TRL'],
 ['TRAIL', 'TRL', 'TRL'],
 ['TRAIL', 'TRLS', 'TRL'],
 ['TRAIL ', 'TRAIL', 'TRL'],
 ['TUNNEL', 'TUNEL', 'TUNL'],
 ['TUNNEL', 'TUNL', 'TUNL'],
 ['TUNNEL', 'TUNLS', 'TUNL'],
 ['TUNNEL', 'TUNNEL', 'TUNL'],
 ['TUNNEL', 'TUNNELS', 'TUNL'],
 ['TUNNEL ', 'TUNNL', 'TUNL'],
 ['TURNPIKE', 'TPK', 'TPKE'],
 ['TURNPIKE', 'TPKE', 'TPKE'],
 ['TURNPIKE', 'TRPK', 'TPKE'],
 ['TURNPIKE', 'TURNPIKE', 'TPKE'],
 ['TURNPIKE', 'TURNPK', 'TPKE'],
 ['TURNPIKE ', 'TRNPK', 'TPKE'],
 ['UNDERPASS', 'UNDERPASS', 'UPAS'],
 ['UNION', 'UN', 'UN'],
 ['UNION', 'UNION', 'UN'],
 ['UNIONS', 'UNIONS', 'UNS'],
 ['VALLEY', 'VALLEY', 'VLY'],
 ['VALLEY', 'VALLY', 'VLY'],
 ['VALLEY', 'VLLY', 'VLY'],
 ['VALLEY', 'VLY', 'VLY'],
 ['VALLEYS', 'VALLEYS', 'VLYS'],
 ['VALLEYS', 'VLYS', 'VLYS'],
 ['VIADUCT', 'VDCT', 'VIA'],
 ['VIADUCT', 'VIA', 'VIA'],
 ['VIADUCT', 'VIADCT', 'VIA'],
 ['VIADUCT', 'VIADUCT', 'VIA'],
 ['VIEW', 'VIEW', 'VW'],
 ['VIEW', 'VW', 'VW'],
 ['VIEWS', 'VIEWS', 'VWS'],
 ['VIEWS', 'VWS', 'VWS'],
 ['VILLAGE', 'VILL', 'VLG'],
 ['VILLAGE', 'VILLAGE', 'VLG'],
 ['VILLAGE', 'VILLG', 'VLG'],
 ['VILLAGE', 'VILLIAGE', 'VLG'],
 ['VILLAGE', 'VLG', 'VLG'],
 ['VILLAGE ', 'VILLAG', 'VLG'],
 ['VILLAGES', 'VILLAGES', 'VLGS'],
 ['VILLAGES', 'VLGS', 'VLGS'],
 ['VILLE', 'VILLE', 'VL'],
 ['VILLE', 'VL', 'VL'],
 ['VISTA', 'VIST', 'VIS'],
 ['VISTA', 'VISTA', 'VIS'],
 ['VISTA', 'VSTA', 'VIS'],
 ['VISTA ', 'VIS', 'VIS'],
 ['VISTA ', 'VST', 'VIS'],
 ['WALK', 'WALK', 'WALK'],
 ['WALKS', 'WALKS', 'WALK'],
 ['WALL', 'WALL', 'WALL'],
 ['WAY', 'WAY', 'WAY'],
 ['WAY', 'WY', 'WAY'],
 ['WAYS', 'WAYS', 'WAYS'],
 ['WELL', 'WELL', 'WL'],
 ['WELLS', 'WELLS', 'WLS'],
 ['WELLS', 'WLS', 'WLS']]
    





def checkEnds(line, ends):
    for end in ends:
        if line.endswith(end):
            return True

nullValues = [None, "0",0,"None", "none", "NONE", "","-99999","77777",77777, " ", "NA", "na", "N/A", "n/a","NULL","Null","<NULL>","null","<null>""<Null>","  ","   ","    ","     "]
otherValues = [ "Other", "other", "OTHER","88888",88888]
tbdValues = ["tbd","TBD","To be determined","Tbd",99999,"99999"]
indetVals = nullValues+otherValues+tbdValues                         


commonSuffixes = [el[1] for el in suffixes]
standardSuffixes = [el[2] for el in suffixes]

prefixes = [["NORTH","N"],
            ["north","N"],
            ["North","N"],
            ["North ","N"],
            ["N","N"],
            ["N.","N"],
            ["SOUTH", "S"],
            ["south","S"],
            ["South","S"],
            ["South ","S"],
            ["S","S"],
            ["S.","S"],
            ["WEST","W"],
            ["west","W"],
            ["West","W"],
            ["West ","W"],
            ["W","W"],
            ["W.","W"],
            ["EAST","E"],
            ["east","E"],
            ["East","E"],
            ["East ","E"],
            ["E","E"],
            ["E.","E"]]

commonPrefixes = [el[0] for el in prefixes]
#commonPrefixes =[item for sublist in commonPrefixes for item in sublist]
standardPrefixes = [el[-1] for el in prefixes]

streetFields = [prefixFld,nameFld,suffixFld]

with arcpy.da.UpdateCursor(fc, streetFields) as cursor:
    for row in cursor:
        roadName = row[1]
        if roadName is None:
            pass
        else:
            roadNameVals = roadName.split(" ")
            for n, i in enumerate(roadNameVals):
                new = str(i)
                roadNameVals[n] = new
            
            if len(roadNameVals) > 1:
                for roadNameVal in roadNameVals:
                    roadNameVal = str(roadNameVal)
                    
                    if roadNameVal.upper() in commonSuffixes:
                        if roadNameVals.index(roadNameVal) == len(roadNameVals)-1:
                            idx = commonSuffixes.index(roadNameVal.upper())
                            newSuffix= standardSuffixes[idx] 
                            idx2 =   roadNameVals.index(roadNameVal)
                            roadNameVals.remove(roadNameVals[idx2])
                       
                    elif roadNameVal.upper() in standardSuffixes:
                        if roadNameVals.index(roadNameVal) == len(roadNameVals)-1:
                            newSuffix= roadNameVal.upper()
                            idx2 =   roadNameVals.index(roadNameVal)
                            roadNameVals.remove(roadNameVals[idx2])
                        
                    if roadNameVal.upper() in commonPrefixes:
                        if roadNameVals.index(roadNameVal) == 0:
                            idx1 = commonPrefixes.index(roadNameVal.upper())
                            newPrefix= standardPrefixes[idx1]
                            idx2 =   roadNameVals.index(roadNameVal)
                            roadNameVals.remove(roadNameVals[idx2])
                        
                    elif roadNameVal.upper() in standardPrefixes:
                        if roadNameVals.index(roadNameVal) == 0:
                            newPrefix= roadNameVal.upper()
                            idx2 =   roadNameVals.index(roadNameVal)
                            roadNameVals.remove(roadNameVals[idx2])
                        
                    if 'newPrefix' not in locals():
                        newPrefix = str(row[0])
                        if newPrefix.upper() in commonPrefixes:
                            idx1 = commonPrefixes.index(newPrefix.upper())
                            newPrefix= standardPrefixes[idx1]
                        elif newPrefix.upper() in standardPrefixes:
                            newPrefix= newPrefix.upper()
# =============================================================================
#                             idx2 =   roadNameVals.index(roadNameVal)
#                             roadNameVals.remove(roadNameVals[idx2])
# =============================================================================
                            
                    if 'newSuffix' not in locals():
                        newSuffix = str(row[2])
                        if newSuffix.upper() in commonSuffixes:
                            idx1 = commonSuffixes.index(newSuffix.upper())
                            newSuffix= standardSuffixes[idx1]
                        elif newSuffix.upper() in standardSuffixes:
                            newSuffix= newSuffix.upper()
# =============================================================================
#                             idx2 =   roadNameVals.index(roadNameVal)
#                             roadNameVals.remove(roadNameVals[idx2])
# =============================================================================

                
                
                newName = ' '.join(roadNameVals)
                newRow= [newPrefix,newName,newSuffix]
                del newSuffix    
                del newPrefix
                del newName
                arcpy.AddMessage( "old row = "+str(row))
                arcpy.AddMessage("new row = "+str(newRow))
                
            else:
                prefix = row[0]
                if prefix is None:
                    pass
                else:
                    if prefix.upper() in commonPrefixes:
                        idx1 = commonPrefixes.index(prefix.upper())
                        newPrefix= standardPrefixes[idx1]
                        
                    elif prefix.upper() in standardPrefixes:
                        newPrefix= prefix.upper()
                    else:
                        newPrefix = prefix.upper()
                suffix = row[2]
                if suffix is None:
                    pass
                else:
                    if suffix.upper() in commonSuffixes:
                        idx = commonSuffixes.index(suffix.upper())
                        newSuffix= standardSuffixes[idx] 
                    elif suffix.upper() in standardSuffixes:
                        newSuffix= suffix.upper()
                    else:
                        newSuffix = suffix.upper()
                    
                newName = row[1]          
                newRow= [newPrefix,newName,newSuffix]
                    
                #print names
                
                arcpy.AddMessage("old row = "+str(row))
                arcpy.AddMessage("new row = "+str(newRow))
                del newSuffix    
                del newPrefix
                del newName
        del row
        cursor.updateRow(newRow)
 