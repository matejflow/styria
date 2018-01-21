import configparser
from pathlib import Path

from ..constants import REQUIRED_CONF_SECTIONS


class ConfigLoader():

    REQUIRED_SECTIONS = REQUIRED_CONF_SECTIONS

    def __init__(self, config_object):
        self.errors = []
        self.config_object = config_object
        self.config_parser = configparser.ConfigParser()
        self.files = self.config_object.config_files

        # raises RuntimeError ir files not found
        self.check_if_conf_file_exists()

        # no error so continue
        self.config_parser.read(self.files)
        self.validate_required_sections()
        # required params not provided, raise RuntimeError
        if self.errors:
            raise RuntimeError('Missing required sections,',
            'please check your conf file')

        # everything is fine, load sections now
        self.load_sections()

    def check_if_conf_file_exists(self):
        if not self.files:
            raise RuntimeError("Conf file not specified")

    def validate_required_sections(self):

        for section in REQUIRED_CONF_SECTIONS:
            if not self.config_parser.has_section(section):
                self.errors.append("Missing required conf section: {}".format(section))
            else:
                for required_key in self.REQUIRED_SECTIONS[section]:
                    if not self.config_parser.has_option(section, required_key):
                        self.errors.append(
                            "Missing required key '{}' in section '{}'".format(
                                required_key, section
                            )
                        )
        if self.errors:
            for error in self.errors:
                print(error)

    def load_sections(self):
        self.load_django()
        self.load_database()
        self.load_email()
        self.load_logger()

    def load_django(self):
        section = self.config_parser['django']

        self.config_object.SECRET_KEY = section.get('SECRET_KEY', fallback='')
        self.config_object.DEBUG = section.getboolean(
            'DEBUG', fallback=self.config_object.DEBUG)
        self.config_object.LOGOUT_AT_INACTIVITY = section.getboolean(
            'LOGOUT_AT_INACTIVITY', fallback=False)
        self.config_object.SESSION_COOKIE_AGE = section.getboolean(
            'SESSION_COOKIE_AGE', fallback=600)
        self.config_object.TIME_ZONE = section.get('TIME_ZONE',
            fallback=self.config_object.TIME_ZONE)

    def load_database(self):
        section = self.config_parser['database']

        self.config_object.DATABASE_ENGINE = section.get('DATABASE_ENGINE',
                                                         fallback='')
        self.config_object.DATABASE_NAME = section.get('DATABASE_NAME',
                                                         fallback='')
        self.config_object.DATABASE_USER = section.get('DATABASE_USER',
                                                         fallback='')
        self.config_object.DATABASE_PASSWORD = section.get('DATABASE_PASSWORD',
                                                         fallback='')
        self.config_object.DATABASE_HOST = section.get('DATABASE_HOST',
                                                         fallback='')
        self.config_object.DATABASE_PORT = section.getint('DATABASE_PORT',
                                                         fallback=5432)

    def load_email(self):
        section = self.config_parser['email']
        self.config_object.EMAIL_HOST = section.get('EMAIL_HOST',
                                                         fallback='')
        self.config_object.EMAIL_HOST_USER = section.get('EMAIL_HOST_USER',
                                                         fallback='')
        self.config_object.EMAIL_HOST_PASSWORD = section.get('EMAIL_HOST_PASSWORD',
                                                         fallback='')
        self.config_object.EMAIL_PORT = section.getint('EMAIL_PORT',
                                                         fallback=587)
        self.config_object.EMAIL_USE_TLS = section.getboolean('EMAIL_USE_TLS',
                                                         fallback=self.config_object.EMAIL_USE_TLS)

    def load_logger(self):
        if self.config_parser.has_section('logging'):
            section = self.config_parser['logging']
            self.config_object.FILELOG_ENABLED = section.getboolean(
                'FILELOG_ENABLED', fallback=self.config_object.FILELOG_ENABLED)
            self.config_object.FILELOG_LOG_LEVEL = section.get(
                'FILELOG_LOG_LEVEL', fallback='WARNING')
            self.config_object.SYSLOG_LOGLEVEL = section.getboolean(
                'SYSLOG_LOGLEVEL', fallback=False)
            self.config_object.SYSLOG_LOG_LEVEL = section.get(
                'SYSLOG_LOG_LEVEL', fallback='WARNING')
            self.config_object.SYSLOG_ADDRESS = section.get(
                'SYSLOG_ADDRESS', fallback='')
            self.config_object.SYSLOG_FACILITY = section.get(
                'SYSLOG_FACILITY', fallback='')
            self.config_object.SYSLOG_SOCKET_TYPE = section.get(
                'SYSLOG_SOCKET_TYPE', fallback='')
