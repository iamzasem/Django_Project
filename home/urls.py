from django.urls import path # type: ignore
from home import views
from django.views.generic.base import TemplateView # type: ignore

urlpatterns = [
  path('', views.index, name='index'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('seo/', views.seo, name='seo'),
    path('thumbnails/', views.thumbnails, name='thumbnails'),
    path('digitalmarketing/', views.digitalmarketing, name='digitalmarketing'),
    path('search/', views.search, name='search'),
    path('myadmin/', views.custom_admin, name='custom_admin'),
    path('german.html', views.german_view, name='german'),
    path('other-topics.html', views.otherTopics, name='other_topics'),
   
    # Topic routes
    path('nouns.html', views.nouns_view, name='nouns'),
    path('articles.html', views.articles_view, name='articles'),
    path('adjectives.html', views.adjectives_view, name='adjectives'),
    path('conjugation.html', views.conjugation_view, name='conjugation'),
    path('cases.html', views.cases_view, name='cases'),
    path('prepositions.html', views.prepositions_view, name='prepositions'),
    path('structure.html', views.structure_view, name='structure'),
    path('listening.html', views.listening_view, name='listening'),
    path('writing.html', views.writing_view, name='writing'),
    path('speaking.html', views.speaking_view, name='speaking'),
    path('culture.html', views.culture_view, name='culture'),
    path('exam.html', views.exam_view, name='exam'),
    path('personal-pronouns.html', views.personal_pronouns_view, name='personal-pronouns'),
    path('verbs-wfrage-ja-nein-normaler.html', views.verbs_wfrage_ja_nein_normaler_view, name='verbs_wfrage_ja_nein_normaler'),
   path('imperative.html', views.imperative_view, name='imperative'),
     path('akkusative.html', views.akkusative_view, name='akkusative'),
    path('possessive.html', views.possessive_view, name='possessive'),
   path('modalverbpresent.html', views.modalverbpresent_view, name='modalverbpresent'),
  path('praterituma1.html', views.praterituma1_view, name='praterituma1'),
  path('trennbare.html', views.trennbare_view, name='trennbare'),
    path('dative.html', views.dative_view, name='dative'),
     path('wechsel.html', views.wechsel_view, name='wechsel'),
      path('partizip2.html', views.partizip2_view, name='partizip2'),
       path('welcherdieser.html', views.welcherdieser_view, name='welcherdieser'),
    path('a2-topics.html', views.a2topics_view, name='a2-topics'),
   path('doch.html', views.doch_view, name='doch'),
 path('reflexive.html', views.reflexive_view, name='reflexive'),
  path('weil.html', views.weil_view, name='weil'),
    path('modal_prateritum.html', views.modal_prateritum_view, name='modal_prateritum'),


]
