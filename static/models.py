from django.db import models

class Type(models.Model):
    id = models.IntegerField(primary_key=True, db_column='typeID')
    name = models.CharField(max_length=200, db_column='typeName')
    published = models.BooleanField()

    class Meta:
        db_table = 'invTypes'

class Item(models.Model):
    id = models.IntegerField(primary_key=True, db_column='itemID')
    type = models.ForeignKey(Type, db_column='typeID')
    location = models.ForeignKey('self', db_column='locationID', related_name='contains')

    class Meta:
        db_table = 'invItems'

class Region(models.Model):
    id = models.IntegerField(primary_key=True, db_column='regionID')
    name = models.CharField(max_length=50, db_column='regionName')

    class Meta:
        db_table = 'mapRegions'

class Constellation(models.Model):
    id = models.IntegerField(primary_key=True, db_column='constellationID')
    region = models.ForeignKey(Region, db_column='regionID')
    name = models.CharField(max_length=50, db_column='constellationName')

    class Meta:
        db_table = 'mapConstellations'

class SolarSystem(models.Model):
    id = models.IntegerField(primary_key=True, db_column='solarSystemID')
    name = models.CharField(max_length=50, db_column='solarSystemName')
    constellation = models.ForeignKey(Constellation, db_column='constellationID')
    security = models.DecimalField(max_digits=5, decimal_places=4)

    class Meta:
        db_table = 'mapSolarSystems'

class MapItem(Item):
    item = models.OneToOneField(Item, primary_key=True, parent_link=True,
                              db_column='itemID')
    solar_system = models.ForeignKey(SolarSystem, db_column='solarSystemID',
                                     null=True)
    constellation = models.ForeignKey(Constellation, db_column='constellationID',
                                      null=True)
    region = models.ForeignKey(Region, db_column='regionID', null=True)
    planetary_orbit = models.IntegerField(null=True, db_column='orbitIndex')
    solar_orbit = models.IntegerField(null=True, db_column='celestialIndex') 

    class Meta:
        db_table = 'mapDenormalize'

