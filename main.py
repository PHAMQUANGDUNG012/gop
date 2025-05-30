# mở code    
import requests
from rich.table import Table
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from colorama import init, Fore
import os, time
import sys 
import base64
import uuid
import os
import json
import dns.resolver
import socket
from random import randint
from pystyle import Write, Colors
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from bs4 import BeautifulSoup
import socket
from datetime import datetime
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")

import os
import requests 
import sys
import time
from pystyle import*
from time import sleep
print('__Các thư viện đã được kiểm tra và cài đặt (nếu cần)__')
os.system('cls' if os.name == 'nt' else 'clear')
#Color
trang = "\033[1;37m"
xanhla = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
xanhla = "\033[1;32m"

#Đánh Dấu Bản Quyền
HD_tool = trang + " " + trang + "[" + do + "+_+" + trang + "] " + trang + "=> "
mquang = trang + " " + trang + "[" + do + "÷_+" + trang + "] " + trang + "=> "
thanh = f'{do}[{trang}</>{do}] {trang}=>'

import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
import os
import sys
import subprocess
from colorama import Fore

# Danh sách thư viện cần kiểm tra
libraries = [
    "requests",
    "tabulate",
    "art",
    "colorama",
    "random_user_agent",
    "dnspython",
    "pystyle",
    "rich"
]
# Hàm chống bung
def check_internet_connection():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
if not check_internet_connection():
    print("\033[1;36mMày tưởng chiêu này t kh biết fix hả, Chiêu này cũ lũ sĩ từ đời nào rồi 😂😂😂!")
    exit()
