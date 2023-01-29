import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "24585748"))
    API_HASH = os.environ.get("API_HASH", "7028654784d762563b9c3ca6f370cefc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6132850724:AAF-SR-ezgOJe3S9e0Zru6a9StiKah2sAHQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGYBu1n--5QtTC-VoqfGAz-nH6pUL1E5TQGhdFDOs9s6j8kpOqrTJMTijWq4n_xDNUeJSdQJ8ieBNAimWw8vp_fLXnOCzAlNzFzTqoxqRiW553qmMlmaZMY6232lX68Cb4lNj-MHSC78f5C1KQ4HKmcemB0mw6_CNgEbdl_tAgLg68CvXFWZK5FyOZiS4Avu3KaYDj64C4809AI9DdTMOjkIZMcP3gcDU_H4LnB11WTl_6Xa_590l9Wdw5En_hyw2hKxVOUwaaNgU6lqYn99NVVHd48k6G0QDxutNXkaCYDWZsKCZaI_TRkaCNql57lIG1fOIGUgltDgUiM3qwyZviUvOp8=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Dj_badnam_op_bot")
    SUPPORT = os.environ.get("SUPPORT", "Top_eagle_fighter1") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "badnam_dakku") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/022e1ffe04f885c3fcd2c.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/1147da33715c41904ad88.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5593177314")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
