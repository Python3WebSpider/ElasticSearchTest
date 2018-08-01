from elasticsearch import Elasticsearch
import json

dsl = {
    'query': {
        'match': {
            'title': '中国领事馆'
        }
    }
}

es = Elasticsearch()
result = es.search(index='news', doc_type='politics', body=dsl)
print(json.dumps(result, indent=2, ensure_ascii=False))

result = es.search(index='news', doc_type='politics')
print(result)
print(json.dumps(result, indent=2, ensure_ascii=False))
