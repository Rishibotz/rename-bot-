"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	👉ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 1.2ɢʙ
👉ᴘʀɪᴄᴇ ₹0 , 0$
	
	**🪙 Silver Tier 🪙** 
	👉ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ 10ɢʙ
👉ᴘʀɪᴄᴇ ₹ 10  ɪɴᴅ /🌎 0.8$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	**💫 Gold Tier 💫**
	👉ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 50ɢʙ
👉ᴘʀɪᴄᴇ ₹ 30  ɪɴᴅ /🌎 1.2$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	**💎 Diamond 💎**
	👉ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 100ɢʙ
👉ᴘʀɪᴄᴇ ₹ 50  ɪɴᴅ /🌎 2.5$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	Pay Using Upi I'd ```8757081330@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @Rk_botowner"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Rk_botowner")], 
        			[InlineKeyboardButton("UPI",url = "https://tools.apgy.in/upi/Rk+botz/8757081330@paytm/"),
        			InlineKeyboardButton("Paypal",url = "https://paypal.me/vinaykumar009?country.x=IN&locale.x=en_GB")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	👉ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 1.2ɢʙ
👉ᴘʀɪᴄᴇ ₹0 , 0$
	
	**🪙 Silver Tier 🪙** 
	👉ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ 10ɢʙ
👉ᴘʀɪᴄᴇ ₹ 10  ɪɴᴅ /🌎 0.8$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	**💫 Gold Tier 💫**
	👉ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 50ɢʙ
👉ᴘʀɪᴄᴇ ₹ 30  ɪɴᴅ /🌎 1.2$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	**💎 Diamond 💎**
	👉ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 100ɢʙ
👉ᴘʀɪᴄᴇ ₹ 50  ɪɴᴅ /🌎 2.5$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	Pay Using Upi I'd ```8757081330@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @Rk_botowner"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Rk_botowner")], 
        			[InlineKeyboardButton("UPI",url = "https://tools.apgy.in/upi/Rk+botz/8757081330@paytm/"),
        			InlineKeyboardButton("Paypal",url = "https://paypal.me/vinaykumar009?country.x=IN&locale.x=en_GB")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	
