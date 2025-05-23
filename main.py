from instagrapi import Client
import time

# ---------- LOGIN ----------
cl = Client()
try:
    cl.login("godhu408", "Oggy420")  # Use environment variables in production!
    print("✅ Logged in successfully.")
except Exception as e:
    print(f"❌ Login failed: {e}")
    exit()

# ---------- LOAD MESSAGES ----------
try:
    with open("messages.txt", "r") as file:
        messages = [line.strip() for line in file if line.strip()]
    print(f"✅ Loaded {len(messages)} messages.")
except Exception as e:
    print(f"❌ Failed to load messages: {e}")
    exit()

# ---------- SET THREAD ID FOR GROUP CHAT ----------
group_thread_id = "9694639830661817"  # Replace with actual thread ID
delay_seconds = 12  # Time delay between messages

# ---------- SEND MESSAGES TO GROUP CHAT ----------
for message in messages:
    try:
        cl.direct_send(message, thread_ids=[group_thread_id])
        print(f"✅ Sent to group (Thread ID: {group_thread_id}): '{message}'")
        time.sleep(delay_seconds)
    except Exception as e:
        print(f"❌ Failed to send message to group: {e}")
