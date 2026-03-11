from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from .models import *
from django.utils.html import format_html


admin.site.register(Experience)
admin.site.register(JoinApplication)

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'updated_on')
    readonly_fields = ('updated_on',)

    fieldsets = (
        ("Branding", {
            "fields": (
                "site_name",
                "logo",
                "favicon",
                "tagline",
                "copyright",
                "nav_color",
                "text_color",
            )
        }),

        ("Contact Information", {
            "fields": (
                "phone",
                "email",
                "address",
                "contect_banner",
                "googlemap",
            )
        }),

        ("Social Media", {
            "fields": (
                "facebook",
                "instagram",
                "linkdin",
                "youtube",
            )
        }),

        ("SEO Settings", {
            "fields": (
                "seo_title",
                "seo_description",
            )
        }),

        ("System Info", {
            "fields": (
                "updated_on",
            )
        }),
        ("Other Settings", {
            "fields": (
                "the_journey_background_video",
                "about_banner",

            )
        }),

    )
    
class WhyJoinInline(admin.TabularInline):
    model = WhyJoin
    extra = 1

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    inlines = [WhyJoinInline]    

@admin.register(TalentCategory)
class TalentCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(OurArties)
class OurArtiesAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_verified", "is_active")
    list_filter = ("category", "is_verified", "is_active")    

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    list_filter = ("is_active",)

@admin.register(WhyChooseSection)
class WhyChooseSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    list_filter = ("is_active",)

@admin.register(WorkingCategory)
class WorkingCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    search_fields = ("title",)
    list_filter = ("is_active", "created_at")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(WorkingProfile)
class WorkingProfileAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_active", "display_order", "created_at")
    list_filter = ("category", "is_active")
    search_fields = ("title", "category__title")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class BenefitKeyInline(admin.TabularInline):
    model = BenefitKey
    extra = 1

@admin.register(BenefitSection)
class BenefitSectionAdmin(admin.ModelAdmin):
    inlines = [BenefitKeyInline]

    list_display = ("title", "is_active")
    list_filter = ("is_active",)

    fieldsets = (
        ("TagLine", {
            "fields": (
                "title",
                "description",
                "image",
                "is_active",
            )
        }),
    )

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

@admin.register(FAQs)
class FAQsAdmin(admin.ModelAdmin):
    list_display = ("question","answer")
    search_fields = ("question",)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name","phone")
    search_fields = ("name","phone")


# End of admin.py