from django.db import models
from django.db.models import Sum, F, FloatField
# Create your models here.


class Record(models.Model):
	GENRE = (('Fictions', 'Fictions'),
			('Poems', 'Poems'),
			('Essays', 'Essays'),
			('Plays', 'Plays'),
			('Childrens', 'Childrens'),
			('Classic_General', 'Classic_General'),
			('Classic_Poem', 'Classic_Poem'),
			('Classic_History', 'Classic_History'),
			('Classic_Folk Tale', 'Classic_Folk Tale'),
			('Classic_Fiction', 'Classic_Fiction'),
			('Misc','Misc'))
	authorKorean = models.CharField(max_length=100, null=True, blank=True ,default="")
	authorEnglish = models.CharField(max_length=100, null=True, blank=True,default="")
	workTitle = models.CharField(max_length=100, null=True, blank=True,default="")
	genre= models.CharField(max_length=200, null=True, choices=GENRE, blank=True, default=GENRE[1])
	translator = models.CharField(max_length=100, null=True, blank=True,default="")
	sourceTitle = models.CharField(max_length=100, null=True, blank=True,default="")
	publisher = models.CharField(max_length=100, null=True, blank=True,default="")
	year = models.CharField(max_length=100,null=True, blank=True, default=" ")
	yearCreated = models.FloatField(null=True, blank=True, default=00.00)
	authorEnglish2 = models.CharField(max_length=300, null=True, blank=True, default="")
	uid2 = models.CharField(max_length=100, default="Not Registered yet")



class AddRequest(models.Model):
	requestid = models.CharField(max_length=100, null=True, blank=True ,default="")
	accepted = models.BooleanField(default=False, null=False)

	GENRE = (('Fictions', 'Fictions'),
			('Poems', 'Poems'),
			('Essays', 'Essays'),
			('Plays', 'Plays'),
			('Childrens', 'Childrens'),
			('Classic_General', 'Classic_General'),
			('Classic_Poem', 'Classic_Poem'),
			('Classic_History', 'Classic_History'),
			('Classic_Folk Tale', 'Classic_Folk Tale'),
			('Classic_Fiction', 'Classic_Fiction'),
			('Misc','Misc'))
	authorKorean = models.CharField(max_length=100, null=True, blank=True ,default="")
	authorEnglish = models.CharField(max_length=100, null=True, blank=True,default="")
	workTitle = models.CharField(max_length=100, null=True, blank=True,default="")
	genre= models.CharField(max_length=200, null=True, choices=GENRE, blank=True, default=GENRE[1])
	translator = models.CharField(max_length=100, null=True, blank=True,default="")
	sourceTitle = models.CharField(max_length=100, null=True, blank=True,default="")
	publisher = models.CharField(max_length=100, null=True, blank=True,default="")
	year = models.CharField(max_length=100,null=True, blank=True, default=" ")
	yearCreated = models.FloatField(null=True, blank=True, default=00.00)
	authorEnglish2 = models.CharField(max_length=300, null=True, blank=True, default="")
	uid2 = models.CharField(max_length=100, default="Not Registered yet")
	other = models.CharField(max_length=300, null=True, blank=True, default="")

