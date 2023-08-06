# django_ga
django google analytics
credit: clintecker
ref: https://github.com/clintecker/django-google-analytics

ใช้งาน
1. เพิ่ม django.contrib.sites ใน INSTALLED_APPS ของไฟล์ settings.py
2. เพิ่ม SITE_ID = 1 ในไฟล์ settings.py 
3. เพิ่ม google_analytics ใน INSTALLED_APPS ของไฟล์ settings.py
4. run ./manage.py migrate 
5. ไปที่หน้า admin จะเห็นหัวข้อ GOOGLE_ANALYTICS แล้วไปสร้าง Analytics ใส่ Analytics Code (ex UA-xxxxxx-x)
6. นำ {% load analytics %} ไปไว้ในหน้า template เช่น base.html
7. ใช้คำสั่ง {% analytics %} ในหน้าเดียวกับข้อ 6
