from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album, Song
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import SignUpForm,ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

# ----------------------------------------ALBUM AREA CRUD-----------------------------------------------------------


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'  # all_objects can be used which is by default contain all the objects of a class

    def get_queryset(self):
        return Album.objects.raw('SELECT * FROM music_album ORDER BY album_title ASC')


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class CreateAlbum(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo', 'is_fovorite']  # template name need not be defined explicitly because
    # create view automatically get default html file as
    # model name_form.html    e:g (album_form.html)


class UpdateAlbum(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo', 'is_fovorite']


class DeleteAlbum(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


# -----------------------------------------SONG CRUD AREA--------------------------------------------------------------


class Index1View1(LoginRequiredMixin, generic.ListView):
    template_name = 'music/index1.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        return Song.objects.raw('SELECT * FROM music_song ORDER BY song_title ASC')


class CreateSong(LoginRequiredMixin, CreateView):
    model = Song
    fields = ['album', 'file_type', 'song_title', 'song_file']


class UpdateSong(LoginRequiredMixin, UpdateView):
    model = Song
    fields = ['album', 'file_type', 'song_title', 'song_file']


class DeleteSong(LoginRequiredMixin, DeleteView):
    model = Song
    success_url = reverse_lazy('music:song-list')

# -----------------------------------------LOG IN AND AUTHENTICATION------------------------------------------------


class SignUpView(View):
    form_class = SignUpForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            return redirect('music:edit')
        return render(request, self.template_name, {'form': form})


@login_required
def user_profile(request):
    if request.method == 'POST':

        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, _('your Profile Updated'))
            return redirect('music:index')
        else:
            messages.success(request, _('Please Enter Correct Information'))

    else:

        profile_form = ProfileForm(request.POST, instance=request.user.profile) #important
    return render(request,'music/profile.html', {'profile_form': profile_form})


















# from django.http import HttpResponse
# from django.http import Http404
# from django.template import loader
# OR
# from django.shortcuts import render,get_object_or_404
# from .models import Album, Song

# def index(request):
# context = { 'all_albums': all_albums,}
# return render(request, 'music/index.html', context)


# def detail(request ,album_id):
# album = get_object_or_404(Album, id = album_id)
# return render(request, 'music/detail.html', {'album': album})


# def favorite(request,album_id):
# album = get_object_or_404(Album, id=album_id)

# try:
# selected_song = album.song_set.get(pk = request.POST['song'])  #obtain particular song from Song class which is inherited from Album class
# except(KeyError, Song.DoesNotExist):
# return  render(request, 'music/detail.html', {
# 'album': album,
# 'error_message': "you did not select any song"
# } )
# else:
# selected_song.is_favorite = True
#  selected_song.save()
# return render(request, 'music/detail.html', {'album': album})
