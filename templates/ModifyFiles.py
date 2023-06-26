'''
    examples:
    1. insert a new function to class
    2. insert a new val before class
    3. replace code
    4. modify fun
'''
template = {
    'type': 'modify',
    'args': ['filePath', 'className', 'newFun', 'funName'],
    'files': [
        {
            'path': '{filePath}',
            'operator': [
                {
                    'type': 'insertAfter',
                    'patt': '''(class\s*?{className}[\s\S]*?{[\s\S]*?)\n}''',
                    'code': '''
    fun {newFun}() {
        // This is new fun
    }\n'''
                },
                {
                    'type': 'insertBefore',
                    'patt': '''(class\s*?{className}[\s\S]*?{[\s\S]*?)\n}''',
                    'code': '''val TAG = "{className}"\n\n'''
                },
                {
                    'type': 'replace',
                    'patt': '''val name : String''',
                    'code': '''val newName : String'''
                },
                {
                    'type': 'insertAfter',
                    'patt': '''(fun\s*?{funName}[\s\S]*?{[\s\S]*?)\n}''',
                    'code': '''\n    val rs = "hello world"

    return rs
'''
                },
            ]
        }
    ]
}
