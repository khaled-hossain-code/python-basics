class human:
    x = 0
    
    def run(self):
        self.x = self.x + 1
        print "So far", self.x

afzal = human()
afzal.run()
afzal.run()