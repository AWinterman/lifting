class Config:
    def __init__(self, environ):
        # 621199332133-i263d35rvh2a5s06cctjsuevm66mt7aq.apps.googleusercontent.com
        # lzyZn2pL8aE2W-nhM_AQCRxl

        # postgres configs
        self.dbname = environ.get('PG_DB_NAME', 'lift')
        self.user = environ.get('PG_USER', 'lift')
        self.password = environ.get('PG_PASSWORD')
        # When deployed to App Engine, the `GAE_ENV` environment variable will
        # be set to `standard`
        self.host = environ.get('PG_HOST', '127.0.0.1')
        self.socket = environ.get("PG_SOCKET")
        self.port = environ.get('PG_PORT')

        # postgres ssl
        self.sslrootcert = environ.get('PG_ROOT_CERT_PATH')
        self.sslcert = environ.get('PG_SSL_CERT')
        self.sslkey = environ.get('PG_SSL_CLIENT_KEY')

        # exporting to gcloud
        self.gcp_service_key = environ.get('GCP_SERVICE_CREDS')
        self.oauth_secret = environ.get('GCP_OAUTH_CLIENT_SECRET')
        self.oauth_scope = environ.get(
                'GCP_OAUTH_SCOPE',
                'https://www.googleapis.com/auth/drive.file'
        ).split(',')

        self.service_credentials = environ.get('SERVICE_ACCOUNT_CREDENTIALS')

        print(self)

    def __str__(self):
        return '\n'.join('%s %s' % item for item in vars(self).items())
