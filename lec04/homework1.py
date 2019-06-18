'''
Input()
from_name に探し始めるニックネームを入力
to_name に探したいニックネームを入力

Nicknames_list_create()
nicknames.txt を [ID ,nickname] のリストにする

Name_ID_chanege()
from_name を from_name_id に、to_name を to_name_id に変換(nicknames.txt)

Links_list_creat()
links.txt を [id(from), id(to)] のリスト links_list にする

Search()
from_name_id から 幅優先探索で to_name_id を探し、探索経路 search_path_id を返す

ID_Name_change()
ID のリストとなっている search_path_id を search_path_nicknames に変換
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
                nicknames_list.append([nicknames_line[0],nicknames_line[2:]])
            else:
                nicknames_list.append([nicknames_line[0:2],nicknames_line[3:]])
    return nicknames_list

def Name_ID_change(from_name, to_name, nicknames_list):
    to_name_id = 0
    from_name_id = 0
    for i in range(len(nicknames_list)):
        if from_name == nicknames_list[i][1]:
            from_name_id = nicknames_list[i][0]
        elif to_name == nicknames_list[i][1]:
            to_name_id = nicknames_list[i][0]
    return from_name_id, to_name_id

def Links_list_create():
    links_list = []
    with open('links.txt') as links:
        links = links.readlines()
        for link in links:
            link = link.replace("\t"," ")
            link = link.replace("\n","")
            if len(link) < 4:
                links_list.append([link[0],link[2]])
            elif link[1] == ' ' and link[3] != ' ':
                links_list.append([link[0],link[2:4]])
            elif link[1] != ' ' and len(link) < 5:
                links_list.append([link[0:2],link[3]])
            else:
                links_list.append([link[0:2],link[3:5]])
    return links_list

def Follow_list_create(from_name_id, links_list, follow_list):
    for i in range(len(links_list)):
        if int(links_list[i][0]) > int(from_name_id):
            break
        elif from_name_id == int(links_list[i][0]):
            follow_list.append(links_list[i][1])
    return follow_list

def Search(from_name_id,to_name_id,links_list):
    search_count = 1
    follow_list_all = []
    next_list = []
    follow_list = Follow_list_create(from_name_id, links_list, [])
    follow_list_all.append(follow_list)
    for i in range(3):
        for j in range(len(follow_list_all[i])):
            if to_name_id not in follow_list_all[i]:
                for k in range(len(follow_list_all[i])):
                    from_name_id = follow_list_all[i][j]
                    next_list.extend(Follow_list_create(from_name_id, links_list,[]))
                    follow_list_all.append(next_list)
            else:
                return search_count
        search_count += 1

def test(from_id, to_id, list):
    serach_count = Search(from_id, to_id, list)
    return search_count

if __name__ == '__main__':
    '''
    from_name , to_name = Input()
    nicknames_list = Nicknames_list_create()
    from_name_id , to_name_id = Name_ID_change(from_name, to_name, nicknames_list)
    links_list = Links_list_create()
    search_count = Search(from_name_id, to_name_id, links_list)
    print(search_count)
    '''
    #########テスト##########
    print('test1:'+str(test(0,1,[['0','1']]))+'  excepted_answer:1')
    
