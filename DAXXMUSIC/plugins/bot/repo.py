from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ ωεℓ¢σмє ƒσя 𝙼𝚛𝚔𝚒𝚕𝚕𝚎𝚛 яєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/HP_Bot_discuss_group"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/Mrkiller_1109"),
          ],
               [
                InlineKeyboardButton("𝗕𝗢𝗧 𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url="https://t.me/Hpbot_update"),

],
[
              InlineKeyboardButton("𝗥𝗘𝗡𝗔𝗠𝗘𝗥 𝗣𝗥𝗢", url=f"https://github.com/harshil8981/RenamePro_Bot"),
              InlineKeyboardButton("︎𝗙𝗜𝗟𝗘 𝗧𝗢 𝗦𝗧𝗥𝗘𝗔𝗠 𝗟𝗜𝗡𝗞", url=f"https://github.com/harshil8981/HPfile_to_link"),
              ],
              [
              InlineKeyboardButton("𝗦𝗨𝗣𝗘𝗥 𝗙𝗜𝗟𝗘 𝗦𝗧𝗢𝗥𝗘", url=f"https://github.com/harshil8981/HPSuperFile_StoreBot"),
InlineKeyboardButton("𝗠𝗔𝗜𝗡𝗧𝗘𝗡𝗔𝗡𝗖𝗘 𝗕𝗢𝗧", url=f"https://github.com/harshil8981/Maintenance-BOT"),
],
[
              InlineKeyboardButton("𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/harshil8981/MRKILLERMUSIC"),
              InlineKeyboardButton("𝗠𝗢𝗩𝗜𝗘︎", url=f"https://github.com/harshil8981/PROFESSOR-BOT"),
 
              ]] 
              
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/b234a3e63c10139f8680c.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )