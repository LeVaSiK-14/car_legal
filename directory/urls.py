from rest_framework import routers
from directory.views import MarkViewSet, BrandViewSet



router = routers.SimpleRouter()
router.register('marks', MarkViewSet)
router.register('brands', BrandViewSet)

urlpatterns = []
urlpatterns += router.urls

# urlpatterns = [
#     path('marks/', MarkViewSet.as_view({'get': 'list', 'post': 'create'})),
#     path('marks/<int:pk>/', MarkViewSet.as_view({'get': 'retrive', 'put': 'update', 
#                                                 'delete': 'destroy'})),
#     path('brands/', BrandViewSet.as_view({'get': 'list', 'post': 'create'})),
#     path('brands/<int:pk>/', BrandViewSet.as_view({'get': 'retrive', 'put': 'update', 
#                                                 'delete': 'destroy'})),
# ]