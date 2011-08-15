from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

class ProjectType(models.Model):
    title = models.CharField(('title'), max_length=100)
    slug = models.SlugField(('slug'), unique=True)
 
    class Meta:
        verbose_name = ('type')
        verbose_name_plural = ('types')
        db_table = 'project_types'
        ordering = ('title',)
 
    def __unicode__(self):
        return u'%s' % self.title


class Client(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(blank=True)
    
    class Meta:
        db_table = 'clients'
        ordering = ('name',)   
        
    def __unicode__(self):
        return self.name
    
class ProjectImage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image_path = models.CharField(max_length=100, blank=True)
    image = models.FileField(upload_to="images/portfolio", blank=True)
    credit = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    tags = TaggableManager()
    is_featured = models.BooleanField('Is this image featured on your main pages?')
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
 
    class Meta:
        db_table = 'project_images'
 
    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return self.slug
        
class Role(models.Model):
    role = models.CharField(max_length=50)

    class Meta:
        db_table = 'roles'
        ordering = ('role',)  
    
    def __unicode__(self):
        return self.role
    
class Project(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    role = models.ForeignKey(Role)
    project_url = models.URLField('Project URL')
    type = models.ManyToManyField(ProjectType, blank=True)
    description = models.TextField(blank=True)
    client = models.ForeignKey(Client)
    completion_date = models.DateField()
    in_development = models.BooleanField()
    is_public = models.BooleanField(default=True)
    images = models.ManyToManyField(ProjectImage)
    is_featured = models.BooleanField()
    
    class Meta:
        db_table = 'projects'
        ordering = ('-completion_date',)
        
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/work/%s/" % self.slug
