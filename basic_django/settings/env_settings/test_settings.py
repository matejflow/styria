from .base_settings import BaseSettings


class TestSettings(BaseSettings):
    """
        Test specific settings
    """

    @property
    def config_files(self):
        file_path = '{}/test.conf'. format(self.SETTINGS_DIR)
        conf_files = self.check_if_file(file_path) or []
        return conf_files
