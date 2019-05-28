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
    target = input()
    starget = list(target)
    #starget = list(sorted(target))
    with open('dictionary.sort.json', 'r') as f5:
        dic = json.load(f5)
        l = list(itertools.product(range(2),repeat=len(starget)))
        l.sort(reverse=True)
        print(starget)
        for i in range(len(l)):
            if i == (len(l)-1):
                print('None')
                exit()
            for j in range(len(starget)):
                if l[i][j] == 1:
                    t.append(starget[j])
            t = sorted(t)
            ans = match(*t,**dic)
            t = []
            if ans != None:
                print(ans)
                exit()
    
    
    
