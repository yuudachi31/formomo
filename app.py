import time
import keyboard
from datetime import datetime

target_time = "15:38"  # 24小時制
print(f"等待到 {target_time} 自動按下 Enter...")

while True:
    now = datetime.now().strftime("%H:%M")
    if now == target_time:
        keyboard.press_and_release('enter')
        print("✅ 已在指定時間按下 Enter")
        print(datetime.now().strftime('%H:%M:%S.%f')[:-3])
        break
print("已結束監控")
    # time.sleep(1)
##11/12 15:00 21:00 https://www.momoshop.com.tw/edm/cmmedm.jsp?lpn=O7x0Cprfkd8  ，  https://www.momoshop.com.tw/mypage/MemberCenter.jsp?func=18&promoNo=20251031191035725
##11/13 15:00 https://www.momoshop.com.tw/edm/cmmedm.jsp?lpn=O7x0Cprfkd8  
##11/13 16:00 google

##11/14 18:00 
##11/18 16:00 https://www.cathay-cube.com.tw/cathaybk/personal/event/overview/credit-card/online-shopping/202511/momo202511_1