# -*- coding:utf-8 -*-  
# python3 python/index.py 8080
import web  
          
urls = (  
    '/(.*)', 'hello'  
)  
app = web.application(urls, globals())  
  
class hello:          
    def GET(self, name):  
        return 'Hello World'  
  
if __name__ == "__main__":  
    app.run()