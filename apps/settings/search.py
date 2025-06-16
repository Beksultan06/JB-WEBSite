from django.db.models import Q

class SearchMixin:
    def get_search_results(self, query):
        if not query:
            return {}

        return {
            'settings': Settings.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(title2__icontains=query) |
                Q(description2__icontains=query) |
                Q(title_bonus1__icontains=query) |
                Q(title_bonus2__icontains=query) |
                Q(title_team__icontains=query)
            ),
            'bonus': Bonus.objects.filter(title__icontains=query),
            'team': Team.objects.filter(
                Q(name__icontains=query) | Q(role__icontains=query)
            ),
            'about': About.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query) | Q(text__icontains=query)
            ),
            'services': Services.objects.filter(
                Q(title__icontains=query) | Q(title2__icontains=query) | Q(title_obj__icontains=query)
            )
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['search_query'] = query
        context['search_results'] = self.get_search_results(query) if query else {}
        return context