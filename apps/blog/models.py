from django.db import models
from utils.base_model import BaseModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Category(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Nome")
    slug = models.SlugField(max_length=255, verbose_name="Slug")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
class Post(BaseModel):
    STATUS_CHOICES = [
        ("draft", "Rascunho"),
        ("published", "Publicado"),
    ]

    title = models.CharField(max_length=255, verbose_name="Título")
    slug = models.SlugField(max_length=255, verbose_name="Slug")
    content = RichTextField(verbose_name="Conteúdo")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    published = models.BooleanField(default=False, verbose_name="Publicado")
    published_at = models.DateTimeField(null=True, blank=True, verbose_name="Publicado em")
    status = models.CharField(max_length=255,  choices=STATUS_CHOICES, verbose_name="Status")
    short_description = models.TextField(verbose_name="Descrição curta")
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
    
    
    
    
    
    
