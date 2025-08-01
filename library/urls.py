from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from library.views import books, auth
from library.views.auth import EmailTokenObtainPairView

urlpatterns = [
    path('books/', books.filtered_books, name='fetch_filtered_books'),
    path('checkout/<int:book_id>/', books.checkout_book, name='checkout_book'),
]

urlpatterns += [
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me/', auth.me_view, name='get_login_user'),
]