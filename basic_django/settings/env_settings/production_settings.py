from .base_settings import BaseSettings


class ProductionSettings(BaseSettings):
    """
        Production specific settings
    """

    DEBUG = False

    @property
    def config_files(self):
        paths_to_check = [
            '/etc/basic_django.conf',
            '~/.basic_django.conf',
            '{}/production.conf'.format(self.SETTINGS_DIR),
            ]
        paths = []
        for file_path in paths_to_check:
            if self.check_if_file(file_path):
                paths.append()
        return paths
