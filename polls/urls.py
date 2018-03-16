from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PollList, PollDetail,ChoiceList,CreateVote,UserCreate,LoginView,PollViewSet

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
	path("login/", LoginView.as_view(), name="login"),
	path("users/", UserCreate.as_view(), name="create_user"),
    path("", PollList.as_view(), name="polls_list"),
    path("<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
]

urlpatterns += router.urls