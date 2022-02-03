from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):

    #Defining the fields
    m_ID = models.CharField(max_length = 20)
    m_name = models.CharField(max_length = 100)
    m_dir_name = models.CharField(max_length = 100)
    
    #Use Min and Max value validators where needed
    #m_release_year >= 1800
    m_release_year = models.IntegerField(validators = [MinValueValidator(
        limit_value = 1800, 
        message = "Please enter a year >= 1800." #Error message
    )])

    #0 <= m_ratings <= 100
    m_ratings = models.IntegerField(validators = [MinValueValidator(
        limit_value = 0,
        message = "Please enter a value >= 0." #Error message
    ),
    MaxValueValidator(
        limit_value = 100,
        message = "Please enter a value <= 100." #Error message
    )])

    class Meta:
        db_table = "movies"