import random
import requests

# دریافت عبارت جستجو از کاربر
search_query = input("Enter Your Search In Github: ")

# ارسال درخواست جستجو به API گیت هاب
response = requests.get(f'https://api.github.com/search/repositories?q={search_query}')
search_results = response.json()

# بررسی وجود نتایج جستجو
if 'items' in search_results and len(search_results['items']) > 0:
    # انتخاب یک نتیجه رندوم
    random_result = random.choice(search_results['items'])
    
    # دریافت لینک پروژه
    project_link = random_result['html_url']
    
    print(f"Random Project: {project_link}")
else:
    print("No search results found.")