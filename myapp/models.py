from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Community(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='communities/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Communities'


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to='events/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='events', null=True, blank=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    max_attendees = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def attendee_count(self):
        return self.attendees.count()

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('attending', 'เข้าร่วม'),
        ('interested', 'สนใจ'),
        ('not_attending', 'ไม่เข้าร่วม')
    ]
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attending_events')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='attending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('event', 'user')
        
    def __str__(self):
        return f'{self.user.username} - {self.event.title} - {self.get_status_display()}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    # Optional: ถ้าต้องการให้ profile ถูก save ทุกครั้งที่ user save
    # (อาจไม่จำเป็นเสมอไป และอาจมีผลกระทบต่อ performance ถ้า user ถูก save บ่อยๆ)
    # try:
    #     instance.profile.save()
    # except UserProfile.DoesNotExist:
    #     UserProfile.objects.create(user=instance)

# ลบ from django.db import models ที่ซ้ำซ้อนท้ายไฟล์นี้ออก
    
from django.db import models

