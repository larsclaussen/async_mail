from functools import lru_cache


@lru_cache()
def get_settings():

    try:
        from simple_settings import settings
        _ = settings.EMAIL_BACKEND
        return settings
    except (RuntimeError, ImportError, ModuleNotFoundError):
        pass
    try:
        from django.conf import settings
        from django.core.exceptions import ImproperlyConfigured
        _ = settings.EMAIL_BACKEND
        return settings
    except (ImportError, ImproperlyConfigured):
        pass
    raise ImportError(
        'Could not load settings. First tried simple_settings, '
        'then django settings'
    )


settings = get_settings()
