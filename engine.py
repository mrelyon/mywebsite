#!/usr/bin/python
import web
import urllib2
render = web.template.render('templates/')
urls = (
    '/', 'index',
    '/(.*)', 'nopage'
)


#app title
apptitle = 'Elyon Labs'

#app description
appdescription = [apptitle,'A boy\'s dream came true']

#login info
loginfo = ''


#app calling
app = web.application(urls, globals())


#get header   
def get_header(name,checkblog):
        global session
        checkuser = session.udata
        return render.masthead(name,checkuser,appdescription,checkblog)

#get footer   
def get_footer(name):
        global session
        checkuser = session.udata
        return render.mastfooter(name,checkuser,appdescription)
    



class index:
    def GET(self):
        name = 'Home - Ayomide Ikechukwu Daniels'
        return render.index(name,appdescription)


#not found        
def notfound():
	       return web.notfound(render.notfound(render))
          

#internal error
def internalerror():
	       return web.internalerror(render.internalerror(render))
               
app.notfound = notfound
app.internalerror = internalerror

class nopage:
    def GET(self,name):
        return render.notfound(name)
    
if __name__ == "__main__":
    app.run()
