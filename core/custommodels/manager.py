from django.contrib.auth.base_user import BaseUserManager



class UserManger(BaseUserManager):
    def create_user(self, email,password: None, **extra_fields):
        if not email:
            raise ValueError("Phone number is required")
        print( f'ectra fields calues{extra_fields}')
        

        #extra_fields['email']= self.normalize_email('email')
        user= self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using= self.db)

        return user
    
    def create_superuser(self, email, password:None, **extra_fields):

        print('this is create supe user:', email)
        
        
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
       

        return self.create_user(email, password, **extra_fields)

    