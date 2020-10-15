import simplekml
import sys
import os
import re


class convert_kmz():

    def __init__(self,**kwargs):
        self.KMLwriter()


    def KMLwriter(self):
        
        # Read the data.txt which is copied from tkgm 
        with open("data.txt") as file_in:
            lineCount=0
            linesArray = []
            for line in file_in:
                lineCount= lineCount +1
                clearLine=re.sub('\s+', ' ', line)
                linesArray.append(clearLine.split())
            

        # Arrange the datas, first append them to a list one by one. 
        newList =[]
        newCount=0
        for i in range(1,lineCount):
            for j in range (1,3):
                newCount = newCount +1
                newList.append(linesArray[i][j])

        # Arrange the datas, then make the coords float. 
        floatList=[]
        floatCount=0
        for i in range(0,newCount):
            floatCount = floatCount +1
            floatList.append(float(newList[i]))
        
        # Arrange the datas, then make them tuples as long lat duos. 
        mappedList=[]
        for i in range(0,newCount):
            if (i%2==0):
                mappedList.append(tuple((floatList[i+1], floatList[i])))
        print(mappedList)


        kml = simplekml.Kml()

        # Note that our polygon outerboundary gets the array we created. 
        pol = kml.newpolygon(name="TKGM Parsel Lokasyonu",
                     outerboundaryis=mappedList)
                     
        pol.style.polystyle.outline = 1
        pol.style.polystyle.colormode = 'random'

        # Save the KML
        kml.savekmz('Parsel.kml')


if __name__ == '__main__':
    convert_kmz()