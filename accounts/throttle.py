from rest_framework.throttling import UserRateThrottle

class CustomUserRegiserThrottle(UserRateThrottle):
    rate= '5/day'
