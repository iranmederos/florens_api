from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.http import JsonResponse


from datetime import timedelta
from django.utils import timezone


from .models import NursUser

#this return left time
def expires_in(token):
    nursuser = NursUser.objects.get(email=token.user.email)
    if str(nursuser.role) == "1":
         time_expired = timedelta(hours=24)
    else:
        departure_time = nursuser.id_shift.departure_time
        now = timezone.now().replace(microsecond=0)
        if now <= departure_time:
            time_expired = departure_time - now
        else:
            time_expired = timedelta(seconds=-1)

    return time_expired

# token checker if token expired or not
def is_token_expired(token):
    return expires_in(token) < timedelta(seconds=0)

# if token is expired new token will be established
# If token is expired then it will be removed
# and new one with different key will be created
def token_expire_handler(token):
    is_expired = is_token_expired(token)
    if is_expired:
        token.delete()
        
    return is_expired


#DEFAULT_AUTHENTICATION_CLASSES
class ExpiringTokenAuthentication(TokenAuthentication):
    """
    If token is expired then it will be removed
    and new one with different key will be created
    """
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            return JsonResponse({'error': 'Invalid Token'}, status=401)
        
        if not token.user.is_active:
            return JsonResponse({'error': 'User is not active'}, status=401)

        is_expired = token_expire_handler(token)
        if is_expired:
            return JsonResponse({'error': 'The Token is expired'}, status=401)
                
        
        return (token.user)