from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )
    title2 = models.CharField(
        max_length=155,
        verbose_name='Заголовок About'
    )
    description2 = models.TextField(
        verbose_name='Описание About'
    )
    image2 = models.ImageField(
        upload_to='settings',
        verbose_name='Фото About'
    )
    title_bonus1 = models.CharField(
        max_length=155,
        verbose_name='Заголовок Bonus'
    )
    title_bonus2 = models.CharField(
        max_length=155,
        verbose_name='Заголовок Bonus2'
    )
    title_team = models.CharField(
        max_length=155,
        verbose_name='Заголовок Team'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Главная НАстройки'


class ImageSlider(models.Model):
    image = models.ImageField(
        upload_to='image',
        verbose_name='Фото'
    )

    class Meta:
        verbose_name_plural = 'Фото Слайдер'

class Bonus(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Наши Бонусы'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Наши бонусы'
    
class Team(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    role = models.TextField(
        verbose_name='Должность'
    )
    image = models.ImageField(
        upload_to='team',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Наша команда' 


##################################

class About(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='about',
        verbose_name='Фото'
    )
    text = models.TextField(
        verbose_name='Текст'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'О нас'

#####################################


class Services(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок',
        default='Экопродукты',
        blank=True, null=True
    )
    title2 = models.CharField(
        max_length=155,
        verbose_name='Заголовок 2',
        default='Продукты с заботой о планете',
        blank=True, null=True
    )
    title_obj = models.CharField(
        max_length=155,
        verbose_name='Заголовка Объекта'
    )
    image_obj = models.ImageField(
        upload_to='services',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Наши услуги'