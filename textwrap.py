import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    return wrapper.fill(text=string)

    
string, max_width = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 4
result = wrap(string, max_width)
print(result)