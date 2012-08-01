from django.db import models
from datetime import datetime
import time

class Notice(models.Model):
    """This model class captures a notice for the front page. We can have
    multiple notices, but typically we should have one, or none."""
    visible = models.BooleanField('visible', default=True)
    title = models.CharField('title', max_length=100)
    content = models.TextField("the content of the post")
    submitted_date = models.DateTimeField('submission date', 
                                          auto_now_add=True)

    def __str__(self):
        return self.title

class Meeting(models.Model):
    """This class captures the details of a meeting."""
    date = models.DateTimeField('the date of the meeting')
    location = models.CharField(
        'the meeting location',
        default="",
        max_length=255)
    locationurl = models.URLField(
        'a map link for the location',
        default="",
        blank=True)
    details = models.TextField('the meeting details', blank=True)
    firm = models.BooleanField('the meeting is firm', default=False)
    speakers_wanted = models.BooleanField('speakers are still wanted',
                                          default=True)
    def __str__(self):
        return self.date.strftime("%c")

class MeetingTalk(models.Model):
    """This class captures a topic being discussed at a meeting."""
    meeting = models.ForeignKey(Meeting, related_name="talks")
    name = models.CharField('the name of the speaker',
                            max_length=100)
    topic = models.CharField('the topic of the talk',
                             max_length=255)
    details = models.TextField('the talk details')
    url = models.URLField('a link to more information',
                          blank=True)

    def __str__(self):
        return "%s: %s" % (self.name, self.topic)

class Article(models.Model):
    """This class represents a written article."""
    author = models.CharField('The article author', max_length=64)
    author_email = models.EmailField("The author's email address")
    date = models.DateTimeField()
    title = models.CharField('The article title', max_length=128)
    contents = models.TextField('The article, in markdown format')

    def __str__(self):
        return self.title
