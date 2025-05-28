
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
import random
import requests
import base64
from datetime import datetime, timedelta
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
thanh = f'{do}[{trang}</>{do}] {trang}=>'


class CanCuocCongDan:
    def __init__(self):
        self.province_codes = {
            "Hà Nội": "001",
            "Hà Giang": "002",
            "Cao Bằng": "004",
            "Bắc Kạn": "006",
            "Tuyên Quang": "008",
            "Lào Cai": "010",
            "Điện Biên": "011",
            "Lai Châu": "012",
            "Sơn La": "014",
            "Yên Bái": "015",
            "Hòa Bình": "017",
            "Thái Nguyên": "019",
            "Lạng Sơn": "020",
            "Quảng Ninh": "022",
            "Bắc Giang": "024",
            "Phú Thọ": "025",
            "Vĩnh Phúc": "026",
            "Bắc Ninh": "027",
            "Hải Dương": "030",
            "Hải Phòng": "031",
            "Hưng Yên": "033",
            "Thái Bình": "034",
            "Hà Nam": "035",
            "Nam Định": "036",
            "Ninh Bình": "037",
            "Thanh Hóa": "038",
            "Nghệ An": "040",
            "Hà Tĩnh": "042",
            "Quảng Bình": "044",
            "Quảng Trị": "045",
            "Thừa Thiên Huế": "046",
            "Đà Nẵng": "048",
            "Quảng Nam": "049",
            "Quảng Ngãi": "051",
            "Bình Định": "052",
            "Phú Yên": "054",
            "Khánh Hòa": "056",
            "Ninh Thuận": "058",
            "Bình Thuận": "060",
            "Kon Tum": "062",
            "Gia Lai": "064",
            "Đắk Lắk": "066",
            "Đắk Nông": "067",
            "Lâm Đồng": "068",
            "Bình Phước": "070",
            "Tây Ninh": "072",
            "Bình Dương": "074",
            "Đồng Nai": "075",
            "Bà Rịa - Vũng Tàu": "077",
            "Hồ Chí Minh": "079",
            "Long An": "080",
            "Tiền Giang": "082",
            "Bến Tre": "083",
            "Trà Vinh": "084",
            "Vĩnh Long": "086",
            "Đồng Tháp": "087",
            "An Giang": "089",
            "Kiên Giang": "091",
            "Cần Thơ": "092",
            "Hậu Giang": "093",
            "Sóc Trăng": "094",
            "Bạc Liêu": "095",
            "Cà Mau": "096"
        }

    def generate_random_number(self, issue_date):
        try:
            issue_date = datetime.strptime(issue_date, "%d/%m/%Y")
            day_of_year = issue_date.timetuple().tm_yday
            if day_of_year < 180:
                num = random.randint(100, 99999)
            else:
                num = random.randint(99999, 999999)
            return str(num).zfill(6)
        except ValueError:
            return None

    def calculate_issue_and_expiry_dates(self, birth_date_str):
        try:
            birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
        except ValueError:
            return {"status": "false", "msg": "Ngày sinh không hợp lệ."}
        
        current_date = datetime.now()
        age = (current_date - birth_date).days // 365

        if age < 14:
            return {"status": "false", "msg": "Công dân chưa đủ tuổi để cấp thẻ CCCD."}
        randay = random.randint(30,90)
        if 14 <= age < 25:
            expiry_age = 25
            issue_date = birth_date + timedelta(days=14*365 + randay)
        elif 25 <= age < 40:
            expiry_age = 40
            issue_date = birth_date + timedelta(days=25*365 + randay)
        elif 40 <= age < 60:
            expiry_age = 60
            issue_date = birth_date + timedelta(days=40*365 + randay)
        else:
            expiry_age = None
            issue_date = birth_date + timedelta(days=60*365 + randay)
            
        if expiry_age:
            tach = str(birth_date_str).split('/')
            so_cuoi = int(tach[-1]) + expiry_age
            expiry_date = tach[0] + '/' + tach[1] + '/' + str(so_cuoi)
        else:
            expiry_date = "Thẻ CCCD có giá trị suốt đời"

        issue_date_str = issue_date.strftime("%d/%m/%Y")
        expiry_date_str = expiry_date if expiry_date != "Thẻ CCCD có giá trị suốt đời" else expiry_date

        return {
            "status": "true",
            "Ngày cấp thẻ": issue_date_str,
            "Hạn thẻ": expiry_date_str
        }

    def generate_cccd(self, province_name, gender, birth_date_str, issue_date_str):
        province_code = self.province_codes.get(province_name)
        if not province_code:
            return {"status": "false", "msg": "Tên tỉnh không hợp lệ."}

        if gender not in ["Nam", "Nữ"]:
            return {"status": "false", "msg": "Giới tính không hợp lệ."}

        try:
            birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
        except ValueError:
            return {"status": "false", "msg": "Ngày sinh không hợp lệ."}

        birth_year = birth_date.year

        if birth_year < 1900 or birth_year > 2099:
            return {"status": "false", "msg": "Năm sinh không hợp lệ."}

        if birth_year < 2000:
            gender_code = 0 if gender == "Nam" else 1
        else:
            gender_code = 2 if gender == "Nam" else 3

        birth_year_code = str(birth_year)[-2:]
        random_number = self.generate_random_number(issue_date_str)

        if not random_number:
            return {"status": "false", "msg": "Ngày cấp thẻ không hợp lệ."}

        cccd = f"{province_code}{gender_code}{birth_year_code}{random_number}"
        return {"status": "true", "socccd": cccd}

    def Create(self, gender, birth_date_str, province_name):
        dates = self.calculate_issue_and_expiry_dates(birth_date_str)
        if dates['status'] != 'true':
            return dates

        cccd = self.generate_cccd(province_name, gender, birth_date_str, dates['Ngày cấp thẻ'])
        if cccd['status'] != 'true':
            return cccd
        else:
            return cccd, dates
