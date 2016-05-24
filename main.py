#!/usr/bin/python
#!/usr/bin/python
#Given a string this program returns the longest substring in alphabetical order#

import webapp2
import time

from google.appengine.api import memcache
from google.appengine.api import users
from google.appengine.api import mail

def alpha(s):
      cachealpha=memcache.get(str(s))
      if cachealpha != None:
            return "Longest substring in alphabetical order is:" +" " +cachealpha
      count=0
      count_final=0
      alpha_store=" "
      alphafinal_store=" "
      init=0
      for char in s:
            if init<=char :
                count+=1
                alpha_store=alpha_store + char 
            elif (count>count_final):
                 count_final=count
                 alphafinal_store=alpha_store
                 alpha_store=char
                 count=1
            else:
                count=1
                alpha_store=char
            init=char
      print "Submitted string :" + str(s)
      if count>count_final : 
           memcache.set(str(s),alpha_store)        
           return "Longest substring in alphabetical order is:" +" " +alpha_store
      else :
           memcache.set(str(s),alphafinal_store)  
           return "Longest substring in alphabetical order is:" +" " +alphafinal_store 
  
#This class will handles any incoming request from the browser
class MainHandler(webapp2.RequestHandler):

	#Handler for the GET requests
  def get(self):
    if 'reset' in self.request.GET.keys():
       memcache.flush_all()
    s = ""

    self.response.write("<h1>Fun with string!!</h1>")
    user = users.get_current_user()
    if user:
          self.response.write("Welcome " + user.nickname() + '<a href="' + users.create_logout_url('/') + '">Logout</a><br>\n')
    else:
          self.response.write("Please <a href=\"" + users.create_login_url('/') + "\">Login or Register</a><br>")
          return
    if 's' in self.request.GET.keys():
      s=str(self.request.GET['s'])
    self.response.write('<html><body><h1>Find the longest string in alphabetical(character) order</h1>')
    #self.response.write('<background color:"blue">')
    self.response.write( "Submitted string: " + str(s) + "<br>" )
    self.response.write(alpha(s))
    self.response.write('<form method="GET">')
    self.response.write('<input name="s" type="text">')
    self.response.write('<input type="submit">')
    self.response.write('</form><br>')
    
    self.response.write("</body></html>")
    if user is None:
          login_url = users.create_login_url(self.request.path)
          self.redirect(login_url)
          return
    to_addr = self.request.get("friend_email")
    if not mail.is_email_valid(to_addr):
            # Return an error message...
            pass

    message = mail.EmailMessage(sender="appspot.com Support <valid-from-address@gmail.com>",
                            subject="Welcome!!")
    message.sender = user.email()
    message.to = "Valid User <valid.user@gmail.com>"
    message.body = """
    
Thanks for using 'imagecin.appspot.com'.Recommend it to your friends..:)...
        """ # generate_invite_link(to_addr)
    
    message.send()



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

