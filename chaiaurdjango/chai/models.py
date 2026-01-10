from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# CHAI VARIETY MODEL
class ChaiVariety(models.Model):
  CHAI_TYPE_CHOICE = [
    ('ML', "MASALA"),
    ('GR', "GINGER"),
    ('KL', "KIWI"),
    ('PL', "PLAIN"),
    ('EL', "ELAICHI"),
  ]
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to="chai/")
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
  price = models.DecimalField(max_digits=4,decimal_places=2, default=0.00)
  description = models.TextField(default="")


  def __str__(self):
    return self.name
  

# RATING CLASS
class RatingChoices(models.IntegerChoices):
  ONE= 1, "1 Star"
  TWO= 2, "2 Star"
  THREE= 3, "3 Star"
  FOUR= 4, "4 Star"
  FIVE= 5, "5 Star"
  
# 1 : MANY
class ChaiReview(models.Model):
  chai = models.ForeignKey(
    ChaiVariety, 
    on_delete = models.CASCADE,
    related_name="chai_reviews"
    )
  
  user = models.ForeignKey(
    User, 
    on_delete= models.CASCADE,
    related_name= "chai_reviews"
    )
  
  reviews = models.IntegerField(choices= RatingChoices.choices)
  comment = models.TextField(blank=True)
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
      return f'{self.user.username} review for {self.chai.name}'

# MANY : MANY

class Store(models.Model):
  name= models.CharField(max_length=100)
  location= models.CharField(max_length=100)
  chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')

  def __str__(self):
    return self.name


# 1:1
class ChaiCertificate(models.Model):
  chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
  certificate_number= models.CharField(max_length=100)
  issued_date= models.DateTimeField(default=timezone.now)
  valid_untill = models.DateTimeField()

  def __str__(self):
    return f'Certificate for {self.chai.name}'
   