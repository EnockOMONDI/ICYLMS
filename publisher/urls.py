from django.conf.urls import patterns, include, re_path
from publisher.views import catalog
from publisher.views import my_publication
from publisher.views import publication
from django.urls import  re_path
urlpatterns = patterns('',
    # Publications(s)
    re_path(r'^publish$', catalog.catalog_page),
    re_path(r'^publication/(\d+)$', publication.publication_page),
    re_path(r'^publication/(\d+)/peer_review_modal$', publication.peer_review_modal),
    re_path(r'^publication/(\d+)/save_peer_review$', publication.save_peer_review),
    re_path(r'^publication/(\d+)/delete_peer_review$', publication.delete_peer_review),
                       
    # My Publications
    re_path(r'^my_publications$', my_publication.my_publications_page),
    re_path(r'^refresh_publications_table$', my_publication.refresh_publications_table),
    re_path(r'^my_publication_modal$', my_publication.my_publication_modal),
    re_path(r'^save_publication$', my_publication.save_publication),
    re_path(r'^delete_publication$', my_publication.delete_publication),
)
