from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
import config

@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	alpha2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("🆁🅴🅿︎🅾︎🆁🆃 🅴🆁🆁🅾︎🆁🆂 👾", url="https://t.me/sthisara_favorites_disscussion")]
                ])

	help_image = config.HPIC
	await message.reply_photo(help_image,  caption="**⚡️𝗘𝗽𝗹𝗶𝘀𝗼𝗻 𝗛𝗲𝗹𝗽 𝗠𝗲𝗻𝘂 ⚡️**\n \n__• 𝙅𝙪𝙨𝙩 𝙎𝙚𝙣𝙙 𝙔𝙤𝙪𝙧 𝙔𝙩 𝙑𝙞𝙙𝙚𝙤 𝙡𝙞𝙣𝙠__\n \n__• 𝘼𝙣𝙙 𝙄 𝙬𝙞𝙡𝙡 𝙜𝙞𝙫𝙚 𝙈𝙚𝙩𝙝𝙤𝙙 𝙡𝙞𝙨𝙩 𝙩𝙤 𝙎𝙚𝙡𝙚𝙘𝙩 𝙔𝙤𝙪𝙧 𝘾𝙝𝙤𝙞𝙘𝙚  💃🏼__\n \n ⚡️ 🄳 ᵉ ᵛ ᵃ ˡ ᵒ ᵖ ᵉ ᵈ   ᵇ ʸ  @sthisara ⚡️\`\n\n",reply_markup=alpha2)
