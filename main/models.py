from django.db import models
from datetime import datetime

class NewsArticle(models.Model):
    """This class captures a news posting or submission. Initially the post
    will appear in a queue that can be viewed by the site administrator, after
    which it can be reviewed, edited, and then posted to the front page."""
    approved = models.BooleanField('approval status', default=False)
    author_name = models.CharField('name of the author', maxlength=100)
    author_email = models.EmailField("author's email address")
    title = models.CharField('article title', maxlength=100)
    content = models.TextField("the content of the post")
    submitted_date = models.DateTimeField('submission date', 
                                          auto_now_add=True)
    modified_date = models.DateTimeField('date/time last modified',
                                         auto_now=True)

    def __str__(self):
        return self.title

    class Admin:
        list_display = ('title', 'submitted_date', 'approved')
        list_filter = ['approved']

class Meeting(models.Model):
    """This class captures the details of a meeting."""
    date = models.DateTimeField('the date of the meeting')
    location = models.CharField(
        'the meeting location',
        default="3444 ME at Carleton University",
        maxlength=255)
    locationurl = models.URLField(
        'a map link for the location',
        default="http://tinyurl.com/2dnrgl",
        blank=True)
    details = models.TextField('the meeting details', blank=True)
    firm = models.BooleanField('is the meeting firm?', default=False)
    speakers_wanted = models.BooleanField('are speakers still wanted?',
                                          default=True)

    def __str__(self):
        return str(self.date)

    class Admin:
        list_display = ('date', 'location', 'firm', 'speakers_wanted')
        list_filter = ['date']
        date_hierarchy = 'date'
        #fields = (
        #        ('Meeting details',
        #            {'fields': ('date', 'location', 'details')}),
        #        )

class MeetingTalk(models.Model):
    """This class captures a topic being discussed at a meeting."""
    meeting = models.ForeignKey(Meeting,
                                edit_inline=models.STACKED,
                                num_in_admin=2)
    name = models.CharField('the name of the speaker',
                            maxlength=100,
                            core=True)
    topic = models.CharField('the topic of the talk',
                             maxlength=255,
                             core=True)
    details = models.TextField('the talk details',
                               core=True)
    url = models.URLField('a link to more information',
                          blank=True,
                          core=False)

    def __str__(self):
        return self.topic

    class Admin:
        list_display = ('name', 'topic', 'meeting')

class Article(models.Model):
    """This class represents a written article."""
    author = models.CharField('The article author', maxlength=64)
    author_email = models.EmailField("The author's email address")
    date = models.DateTimeField()
    title = models.CharField('The article title', maxlength=128)
    contents = models.TextField('The article, in markdown format')

    def __str__(self):
        return self.title

    class Admin:
        list_display = ('title', 'author')
