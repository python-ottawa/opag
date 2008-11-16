from django.core.paginator import Paginator, InvalidPage
from django.http import Http404

class OpagPaginator(Paginator):
    def __init__(self, request=None, query_set=None, current_page=1, page_size=20, padding=3 ):
        from re import sub
        Paginator.__init__(self, query_set, page_size)
        if request is None or query_set is None:
            raise Http404
        self.path = sub( r'page/\d+/?$', '', request.path )
        self.path = sub( r'/$', '', self.path )
        self.query_str = '?' + request.GET.urlencode()
        if self.query_str == '?':
            self.query_str = ''
        self.current_page = int( current_page )
        self.page_size = page_size
        start = self.current_page - padding
        end = self.current_page + padding
        if start < 0:
            end += 0 - start
            start = 0
            if end >= self.num_pages:
                end = self.num_pages-1
        if end >= self.num_pages:
            start -= end - self.num_pages + 1
            end = self.num_pages-1
            if start < 0:
                start = 0
        self.first = start+1
        self.last = end+1
        self.page_numbers = [ { 'page': (p+1), 'url': self.path + '/page/' + str(p+1) + '/' + self.query_str } \
                                for p in range( start, end+1 ) ]
        self.first_url = self.path + '/page/1/' + self.query_str
        self.prev_enabled = int( current_page ) > int( self.first )
        self.prev_url = self.path + '/page/' + str( self.current_page - 1 ) + '/' + self.query_str
        self.next_enabled = int( current_page ) < int( self.last )
        self.next_url = self.path + '/page/' + str( self.current_page + 1 ) + '/' + self.query_str
        self.last_url = self.path + '/page/' + str( self.num_pages ) + '/' + self.query_str
        self.is_paginated = self.num_pages > 1

    def get_page(self, page_num=None):
        try:
            if page_num is None:
                return Paginator.page(self, self.current_page)
            else:
                return Paginator.page(self, page_num)
        except InvalidPage:
            raise Http404, "page_num is %s" % page_num
