class News:
    '''
    Movie class to define News Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = '"https://bsmedia.business-standard.com/_media/bs/img/article/2021-08/29/full/1630211155-3037.jpg",'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count