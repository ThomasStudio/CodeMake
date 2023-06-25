template = {
    'type': 'create',
    'args': ['path', 'className'],
    'files': [
        {
            'path': '{path}/{className}.kt',
            'code': '''class {className}() {
            
    val name : String = ''

    fun test(n:String) {
        name = n
    }

    val h = "hello world adfja l;dkfjla dfjklad jfoaijdf asdjfaio jdf;ladjif osd"

}
            '''
        },
        {
            'path': '{path}/{className}IF.kt',
            'code': '''class {className}IF() {
            
    val name : String = ''

    fun testIF(n:String) {
        name = n
    }

    val h = "hello"

}
            '''
        }

    ]
}