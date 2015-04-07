from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.view_groups', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', 'app.views.user_login', name='user_login'),
    url(r'^register/$', 'app.views.user_register', name='user_register'),
    url(r'^dashboard/$', 'app.views.view_groups', name='dashboard'),
    url(r'^logout/$', 'app.views.logout_user', name='logout'),
    url(r'^groups/join/(?P<key>.+)/$','app.views.join_remote',name='join_group'),
    url(r'^groups/add/$','app.views.add_group_screen', name='add_group_screen'),
    url(r'^groups/unsubscribe/(?P<key>.+)/$','app.views.unsubscribe_to_group', name='unsubscribe_to_group'),
    url(r'^groups/subscribe/$','app.views.subscribe_to_group', name='subscribe_to_group'),
    url(r'^groups/create/$','app.views.create_group', name='create_group'),
    url(r'^groups/(?P<key>.+)/assignment/(?P<pk>.+)/$','app.views.view_assignment', name='view_assignment'),
    url(r'^groups/(?P<key>.+)/add/$','app.views.add_assignment', name='add_assignment'),
    url(r'^groups/(?P<key>.+)/$','app.views.individual_group_page', name='individual_page_view'),
    url(r'^groups/$', 'app.views.view_groups', name='view_groups'),
    url(r'^admin/', include(admin.site.urls)),
)
