from newsletter.models import News_Letter
def add_variable_to_context(request):
    current_news_letter = News_Letter.objects.all().order_by('-start_date').first()
    return {
        'current_newsletter':current_news_letter,
    }