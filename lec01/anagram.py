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
    starget = list(target)
    with open('dictionary.sort.json', 'r') as f5:
        dic = json.load(f5)
        '''
        l = list(itertools.product(range(2),repeat=len(starget)))
        l.sort(reverse=True)
        print(starget)
        '''
        for k in range(len(starget),5,-1):
            l = list(itertools.combinations(starget,k))
            for j in l:
                j = sorted(j)
                ans = match(*j,**dic)
                if ans != None:
                    for e in ans:
                        if e in ['j','k','x','z','q']:
                            cou += 3
                        elif e in ['c','f','h','l','m','p','v','w','y']:
                            cou += 2
                        else:
                            cou += 1
                    print(ans+str(cou))
                    cou = 0
    
    
    
