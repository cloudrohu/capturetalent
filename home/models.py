from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Class Setting Start Here
class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200,)
    logo = models.ImageField(upload_to="settings/", blank=True, null=True)
    favicon = models.ImageField(upload_to="settings/", blank=True, null=True)
    tagline = models.CharField(max_length=300, blank=True)
    copyright = models.CharField(max_length=300, blank=True)
    nav_color = models.CharField(max_length=300, blank=True)
    text_color = models.CharField(max_length=300, blank=True)
    about_banner = models.ImageField(upload_to="about_banner/", blank=True, null=True)
    contect_banner = models.ImageField(upload_to="contect_banner/", blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    googlemap = models.TextField(blank=True, null=True)
    the_journey_background_video = models.FileField(upload_to="the_journey_background_video/", blank=True, null=True)
    youtube = models.URLField(max_length=500, blank=True)
    instagram = models.URLField(max_length=500, blank=True)
    linkdin = models.URLField(max_length=500, blank=True)
    facebook = models.URLField(max_length=500, blank=True)

    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(blank=True)

    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Global Site Settings"
# Class Setting End Here

# Class Hero Start Here
class HeroSection(models.Model):
    heading = models.CharField(max_length=200)
    background_video = models.FileField(upload_to="hero_videos/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.heading

class WhyJoin(models.Model):
    hero = models.ForeignKey(HeroSection,on_delete=models.CASCADE,related_name="benefits")
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
# Class Hero End Here

# TALENT CATEGORY START HERE
class TalentCategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="talent_categories/")
    short_description = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Talent Category"
        verbose_name_plural = "Talent Categories"
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
class OurArties(models.Model):
    category = models.ForeignKey(TalentCategory,on_delete=models.CASCADE,related_name="Arties")
    title = models.CharField(max_length=150)
    profile_image = models.ImageField(upload_to="talents/")
    bio = models.TextField(blank=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


# TALENT CETEGOY END HERE    

# ABOUT START HERE
class AboutSection(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="about_section/")
    about_us = models.TextField()
    mission = models.TextField(blank=True,null=True)
    vision = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"
        ordering = ['-created_at']

    def __str__(self):
        return self.title  
# ABOUT END HERE    

# WHY CHOOSE SECTION START HERE
class WhyChooseSection(models.Model):
    icon = models.CharField(max_length=100,null=True,blank=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Why Section"
        verbose_name_plural = "Why Section"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
# WHY CHOOSE SECTION END HERE    

# WORKING PROFILE AND CATEGORY START HERE
class WorkingCategory(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="working_category/")
    description = models.TextField(blank=True)
    
    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Working Category"
        verbose_name_plural = "Working Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class WorkingProfile(models.Model):

    category = models.ForeignKey("WorkingCategory",on_delete=models.CASCADE,related_name="profiles")

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="working_profile/")
    description = models.TextField(blank=True)

    slug = models.SlugField(unique=True, blank=True)

    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "-created_at"]
        verbose_name = "Working Profile"
        verbose_name_plural = "Working Profiles"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
# WORKING PROFILE AND CATEGORY END HERE

# TESTIMONIALS START HERE
class Testimonials(models.Model):
    name = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="working_category/",blank=True)
    
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
   
# TESTIMONIALS END HERE

# BENEFIT START HERE
class BenefitSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="benefit_section/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class BenefitKey(models.Model):
    section = models.ForeignKey(BenefitSection,on_delete=models.CASCADE,related_name="benefit_keys")
    key_text = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.key_text
# BENEFIT END HERE

# SERVICES START HERE
class Services(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
# SERVICES END HERE

# FAQS START HERE
class FAQs(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question
# FAQS END HERE

# CONTACT START HERE
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
# CONTACT END HERE

# Experiance START HERE
class Experience(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
# Experiance END HERE
    
# JOIN START HERE
class JoinApplication(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    talent = models.ForeignKey(TalentCategory, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    
# JOIN END HERE
    
