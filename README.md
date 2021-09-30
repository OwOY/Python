<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png" height="400px"/>
 </div>
 
---- 
  
### 紀錄一些實用小技巧
- Getattr
getattr(object, name)   #object = 物件  #name = 函式名稱
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
