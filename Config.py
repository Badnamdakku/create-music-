import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "24585748"))
    API_HASH = os.environ.get("API_HASH", "7028654784d762563b9c3ca6f370cefc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5689681976:AAFE4FLueeHZGU6sTN7IE6s0NUT0bbqXywM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOMABu0CKgy_EVeoG-Nkygcld2PjHR8kbcZMTn1NqJ6tYT_ytPSwzAcXNdWE53LJUr2UP0Jzjzv0azv67PaXBMGAO7xAu1KL5CT0ze5pmABGvMGgGK16jkbq6qndqnS1rjYW3VXB8RTmN5VD3jVzzabH1BSO0QyfDF18VskN552rK6_yp0C7aF_x7oH_ve2gKxYorhO-dcFmBhtEVGA_A9QfwWtaCGtoPoevABQrmYfZ53kC1Q9pLYrRk7X6tmy6EFksUpYy8vOBW7vWBcP3P3GCcsLYbuCDw25ceo7lndm9N2-OahKTo3QXbSy7f36eKG5_QjAZK1_zD2ZwfG856XKRnIWU=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Dj_badnam_bot")
    SUPPORT = os.environ.get("SUPPORT", "Top_eagle_fighter1") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "badnam_dakku") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/022e1ffe04f885c3fcd2c.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/1147da33715c41904ad88.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5593177314")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
