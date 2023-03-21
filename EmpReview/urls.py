from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('people/', views.PersonView.as_view(), name='people'),
    path('person/<uuid:pk>', views.PersonDetail, name='person-detail'),
    path('review/<uuid:pk>', views.ReviewDetailView.as_view(), name='review-detail'),
    path('approval/<uuid:pk>', views.ApprovalDetailView.as_view(), name='approval-detail'),
    path('reviews/my_created_reviews.html', views.ReviewsByRequester.as_view(), name='my_created_reviews'),
    path('people_choice.html', views.search_person, name='people_choice'),
    path('success.html', views.success, name='success'),
    path('name-autocomplete/', views.NameAutoComplete.as_view(), name='name-autocomplete'),
    path('get_or_create/<int:id>', views.get_or_create, name='get-or-create')
    ]

# Person CRUD URLs

urlpatterns += [
    path('person/create', views.add_person, name='person-create'),
    path('person/<uuid:pk>/update/', views.PersonUpdate.as_view(), name='person-update'),
    path('person/<uuid:pk>/delete/', views.PersonDelete.as_view(), name='person-delete'),
    ]

# Review CRUD URLs

urlpatterns += [
    path('review/create/<uuid:pk>', views.add_review, name='review-create'),
    # path('review/<uuid:pk>/update/', views.ReviewUpdate.as_view(), name='review-update'),
    # path('review/<uuid:pk>/delete/', views.ReviewDelete.as_view(), name='review-delete'),
    ]

urlpatterns += [
    path('approval/create/<uuid:pk>', views.add_approval, name='approval-create'),
    # path('approval/<uuid:pk>/update/', views.ApprovalUpdate.as_view(), name='approval-update'),
    # path('approval/<uuid:pk>/delete/', views.ReviewDelete.as_view(), name='approval-delete'),
]

# urlpatterns += [
#     path('user_creation/', views.add_users_to_db, name='add-users-to-db'),
#     path('update_profiles/', views.create_or_update_profile, name='create-update-profile'),
#     ]

urlpatterns += [
    path('scratchtest/', views.scratch_test, name='scratchtest'),
    ]