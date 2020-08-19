from django.db import models

# Create your models here.


class Service(models.Model):
    driver = models.ForeignKey(
        'driver.Driver', on_delete=models.CASCADE, verbose_name='사용자')
    content = models.TextField(verbose_name='배송 정보')
    delivery = models.ImageField(
        upload_to='map', verbose_name='배송')  # 과거 배송건을 기록
    use_date = models.DateTimeField(auto_now_add=True, verbose_name='사용날짜')

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'shortD_service'
        verbose_name = '배송'
        verbose_name_plural = '배송'
