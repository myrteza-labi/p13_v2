from django.db import migrations

def copy_data_from_old_models(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    for old in OldProfile.objects.all():
        fields = [f.name for f in OldProfile._meta.fields if f.name != 'id']
        data = {field: getattr(old, field) for field in fields}
        NewProfile.objects.create(**data)

def reverse_copy_data(apps, schema_editor):
    NewProfile = apps.get_model('profiles', 'Profile')
    NewProfile.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_data_from_old_models, reverse_copy_data),
    ]
