from bs4 import BeautifulSoup

demo='http://python123.io/ws/demo.html'

soup=BeautifulSoup(demo,'html.parser')

# head 节点
soup.head 

# head 儿子节点
soup.head.contents

soup.body.contents 

# len 获得 儿子节点的数量 
len(soup.body.contents)

soup.body.contents[1]

# 遍历儿子节点
for child in soup.body.children:
    print(child)


# 上行遍历
soup.title.parent

soup.html.parent

soup.parent # empty

soup=BeautifulSoup(demo,'html.parsar')

for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

# 平行遍历
# 遍历后续节点
for sibling in soup.a.next_siblings:
    print(sibling)
# 遍历前续节点
for sibling in soup.a.previous_siblings:
    print(sibling)



