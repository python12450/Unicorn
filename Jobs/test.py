import multiprocessing,time
def ptr(**kwargs):
    p = 7 if "i" not in kwargs.keys() else int(kwargs["i"])
    for i in range(p):
        print(i)
        time.sleep(1)
class A(object):
    def __init__(self):
        self.pool=multiprocessing.Pool()
        self.i=20
    def st(self):
        self.pool.apply_async(ptr,kwds={"i":20})
    def join(self):
        self.pool.close()
        self.pool.join()
if __name__=="__main__":
    a=A()
    a.st()
    print a.__dict__
    time.sleep(5)
    a.st()
    a.join()
