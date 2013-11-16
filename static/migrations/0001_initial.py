# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Type'
        db.create_table('invTypes', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='typeID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='typeName')),
            ('published', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'static', ['Type'])

        # Adding model 'Item'
        db.create_table('invItems', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='itemID')),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['static.Type'], db_column='typeID')),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contains', db_column='locationID', to=orm['static.Item'])),
        ))
        db.send_create_signal(u'static', ['Item'])

        # Adding model 'Region'
        db.create_table('mapRegions', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='regionID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='regionName')),
        ))
        db.send_create_signal(u'static', ['Region'])

        # Adding model 'Constellation'
        db.create_table('mapConstellations', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='constellationID')),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['static.Region'], db_column='regionID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='constellationName')),
        ))
        db.send_create_signal(u'static', ['Constellation'])

        # Adding model 'SolarSystem'
        db.create_table('mapSolarSystems', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='solarSystemID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='solarSystemName')),
            ('constellation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['static.Constellation'], db_column='constellationID')),
            ('security', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=4)),
        ))
        db.send_create_signal(u'static', ['SolarSystem'])

        # Adding model 'MapItem'
        db.create_table('mapDenormalize', (
            ('item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['static.Item'], unique=True, primary_key=True, db_column='itemID')),
            ('solar_system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['static.SolarSystem'], null=True, db_column='solarSystemID')),
            ('constellation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['static.Constellation'], null=True, db_column='constellationID')),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['static.Region'], null=True, db_column='regionID')),
            ('planetary_orbit', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='orbitIndex')),
            ('solar_orbit', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='celestialIndex')),
        ))
        db.send_create_signal(u'static', ['MapItem'])


    def backwards(self, orm):
        # Deleting model 'Type'
        db.delete_table('invTypes')

        # Deleting model 'Item'
        db.delete_table('invItems')

        # Deleting model 'Region'
        db.delete_table('mapRegions')

        # Deleting model 'Constellation'
        db.delete_table('mapConstellations')

        # Deleting model 'SolarSystem'
        db.delete_table('mapSolarSystems')

        # Deleting model 'MapItem'
        db.delete_table('mapDenormalize')


    models = {
        u'static.constellation': {
            'Meta': {'object_name': 'Constellation', 'db_table': "'mapConstellations'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'constellationID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'constellationName'"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['static.Region']", 'db_column': "'regionID'"})
        },
        u'static.item': {
            'Meta': {'object_name': 'Item', 'db_table': "'invItems'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'itemID'"}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contains'", 'db_column': "'locationID'", 'to': u"orm['static.Item']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['static.Type']", 'db_column': "'typeID'"})
        },
        u'static.mapitem': {
            'Meta': {'object_name': 'MapItem', 'db_table': "'mapDenormalize'", '_ormbases': [u'static.Item']},
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['static.Constellation']", 'null': 'True', 'db_column': "'constellationID'"}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['static.Item']", 'unique': 'True', 'primary_key': 'True', 'db_column': "'itemID'"}),
            'planetary_orbit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'orbitIndex'"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['static.Region']", 'null': 'True', 'db_column': "'regionID'"}),
            'solar_orbit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'celestialIndex'"}),
            'solar_system': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['static.SolarSystem']", 'null': 'True', 'db_column': "'solarSystemID'"})
        },
        u'static.region': {
            'Meta': {'object_name': 'Region', 'db_table': "'mapRegions'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'regionID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'regionName'"})
        },
        u'static.solarsystem': {
            'Meta': {'object_name': 'SolarSystem', 'db_table': "'mapSolarSystems'"},
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['static.Constellation']", 'db_column': "'constellationID'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'solarSystemID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'solarSystemName'"}),
            'security': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '4'})
        },
        u'static.type': {
            'Meta': {'object_name': 'Type', 'db_table': "'invTypes'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'typeID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'typeName'"}),
            'published': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['static']