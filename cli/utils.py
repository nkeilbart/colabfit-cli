from pymongo import MongoClient
from pprint import pprint
import json
import requests
def _query(text=None, elements=None, elements_exact=None, properties=None):
    #ds_client = MongoClient("mongodb://CLI:CLI@localhost:27017")['cf-update-2023-11-30']['datasets']
    query = {}
    if text is not None:
        query['$text']={'$search':text}
    if elements is not None:
        if elements_exact is not None:
            raise Exception('Only one of elements or elements-exact should be specified')
        else:
            query['aggregated_info.elements']={'$all':elements.upper().split(' ')}
    if elements_exact is not None:
            ee = elements_exact.upper().split(' ')
            query['aggregated_info.elements']={"$size":len(ee), '$all': ee}
    if properties is not None:
            query['aggregated_info.property_types']={'$all':properties.split(' ')}



    #post to REST API
    q = requests.post('https://cf.hsrn.nyu.edu/datasets',json=query) 
    #q = ds_client.find(query,{'name':1,'colabfit-id':1,'authors':1,'links':1,'aggregated_info.elements':1,'aggregated_info.property_types':1,'aggregated_info.nconfigurations':1, 'description':1})
    return q
    
def format_print(doc):
    new_doc={}
    doc.pop('_id')
    new_doc['colabfit-id']=doc['colabfit-id']
    new_doc['name']=doc['name']
    new_doc['authors']=doc['authors']
    new_doc['description']=doc['description']
    new_doc['links']=doc['links']
    new_doc['links'].append('https://materials.colabfit.org/id/%s'%doc['colabfit-id'])
    new_doc['aggregated_info']=doc['aggregated_info']
    pprint (new_doc,sort_dicts=False)
