# Generated by Django 3.2.6 on 2021-09-02 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mark',
            options={'verbose_name': 'Марка', 'verbose_name_plural': 'Марки'},
        ),
        migrations.RenameField(
            model_name='mark',
            old_name='bramd',
            new_name='brand',
        ),
    ]