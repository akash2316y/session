import os
from pyrogram import Client

#api id or api hash fill here 👇🏻

api_id = 
api_hash = ""

try:
    os.remove("unknown.session")
except:
    pass

with Client("unknownbotz", api_id=api_id, api_hash=api_hash) as app:
    session = (
        "**ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ 👇🏻**\n\n"
        f"`{app.export_session_string()}`\n\n"
        "**ʙʏ: [ᴜɴᴋɴᴏᴡɴʙᴏᴛᴢ](https://t.me/UnknownBotz)**"
    )

    # Saved Messages me string bhejna
    app.send_message("me", session, disable_web_page_preview=True)

    # UnknownBotz related channels join
    try:
        app.join_chat("UnknownBotz")
    except:
        pass

    print("✅ String Session Has 🌟 Been Sent")
    print("🔥 Check Your Telegram Saved Messages ✨")

# session file delete
try:
    os.remove("unknownbotz.session")
except:
    pass
