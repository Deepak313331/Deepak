from django.db import models


class UserDetailss(models.Model):
    nname = models.CharField(max_length=50)
    eemail = models.CharField(max_length=50)
    eephone = models.IntegerField()
    epas = models.CharField(max_length=50)
    eadd = models.CharField(max_length=50)
    egen = models.CharField(max_length=10)
    elook = models.CharField(max_length=50)

    def __str__(self):
        return "NAME IS::" + str(self.nname) + "Email ID is::" + str(self.eemail) + "Phone::" + str(
            self.eephone) + "Users's Password::" + str(self.epas) + "Gender::" + str(self.egen) + "Looking For::" + str(
            self.elook)


class admindetails(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class ownersignup(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()


class category(models.Model):
    cat_id = models.IntegerField()
    cat_name = models.CharField(max_length=20)


class sub_cat(models.Model):
    sub_cat_id = models.IntegerField()
    sub_cat_name = models.CharField(max_length=20)
    cat_id = models.IntegerField()


class view_room_db(models.Model):
    location = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    file_upload = models.CharField(max_length=100, default='')
    room_price = models.IntegerField()
    room_facility = models.CharField(max_length=50)


class image_upload(models.Model):
    file_uplo = models.CharField(max_length=50)


class db_try(models.Model):
    db = models.CharField(max_length=50, default='')