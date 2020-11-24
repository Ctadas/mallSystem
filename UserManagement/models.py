from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group
from django.conf import settings
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator, URLValidator
from django.utils.timezone import now

from UserManagement.common import PhoneValidator



# 工厂函数，用于为指定模型追加字段
def model_modify_class_factory(model, model_admin=None):
	class CommonModelMeta:
		pass

	class CommonModelModifierBase(type):
		def __new__(cls, name, bases, attrs):
			module = attrs.pop('__module__') 
			parents = [base for base in bases if isinstance(base, CommonModelModifierBase)]
			if parents:

				# 查看是否有meta
				if 'Meta' in attrs:
					if not hasattr(model, 'Meta'):
						setattr(model, 'Meta', CommonModelMeta)

					for meta_attr, meta_value in attrs['Meta'].__dict__.items():
						if meta_attr.startswith('_'):
							continue
						setattr(model.Meta, meta_attr, meta_value)


				fields = []  
				for obj_name, obj in attrs.items():
					if isinstance(obj, models.Field):
						fields.append(obj_name)

						# 若字段已经存在，删除
						if hasattr(model, obj_name):
							delattr(model, obj_name)
						model.add_to_class(obj_name, obj)
				if not model_admin is None:
				   model_admin.fieldsets = list(model_admin.fieldsets)
				   model_admin.fieldsets.append((name, {'fields': fields}))
			return super(CommonModelModifierBase, cls).__new__(cls, name, bases, attrs)

	# 向已有表中注入字段
	class CommonModelModifier(metaclass=CommonModelModifierBase):
		pass

	return  CommonModelModifier

# 用户管理器
class UserManager(BaseUserManager):

	# 创建用户
	def create_user(self, username, password, wx_open_id=None, nickname=None, phone=None):
		# 检查用户名、密码、昵称是否为空
		if not username:
			raise UserCreataionException(message="用户名为空")
		if not password:
			raise UserCreataionException(message="密码为空")


		user = self.model(username=username, nickname=nickname, phone=phone, wx_open_id=wx_open_id)
		# 昵称为空，给定一昵称
		if not nickname:
			user.nickname = '新用户%s'%username
		user.set_password(password)
		user.save(using=self._db)

		return user

	# 创建超级用户
	def create_superuser(self, username, password, nickname=None, **kwargs):
		# 检查用户名、密码、昵称是否为空
		if not username:
			raise UserCreataionException(message="用户名为空")
		if not password:
			raise UserCreataionException(message="密码为空")

		# 昵称为空，给定一昵称
		if not nickname:
			nickname = '新用户'

		user = self.model(username=username, nickname=nickname, is_superuser=True, **kwargs)
		user.set_password(password)
		user.save(using=self._db)

		return user



# 用户模型
class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(_("用户名"), max_length=30, unique=True, validators=[MinLengthValidator(5), MaxLengthValidator(20)])
	nickname = models.CharField(_("昵称"), null=True, blank=True, max_length=30, validators=[MinLengthValidator(2), MaxLengthValidator(20)])
	phone = models.CharField(_("手机号"), unique=True, max_length=20, blank=True, null=True, validators=[PhoneValidator()])
	create_time = models.DateTimeField(_("创建时间"), default=now)
	wx_open_id = models.CharField(_("微信id"), unique=True, max_length=100, blank=True, null=True)
	
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['nickname', 'create_time']

	# 管理器
	objects = UserManager()

	groups = models.ManyToManyField(
		Group,
		through = "UserGroupRef",
		verbose_name=_('用户组'),
		blank=True,
		help_text=_(
			'用户组'
		),
		related_name="user_set",
		related_query_name="user",
	)

	class Meta:
		db_table = 't_user'
		permissions = [
		]

	@property
	def is_staff(self):
		# 只有超级用户可以进入管理后台
		return self.is_superuser


# 用户组
class UserGroup(model_modify_class_factory(Group)):

	class Meta:
		db_table = 't_user_group'

	create_time = models.DateTimeField(_("创建时间"), default=now)
	parent = models.ForeignKey('self', models.CASCADE, null=True)

# 用户与组关联
class UserGroupRef(models.Model):
	class Meta:
		db_table = 't_user_group_ref'

	user = models.ForeignKey(User, models.CASCADE)
	group = models.ForeignKey(Group, models.CASCADE)
	create_time = models.DateTimeField(_("创建时间"), default=now)

