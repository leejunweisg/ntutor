# Generated by Django 3.1.6 on 2021-02-26 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('listingID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('datePosted', models.DateTimeField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('schoolCode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('schoolName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TuitionSession',
            fields=[
                ('tuitionSessionID', models.AutoField(primary_key=True, serialize=False)),
                ('completed', models.BooleanField(default=False)),
                ('learner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='learner', to='users.profile')),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.listing')),
                ('tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tutor', to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('moduleID', models.AutoField(primary_key=True, serialize=False)),
                ('moduleCode', models.CharField(max_length=20)),
                ('moduleName', models.CharField(max_length=200)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.school')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.module'),
        ),
        migrations.AddField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]