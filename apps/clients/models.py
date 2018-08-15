from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	payday = models.DateTimeField(blank=True, null=True)
	info = models.TextField(blank=True, null=True)
	amount = models.CharField(blank=True, null=True, max_length=75)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.user.username}'



# @receiver(post_save, sender=User)
# def create_user_customer(sender, instance, created, **kwargs):
# 	if created:
# 		Client.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_customer(sender, instance, **kwargs):
#     instance.client.save()
