from django.apps import AppConfig

# Configuration class for the 'finance' app
class FinanceConfig(AppConfig):

    # Specifies the default primary key field to use for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Specifies the name of the app
    name = 'finance'
