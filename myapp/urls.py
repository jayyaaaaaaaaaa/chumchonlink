from myapp import views
# from django.contrib.auth import views as auth_views # ไม่จำเป็นแล้วสำหรับ login/logout view พื้นฐาน
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create router and register viewsets
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.UserProfileViewSet)
# ... (viewsets อื่นๆ ของคุณ) ...
router.register(r'events', views.EventViewSet)
router.register(r'attendances', views.AttendanceViewSet)

# Webpage URLs
urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('events/create/', views.EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/edit/', views.EventUpdateView.as_view(), name='event_update'),
    path('events/<int:pk>/attend/', views.attend_event, name='attend_event'),
    path('profile/', views.user_profile, name='user_profile'), # allauth อาจมี view ของตัวเองสำหรับ profile
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.user_profile, name='view_profile'),
    path('dashboard/', views.dashboard_page, name='dashboard'),

    # Authentication URLs จะถูกจัดการโดย allauth ผ่าน path('accounts/', include('allauth.urls')) ใน project urls.py

    # API URLs
    path('api/', include(router.urls)),
]