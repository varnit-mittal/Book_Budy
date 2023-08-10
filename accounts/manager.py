from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self,email,phone_number,password=None,**extra_fields):
        if(not phone_number or not email):
            raise ValueError("Phone Number is required")
        
        email=self.normalize_email(email)
        user=self.model(email=email,phone_number=phone_number,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self,email,phone_number,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('payment',True)

        if(extra_fields.get('is_staff') is not True):
            raise ValueError('Superuser must have is_staff True')
        
        return self.create_user(email,phone_number,password,**extra_fields)