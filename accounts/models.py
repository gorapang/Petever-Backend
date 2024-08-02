from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        """
        일반 사용자를 생성하는 메서드.
        이메일과 사용자 이름을 필수로 제공해야 하며, 비밀번호도 제공해야 합니다.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('The Username must be set'))
        if not password:
            raise ValueError(_('The Password must be set'))
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        """
        슈퍼유저를 생성하는 메서드.
        슈퍼유저는 추가 필드가 설정되어야 합니다.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        
        return self.create_user(username, email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    """
    사용자 모델을 정의합니다.
    AbstractBaseUser와 PermissionsMixin을 상속받아 사용자 인증과 권한 관리 기능을 추가합니다.
    """
    username = models.CharField(max_length=150, unique=True, blank=False)
    email = models.EmailField(_('email address'), max_length=254, unique=True, blank=False)
    password = models.CharField(max_length=128, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when created

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email' # 로그인 시 사용할 필드. 기본적으로 이메일을 사용합니다.
    REQUIRED_FIELDS = ['username']   # 사용자 생성 시 필수 필드 목록

    def __str__(self):
        return self.username