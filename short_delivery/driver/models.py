from django.db import models

# Create your models here.


class Driver(models.Model):
    email = models.EmailField(verbose_name='이메일')
    name = models.CharField(max_length=32, verbose_name='이름', default=None)
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'shortD_Driver'
        verbose_name = '운전자'
        verbose_name_plural = '운전자'
