'''
##########################関数の概要################################
Input()
from_name に探し始めるニックネームを入力
to_name に探したいニックネームを入力

Nicknames_list_create()
nicknames.txt を [ID ,nickname] のリストにする

Name_ID_chanege()
from_name を from_name_id に、to_name を to_name_id に変換(nicknames.txt)

Links_list_creat()
links.txt を [id(from), id(to)] のリスト links_list にする

Follow_list_create(from_name_id, links_list, follow_list)
from_name_id から辿れる id をリストにして返す

Search()
from_name_id から 幅優先探索で to_name_id を探し、探索ステップ数 search_count を返す

test()
作成した test を実行する
'''
def Input():
    print('From name : ', end = '')
    from_name = input()
    print('To name : ',end = '')
    to_name = input()
    return from_name, to_name


def Nicknames_list_create():
    nicknames_list = []
    with open('nicknames.txt') as nicknames:
        nicknames_lines = nicknames.readlines()
        for nicknames_line in nicknames_lines: 
            nicknames_line = nicknames_line.replace("\t"," ") #タブ -> 空白
            nicknames_line = nicknames_line.replace("\n","") #改行 -> 削除
            if nicknames_line[1]==' ':
                nicknames_list.append([int(nicknames_line[0]),nicknames_line[2:]])
            else:
                nicknames_list.append([int(nicknames_line[0:2]),nicknames_line[3:]])
    return nicknames_list


def Name_ID_change(from_name, to_name, nicknames_list):
    to_name_id = 0
    from_name_id = 0
    for i in range(len(nicknames_list)):
        if from_name == nicknames_list[i][1]:
            from_name_id = int(nicknames_list[i][0])
        elif to_name == nicknames_list[i][1]:
            to_name_id = int(nicknames_list[i][0])
    return from_name_id, to_name_id


def Links_list_create():
    links_list = []
    with open('links.txt') as links:
        links = links.readlines()
        for link in links:
            link = link.replace("\t"," ")
            link = link.replace("\n","")
            if len(link) < 4:
                links_list.append([int(link[0]),int(link[2])])
            elif link[1] == ' ' and link[3] != ' ':
                links_list.append([int(link[0]),int(link[2:4])])
            elif link[1] != ' ' and len(link) < 5:
                links_list.append([int(link[0:2]),int(link[3])])
            else:
                links_list.append([int(link[0:2]),int(link[3:5])])
    return links_list


def Follow_list_create(from_name_id, links_list, follow_list):
    for link in links_list:
        if link[0] > from_name_id:
            break
        elif from_name_id == link[0]:
            follow_list.append(link[1])
    return follow_list


def Search(from_name_id,to_name_id,links_list):
    search_count = 1
    follow_list_all = []
    follow_list = Follow_list_create(from_name_id, links_list, [])
    follow_list_all.append(follow_list)
    for i in range(5):
        next_list = []
        if to_name_id not in follow_list_all[i]:
            for id in follow_list_all[i]:
                from_name_id = id
                next_list.extend(Follow_list_create(from_name_id, links_list,[]))
            if next_list == []:
                return 'Not Found'
            else:
                follow_list_all.append(next_list)
            #print(follow_list_all)
        else:
            return search_count
        search_count += 1

        
def test(from_id, to_id, list):
    if list == [[]]:
        return 'Not Fount'
    else:
        search_count = Search(from_id, to_id, list)
        return search_count

if __name__ == '__main__':
    from_name , to_name = Input()
    nicknames_list = Nicknames_list_create()
    from_name_id , to_name_id = Name_ID_change(from_name, to_name, nicknames_list)
    links_list = Links_list_create()
    search_count = Search(from_name_id, to_name_id, links_list)
    print(search_count)
  
    #########テスト##########
    print('test1:'+str(test(0,1,[[0,1]]))+'  excepted_answer:1')
    print('test2:'+str(test(0,1,[[]]))+'  excepted_answer:Not Found')
    print('test3:'+str(test(0,1,[[0,2]]))+'  excepted_answer:Not Found')
    print('test4:'+str(test(0,2,[[0,1],[1,2]]))+'  excepted_answer:2')
    print('test5:'+str(test(0,2,[[0,1],[0,2],[1,2]]))+'  excepted_answer:1')
    print('test6:'+str(test(0,2,[[0,1],[0,3],[1,0],[1,2],[1,4],[2,1]]))+'  expected_answer:2')
    
'''
###############出力結果################
From name : jacob
To name : nancy
2
test1:1  excepted_answer:1
test2:Not Fount  excepted_answer:Not Found
test3:Not Found  excepted_answer:Not Found
test4:2  excepted_answer:2
test5:1  excepted_answer:1
test6:2  expected_answer:2

'''
