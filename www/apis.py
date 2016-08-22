import json, logging, inspect, functools 

class APIError(Exception):
    '''
    the base APIError which contains error(required),data(optional) and message(optional)
    '''

    def __init__(self, error, data='', message=''):
        super(APIError,self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class APIValueError(APIError):
    '''
    Indicate the input value has error or invalid. THe data specifies the erro field of input form
    '''
    def __init__(self, field, message=''):
        super(APIValueError,self).__init__('value:invalid',field, message)

class APIResourceNotFoundError(APIError):
    '''
    Indicate thr resource was not found. The data specifies thr resource name
    '''
    def __init__(self,field,message=''):
        super(APIResourceNotFoundError,self).__init__('value:not found',field,message)

class APIPermissionError(APIError):
    '''
    Indicate the api has no permission
    '''
    def __init__(self,message=''):
        super(APIPermissionError,self).__init__('permission:forbidden','permission',message)