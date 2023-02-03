from rest_framework.routers import SimpleRouter
from .views import UserView


router = SimpleRouter()

router.register("", UserView)

urlpatterns = router.urls
