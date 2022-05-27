<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png" height="400px"/>
 </div>
 
---- 
  
### 紀錄一些實用小技巧
- Getattr  
getattr(object, name)  
>> object = 物件  
>> name = 函式名稱  
```
class test:
    def __init__(self):
        pass
    
    def get(self, x):
        print(x)


if __name__ == '__main__':
    T = test()
    c = getattr(T, 'get')
    c(5)
```
>> print : 5
- Setattr
setattr(object, name, value)  #object = 物件  #name = 函式名稱  #value = 值
```
class test:
    def __init__(self):
        pass
    
    def get(self, x):
        print(x)


if __name__ == '__main__':
    T = test()
    setattr(T, 'post', 3)
    print(T.post)
``` 
>> print : 3
### Decorator
1. Ex: 
```
def test(func):
    def wrapper(x):
        func(x)
    return wrapper

@test
def get(x):
    print(x)
get(5)

```
2. Ex:
```
def author_check(*users):
    def get_author_check(func):
        def decorated_view(self):
            if 'IQC' in users:
                return func(self)
            else:
                return ApiResponse.emitErrorOutput(E_CODE_PARAMETERS_BLANK, "權限不足", "")
        return decorated_view 
    return get_author_check
```

### Multiprocess
- start 啟動
``` 
from multiprocessing import Process  
def run5_post(x):  
    run(x)
if __name__ == '__main__':      
    t1 = Process(target=run5_post, args=(1,))  
    t2 = Process(target=run5_post, args=(2,))  
    t1.start()  
    t2.start()  
```
- join 阻塞(確保子進程全跑完才跑主線程)
```
import multiprocess as mp

def run(x)
    print(x)
    sleep(x)

if __name__ == '__main__':
    task_list = []
    i =5
    while i > 0:
        task = mp.Process(target=run, args(i,)
        task.start()
        task_list.append(task)
        i -= 1
    for task in task_list:
        task.join()
    print('done')
```
- queue 運用
```
import multiprocess as mp

class test:
    def __init__(self):
        self.queue = mp.Queue()
    
    def log(self):
        while not self.queue.empty():
            self.queue.get()
            # write log
        
    
    def main(self):
        task_list = []
        i =5
        while i > 0:
            task = mp.Process(target=run, args(i,)
            task.start()
            task_list.append(task)
            self.queue.put(i + '已進行')
            i -= 1
            
        for task in task_list:
            task.join()
        self.log()

if __name__ == '__main__':
    print('schedule start')
    test().main()
    print('done')
    
```
