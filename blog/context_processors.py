from .models import SiteSettings, Page

def site_settings(request):
    settings = SiteSettings.objects.first()
    pages = Page.objects.all()
    return {
        'site_settings': settings,
	'pages': pages
    }
