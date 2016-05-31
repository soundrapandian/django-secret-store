from models import SecretType, SecretStore

class Secret:
    _secrets = {}
    
    def __init__(self, secrets):
        self._secrets = secrets
    
    def get_user_name(self):
        return self._secrets.get('USERNAME', None)
        
    def get_password(self):
        return self._secrets.get('PASSWORD', None)
        
    def get_token(self):
        return self._secrets.get('TOKEN', None)
        
    def get(self, type):
        return self._secrets.get(type, None)
    
def get_secret(key_text):
    secrets = SecretStore.objects.filter(key=key_text)
    sec_dict = {}
    for secret in secrets:
        sec_dict[secret.type.name] = secret.value
    return Secret(sec_dict)