from django.db import models
from categories.models import CategoryBase

class Disease(CategoryBase):
	doid = models.CharField(max_length=30, primary_key=True)

	class Meta(CategoryBase.Meta):
		verbose_name_plural = 'diseases'