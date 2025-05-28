import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
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
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config
def clear():
    os.system("cls" if os.name == "nt" else "clear")
clear()    
print("\033[1;31m[\033[1;37m🌸\033[1;31m] \033[1;37m=> \033[1;32mCảm Bạn Đã sử dụng Tool của PHAMQUANGDUNG Nhé! chúc bạn một ngày vui\033[1;37m....!")