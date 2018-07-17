from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
app_name = 'music'

urlpatterns = [

    # ---------------------------------------LOGIN AND SIGNUP----------------------------------------------------------

    url(r'^register/$', views.SignUpView.as_view(), name='register'),

    url(r'^register/edit/$', views.user_profile, name='edit'),


    url(r'^login/$', auth_views.login, name='login'),

    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),


    # ---------------------------------------PASSWORD CHANGE-----------------------------------------------------------

    url(r'^password-change/$', auth_views.password_change,
        {'template_name': 'registration/password_change_form.html',
         'post_change_redirect': 'registration/password_change_done.html'}, name='password_change'),

    url(r'^password-change/registration/password_change_done.html/$', auth_views.password_change_done,
        {'template_name':'registration/password_change_done.html'}, name='password_change_done'),



    # ----------------------------------------PASSWORD RESET------------------------------------------------------------

    url(r'password-reset/$' ,
        PasswordResetView.as_view(template_name='music/password_reset_form.html',
         success_url=reverse_lazy('music:password_reset_done'),  email_template_name='music/password_reset_email.html',
         subject_template_name='music/password_reset_subject.txt'), name='password_reset'),

    url(r'password-reset/done/$' , PasswordResetDoneView.as_view(template_name='music/password_reset_done.html') ,name='password_reset_done'),


    url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(template_name='music/password_reset_confirm.html', success_url=reverse_lazy('music:password_reset_complete')), name="password_reset_confirm" ),


    url(r'^reset/complete/$', PasswordResetCompleteView.as_view(template_name='music/password_reset_complete.html'), name="password_reset_complete"),



    # ---------------------------------------ALBUM AREA----------------------------------------------------------------
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/3/

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # ?P<> used to store int id in url pattern and [0-9]+ conains all the possible integers

    # /music/album/add/
    url(r'^album/add/$', views.CreateAlbum.as_view(), name='album-add'),

    # /music/album/3
    url(r'^album/(?P<pk>[0-9]+)/$', views.UpdateAlbum.as_view(), name='album-update'),

    # /music/3/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.DeleteAlbum.as_view(), name='album-delete'),




    # --------------------------------------------SONG AREA--------------------------------------------------------

    # /music/songs
    url(r'^songs/$', views.Index1View1.as_view(), name='song-list'),

    # /music/songs/3
    url(r'^songs/(?P<pk>[0-9]+)/$', views.Index1View1.as_view(), name='song-added-view'),

    # /music/songs/add
    url(r'^songs/add/$', views.CreateSong.as_view(), name='song-add'),

    # /music/songs/3/update
    url(r'^songs/(?P<pk>[0-9]+)/update/$', views.UpdateSong.as_view(), name='song-update'),

    # /music/songs/3/delete
    url(r'^songs/(?P<pk>[0-9]+)/delete/$', views.DeleteSong.as_view(), name='song-delete'),



]
