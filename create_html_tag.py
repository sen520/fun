def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join('%s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s %s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s/>' % (name, attr_str)


print(tag('a', 'text', href='http://baidu.com'))
a = {'name': 'br'}
print(tag(**a))