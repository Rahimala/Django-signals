# from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete
#
# @receiver(user_logged_in, sender=User)
# def login_success(sender, request, user, **kwargs):
#     print("-------------------------------------")
#     print("Logged in signal.. Run Intro")
#     print("Sender:", sender)
#     print("Request:", request)
#     print("User:", user)
#     print("User Password:", user.password)
#     print(f'kwargs: {kwargs}')
# #user_logged_in.connect(login_success, sender=User)
#
# @receiver(user_logged_out, sender=User)
# def log_out(sender, request, user, **kwargs):
#     print("-------------------------------------")
#     print("Logged Out signal.. Run Intro...")
#     print("Sender:", sender)
#     print("Request:", request)
#     print("User:", user)
#     print("User Password:", user.password)
#     print(f'kwargs: {kwargs}')
# #ser_logged_out.connect(log_out, sender=User)
#
# @receiver(user_login_failed)
# def login_failed(sender, request,credentials, **kwargs):
#     print("-------------------------------------")
#     print("Login failed signal...")
#     print("Sender:", sender)
#     print("Credentials:", credentials)
#     print("Request:", request)
#     print(f'kwargs: {kwargs}')
# #user_login_failed.connect(login_failed
#
# @receiver(pre_save, sender=User)
# def at_beginnng_save(sender, instance, **kwargs):
#         print("-------------------------------------")
#         print("Pre Save signal...")
#         print("Sender:", sender)
#         print("Instance:", instance)
#         print(f'kwargs: {kwargs}')
# #pre_save.connect(at_beginnng_save, sender=User)
#
# @receiver(post_save, sender=User)
# def at_ending_save(sender, instance, created, **kwargs):
#     if created:
#         print("-------------------------------------")
#         print("Post Save signal...")
#         print("New Record")
#         print("Sender:", sender)
#         print("Instance:", instance)
#         print("Created:", created)
#         print(f'kwargs: {kwargs}')
#     else:
#         print("-------------------------------------")
#         print("Post Save signal...")
#         print("New Update")
#         print("Sender:", sender)
#         print("Instance:", instance)
#         print(f'kwargs: {kwargs}')
#
# #post_save.connect(at_ending_save, sender=User)
#
# @receiver(pre_delete, sender=User)
# def at_beginnng_delete(sender, instance, **kwargs):
#         print("-------------------------------------")
#         print("Pre Delete Signal...")
#         print("Sender:", sender)
#         print("Instance:", instance)
#         print(f'kwargs: {kwargs}')
# #pre_delete.connect(at_beginnng_delete, sender=User)
#
# @receiver(post_delete, sender=User)
# def at_ending_delete(sender, instance, **kwargs):
#         print("-------------------------------------")
#         print("Post Delete Signal...")
#         print("Sender:", sender)
#         print("Instance:", instance)
#         print(f'kwargs: {kwargs}')
# #post_delete.connect(at_ending_delete, sender=User)
#
# @receiver(pre_init, sender=User)
# def at_beginnng_init(sender, *args, **kwargs):
#         print("-------------------------------------")
#         print("Pre Init Signal...")
#         print("Sender:", sender)
#         print(f'Args: {args}')
#         print(f'kwargs: {kwargs}')
# #pre_init.connect(at_beginnng_init, sender=User)
#
# @receiver(post_init, sender=User)
# def at_ending_init(sender, *args, **kwargs):
#         print("-------------------------------------")
#         print("Post init Signal...")
#         print("Sender:", sender)
#         print(f'Args: {args}')
#         print(f'kwargs: {kwargs}')
# #post_init.connect(at_ending_init, sender=User)
