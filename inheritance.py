class human:
    x = 0
    name = ""

    def __init__(self,name):
      self.name = name
      print "Inside constructor"

    def run(self):
        self.x = self.x + 1
        print self.name, "So far", self.x

    def __del__(self):
      print "inside destructor"

#afzal = human("Afzal")
#afzal.run()

class doctor(human):
  degree = "doctorate"

  def __init__(self,name):
    human(name)

  def enjoy(self):
    self.run()

sagir = doctor("sagir")

sagir.enjoy()