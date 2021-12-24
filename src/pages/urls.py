from django.urls import path
from .views import HomePageView, AboutPageView, PostPageView, LogoutView

urlpatterns = [
    path('', HomePageView, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('post/', PostPageView, name='post'),
    path('logout/', LogoutView.as_view(), name = 'logout' ),
]
