import simplekml
import geocoder
import pickle

with open('my_dict.pkl', 'rb') as f:
    mydict = pickle.load(f)

# Use SimpleKml to write the KML file
kml = simplekml.Kml()
for ctgy in mydict:
    fol = kml.newfolder(name=ctgy)
    for entry in mydict[ctgy]:
        # Geocode addresses
        g = geocoder.google(entry["LOCATION NAME"])  # Customize this column name
        pnt = fol.newpoint(name=entry["CUSTOMER NAME"], coords=[(g.lng, g.lat)], description=entry["STATUS"])  # Customize these column names
        if entry["REP CATEGORY"] != "":
            pnt.style.iconstyle.icon.href = entry["REP CATEGORY"]  # Customize this column name

kml.save("output.kml")