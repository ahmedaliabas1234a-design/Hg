import random
import string
import datetime

# إعدادات المولد
DOMAINS = ["gmail.com", "hotmail.com", "outlook.com"]
CHARS = string.ascii_lowercase + string.digits

def generate_account():
    # اسم مستخدم عشوائي بطول 8-12 حرف
    user = ''.join(random.choices(CHARS, k=random.randint(8, 12)))
    domain = random.choice(DOMAINS)
    
    # كلمة مرور قوية جداً (16 خانة)
    password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=16))
    
    return f"{user}@{domain}", password

# تنفيذ العملية
def save_accounts(count=20):
    filename = "accounts.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"--- تقرير توليد الحسابات | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ---\n\n")
        
        for i in range(1, count + 1):
            email, password = generate_account()
            line = f"[{i}] البريد: {email} | الرمز: {password}\n"
            f.write(line)
            print(f"تم توليد حساب رقم {i}")
            
    print(f"\n✅ اكتملت المهمة! تم حفظ {count} حساب في ملف {filename}")

# تشغيل الأداة
save_accounts(20)
