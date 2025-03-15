import os
import discord
import pandas as pd
from discord.ext import commands

# Token bot
TOKEN = #please insert your BOT token
# Khai báo intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Đọc danh sách học viên
absent_students = {}  # Dictionary lưu trữ {channel_id: (discord_id, student_name, session_date)}

try:
    df = pd.read_csv("channels.csv")  # Đọc file CSV
    for index, row in df.iterrows():
        absent_students[str(row["channel_id"])] = (row["discord_id"], row["student_name"], row["session_date"])  # Lưu vào dictionary
except Exception as e:
    print(f"❌ Lỗi khi đọc file CSV: {e}")

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành công với tên {bot.user}")

    # Gửi tin nhắn nhắc nhở
    for channel_id, (discord_id, student_name, session_date) in absent_students.items():
        channel = bot.get_channel(int(channel_id))
        if channel:
            message = f"🔔 <@{discord_id}>, bạn đã vắng học vào **{session_date}**. Vui lòng cập nhật lý do hoặc xem lại bài học nhé!"
            await channel.send(message)
            print(f"✅ Đã gửi tin nhắn cho {student_name} (ID: {discord_id}) trong channel {channel_id}")
        else:
            print(f"❌ Không tìm thấy channel {channel_id}")

bot.run(TOKEN) 
