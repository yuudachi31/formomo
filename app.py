from datetime import datetime
import keyboard
import time

# === 設定目標時間（精準到毫秒） ===
target_time = "15:41:00.000"  # 格式: HH:MM:SS.mmm
print(f"🎯 等待到 {target_time} 自動按下 Enter...\n")

# === 準備時間轉換 ===
today = datetime.now().strftime("%Y-%m-%d")
target_dt = datetime.strptime(f"{today} {target_time}", "%Y-%m-%d %H:%M:%S.%f")

# === 持續監控 ===
while True:
    now = datetime.now()
    if now >= target_dt:
        start_exec = datetime.now()  # 真正執行的瞬間
        keyboard.press_and_release('enter')
        end_exec = datetime.now()

        # 計算延遲時間（毫秒）
        delay_ms = (end_exec - target_dt).total_seconds() * 1000

        print(f"✅ 目標時間: {target_dt.strftime('%H:%M:%S.%f')[:-3]}")
        print(f"⌚ 實際觸發: {end_exec.strftime('%H:%M:%S.%f')[:-3]}")
        print(f"⚡ 誤差: {delay_ms:.3f} 毫秒")
        break

    time.sleep(0.0005)  # 降低 CPU 使用率（0.5毫秒檢查一次）

print("\n🕹️ 已結束監控")
    # time.sleep(1)
##11/12 15:00 21:00 https://www.momoshop.com.tw/edm/cmmedm.jsp?lpn=O7x0Cprfkd8  ，  https://www.momoshop.com.tw/mypage/MemberCenter.jsp?func=18&promoNo=20251031191035725
##11/13 15:00 https://www.momoshop.com.tw/edm/cmmedm.jsp?lpn=O7x0Cprfkd8  
##11/13 16:00 google

##11/14 18:00 
##11/18 16:00 https://www.cathay-cube.com.tw/cathaybk/personal/event/overview/credit-card/online-shopping/202511/momo202511_1