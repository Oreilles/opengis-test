from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Pipe, Valve


class PipeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Pipe
        fields = ['id', 'geom']
        geo_field = "geom"
        auto_bbox = True


class ValveSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Valve
        fields = ['id', 'geom']
        geo_field = "geom"
