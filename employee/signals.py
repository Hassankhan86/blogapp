# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from .models import Employee

# # @receiver(post_save, sender=User)
# def customer_profile(sender, instance, created, **kwargs):
#     if created:
#         Employee.objects.create(
#             user=instance,
#             fullname=instance.username,
    



#         )

      
#         print('Profile Created')

# post_save.connect(customer_profile,sender=User)