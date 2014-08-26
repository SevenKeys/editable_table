from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$','tables.views.show_rooms', name='rooms'),
	url(r'^users/$','tables.views.show_users', name='users'),
	url(r'^add_room/$','tables.views.add_room', name='add_room'),
	url(r'^change/$','tables.views.change_data', name='change'),
	)