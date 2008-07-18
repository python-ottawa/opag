def make_bctrail(bclist):
    """This tag creates a breadcrumb trail based on the input. It expects an
    array with an odd number of elements. For each set of two elements it
    creates a link to the name, with the url provided as the link. The last
    element in the array is assumed to be just a name, for the current page. 
    ie. ['Home', '/index.html', 'Current page']"""
    bclist.reverse()
    text = ''
    while len(bclist) > 1:
        name = bclist.pop()
        link = bclist.pop()
        text += '<a href="%s">%s</a> /' % (link, name)

    text += ' %s' % bclist.pop()
    return text
