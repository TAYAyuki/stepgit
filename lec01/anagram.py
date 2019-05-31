'''
#dictionary.wordsファイルの小文字処理
with open('dictionary.words.txt','r') as f:
    with open('dictionary.lower.txt', 'w') as f2:
        for line in f:
            s = line.lower()
            f2.write(s)
'''
'''
#{英単語:sortした英単語のリスト}
import json
with open('dictionary.lower.txt', "r") as f3:
    with open('dictionary.sort.json', "w") as f4:
        dic = {}
        lines = f3.readlines()
        for line in lines:
            line = line.strip() #ln del
            dic[line] = sorted(line)
        json.dump(dic,f4)
'''
'''
#sortした英単語のリスト全部をsort
import json
with open('dictionary.sort.json', "r") as f:
    with open('dictionary.sortall.json', "w") as f2:
        dic = json.load(f)
        dic_sorted = sorted(dic.items(), key=lambda x:x[1])
        json.dump(dic_sorted,f2)
        
'''
            
import json
from bs4 import BeautifulSoup
import urllib.request as req
import re
from selenium import webdriver

url = "https://icanhazwordz.appspot.com"
res = req.urlopen(url)
html = res.read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
div = soup.find_all("div")
driver = webdriver.Chrome()
driver.get(url)

moji = ''
for tag in div:
    try:
        string_ = tag.get("class").pop(0)
        if string_ in "letter":
             moji += tag.string
    except:
        pass
moji = moji.lower()
print(moji)

if __name__ == "__main__":
    answer = ''
    real_answer = ''
    t = []
    counter = 0
    maximum = 0
    #target = input()
    target = moji
    
    sorted_target = list(sorted(target))
    holdtarget = list(sorted(target))
    with open('dictionary.sortall.json', 'r') as f5:
        dic = json.load(f5)
        for i in range(len(dic)):
            for j in range(len(dic[i][1])):
                if dic[i][1][j] in sorted_target:
                    sorted_target.remove(dic[i][1][j])
                    if j == len(dic[i][1])-1:
                        answer = dic[i][0]
                else:
                    sorted_target = list(sorted(target))
                    break
                    
            if answer != None:
                for e in answer:
                    if e in ['j','k','x','z','q']:
                        counter += 3
                    elif e in ['c','f','h','l','m','p','v','w','y']:
                        counter += 2
                    else:
                        counter += 1
                if counter >= maximum:
                    real_answer = answer
                    maximum = counter
                counter = 0
                answer = None
                sorted_target = holdtarget
        print(real_answer)
        driver.find_element_by_name('move').send_keys(real_answer)
        driver.find_element_by_type('Submit').click()
