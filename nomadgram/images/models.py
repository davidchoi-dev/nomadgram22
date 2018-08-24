from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from nomadgram.users import models as user_models

@python_2_unicode_compatible
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Image(TimeStampedModel):
    
    """ image Model """
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    
    # representation
    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)
    
@python_2_unicode_compatible
class Comment(TimeStampedModel):
    
    """ Comment Model """
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)

    image = models.ForeignKey(Image, null=True, on_delete=models.PROTECT)

    # representation
    def __str__(self):
        return self.message

class Like(TimeStampedModel):
    
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT)
    image = models.ForeignKey(Image, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)