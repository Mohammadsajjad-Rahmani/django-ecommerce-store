from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from jalali_date import date2jalali, datetime2jalali

# date2jalali : y/m/d
# datetime2jalali h/m/s_y/m/d
from article_module.models import Article, ArticleCategory, ArticleComments


# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_module/article_page.html'
    paginate_by = 1

    # def get_context_data(self, *args, object_list=None, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     # print(self,kwargs)
    #     # date = datetime2jalali(self.request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
    #     # context['date'] = date
    #     categoty_name = self.kwargs.get('category')
    #     if categoty_name is not None:
    #         article_lists = Article.objects.filter(is_active=True, category__url_title__iexact=categoty_name)
    #         context['article_list'] = article_lists
    #     return context

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_active=True)
        # print(self.kwargs) # ba estefade az kwargs be category <str:category> dar url dastresi darim
        # print(query)
        print("sasdad:",self.kwargs.get('category'))
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(
                category__url_title__iexact=category_name)  # dar vaqe in category eshare behamon field manytomany model ha dare va yani inke bro toy jadvali ke bahash ertebat darim yani article_category va onhaii ke url_title daqiqan barabar daran ba categoryname ro neshon bede
        return query  # query hqmon mahsolat ro barmigardone


def article_category_component(request: HttpRequest):
    article_main_category = ArticleCategory.objects.prefetch_related('article_set__category').filter(is_active=True, parent_id=None)
    # dige qurey nazane be database
    context = {
        'main_categories': article_main_category
    }
    return render(request, 'components/article_category_partial.html', context)


# def printt(request):
#     context = {'print': 'print'}
#     return render(request, 'components/article_category_partial.html', context)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail.html'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        # print(kwargs.get('object'))
        articlee: Article = kwargs.get('object')  # maqale sahfe ii ke tosh hastim ro nneshon mide
        context['comments'] = ArticleComments.objects.filter(article_id=articlee.id, parent_id=None).order_by('-created_date').prefetch_related('articlecomments_set')
        # in kar be lahaze performance khobe chon toye yek query miad sub_message haye on nazare parent ro ham miare ba khodesh va niazi  nist toye ye halqe for hey query bezne be database
        context['comments_count'] = ArticleComments.objects.filter(article_id=articlee.id).count()

        return context


def CreateArticleComment(request: HttpRequest):
    if request.user.is_authenticated:
        article_comment = request.GET.get('articleComment')
        article_id = request.GET.get('articleId')
        parent_id = request.GET.get('parentId')
        # print(request.GET.get('articleComment'))
        # print(article_comment, article_id, parent_id)
        new_comment = ArticleComments(article_id=article_id, parent_id=parent_id, text=article_comment,user_id=request.user.id)
        new_comment.save()
        context = {
            'comments': ArticleComments.objects.filter(article_id=article_id, parent_id=None).order_by('-created_date').prefetch_related('articlecomments_set'),
            'comments_count': ArticleComments.objects.filter(article_id=article_id).count()
        }
        return render(request, 'includes/article_detail_partial.html', context)
    return HttpResponse('hello dorost kar mikone')
