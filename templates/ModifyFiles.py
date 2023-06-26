'''
    examples:
    1. insert a new function to class
    2. insert a new val before class
    3. replace code
'''
template = {
    'type': 'modify',
    'args': ['filePath', 'className', 'newFun'],
    'files': [
        {
            'path': '{filePath}',
            'operator': [
                {
                    'type': 'insertAfter',
                    'patt': '''(class[\s\S]+{className}[\s\S]+{[\s\S]+)\n}''',
                    'code': '''
    fun {newFun}() {
        // This is new fun
    }\n'''
                },
                {
                    'type': 'insertBefore',
                    'patt': '''(class[\s\S]+{className}[\s\S]+{[\s\S]+)\n}''',
                    'code': '''val TAG = "{className}"\n\n'''
                },
                {
                    'type': 'replace',
                    'patt': '''val name : String''',
                    'code': '''val newName : String'''
                },
            ]
        }
    ]
}
