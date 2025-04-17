from django.contrib.gis.db import models
from django.contrib.gis.db.models.functions import GeoFunc


# from django.db import models
class Buffer(GeoFunc):
    function='ST_Buffer'

class Pipe(models.Model):
    geom = models.LineStringField(srid=4326)
    closed = models.BooleanField(default=False)


class Valve(models.Model):
    geom = models.PointField(srid=4326)
    closed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        Pipe.objects.filter(geom__intersects=self.geom).update(closed=self.closed)
        # Pipe.objects.filter(geom__intersects=Buffer(self.geom, 100)).update(closed=self.closed)
        super(Valve, self).save(*args, **kwargs)
