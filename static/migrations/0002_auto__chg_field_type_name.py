# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Type.name'
        db.alter_column('invTypes', 'typeName', self.gf('django.db.models.fields.CharField')(max_length=200, db_column='typeName'))

    def backwards(self, orm):

        # Changing field 'Type.name'
        db.alter_column('invTypes', 'typeName', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='typeName'))

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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "'typeName'"}),
            'published': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['static']