from django.db import models
class maintables(models.Model):
    User_id=models.CharField(max_length=20,unique=True,primary_key=True)
    MName=models.CharField(max_length=60)
    e_mail=models.EmailField(max_length=254,default='fff@gmail.com')
    Phone_No=models.CharField(max_length=10)
    UniqeUserNu=models.IntegerField(unique=True,null=False)
    password=models.CharField(max_length=10)




    def __str__(self):
        return self.User_id


class chattables(models.Model):
    Sender_id=models.CharField(max_length=20)
    Recever_id=models.CharField(max_length=20)
    Message=models.CharField(max_length=200)
    Files22=models.FileField(upload_to="chatting/files/",default="null")
    timeanddate=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.Sender_id
# Create your models here.
