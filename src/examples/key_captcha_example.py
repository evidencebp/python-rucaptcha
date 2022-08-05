import asyncio

from src.python_rucaptcha.enums import KeyCaptchaEnm
from src.python_rucaptcha.KeyCaptcha import KeyCaptcha, aioKeyCaptcha

# Rucaptcha API Key from your account
RUCAPTCHA_KEY = "ad9053f111111111111111fa758570"

s_s_c_user_id = "184015"
s_s_c_session_id = "0917788cad24ad3a69813c4fcd556061"
s_s_c_web_server_sign = "02f7f9669f1269595c4c69bcd4a3c52e"
s_s_c_web_server_sign2 = "d888700f6f324ec0f32b44c32c50bde1"
pageurl = "https://rucaptcha.com/demo/keycaptcha"

lemin_captcha = KeyCaptcha(
    rucaptcha_key=RUCAPTCHA_KEY,
    pageurl=pageurl,
    s_s_c_user_id=s_s_c_user_id,
    s_s_c_session_id=s_s_c_session_id,
    s_s_c_web_server_sign=s_s_c_web_server_sign,
    s_s_c_web_server_sign2=s_s_c_web_server_sign2,
    method=KeyCaptchaEnm.KEYCAPTCHA.value,
)
result = lemin_captcha.captcha_handler()

print(result)


async def run():
    try:
        lemin_captcha = await aioKeyCaptcha(
            rucaptcha_key=RUCAPTCHA_KEY,
            pageurl=pageurl,
            s_s_c_user_id=s_s_c_user_id,
            s_s_c_session_id=s_s_c_session_id,
            s_s_c_web_server_sign=s_s_c_web_server_sign,
            s_s_c_web_server_sign2=s_s_c_web_server_sign2,
            method=KeyCaptchaEnm.KEYCAPTCHA.value,
        ).captcha_handler()
        print(lemin_captcha)
    except Exception as err:
        print(err)


asyncio.run(run())