# Hàm kiểm tra và cài đặt thư viện
def install_libraries():
    missing_libraries = []
    for lib in libraries:
        try:
            __import__(lib)
        except ImportError:
            missing_libraries.append(lib)

    if missing_libraries:
        print(f"🔧 Đang cài đặt các thư viện cần thiết : {', '.join(missing_libraries)} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing_libraries])
        print("\033[1;32m✅ Cài đặt thành công!!")
        os.system("cls" if os.name == "nt" else "clear") 
        

# Chạy kiểm tra và cài đặt nếu cần
try:
    import os, random, string, requests, time, webbrowser
    from rich.console import Console
    from datetime import datetime, timedelta
    from rich.text import Text
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareName, OperatingSystem
    import dns.resolver
    import socket
except:
    install_libraries()
os.system("")
# Hàm xóa màn hình
def clear():
    os.system("cls" if os.name == "nt" else "clear")  # Xóa màn hình tùy theo hệ điều hành
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8']
org_socket = socket.getaddrinfo
os.system('cls' if os.name == 'nt' else 'clear')

def google_socket(host, port, family=0, type=0, proto=0, flags=0):
    try:
        info = resolver.resolve(host)
        ip_address = info[0].to_text()
        return org_socket(ip_address, port, family, type, proto, flags)
    except:
        return org_socket(host, port, family, type, proto, flags)

# hàm chống bug 
def check_internet_connection():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
if not check_internet_connection():
    print("\033[1;36mMày tưởng chiêu này t kh biết fix hả, Chiêu này cũ lũ sĩ từ đời nào rồi 😂😂😂!")
    exit()

socket.getaddrinfo = google_socket
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
clear()
console = Console()
text = Text("MENU", style="bold")
colors = ["red", "orange", "yellow", "green"]  # Không có màu trắng

for i, char in enumerate(text.plain):
    text.stylize(colors[i % len(colors)], i, i + 1)
    
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
# =======================[ NHẬP KEY ]=======================
import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")
sleep(1)
banner=f"""
██████╗   ██████╗  ██████╗  ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗ ██╔═══██╗ ██╔══██╗ ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██████╔╝ ██║   ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
██╔═══╝  ██║▄▄ ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
██║      ╚██████╔╝ ██████╔╝    ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝       ╚══▀▀═╝  ╚═════╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ 
\033[1;35m═════════════════════════════════════════════════════════
\033[1;35m{do}[{trang}</>{do}] {trang}=>  \033[1;36mADMIN   \033[1;35m  ║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m PHAM QUANG DŨNG
\033[1;35m{do}[{trang}</>{do}] {trang}=>  \033[1;36mADMIN   \033[1;35m  ║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m PHƯỚC AN                  
\033[1;35m{do}[{trang}</>{do}] {trang}=>  \033[1;36mZALO\033[1;35m      ║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m 0336502026
\033[1;35m{do}[{trang}</>{do}] {trang}=>  \033[1;36mBOX ZALO\033[1;35m  ║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m https://zalo.me/g/mprgxe166                       
\033[1;36m{do}[{trang}</>{do}] {trang}=>  \033[1;36mHÔM NAY   \033[1;35m║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m {ngay_hom_nay}/{thang_nay}/{nam_}                   
\033[1;35m═════════════════════════════════════════════════════════            
"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.001)


# Hàm rút gọn link bằng YeuMoney
def get_shortened_link_yeumoney(url):
    token = "8651d2430b5ef302a4b52583279bbc6dd1449990d7ae82f2d757357abd5088fb"  # Thay bằng token của bạn
    api_url = f"https://yeumoney.com/QL_api.php?token={token}&format=text&url={url}"

    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()  # Lấy link rút gọn
        else:
            return "Lỗi khi kết nối API!"
    except Exception as e:
        return f"Lỗi: {e}"

# Hàm tạo key ngẫu nhiên
def generate_random_key(length=8):
    """Tạo chuỗi ngẫu nhiên với chữ cái + số."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_key(is_admin=False):
    """Tạo key, admin key không hết hạn."""
    if is_admin:
        return "PQD-ADMIN"  # Key admin không có ngày hết hạn
    else:
        return f"PQD-{generate_random_key(6)}"  # Key user

# Hàm lưu key vào file (chỉ lưu 1 key)
def save_key_to_file(key):
    """Lưu key vào file, ghi đè để chỉ lưu 1 key."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Thời gian lưu key
    with open("KEYPQD.txt", "w") as f:  # Dùng mode "w" để ghi đè
        f.write(f"{key} | {timestamp}\n")

# Hàm kiểm tra và xóa key nếu đã qua 00:00
def clean_expired_key():
    """Xóa key nếu đã qua 00:00 của ngày hôm sau."""
    if not os.path.exists("KEYPQD.txt"):
        return
    
    updated_lines = []
    current_time = datetime.now()
    current_date = current_time.date()  # Ngày hiện tại
    
    with open("KEYPQD.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            try:
                key, timestamp = line.strip().split(" | ")
                key_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                key_date = key_time.date()  # Ngày tạo key
                # Nếu key không phải admin và đã qua ngày mới (00:00), bỏ qua
                if not key.startswith("PQD-ADMIN") and key_date == current_date:
                    updated_lines.append(line)
                elif key.startswith("PQD-ADMIN"):  # Giữ lại key admin
                    updated_lines.append(line)
            except:
                continue
    
    # Ghi lại key còn hiệu lực (nếu không còn key nào thì file sẽ trống)
    with open("KEYPQD.txt", "w") as f:
        f.writelines(updated_lines)

# Hàm kiểm tra key hợp lệ
def is_valid_key(key, expected_key):
    """Kiểm tra key có hợp lệ không."""
    clean_expired_key()  # Dọn dẹp key hết hạn trước
    
    if key == "PQD-ADMIN":
        return True  # Key admin hợp lệ mọi lúc
    elif key == expected_key:  # So sánh với key đã tạo
        return True
    return False

# Hàm kiểm tra key đã lưu và còn hạn không
def check_stored_key():
    """Kiểm tra xem có key nào còn hạn trong file không, trả về key nếu hợp lệ."""
    clean_expired_key()  # Dọn dẹp key hết hạn trước
    
    if not os.path.exists("KEYPQD.txt"):
        return None, None
    
    current_time = datetime.now()
    current_date = current_time.date()  # Ngày hiện tại
    with open("KEYPQD.txt", "r") as f:
        for line in f:
            try:
                stored_key, timestamp = line.split(" | ")
                stored_key = stored_key.strip()
                key_time = datetime.strptime(timestamp.strip(), "%Y-%m-%d %H:%M:%S")
                key_date = key_time.date()  # Ngày tạo key
                if stored_key == "PQD-ADMIN":
                    return stored_key, stored_key  # Key admin luôn hợp lệ
                elif stored_key.startswith("PQD-"):
                    if key_date == current_date:  # Key chỉ hợp lệ trong cùng ngày
                        return stored_key, stored_key
            except:
                continue
    return None, None

# ======= Chạy Tool =======
try:
    admin_key = "PQD-ADMIN"
    
    # Kiểm tra xem có key nào còn hạn trong file không
    stored_key, user_key = check_stored_key()
    
    # Nếu không có key còn hạn, tạo key mới và yêu cầu người dùng vượt link
    if not stored_key:
        user_key = generate_key(is_admin=False)
        # Tạo link YeuMoney chứa key
        link_can_rut = f"https://www.webkey.x10.mx/?ma={user_key}"  # Thay bằng URL mới của bạn
        short_link = get_shortened_link_yeumoney(link_can_rut)
        print(f"{do}[{trang}</>{do}] {trang}=> LINK LẤY KEY : {short_link}")
        
        while True:
            nhap_key = input(f"{thanh} Nhập Key Đã Vượt : ").strip()
            
            if is_valid_key(nhap_key, user_key):
                # Lưu key vừa nhập thành công vào file (ghi đè key cũ)
                save_key_to_file(nhap_key)
                print("\033[1;32m✅ Key hợp lệ! Đang check key...", end="\r")
                time.sleep(3)  # Chờ 3 giây trước khi vào tool
                print("\033[F\033[K" * 3, end="")  # Xóa 3 dòng vừa in
                break  
            else:
                print("\033[1;31m❌ Key không hợp lệ. Vui lòng vượt link lại để lấy key!", end="\r")
                time.sleep(2)
                print("\033[F\033[K" * 2, end="")  # Xóa 2 dòng vừa in
    else:
        # Nếu có key còn hạn, hiển thị link YeuMoney nhưng không yêu cầu nhập lại
        link_can_rut = f"https://www.webkey.x10.mx/?ma={stored_key}"
        short_link = get_shortened_link_yeumoney(link_can_rut)
        print(f"{thanh} LINK LẤY KEY : {short_link}")
        print(f"{thanh} Key còn hạn. Đang xác nhận key...")
        time.sleep(3)  # Chờ 3 giây trước khi vào tool
        print("\033[F\033[K" * 4, end="")

except Exception as e:
    console.print(f"[bold red]ErrolKey: {e}[/bold red]")
    exit('Bạn định bug à,có cái lồn 😆')
    
import os
os.system("cls" if os.name == "nt" else "clear")
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
xoss('\n\033[1;32m[●] Đang Load API Tool...');time.sleep(0.10)
xoss('\n\033[1;36m[●] kiểm tra sever tool...')
xoss('\n\033[1;33m[●] kiểm tra bản update.. ')
xoss('\n\033[1;34m[●] Tiến hành vào tool...')
def Update():
    exit('\033[1;31m[●] Đang Tiến Hành Vào Tool...... ')
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()

if __name__ == "__main__":
    main()
# Mã màu ANSI cho 7 sắc cầu vồng
rainbow_colors = [
    "\033[91m",  # Đỏ
    "\033[93m",  # Vàng
    "\033[92m",  # Xanh lá
    "\033[96m",  # Xanh dương nhạt
    "\033[94m",  # Xanh dương
    "\033[95m",  # Tím
    "\033[97m"   # Trắng
]

def banner():
    banner = f"""
██████╗   ██████╗  ██████╗  ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗ ██╔═══██╗ ██╔══██╗ ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██████╔╝ ██║   ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
██╔═══╝  ██║▄▄ ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
██║      ╚██████╔╝ ██████╔╝    ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝       ╚══▀▀═╝  ╚═════╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ 
\033[1;35m═════════════════════════════════════════════════════════
\033[1;35m{do}[{trang}</>{do}] {trang}=>  \033[1;36mADMIN   \033[1;35m  ║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m PHAM QUANG DŨNG
\033[1;35m{do}[{trang}</>{do}] {trang}=>  \033[1;36mADMIN   \033[1;35m  ║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m PHƯỚC AN                  
\033[1;35m{do}[{trang}</>{do}] {trang}=>  \033[1;36mZALO\033[1;35m      ║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m 0336502026
\033[1;35m{do}[{trang}</>{do}] {trang}=>  \033[1;36mBOX ZALO\033[1;35m  ║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m https://zalo.me/g/mprgxe166                       
\033[1;36m{do}[{trang}</>{do}] {trang}=>  \033[1;36mHÔM NAY   \033[1;35m║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m {ngay_hom_nay}/{thang_nay}/{nam_}                   
\033[1;35m═════════════════════════════════════════════════════════   
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)
banner()

if __name__ == "__main__":
    main()
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "🌸"
# Mã màu ANSI cho nhiều màu sắc
rainbow_colors = [
    "\033[91m",  # Đỏ
    "\033[93m",  # Vàng
    "\033[92m",  # Xanh lá
    "\033[96m",  # Xanh dương nhạt
    "\033[94m",  # Xanh dương
    "\033[95m",  # Tím
    "\033[97m"   # Trắng
]

reset_color = "\033[0m"  # Màu mặc định

def in_dong_khung_cau_vong(text):
    # Tạo khung với màu sắc thay đổi cho mỗi ký tự trong thanh ngang và nội dung
    khung_tren = "┌"
    khung_duoi = "└"
    
    for i in range(len(text) + 2):
        khung_tren += rainbow_colors[i % len(rainbow_colors)] + "─" + reset_color
    khung_tren += "┐"
    
    # Tô màu cho nội dung bên trong
    noi_dung = ""
    for i, char in enumerate(text):
        noi_dung += rainbow_colors[i % len(rainbow_colors)] + char
    noi_dung = noi_dung + reset_color
    
    dong_duoc_khung = f"{khung_tren}\n{rainbow_colors[6]}│ {noi_dung} │{reset_color}\n{khung_duoi}"
    
    print(dong_duoc_khung)

# Mã màu ANSI cho nhiều màu sắc
rainbow_colors = [
    "\033[91m",  # Đỏ
    "\033[93m",  # Vàng
    "\033[92m",  # Xanh lá
    "\033[96m",  # Xanh dương nhạt
    "\033[94m",  # Xanh dương
    "\033[95m",  # Tím
    "\033[97m"   # Trắng
]

reset_color = "\033[0m"  # Màu mặc định

def in_mau(text):
    # Tô màu cho nội dung
    noi_dung = ""
    for i, char in enumerate(text):
        noi_dung += rainbow_colors[i % len(rainbow_colors)] + char
    noi_dung += reset_color
    
    print(noi_dung)

time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngayhomnay = now.strftime("%d")
thangnay = now.strftime("%m")
nam = now.strftime("%Y")  
ip = requests.get('https://kiemtraip.com/raw.php').text  
    
# hàm chống bug 
def check_internet_connection():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
if not check_internet_connection():
    print("\033[1;36mMày tưởng chiêu này t kh biết fix hả,Chiêu này cũ lũ sĩ từ đời nào rồi 😂😂😂!")
    exit()
# Các dòng được đóng khung 7 sắc cầu vồng
banne=f'''\033[1;36m
██████╗   ██████╗  ██████╗  ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗ ██╔═══██╗ ██╔══██╗ ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██████╔╝ ██║   ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
██╔═══╝  ██║▄▄ ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
██║      ╚██████╔╝ ██████╔╝    ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝        ══▀▀═╝  ╚═════╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
{trang}-----------------------------------------------------------------
{thanh} {xanhla}ZALO ADMIN : {trang}0336502026(PQD-TOOL)
{thanh} {lam}Zalo Box : {trang}https://zalo.me/g/mprgxe166
{thanh} {lam}IP MẠNG : {trang}{ip}
{thanh} {xanhla}NGÀY : {trang}{ngayhomnay}/{thangnay}/{nam}{lam} GIỜ : {trang}{time}
{trang}-----------------------------------------------------------------
╔═══════════════════════════╗
║ TOOL TRAODOISUB FACEBOOK  ║
╚═══════════════════════════╝
{thanh} {luc}Nhập {red}[{vang}1{red}] {luc}Tool TDS FACEBOOK[ĐANG LÀM]
{thanh} {luc}Nhập {red}[{vang}2{red}] {luc}Tool TDS TIKTOK[ĐANG LÀM]{trang}
╔════════════════════════════╗
║ TOOL TUONGTACCHEO FACEBOOK ║
╚════════════════════════════╝
{thanh} {luc}Nhập {red}[{vang}3{red}] {luc}Tool TTC Facebook{trang}
╔════════════════════════════╗
║ TOOL TIỆN ÍCH MỚI          ║
╚════════════════════════════╝
{thanh} {luc}Nhập {red}[{vang}4{red}] {luc}Tool FAKE CĂN CƯỚC
{thanh} {luc}Nhập {red}[{vang}5{red}] {luc}Tool REG Page PRO5[ĐANG LÀM]
{thanh} {luc}Nhập {red}[{vang}6{red}] {luc}Tool Kết Bạn Facebook[ĐANG LÀM]
{thanh} {luc}Nhập {red}[{vang}7{red}] {luc}THOÁT TOOL
{trang}-----------------------------------------------------------------'''
print(banne)
chon = str(input('\033[91m🌸 \033[93m➩\033[96m CHỌN : \033[92m'))
def check_internet_connection():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
if not check_internet_connection():
    print("\033[1;31mCheck Mạng Wifi Đi! BUNG ĐÂU CÓ DỄ :)))")
    exit()
#golike
if chon == '1':
    exec(requests.get('').text)
elif chon == '2':
    exec(requests.get(' ').text)
elif chon == '3':
    exec(requests.get('https://raw.githubusercontent.com/PHAMQUANGDUNG012/gop/refs/heads/main/ttc.py').text)
#trao đổi sub
elif chon == '4':
	exec(requests.get('https://raw.githubusercontent.com/PHAMQUANGDUNG012/gop/refs/heads/main/cancuoc.py').text)
elif chon == '5':
	exec(requests.get('').text)
#tương tác chéo
elif chon == '6':
	exec(requests.get('').text)
elif chon == '7':
	exec(requests.get('https://raw.githubusercontent.com/PHAMQUANGDUNG012/gop/refs/heads/main/thoat.py').text)
elif chon == '8':
	exec(requests.get('').text)
elif chon == '9':
	exec(requests.get('').text)
elif chon == '10':
	exec(requests.get('').text)
elif chon == '11':
	exec(requests.get('').text)
elif chon == '12':
	exec(requests.get('').text)
elif chon == '13':
	exec(requests.get('').text)
elif chon == '14':
	exec(requests.get('').text)
elif chon == '15':
	exec(requests.get('').text)
elif chon == '16':
	exec(requests.get('').text)
elif chon == '17':
	exec(requests.get('').text)
elif chon == '18':
	exec(requests.get('').text)
elif chon == '19':
	exec(requests.get('').text)
elif chon == '20':
	exec(requests.get('').text)
elif chon == '21':
	exec(requests.get('').text)
elif chon == '22':
	exec(requests.get('').text)

else:

    print("Mày Bị Mù À?")
    exit()
