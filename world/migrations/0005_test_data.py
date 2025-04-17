from django.db import migrations


def test_data(apps, _schema_editor):
    Pipe = apps.get_model('world', 'Pipe')
    Pipe.objects.create(geom='SRID=4326;LINESTRING(6.4961 46.4359, 7.4709 46.8374)', closed=False)
    Pipe.objects.create(geom='SRID=4326;LINESTRING(5.0687 45.8711, 5.9539 48.8678)', closed=False)
    Pipe.objects.create(geom='SRID=4326;LINESTRING(9.1834 45.9487, 9.3187 46.9156, 8.5411 46.9733, 7.8649 46.1481)', closed=False)

    Valve = apps.get_model('world', 'Valve')
    Valve.objects.create(geom='SRID=4326;POINT(6.7136 46.5999)', closed=False)
    Valve.objects.create(geom='SRID=4326;POINT(6.8787 46.6151)', closed=False)
    Valve.objects.create(geom='SRID=4326;POINT(6.7599 46.5673)', closed=False)
    Valve.objects.create(geom='SRID=4326;POINT(6.5818 46.6849)', closed=False)

class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_alter_pipe_geom_alter_valve_geom'),
    ]

    operations = [
        migrations.RunPython(test_data),
    ]
