from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager




class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, name, password=None):
        """Create a new user"""
        if not email:
            raise ValueError("User must have an email.")

        #normalize the email
        email = self.normalize_email(email)

        #create a user form model
        user = self.model(email=email, name=name)

        user.set_password(password)

        user.save(using = self._db)

        return user


    def create_superuser(self, email, name, password):
        """Create and save a new user with given details"""

        user = self.create_user(email, name, password)
        #not specified in user-profile but is set to false by the permissionsmixin 
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user





class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ database model for users in the system """
    email = models.EmailField(length=255, unique=True)
    name = models.CharField(length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = ["name"]

    def get_full_name(self):
        """ retrieves full name of user """
        return self.name


    def get_short_name(self):
        """ retrieves short name of user """
        return self.name

    def __str__(self):
        """ returns string representation of our user """
        return self.email
