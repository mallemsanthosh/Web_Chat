# Generated by Django 3.2.3 on 2021-05-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chattables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sender_id', models.CharField(max_length=20)),
                ('Recever_id', models.CharField(max_length=20)),
                ('Message', models.CharField(max_length=200)),
                ('Files22', models.FileField(default='null', upload_to='chatting/files/')),
                ('timeanddate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='maintables',
            fields=[
                ('User_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('MName', models.CharField(max_length=60)),
                ('e_mail', models.EmailField(default='fff@gmail.com', max_length=254)),
                ('Phone_No', models.CharField(max_length=10)),
                ('UniqeUserNu', models.IntegerField(unique=True)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]