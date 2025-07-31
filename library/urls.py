from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from library.views import books

urlpatterns = [
    path('books/', books.filtered_books, name='fetch_filtered_books'),
    path('checkout/<int:book_id>/', books.checkout_book, name='checkout_book'),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]