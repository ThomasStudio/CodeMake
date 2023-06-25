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
    }'''
                },
                {
                    'type': 'insertBefore',
                    'patt': '''(class[\s\S]+{className}{[\s\S]+)\n}''',
                    'code': '''
    val TAG = "{className}"'''
                },
            ]
        }
    ]
}
