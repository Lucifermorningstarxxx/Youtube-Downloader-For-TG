from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
import config

@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	alpha2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("ʀᴇᴘᴏʀᴛ ʙᴜɢs 👾", url="https://t.me/AlphaX_SUPPORT")]
                ])

	help_image = config.HPIC
	await message.reply_photo(help_image,  caption="**💡 HELP Menu...**\n \n__• Just Send your Youtube video url 🌟__ \n__• And i will give Method list to select your choice 😋__\n \n======================\•Thank You For Using Eplison Bot ☺️⚡️`\n\n",reply_markup=alpha2)
