import decouple

FIRST_NAME = decouple.config("FIRST_NAME", default="Jonh")
LAST_NAME = decouple.config("LAST_NAME", default=None)
GITHUB_USERNAME = decouple.config("GITHUB_USERNAME", default=None)
LINKEDIN = decouple.config("LINKEDIN", default=None)
BIRTH_DT = decouple.config("BIRTH_DT", default=None)
PHONE = decouple.config("PHONE", default=None)
EMAIL = decouple.config("EMAIL", default=None)
WORK = decouple.config("WORK", default=None)
WORK_AREA = decouple.config("WORK_AREA", default=None)
LOCATION = decouple.config("LOCATION", default=None)
