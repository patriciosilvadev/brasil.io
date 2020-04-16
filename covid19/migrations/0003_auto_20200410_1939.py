# Generated by Django 2.2 on 2020-04-10 22:39
from localflavor.br.br_states import STATE_CHOICES

from django.conf import settings
from django.db import migrations


def create_covid19_state_permissions(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    StateSpreadsheet = apps.get_model('covid19', 'StateSpreadsheet')

    content_type = ContentType.objects.get_for_model(StateSpreadsheet)
    for uf, name in STATE_CHOICES:
        codename = settings.COVID_IMPORT_PERMISSION_PREFIX + uf
        name = f'Can import Covid-19 data for {name}'
        Permission.objects.create(codename=codename, name=name, content_type=content_type)


def delete_covid19_state_permissions(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    Permission.objects.filter(codename__startswith=settings.COVID_IMPORT_PERMISSION_PREFIX).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0011_update_proxy_permissions'),
        ('covid19', '0002_auto_20200410_1919'),
    ]

    operations = [
        migrations.RunPython(
            create_covid19_state_permissions,
            delete_covid19_state_permissions,
        )
    ]