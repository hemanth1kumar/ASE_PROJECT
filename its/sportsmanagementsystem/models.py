from django.db import models
import django.utils.timezone
# Create your models here.

class Player(models.Model):
	student_id=models.CharField(max_length=200)
	first_name = models.CharField(max_length=42)
	last_name = models.CharField(max_length=42)
	email_id = models.EmailField(max_length=75)
	phone_no =models.CharField(max_length=10) 
	sport_id = models.CharField(max_length=200)
	password= models.CharField('password',max_length=50)
	year = models.IntegerField()
	id=models.CharField(primary_key=True,max_length=200)

class Sport(models.Model):
	sport_id = models.CharField(primary_key=True,max_length=200) 
	sport_name = models.CharField(max_length=42)
	equipment = models.CharField(max_length=75)
	catogery=models.CharField(max_length=10) 
	no_of_players = models.IntegerField()

class Coach(models.Model):
	coach_id=models.CharField(primary_key=True,max_length=200)
	coach_name = models.CharField(max_length=42)
	sport_name = models.CharField(max_length=200)
	coach_type =models.CharField(max_length=10)
	experience= models.IntegerField() 
	contact= models.CharField(max_length=200)
	password= models.CharField('password',max_length=50)

class Complaint(models.Model):
	complaint_id=models.CharField(primary_key=True,max_length=200)
	student_id=models.CharField(max_length=200)
	about= models.TextField(max_length=42)
	datetime=models.DateTimeField(auto_now_add=True)

class Tournament(models.Model):
	tournament_id=models.CharField(primary_key=True,max_length=12)
	sport_id = models.CharField(max_length=200)
	level =models.CharField(max_length=200)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	result= models.CharField(max_length=50)	

class Schedule(models.Model):
	tournament_name=models.CharField(max_length=12)
	sport_name = models.CharField(max_length=200)
	opponent_1 =models.CharField(max_length=10) 
	opponent_2 = models.CharField(max_length=200)
	sport_name=models.CharField(max_length=200)
	tournament_id=models.CharField(max_length=12)
	datetime = models.DateTimeField()
	match_id = tournament_id=models.CharField(max_length=12)
class announcement(models.Model):
	annoucement_id=models.IntegerField(primary_key=True)
	sender=models.CharField(max_length=10) 
	receiver= models.CharField(max_length=200)
	message = models.TextField()
	datetime = models.DateTimeField()

class Performance(models.Model):
	id=models.CharField(max_length=200)
	sport_id=models.CharField(max_length=200)
	role=models.CharField(max_length=10) 
	performance= models.CharField(max_length=200)
	date = models.DateTimeField()