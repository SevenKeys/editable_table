from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$','tables.views.show_rooms', name='rooms'),
	url(r'^users/$','tables.views.show_users', name='users'),
	url(r'^add_room/$','tables.views.add_room', name='add_room'),
	url(r'^add_user/$','tables.views.add_user', name='add_user'),
	url(r'^change/(?P<room_char>\w+_?\w+)_(?P<room_id>[0-9]+)/$','tables.views.change_data', name='change'),
	url(r'^success/$','tables.views.success', name='success'),
)
