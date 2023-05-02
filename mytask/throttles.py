from rest_framework.throttling import SimpleRateThrottle

class InvalidMethodThrottle(SimpleRateThrottle):
    scope= 'invalid_method'
    rate = '3/hour'

    def allow_request(self, request, view):
        if request.method not in view.allowed_methods:
            return True
        return super().allow_request(request, view)
    
    def get_cache_key(self, request, view):        
        if request.user.is_authenticated:            
            return None       
        return self.cache_format % { 
            'scope': self.scope,                  
            'ident':   self.get_ident(request)        
        }