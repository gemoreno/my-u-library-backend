from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from library.views import books, auth, checkouts
from library.views.auth import EmailTokenObtainPairView

urlpatterns = [
    path('books/', books.books_handler, name='books_handler'),
    path('books/checked_out/', books.filtered_checked_books, name='fetch_filtered_books'),
    path('checkouts/checkout_book/<int:book_id>/', checkouts.checkout_book, name='checkout_book'),
    path('checkouts/', checkouts.list_checkouts, name='list_checkouts'),
    path('checkouts/<int:checkout_id>/return/', checkouts.return_book, name='return_book'),
]

urlpatterns += [
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me/', auth.me_view, name='get_login_user'),
    path('auth/register/', auth.register_user, name='register_user'),
]