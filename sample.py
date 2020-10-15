import simplekml

kml = simplekml.Kml()

pol = kml.newpolygon(name="Atrium Garden",
                     outerboundaryis=[(18.43348,-33.98985), (18.43387,-33.99004),
                                      (18.43410,-33.98972), (18.43371,-33.98952),
                                      (18.43348,-33.98985)])


kml.newpoint(name="Home", coords=[( 19.033002,21.026512 )])
# boylam , enlem
# longtitude , latitude

kml.save("samplePolygon.kml")