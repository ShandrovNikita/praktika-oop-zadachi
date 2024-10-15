class StringVar(object):
  def __init__ (self,string):
    self.string=string
  def get_string(self):
    return self.string
  def set_string(self, value):
    self.string=value
string=StringVar("shish")
string.get_string()
string.set_string("sssss")
string.get_string()
