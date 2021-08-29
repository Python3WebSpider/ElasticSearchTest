from elasticsearch import Elasticsearch

es = Elasticsearch()

datas = [
    {
        'title': '高考结局大不同',
        'url': 'https://k.sina.com.cn/article_7571064628_1c3454734001011lz9.html',
    },
    {
        'title': '进入职业大洗牌时代，“吃香”职业还吃香吗？',
        'url': 'https://new.qq.com/omn/20210828/20210828A025LK00.html',
    },
    {
        'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
        'url': 'http://view.inews.qq.com/a/EDU2021041600732200',
    },
    {
        'title': '他，活出了我们理想的样子',
        'url': 'https://new.qq.com/omn/20210821/20210821A020ID00.html',
    }
]

for data in datas:
    es.index(index='news', body=data)
