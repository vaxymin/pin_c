from django.db import models


# Create your models here.


class UserPinner(models.Model):
    user_id = models.CharField(primary_key=True, editable=False, max_length=255)
    user_name = models.CharField(max_length=100)
    user_surname = models.CharField(max_length=100)
    avatar = models.URLField(blank=True)

    def print_attr(self):
        for k, v in self.__dict__.items():
            if '__' not in k:
                print("{}: {}".format(k, v))

    def __str__(self):
        return self.user_name


class Board(models.Model):
    board_id = models.CharField(primary_key=True, editable=False, max_length=255)
    pin_name = models.CharField(max_length=25)
    user_pinner = models.ForeignKey(UserPinner, on_delete=models.CASCADE)

    def print_attr(self):
        for k, v in self.__dict__.items():
            if '__' not in k:
                print("{}: {}".format(k, v))

    def __str__(self):
        return self.pin_name


class Pin(models.Model):
    pin_id = models.CharField(primary_key=True, editable=False, max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=50, blank=True)

    def print_attr(self):
        for k, v in self.__dict__.items():
            if '__' not in k:
                print("{}: {}".format(k, v))

    def __str__(self):
        return self.title


class Image(models.Model):
    image_id = models.CharField(primary_key=True, editable=False, max_length=255)
    pin = models.ForeignKey(Pin, related_name='images', on_delete=models.CASCADE)
    url = models.URLField(blank=True, null=True)

    def print_attr(self):
        for k, v in self.__dict__.items():
            if '__' not in k:
                print("{}: {}".format(k, v))

    def __str__(self):
        return self.url
