#INHERITANCE 
class A:
  def __init__(self):
     self._my="I am proteceted attributes"
  def _mym(self):
    print("I am protected method")

class B(A):
     def __init__(self):
         super().__init__()
     def apm(self):
         print(self._my)
         self._mym()
class C(B):
    def __init__(self):
       super().__init__(self._my)
       self._mym()
obj=C()
obj.apm()







class A:
    pass
class B(A):
    pass
class C(A):
    pass

