from django.db import models

class Books(models.Model):
    book_id = models.AutoField
    book_name = models.CharField(max_length=500)
    category = models.CharField(max_length=500, default="")
    subcategory = models.CharField(max_length=500, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=30000000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="app/images", default="")

    def __str__(self):
        return self.book_name

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111, default="")


    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    named = models.CharField(max_length=100000, default="")
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.named

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    query= models.TextField(default="")

    def __str__(self):
        return self.name