from pprint import pprint
import json
import requests
import os

def _query(text=None, elements=None, elements_exact=None, properties=None):
    query = {}
    if text is not None:
        query['$text']={'$search':text}
    if elements is not None:
        if elements_exact is not None:
            raise Exception('Only one of elements or elements-exact should be specified')
        else:
            query['aggregated_info.elements']={'$all':[e.capitalize() for e in elements.split(' ')]}
    if elements_exact is not None:
            ee = [e.capitalize() for e in elements_exact.split(' ')]
            query['aggregated_info.elements']={"$size":len(ee), '$all': ee}
    if properties is not None:
            query['aggregated_info.property_types']={'$all':properties.split(' ')}



    #post to REST API
    q = requests.post('https://cf.hsrn.nyu.edu/datasets',json=query) 
    return q.json()
    
def format_print(doc):
    new_doc={}
    new_doc['colabfit-id']=doc['colabfit-id']
    new_doc['name']=doc['name']
    new_doc['authors']=doc['authors']
    new_doc['description']=doc['description']
    new_doc['links']=doc['links']
    new_doc['links']['colabfit']='https://materials.colabfit.org/id/%s'%doc['colabfit-id']
    #new_doc['aggregated_info']=doc['aggregated_info']
    pprint (new_doc,sort_dicts=False)

def _download(doc,format):
    e_id = doc['extended-id']
    #better option needed
    if format in ["xyz", "XYZ"]:
        os.system('wget https://materials.colabfit.org/dataset-xyz/%s.xyz.xz' %eid) 
    if format in ["lmdb", "LMDB"]:
        os.system('wget https://materials.colabfit.org/dataset-lmdb/%s.lmdb' %eid)
    
