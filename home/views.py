from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, FormView, TemplateView

from .models import (
    HeroSection,
    SiteSetting,
    TalentCategory,
    AboutSection,
    WhyChooseSection,
    WorkingCategory,
    WorkingProfile,
    Testimonials,
    BenefitSection,
    Services,
    FAQs,
    ContactMessage
)

class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        site_setting = SiteSetting.objects.order_by('-id').first()
        hero = HeroSection.objects.filter(is_active=True).first()
        work_category = WorkingCategory.objects.filter(is_active=True)[:8]
        work_profile = WorkingProfile.objects.filter(is_active=True).select_related('category')[:8]
        testimonials = Testimonials.objects.all()[:8]
        about = AboutSection.objects.filter(is_active=True).first()
        categories = TalentCategory.objects.filter(is_active=True)[:4]
        whychoose = WhyChooseSection.objects.filter(is_active=True)[:4]

        context = {
            'site_setting': site_setting,
            'categories': categories,
            'work_category': work_category,
            'work_profile': work_profile,
            'about': about,
            'testimonials': testimonials,
            'hero': hero,
            'whychoose': whychoose,
        }

        return render(request, self.template_name, context)
    
class AboutView(View):
    template_name = 'about.html'

    def get(self, request):
        site_setting = SiteSetting.objects.order_by('-id').first()
        about = AboutSection.objects.filter(is_active=True).first()
        services = Services.objects.filter()[:8]
        faq = FAQs.objects.filter()[:8]
        benefit_section = BenefitSection.objects.filter(is_active=True).first()
        

        context = {
            'site_setting': site_setting,
            'about': about,
            'benefit_section': benefit_section,
            'services': services,
            'faq': faq,

        }

        return render(request, self.template_name, context)

class Talent(View):
    template_name = 'talent.html'

    def get(self, request):
        site_setting = SiteSetting.objects.order_by('-id').first()
        
        context = {
            'site_setting': site_setting,
        }

        return render(request, self.template_name, context)

class Portfolio(View):
    template_name = 'portfolio.html'

    def get(self, request):
        site_setting = SiteSetting.objects.order_by('-id').first()
        categories = WorkingCategory.objects.filter(is_active=True)
        profiles = WorkingProfile.objects.filter(is_active=True).select_related('category')
        
        context = {
            'site_setting': site_setting,
            'categories': categories,
            'profiles': profiles,
        }

        return render(request, self.template_name, context)

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html', {'site_setting': SiteSetting.objects.last()})

    def post(self, request):
        # Data Save Logic
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        return redirect('home:thank-you') # Redirect to Thank You Page

class ThankYouView(View):
    def get(self, request):
        return render(request, 'thank-you.html', {'site_setting': SiteSetting.objects.last()})

