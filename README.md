import pandas as pd
import simplekml

df = pd.read_excel("test.xls").fillna('')

location_set = []
[location_set.append(i) for i in list(df['LOCATION NAME']) if not i in location_set]
kml = simplekml.Kml()
doc = kml.newdocument(name = 'Test Location')
fld = []
pnt = []
for i in range(len(location_set)):
    fld.append(doc.newfolder(name = location_set[i]))

sharedstyle = simplekml.Style()
sharedstyle.labelstyle.scale = 0.85
sharedstyle.iconstyle.color = 'ff0000aa'
sharedstyle.iconstyle.scale = 0.7
sharedstyle.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
      

for j in range(len(df['ID'])):
    pnt.append(fld[location_set.index(df.loc[j]['LOCATION NAME'])].newpoint())
    pnt[j].name = df.loc[j]['CUSTOMER NAME']
    pnt[j].description = df.loc[j]['REGION NAME'] + ',' + df.loc[j]['REP CATEGORY'] + ',' + df.loc[j]['STATUS'] 
    pnt[j].coords = [(df.loc[j]['LONGITUDE'], df.loc[j]['LATITUDE'])]
    pnt[j].style = sharedstyle

kml.save('test.kml')
