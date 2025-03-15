import os
import csv
import discord
from discord.ext import commands

==== CONFIG ====
BASE_DIR = "/Users/haiaunguyen/Desktop/DiscordBot/"
TEMPLATES_FILE = os.path.join(BASE_DIR, "templates.csv")
MESSAGES_FILE = os.path.join(BASE_DIR, "messages.csv")
DISCORD_BOT_TOKEN = #please enter your BOT's token

if not DISCORD_BOT_TOKEN:
    raise ValueError("❌ Không tìm thấy token bot! Vui lòng đặt biến môi trường DISCORD_BOT_TOKEN.")

==== DISCORD BOT ====
intents = discord.Intents.default()
intents.message_content = True  # Cho phép bot đọc nội dung tin nhắn
intents.members = True  # Lấy danh sách thành viên để tag đúng tên
bot = commands.Bot(command_prefix="!", intents=intents)

==== HÀM ĐỌC FILE CSV KHÔNG CÓ BOM ====
def load_csv(file_path):
    """ Đọc file CSV và loại bỏ BOM nếu có """
    if not os.path.exists(file_path):
        print(f"❌ Không tìm thấy file {file_path}. Kiểm tra lại đường dẫn!")
        return []

    with open(file_path, mode="r", encoding="utf-8-sig") as file:  # Dùng utf-8-sig để loại BOM
        reader = csv.DictReader(file)
        return [row for row in reader]

def load_templates():
    """ Tải nội dung mẫu tin nhắn từ file templates.csv """
    templates = {}
    for row in load_csv(TEMPLATES_FILE):
        if "message_type" in row and "template_content" in row:
            templates[row["message_type"].strip()] = row["template_content"].strip()
        else:
            print(f"⚠️ Dòng lỗi trong {TEMPLATES_FILE}: {row}")
    return templates

def load_messages():
    """ Tải danh sách tin nhắn từ file messages.csv """
    messages = []
    for row in load_csv(MESSAGES_FILE):
        if all(col in row for col in ["channel_id", "message_type", "learner_id"]):
            messages.append(row)
        else:
            print(f"⚠️ Dòng lỗi trong {MESSAGES_FILE}: {row}")
    return messages

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành công với tên {bot.user}")

    templates = load_templates()
    messages = load_messages()

    for msg in messages:
        channel_id = msg.get("channel_id")
        if not channel_id:
            print(f"⚠️ Thiếu 'channel_id' trong file {MESSAGES_FILE}")
            continue

        channel = bot.get_channel(int(channel_id))
        if channel:
            # Lấy mẫu tin nhắn
            template = templates.get(msg.get("message_type"), "⚠️ Không tìm thấy mẫu tin nhắn.")

            # Format message với tag user đúng cách
            try:
                learner_tag = f"<@{msg.get('learner_id')}>"
                mentor_tag = f"<@{msg.get('mentor_id')}>"

                message = template.format(
                    learner_id=learner_tag,
                    mentor_id=mentor_tag,
                    session_date=msg.get("session_date", "???"),
                    AssignmentGroup__name=msg.get("AssignmentGroup__name", "⚠️ Không tìm thấy giá trị")
                )  # Đóng đúng dấu ngoặc ở đây

                await channel.send(message)
                print(f"✅ Đã gửi tin nhắn cho {msg.get('learner_id')} trong channel {msg.get('channel_id')}")
            except KeyError as e:
                print(f"⚠️ Thiếu biến {e} trong template {msg.get('message_type')}")
        else:
            print(f"❌ Không tìm thấy channel {channel_id}")

bot.run(DISCORD_BOT_TOKEN)
