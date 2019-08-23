from rest_framework import routers
from application import views as myviews

router = routers.DefaultRouter()
router.register(r'loanapp', myviews.ApplicationViewset, 'loanapp')
router.register(r'status', myviews.StatusViewset, 'status')
