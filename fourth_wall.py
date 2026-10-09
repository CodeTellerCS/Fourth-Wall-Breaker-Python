import os
import time
import pyautogui
import random

# المستوى 1: كشف الهوية
real_name = os.getlogin()
print(f"[!] SECURITY BREACH: I know who you are, {real_name}...")
time.sleep(2) # صمت برمجي قصير لبناء التوتر

# المستوى 2: سلب السيطرة
print("[!] TAKING CONTROL. Don't try to move the mouse...")
time.sleep(1)

for i in range(20): 
    x = random.randint(100, 1000)
    y = random.randint(100, 800)
    pyautogui.moveTo(x, y, duration=0.1)

# المستوى 3: ترك الأثر في العالم الحقيقي
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
file_path = os.path.join(desktop_path, 'I_AM_HERE.txt')

with open(file_path, 'w') as file:
    file.write(f"Did you really think you can just close me, {real_name}?\n")
    file.write("I am always watching.")

time.sleep(1)
os.startfile(file_path) # فتح الملف