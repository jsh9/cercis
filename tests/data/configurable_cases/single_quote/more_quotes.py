def func():
    a = ''
    b = ""
    c = "'"
    d = "\""
    e = '""'
    f = "'"
    g = "hello""world"  # should be a space between 2 single quotes for readability
    h = "hello" "world"
    i = (
        "hello"
        'world'
    )
    j = (
        "hello_hello_hello_hello_hello_hello_hello_hello"
        "world_world_world_world_world_world_world_world_world"
    )



# output

def func():
    a = ''
    b = ''
    c = "'"
    d = '"'
    e = '""'
    f = "'"
    g = 'hello' 'world'  # should be a space between 2 single quotes for readability
    h = 'hello' 'world'
    i = 'hello' 'world'
    j = (
        'hello_hello_hello_hello_hello_hello_hello_hello'
        'world_world_world_world_world_world_world_world_world'
    )
