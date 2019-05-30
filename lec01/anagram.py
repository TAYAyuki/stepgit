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
import itertools

def match(*target,**d):
    target = list(target)
    for k,v in d.items():
        if target == v:
            return k   
            
if __name__ == "__main__":
    ans = ''
    t = []
    cou = 0
    target = input()
    starget = list(sorted(target))
    holdtarget = list(sorted(target))
    with open('dictionary.sortall.json', 'r') as f5:
        dic = json.load(f5)
        for i in range(len(dic)):
            for j in range(len(dic[i][1])):
                if dic[i][1][j] in starget:
                    starget.remove(dic[i][1][j])
                     #print(dic[i][1])
                    if j == len(dic[i][1])-1:
                        ans = dic[i][0]
                        #print(ans)
                     
                else:
                    starget = list(sorted(target))
                    break
                    
            if ans != None:
                for e in ans:
                    if e in ['j','k','x','z','q']:
                        cou += 3
                    elif e in ['c','f','h','l','m','p','v','w','y']:
                        cou += 2
                    else:
                        cou += 1
                if cou >= 8:
                    print(ans+str(cou))
                cou = 0
                ans = None
                starget = holdtarget
     
    
