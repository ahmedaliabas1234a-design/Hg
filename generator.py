import random
import string

# دالة لتوليد كلمة مرور عشوائية قوية
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(chars) for _ in range(length))

# دالة توليد الإيميل
def generate_email(domain):
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{user}@{domain}"

# تحديد النطاقات
domains = ["gmail.com", "hotmail.com"]

# توليد البيانات وحفظها في ملف
with open("accounts.txt", "w") as f:
    for _ in range(10): # توليد 10 حسابات
        domain = random.choice(domains)
        email = generate_email(domain)
        password = generate_password()
        
        # تنسيق البيانات بشكل منظم
        line = f"الإيميل: {email} | كلمة المرور: {password}\n"
        f.write(line)
        print(line.strip())

print("\n--- تم حفظ 10 حسابات في ملف 'accounts.txt' ---")
