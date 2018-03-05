#encoding: utf-8
'''
movies = []
movie = {}


movie['title'] = raw_input('1：')
movie['cover'] = raw_input('2')
movie['screenshot'] = raw_input('3')
movie['year'] = raw_input('4')
movie['country'] = raw_input('5')
movie['category'] = raw_input('6')
movie['douban_rating'] = raw_input('7')
movie['duration'] = raw_input('8')
movie['director'] = raw_input('9')
movie["profile"] = raw_input('11')
movie['down_load'] = raw_input('12')


movies.append(movie)

with open('ttest', 'a+') as fw:
    fw.seek(0)
    fw.truncate()
    fw.write(str(movies))

'''
def read_file(filename):
    '''
    用来读取文件内容，返回一个字典
    :param filename: 文件名
    :return: 文件N内容的字典
    :
    '''
    with open(filename,'a+') as fr:
        fr.seek(0)
        content = fr.read()
        print content
        if len(content):#这里判断文件内容是否为空的，如果不为0的话就为是真
           return eval(content)
        return {}


movies = read_file('ttest')  # 获取电影信息