def clear():
    os.system("cls" if os.name == "nt" else "clear") 
# hàm chống bug 
def validate_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Lỗi: Trường hợp này không được để trống. Vui lòng nhập lại.")

def validate_date(prompt):
    while True:
        date_str = input(prompt).strip()
        if not date_str:
            print("Lỗi: Trường hợp này không được để trống. Vui lòng nhập lại.")
            continue
        try:
            return datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            print("Lỗi: Ngày không hợp lệ. Vui lòng nhập lại theo định dạng dd/mm/yyyy.")

def validate_gender(prompt):
    while True:
        gender = input(prompt).capitalize().strip()
        if not gender:
            print("Lỗi: Trường hợp này không được để trống. Vui lòng nhập lại.")
        elif gender in ["Nam", "Nữ"]:
            return gender
        else:
            print("Lỗi: Giới tính không hợp lệ. Chỉ nhập 'Nam' hoặc 'Nữ'.")

def validate_socccd(prompt):
    while True:
        socccd = input(prompt).strip()
        if not socccd:
            print("Lỗi: Trường hợp này không được để trống. Vui lòng nhập lại.")
        elif (socccd.isdigit() and len(socccd) == 12):
            return socccd
        else:
            print("Lỗi: Số CCCD không hợp lệ. Nhập 12 chữ số.")

def validate_province(prompt, valid_provinces):
    while True:
        province = input(prompt).title().strip()
        if not province:
            print("Lỗi: Trường hợp này không được để trống. Vui lòng nhập lại.")
        for prv in valid_provinces:
            if prv in province:
                return province
        print("Lỗi: Tên tỉnh/thành không hợp lệ. Vui lòng nhập lại.")

def validate_url(prompt):
    while True:
        url = input(prompt).strip()
        if not url:
            print("Lỗi: Trường hợp này không được để trống. Vui lòng nhập lại.")
        elif requests.utils.urlparse(url).scheme in ['http', 'https']:
            return url
        else:
            print("Lỗi: Link không hợp lệ. Vui lòng nhập một URL hợp lệ bắt đầu bằng http hoặc https.")
banne = f'''
\033[1;36m
██████╗   ██████╗  ██████╗  ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗ ██╔═══██╗ ██╔══██╗ ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██████╔╝ ██║   ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
██╔═══╝  ██║▄▄ ██║ ██║  ██║    ██║   ██║   ██║██║   ██║██║     
██║      ╚██████╔╝ ██████╔╝    ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝        ╚══▀▀═╝ ╚═════╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ 
\033[1;35m╔════════════╗═════════════════════════════════════════\033[1;35m╗
\033[1;35m║            ║                                         \033[1;35m║ 
\033[1;35m║  \033[1;36mADMIN   \033[1;35m  ║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m PHAM QUANG DŨNG                   \033[1;35m║
\033[1;35m║  \033[1;36mMBBANK\033[1;35m    ║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m 0336502026                        \033[1;35m║
\033[1;35m║  \033[1;36mTELEGRAM \033[1;35m ║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m CHUOTHAMTO                        \033[1;35m║
\033[1;35m║  \033[1;36mHÔM NAY   \033[1;35m║▶\033[1;36m[ \033[1;31m+ \033[1;36m]\033[1;34m {ngay_hom_nay}/{thang_nay}/{nam_}                   \033[1;35m     ║
\033[1;35m║            ║                                         ║   
\033[1;35m╚════════════╝═════════════════════════════════════════╝          '''
clear()
print(banne)
option = validate_non_empty(f"{thanh}\033[1;37mCó muốn tự động tạo số CCCD không tạo có thể trùng với người thật (Y/n):{tim} ")
if option.lower() != 'y':
    name = validate_non_empty(f"{thanh}\033[1;37mNhập Tên:{tim} ")
    socccd = validate_socccd(f"{thanh}\033[1;37mNhập Số CCCD:{tim} ")
    birthday = validate_date(f"{thanh}\033[1;37mNhập Ngày Sinh (dd/mm/yyyy):{tim} ")
    sex = validate_gender(f"{thanh}\033[1;37mNhập Giới Tính (Nam/Nữ):{tim} ")
    quequan = validate_province(f"{thanh}\033[1;37mNhập Quê Quán ( Ví dụ: Thị trấn Đình Cả, Võ Nhai, Thái Nguyên ):{tim} ", CanCuocCongDan().province_codes)
    hangtren = validate_non_empty(f"{thanh}\033[1;37mNhập Hàng Trên Của Nơi Thường Trú ( Ví dụ: 30/18/19, Thống ) (Bỏ Qua Gõ None):{tim} ")
    hangduoi = validate_province(f"{thanh}\033[1;37mNhập Hàn Dưới Nơi Thường Trú ( Ví dụ: Nhất, Phường 10, Gò Vấp, TP.Hồ Chí Minh ):{tim} ", CanCuocCongDan().province_codes)
    thuongtru = validate_province(f"{thanh}\033[1;37mNhập Nơi Thường Trú Đầy Đủ ( Ví dụ: 30/18/19, Thống Nhất, Phường 10, Gò Vấp, TP.Hồ Chí Minh ):{tim} ", CanCuocCongDan().province_codes)
    noisinh = validate_province(f"{thanh}\033[1;37mNhập Nơi Sinh ( Ví dụ: Thái Nguyên ):{tim} ", CanCuocCongDan().province_codes)
    ngaycap = validate_date(f"{thanh}\033[1;37mNhập Ngày Cấp (dd/mm/yyyy):{tim} ")
    thoihan = validate_date(f"{thanh}\033[1;37mNhập Thời Hạn (dd/mm/yyyy):{tim} ")
    anhthe = validate_url(f"{thanh}\033[1;37mNhập Link Ảnh Thẻ:{tim} ")
    clear()
    print(banne)
