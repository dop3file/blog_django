from django.db.models import Q


def search(article_obj, search_text):
    return article_obj.objects.filter(
            Q(title__icontains=search_text) | Q(text__icontains=search_text)
        )