from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
import config

@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Alpha = InlineKeyboardMarkup([
        
        [InlineKeyboardButton(config.G1N, url=config.G1L)],
        [InlineKeyboardButton(config.G2N, url=config.G2L)]

    ])
    thumbnail_url = config.SPIC
    await message.reply_photo(thumbnail_url, caption=f"**🙂 Hi <b>{message.from_user.first_name}**__</br>\n\n<b>__• ⵊ’ᴍ Eᴘʟɪsᴏɴ 😊</b>\n__ⵊ’ᴍ Aɴ Aᴅᴠᴀɴᴄᴇᴅ YT Dᴏᴡᴍʟᴏᴀᴅᴇʀ Bᴏᴛ ꜰᴏʀ Tᴇʟᴇɢʀᴀᴍ__</br>\n\n<b>• **Jᴜsᴛ Sᴇɴᴅ Mᴇ ᴀɴʏ YᴏᴜTᴜʙᴇ Lɪɴᴋ ᴛᴏ Gᴇᴛ Aᴜᴅɪᴏ & Vɪᴅᴇᴏ ⚡️**</b>\n• **⚙ Type /help to get instructins...**\n \n───── ❝ **Lets Roll** ❞ ─────\n ", reply_markup=Alpha)
    raise StopPropagation
