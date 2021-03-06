# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from utils import getVal

# Create your models here.
class CensusTract(models.Model):
  year = models.CharField(max_length=5)
  tract_number = models.IntegerField()
  black_total = models.IntegerField()
  white_total = models.IntegerField()
  population_total = models.IntegerField()
  county = models.IntegerField()
  state = models.IntegerField()

  def __str__(self):
      return str(self.tract_number)+ ' : ' + str(self.year)

  @classmethod
  def create(self, response, census_map, data_year):
      """Parse the response and then create a workable object for
        saving the tract object
      """
      response_val = response.json()
      res_dict = dict(zip(response_val[0], response_val[1]))
      model_dict = {census_map[name]: val for name, val in res_dict.iteritems()}
      model_dict['year'] = data_year
      tract = self(**model_dict)
      tract.save()
      return tract

  @property
  def percent_black(self):
    total = self.population_total
    black = self.black_total
    if total and black:
        return int(100 * (float(black) / total))
    return None
  @property
  def percent_white(self):
    total = self.population_total
    white = self.white_total
    if total and white:
        return int(100 * (float(white) / total))
    return none


class Property(models.Model):
  # noinspection PyInterpreter
  """A Property that is going up for auction including whether the property was
      Deeded or Not.
    """
  year = models.IntegerField()
  address = models.CharField(max_length=50)
  property_pin = models.IntegerField()
  zip_code = models.IntegerField(null=True, blank=True)
  property_value = models.IntegerField(null=True)
  property_class_code = models.CharField(max_length=50, null=True)
  owner_address = models.CharField(null=True,max_length=50)
  lat = models.FloatField(null=True,)
  lng = models.FloatField(null=True,)
  min_bid = models.DecimalField(null=True,max_digits=20,decimal_places=2)
  status = models.CharField(max_length=15, null=True)
  highest_sales_price = models.DecimalField(null=True,max_digits=20,decimal_places=2)
  finished_sq_feet = models.PositiveSmallIntegerField(null=True,)
  acreage = models.DecimalField(max_digits=10,decimal_places=2, null=True)
  bedrooms = models.PositiveSmallIntegerField(null=True,)
  constructed_year = models.PositiveSmallIntegerField(null=True,)
  census_tract = models.ForeignKey(CensusTract, null=True, on_delete = models.CASCADE)

  class Meta:
      verbose_name_plural = "properties"
  def __str__(self):
    return self.address + ' : ' + str(self.year) + " :  " + str(self.status)


  @classmethod
  def create(self, location_dict, csv_dict):
    dict_map = {
        'year' : ('TaxYear', 'year'),
        'address': ('Parcel Address', 'address'),
        'property_pin': ('Pin',),
        'census_tract': ('census_tract','Tract', 'tract'),
        'zip_code': ('Zip',),
        'min_bid': ('Min. Bid',),
        'property_value': ('Market','property_value'),
        'property_class_code': ('PropertyClassCode','property_class_code'),
        'owner_address': ('Owner Address',),
        'lat': ('lat', 'Lat'),
        'lng': ('lng', 'Lng'),
        'status': ('Status',),
        'highest_sales_price': ('HighestSalePrice','highest_sales_price'),
        'finished_sq_feet': ('FinishedSqFt.', 'finished_sq_feet'),
        'acreage': ('Acreage','acreage'),
        'bedrooms': ('Bedrooms', 'bedrooms'),
        'constructed_year': ('Constructed Year','constructed_year'),
    }
    csv_dict.update(location_dict)
    mapped_dict = {key: getVal(opts, csv_dict) for key, opts in dict_map.iteritems()}
    properties = self.objects.filter(property_pin=mapped_dict['property_pin'], year=mapped_dict['year'])
    if not properties:
        property = self(**mapped_dict)
        property.save()
        return property
    else:
        return properties[0]