else:
    socccd = 'auto'
    ngaycap = 'auto'
    thoihan = 'auto'
    name = validate_non_empty(f"{thanh}\033[1;37mNhập Tên:{tim} ")
    birthday = validate_date(f"{thanh}\033[1;37mNhập Ngày Sinh (dd/mm/yyyy):{tim} ")
    sex = validate_gender(f"{thanh}\033[1;37mNhập Giới Tính (Nam/Nữ):{tim} ")
    quequan = validate_province(f"{thanh}\033[1;37mNhập Quê Quán ( Ví dụ: Thị trấn Đình Cả, Võ Nhai, Thái Nguyên ):{tim} ", CanCuocCongDan().province_codes)
    hangtren = validate_non_empty(f"{thanh}\033[1;37mNhập Hàng Trên Của Nơi Thường Trú ( Ví dụ: 30/18/19, Thống ) (Bỏ Qua Gõ None):{tim} ")
    hangduoi = validate_province(f"{thanh}\033[1;37mNhập Hàn Dưới Nơi Thường Trú ( Ví dụ: Nhất, Phường 10, Gò Vấp, TP.Hồ Chí Minh ):{tim} ", CanCuocCongDan().province_codes)
    thuongtru = validate_province(f"{thanh}\033[1;37mNhập Nơi Thường Trú Đầy Đủ ( Ví dụ:  30/18/19, Thống Nhất, Phường 10, Gò Vấp, TP.Hồ Chí Minh ):{tim} ", CanCuocCongDan().province_codes)
    noisinh = validate_province(f"{thanh}\033[1;37mNhập Nơi Sinh ( Ví dụ: Thái Nguyên ):{tim} ", CanCuocCongDan().province_codes)
    anhthe = validate_url(f"{thanh}\033[1;34mNhập Link Ảnh Thẻ:{tim} ")
    clear()
    print(banne)
can_cuoc = CanCuocCongDan()
res = can_cuoc.Create(sex, birthday.strftime("%d/%m/%Y"), noisinh)
if isinstance(res, dict) and res.get('status') == 'false':
    print("Lỗi: ", res['msg'])
else:
    if isinstance(res, tuple) and len(res) == 2:
        cccd, dates = res
    else:
        print("Lỗi: Không thể tạo CCCD. Đã nhận kết quả không mong đợi.")
        exit()

    if socccd == 'auto':
        socccd = cccd['socccd']
    if ngaycap == 'auto':
        ngaycap = dates['Ngày cấp thẻ']
    if thoihan == 'auto':
        thoihan = dates['Hạn thẻ']
    
    print("Đang Tạo ...")
    response = requests.post("https://nguyenxuantrinh.id.vn/fake-cccd/api.php", data={
        "name": name,
        "socccd": socccd,
        "birthday": birthday.strftime("%d/%m/%Y"),
        "sex": sex,
        "quequan": quequan,
        "hangtren":hangtren,
        "hangduoi": hangduoi,
        "thuongtru": thuongtru,
        "ngaycap": ngaycap,
        "thoihan": thoihan,
        "anhthe": anhthe
    }).json()

    status = response["status"]
    print(response["msg"])
    if status != "success":
        exit()
    with open("mat_truoc.jpeg", "wb") as f:
        f.write(base64.b64decode(response.get("mat_truoc", "")))
    with open("mat_sau.jpeg", "wb") as f:
        f.write(base64.b64decode(response.get("mat_sau", "")))
    print("Đã Lưu Vào File mat_truoc.jpeg và mat_sau.jpeg")





