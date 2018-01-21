from ..constants import INSTALLED_APPS, MIDDLEWARE
from .base_settings import BaseSettings


class DevelopmentSettings(BaseSettings):
    """
        Development specific settings
    """

    INSTALLED_APPS = INSTALLED_APPS + [
        'debug_toolbar'
    ]

    MIDDLEWARE = MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]

    @property
    def config_files(self):
        file_path = '{}/development.conf'. format(self.SETTINGS_DIR)
        conf_files = self.check_if_file(file_path) or []
        return conf_files
