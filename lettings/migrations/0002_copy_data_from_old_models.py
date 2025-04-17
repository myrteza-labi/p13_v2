from django.db import migrations


def copy_lettings_data(apps, schema_editor):
    pass
    # OldAddress = apps.get_model('oc_lettings_site', 'Address')  # Désactivé pour les tests
    # OldLetting = apps.get_model('oc_lettings_site', 'Letting')  # Désactivé pour les tests

    # NewAddress = apps.get_model('lettings', 'Address')
    # NewLetting = apps.get_model('lettings', 'Letting')

    # Boucle désactivée car elle dépend des anciens modèles
    # for old_address in OldAddress.objects.all():
    #     new_address = NewAddress.objects.create(
    #         number=old_address.number,
    #         street=old_address.street,
    #         city=old_address.city,
    #         state=old_address.state,
    #         zip_code=old_address.zip_code,
    #         country_iso_code=old_address.country_iso_code
    #     )

    #     # Lier le letting à la nouvelle adresse
    #     old_letting = OldLetting.objects.get(address=old_address)
    #     NewLetting.objects.create(
    #         title=old_letting.title,
    #         address=new_address
    #     )


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_lettings_data),
    ]
