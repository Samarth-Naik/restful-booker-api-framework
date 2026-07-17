import requests

class ApiClient:
    
    @staticmethod
    def get(url,headers=None):
        return requests.get(url,headers=headers)
    
    @staticmethod
    def post(url,payload,headers=None):
        return requests.post(url,json=payload,headers=headers)
    
    @staticmethod
    def put(url,payload,headers=None):
        return requests.put(url,json=payload,headers=headers)
    
    @staticmethod
    def patch(url,payload,headers=None):
        return requests.patch(url,json=payload,headers=headers)
    
    @staticmethod
    def delete(url, headers=None):
        return requests.delete(url, headers=headers)