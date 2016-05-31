# django-secret-store
Secret store for django applications to avoid hardcoding or storing sensitive data as plain text

## Setup
1. Copy store directory to a suitable location with in your application
2. Add store app to INSTALLED_APPS set in settings.py
3. Run syncdb to let django create store tables in database

## Usage
1. Secret store has only admin page to add or change data. http[s]://[your application url]/admin/store
2. Store structure
2.1. Each secret entity will have a key identifier and one or more secret items
2.2. Add secret types in http[s]://[your application url]/admin/store/secrettype/. Example of secret type are username, password, and token.
2.3. Add secret entities in http[s]://[your application url]/admin/store/secretstore/. Give a key identifier, select type [see 2.2], and value [sensitive data].
3. In code,
```
s = store.get_secret('[key identifier]')
s.get('[secret type]') #returns value stored as given secret type
s.get_user_name() #returns value stored as "username" type
s.get_password() #returns value stored as "password" type
s.get_token() #returns value stored as "token" type
```
