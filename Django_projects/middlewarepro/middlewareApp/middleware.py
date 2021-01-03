from django.shortcuts import HttpResponse

#Activating Function Based Middleware

'''def my_middleware(get_response):
    #One-time configuration and initialization
    print("one-time INITIALIZATION")

    def my_function(request):
        print("this is before view")
        #code to be executed for each request before the view (and later middleware) are called.
        response=get_response(request)
        print("this is after view")
        #code to be executed for each request/response after the view is called
        return response
    return my_function'''

#Class Based Middleware

'''class my_middleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time INITIALIZATION")

    def __call__(self,request):
        print("this is before view")
        response=self.get_response(request)
        print("this is after view")
        return response'''

#Multiple Class Based Middleware
'''class firstmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time INITIALIZATION")

    def __call__(self,request):
        print("this is before FIRST MIDDLEWARE")
        response=self.get_response(request)
        print("this is after FIRST MIDDLEWARE")
        return response

class secoundmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("two time INITIALIZATION")

    def __call__(self,request):
        print("this is before SECOUND MIDDLEWARE")
        response=self.get_response(request)
        print("this is after SECOUND MIDDLEWARE")
        return response'''

#Hooks middleware
'''class myprocessmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        #One-time configuration and initialization

    def __call__(self,request):
        print("this is request")
        #code to be executed for each request before the view (and later middleware) are called.
        response=self.get_response(request)
        print("this is reponse")
        #code to be executed for each request/response after the view is called
        return response

    def process_view(request,*args,**kwargs):
        print("this is process view")
        return None'''

    
#Exception middleware
#Example-1
'''class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        #One-time configuration and initialization

    def __call__(self,request):
        #code to be executed for each request before the view (and later middleware) are called.
        response=self.get_response(request)
        #code to be executed for each request/response after the view is called
        return response
    
    def process_exception(self,request,exception):
        print("Exception occurd")
        msg=exception
        class_name=exception.__class__.__name__
        print(class_name)
        print("this is message ",msg)
        return HttpResponse(msg)'''

#Example-2
'''class StackOverflowMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
        #One-time configuration and initialization
        print("this will initialize first")
    
    def __call__(self,request):
        #code to be executed for each request before the view (and later middleware) are called.
        response=self.get_response(request)
        print("this will initialize at last")
        #code to be executed for each request/response after the view is called
        return response

    def process_exception(self, request, exception):
        print(exception.__class__.__name__)   #It will show ZeroDivisionError
        print (exception)                      #It will show division by zero
        return HttpResponse(exception)          #It will show division by zero on homepage'''


#Template Middelware

class MyTemplatesMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_template_response(self,request,response):
        print("process templates response from middleware")
        response.context_data['name']='Sohail'
        return response