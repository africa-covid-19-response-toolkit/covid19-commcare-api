from starlette.config import Config
from starlette.datastructures import Secret

config = Config('.env')

FORM_XMLNS = 'http://openrosa.org/formdesigner/158EB23A-DCFF-4680-90DA-A52D95628A8C'
FORM_APP_ID = '7c00659a2a5f4ce8aa635c879f54e136'

BASE_URL =  'https://www.commcarehq.org/a/ethiocovid19/api/v0.5/form/?xmlns={0}&app_id={1}'.format(FORM_XMLNS, FORM_APP_ID)

USERNAME = config('COMMCARE_USERNAME', cast=str, default='')
PASSWORD = config('COMMCARE_PASSWORD', cast=Secret, default='')