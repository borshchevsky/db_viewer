from rest_framework.routers import DefaultRouter

from api.views import DBModelView

router = DefaultRouter()
router.register('db', DBModelView)
