
# Generated by Django 3.0.3 on 2021-02-07 12:00

# Generated by Django 3.0.3 on 2021-02-15 11:57


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('service', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('note', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Appointment',
            },

        ),
    ]
