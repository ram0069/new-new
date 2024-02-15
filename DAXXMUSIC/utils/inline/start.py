from pyrogram.types import InlineKeyboardButton

import config
from DAXXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["⛩ 𝙎𝙪𝙢𝙢𝙤𝙣 𝙢𝙚 ⛩"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["𝙎𝙐𝙋𝙋𝙊𝙍𝙏 🔥"], url=f"https://t.me/soulkigandugadari"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["⛩ 𝙎𝙪𝙢𝙢𝙤𝙣 𝙢𝙚 ⛩"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["𝙊𝙒𝙉𝙀𝙍 ⚡️"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["𝙎𝙐𝙋𝙋𝙊𝙍𝙏 🔥"], url=f"https://t.me/soulkigandugadari"),
        ],
        [
            InlineKeyboardButton(text=_["𝙎𝙆𝙄𝙇𝙇'𝙎 ✨"], callback_data="settings_back_helper"),
        ],
    ]
    return buttons
