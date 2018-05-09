from pyquery import PyQuery as pq
doc = pq('http://localhost:3000')
# doc1 = pq(url='https://www.baidu.com')
# print(doc)
print(doc('#voteSuccess'))