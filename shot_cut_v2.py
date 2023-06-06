from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re 
import os 
import cv2
import random

def cut(driver,urls):
    try:
        time1 = time.time()
        driver.get(urls)
        time.sleep(random.uniform(0.5, 5)) # 随机等待
        save_name = ''.join(re.findall(r'[A-Za-z0-9]', urls)) + '.png'
        # 获取页面高度
        scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        # 设置视口大小和网页高度
        driver.set_window_size(375, scroll_height)
        if os.path.exists(save_imgs+save_name):
            pass 
        else:
            driver.save_screenshot(save_imgs+save_name)

        img=cv2.imread(save_imgs+save_name)
        if img is None:
            print('None cut_img',urls)
            w.write(urls+'\n')
        return

    except Exception as e:
        print(str(e))
        print("bad urls: ",urls)
        w.write(urls+'\n')
        return

if __name__ == "__main__":
    options = Options()
    options.add_argument('--headless')     # 无头模式，不显示浏览器界面
    options.add_argument('--disable-gpu')  # 禁用GPU加速
    options.add_argument('--referer=www.baidu.com')    #add referer ？？？
    options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    path_to_chromedriver = r'C:\Users\97696\Downloads\chromedriver.exe'
    # 创建Chrome浏览器实例
    driver = webdriver.Chrome(path_to_chromedriver, options=options)

    save_imgs = './imgs_cut_v2/'
    if not os.path.exists(save_imgs):
        os.mkdir(save_imgs)

    f = open('./urls.txt','r')
    w = open('save_error_url.txt','w')
    line = f.readline()
    while line:
        urls = line.strip('\n')
        print("Processing: ",urls)
        cut(driver,urls)
        line = f.readline()

    w.close()
    driver.quit()
