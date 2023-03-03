from rest_framework import  authentication, exceptions

from rest_framework.authentication import get_authorization_header

from authentication.authentication import ExpiringTokenAuthentication

class Authentication(authentication.BaseAuthentication):
    user = None
    
    def get_user(self,request):
        """
        Return:
            * user      : User Instance or 
            * message   : Error Message or 
            * None      : Corrup Token
        """
        token = get_authorization_header(request).split()
        
        if token:
            try:
                token = token[1].decode()
            except:
                return None            
        
            token_expire = ExpiringTokenAuthentication()
            user = token_expire.authenticate_credentials(token)
            
            if user != None:
                self.user = user
                return user
        
        return None

    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        if user is None:
             raise exceptions.AuthenticationFailed('No se han enviado las credenciales.')
        return super().dispatch(request, *args, **kwargs)
    