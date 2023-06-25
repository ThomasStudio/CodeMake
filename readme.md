# CodeLab

# create code by template

## 1. use python file as code template
## 2. prompt user to input args
## 3. generate code by template and args


# Preview code
## 1. user can preview code
## 2. the code preview will change after args changed

# python template
one py file for one template

## template to create file
1. in template, ```'type':'create'```
2. prompt user to input args
3. replace args in path and code
4. create new file by ```path```, insert text to new file by ```code```


```python
xxx.py
template = {
    'type': 'create',
    'args': ['path', 'className', 'arg2'],
    'files': [
        {
            'path': '{path}/{className}.kt',
            'code': '''class {className}(){
    val name : String = ''
    fun test(n:String) {
        name = n
    }
}
            '''
        }
    ]
}

yyy.py
template = {
    'type':'create',
    'args':['path','className','interfaceName', 'arg2'],
    'files':[
        {
            'path':'{path}/{interfaceName}.kt',
            'code':'''interface {interfaceName}(){
    fun test()
}
            '''
        },
        {
            'path':'{path}/{className}.kt',
            'code':'''class {className}() : {interfaceName}{
    val name : String = ''
    override fun test() {
        name = 'hello world'
    }
}
            '''
        },
    ]
}
```

## template to modify file
1. in template, ```'type':'modify',```
2. prompt user to input args
3. replace args in path, patt and code
4. modify file by ```path```, if ```type == replace```, replace ```patt``` to ```code```
5. modify file by ```path```, if ```type == insertAfter```, insert ```code``` after ```patt```
6. modify file by ```path```, if ```type == insertBefore```, insert ```code``` before ```patt```


```python
xxx.py
template = {
    'type': 'modify',
    'args': ['filePath', 'className', 'newFun'],
    'files': [
        {
            'path': '{filePath}',
            'operator': [
                {
                    'type': 'insertAfter',
                    'patt': '''(class[\s\S]+{className}{[\s\S]+)\n}''',
                    'code': '''
    fun {newFun}() {
        // This is new fun
    }
            '''
                },
                {
                    'type': 'insertBefore',
                    'patt': '''(class[\s\S]+{className}{[\s\S]+)\n}''',
                    'code': '''
    val TAG = "{className}"
            '''
                },
            ]
        }
    ]
}
```