class idle:
    def execute(self):
        print('it is a from python')
class pycharm:
    def execute(self):
        print('it is from jetbrains')
class lap:
    def laptop(self,ide):
        ide.execute()
ide=idle()
c=lap()
c.laptop(ide)