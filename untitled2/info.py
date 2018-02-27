# -*- coding: UTF-8 -*-
import time
USER_FILENAME = 'users'
#常量，存的是存储用户信息的文件名
LOG_FILENAME = 'shop.log'
#常量，存的是日志文件名
PRODUCT_FILENAME = 'products'
#常量，存的是商品信息的文件名
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

def write_file(filename,content):
    '''
    用来读取文件内容，返回一个字典
    :param filename: 文件名
    :return: 文件N内容的字典
    '''
    with open(filename,'a+') as fw:
        fw.seek(0)
        fw.truncate()
        fw.write(str(content))

def write_log(username,operation):
    '''
    写日志函数
    :param username:用户名
    :param operation:用户的操作信息
    :return:
    '''
    w_time = time.strftime('%Y-%m-%d %H%M%S')
    with open(LOG_FILENAME,'a+') as fw:
        log_content = '%s %s %s \n'%(w_time,username,operation)
        fw.write(log_content)


def login():
    '''
    登录函数，如果登录成功返回登录用户名，登录失败返回None
    :return:
    '''
    print('欢迎登录白羊座商品系统'.center(50,'*'))
    username = raw_input('请输入用户名：')
    password = raw_input('请输入密码：')
    #strip用于移除头尾指定字符
    user_dic = read_file(USER_FILENAME)#获取到所有的用户信息
    if username=='' or password =='':
        print('账号或者密码不能为空！')
    else:
        if username in user_dic:
            if user_dic[username]['password'] == password:  # 登录成功
                write_log(username, '登录成功！')
                return username
            else:
                write_log(username, '密码不正确！')
                print('密码不对！')

        else:
            print('用户不存在')


def is_price(s):
    '''
    这个函数的作用是用来判断价格是否合法，
    :param s:
    :return:
    '''

    s = str(s)
    if s.count('.')==1:#判断小数点个数
        sl = s.split('.')#按照小数点进行分割
        left = sl[0]#小数点前面的
        right = sl[1]#小数点后面的
        if left.startswith('-') and left.count('-')==1 and right.isdigit():
            lleft = left.split('-')[1]#按照-分割，然后取负号后面的数字
            if lleft.isdigit():
                return False
        elif left.isdigit() and right.isdigit():
            #判断是否为正小数
            return True
    elif s.isdigit():
        s = int(s)
        if s!=0:
            return True
    return False


def add_product():
    products_dic = read_file(PRODUCT_FILENAME)#获取商品信息
    p_name = raw_input('请输入商品名称：')
    p_id = raw_input('请输入商品id：')
    p_price = raw_input('请输入商品价格：')
    if p_name != '' and p_id != '' and p_price != '':
        # if和elif都是条件为真的时候才走的
        if p_name in products_dic:
            print('商品已存在！')
        elif not is_price(p_price):
            # not True是flase，指定走不到这里
            # not Flase，就是true，就走这了
            print('商品价格不合法！')
        else:
            products_dic[p_name] = {'id': p_id, 'price': p_price}
            # products是存最新所有商品，给这个字典添加商品
            write_file(PRODUCT_FILENAME,products_dic)
            #调用写文件的函数，把商品信息写入到文件中
            write_log(username,'添加了商品信息 商品名【%s】 商品价格【%s】 商品id【%s】'
                      %(p_name,p_price,p_id))
            print('商品添加成功')
    else:
        print('商品名称、商品id、商品价格都不能为空')

def del_product():
    '''
    删除商品
    :return:
    '''
    products_dic = read_file(PRODUCT_FILENAME)  # 获取商品信息
    print('可以删除的有',products_dic.keys())
    p_name = raw_input('请输入你要删除的商品名称：')
    if p_name !='':
        if p_name in products_dic:
            products_dic.pop(p_name)
            write_file(PRODUCT_FILENAME,products_dic)
            print('删除成功')
            write_log(username,'删除了【%s】'%p_name)
        else:
            print('商品名称不存在！')
    else:
        print('商品名称不能为空')
def query_product():
    '''
    查询商品
    :return:
    '''
    products_dic = read_file(PRODUCT_FILENAME)
    p_name = raw_input('请输入你要查询的商品名称：')
    if p_name in products_dic:
        p_id = products_dic[p_name]['id']
        p_price = products_dic[p_name]['price']
        msg = '商品名称是:【%s】,商品id是【%s】，商品价格是【%s】' % (p_name, p_id, p_price)
        print(msg)
        write_log(username,msg)
    else:
        print('你输入的商品不存在！')
def n_exit():
    exit('程序退出')

def add_user():
    users_dic = read_file(USER_FILENAME)#获取用户信息
    username = raw_input('用户名：')
    passwd = raw_input('用户密码：')
    blance = raw_input('用户的钱：')
    if username != '' and passwd != '' and blance != '':
        # if和elif都是条件为真的时候才走的
        if username in users_dic:
            print('用户名已存在！')
        elif not is_price(blance):
            # not True是flase，指定走不到这里
            # not Flase，就是true，就走这了
            print('钱不合法！')
        else:
            users_dic[username] = {'password': passwd, 'price': blance}
            # products是存最新所有商品，给这个字典添加商品
            write_file(USER_FILENAME,users_dic)
            #调用写文件的函数，把商品信息写入到文件中
            write_log(username,'添加了用户信息 用户名【%s】 钱是【%s】'
                      %(username,blance))
            print('用户添加成功')

def del_user():
    '''
     删除用户
     :return:
     '''
    users_dic = read_file(USER_FILENAME)  # 获取商品信息
    print('可以删除的有', users_dic.keys())
    username = raw_input('请输入你要删除的用户名：')
    if username != '':
        if username in users_dic:
            if username!='admin':
                users_dic.pop(username)
                write_file(USER_FILENAME, users_dic)
                print('删除成功')
                write_log(username, '删除了【%s】' % username)
            else:
                print('admin用户不能被删除！')
        else:
            print('用户不存在！')
    else:
        print('用户名不能为空')

def modify_user():
    users_dic = read_file(USER_FILENAME)  # 获取商品信息
    username = raw_input('请输入要修改的用户名:')
    blance = raw_input('请输入你要修改的金额：')
    passwd = raw_input('请输入你要修改的密码：')
    if username!='' and (blance!='' or passwd!=''):
        if username in users_dic:
            if blance!='':
                users_dic[username]['moeny']=blance
            elif passwd!='':
                users_dic[username]['password'] = passwd
            else:
                users_dic[username]['money'] = blance
                users_dic[username]['password'] = passwd
            write_file(USER_FILENAME,users_dic)#写用户信息
            write_log(username,'修改了%s用户'%username)
        else:
            print('用户不存在')
    else:
        print('用户名不能为空，金额和密码至少一个不能为空！')

def modify_user():
    users_dic = read_file(USER_FILENAME)  # 获取商品信息
    username = raw_input('请输入要修改的用户名:')
    blance = raw_input('请输入你要修改的金额：')
    passwd = raw_input('请输入你要修改的密码：')
    if username!='' and (blance!='' or passwd!=''):
        if username in users_dic:
            if blance!='':
                users_dic[username]['moeny']=blance
            elif passwd!='':
                users_dic[username]['password'] = passwd
            else:
                users_dic[username]['money'] = blance
                users_dic[username]['password'] = passwd
            write_file(USER_FILENAME,users_dic)#写用户信息
            write_log(username,'修改了%s用户'%username)
        else:
            print('用户不存在')
    else:
        print('用户名不能为空，金额和密码至少一个不能为空！')

def manager_user():
    choice = raw_input('1、添加用户 2、删除 3、修改用户 0退出：')
    if choice in manager_user_menu:
        manager_user_menu[choice]()
    else:
        print('请请输入0-3的选项！')

manager_user_menu  = {
    "1":add_user,
    "2":del_user,
    "3":modify_user,
    "0":n_exit
}#这个用户管理函数做的映射
product_manger = {
    "1":add_product,
    "2":del_product,
    "3":query_product,
    "0":n_exit,
}#这个是产品管理
admin_menu = {"4":manager_user}
admin_menu.update(product_manger)
#admin的菜单，为了普通用户操作用户管理


def welcome():
    global username
    username = login()#调用登录函数，获取登录状态

    if username:
        if username=='admin':
            choice = raw_input('1 添加商品、2删除商品、3查询商品、4用户管理、0退出')
            if choice in admin_menu:
                admin_menu[choice]()
            else:
                print('请请输入0-4的选项！')
        else:
            choice = raw_input('1 添加商品、2删除商品、3查询商品、0退出:')
            if choice in product_manger:
                product_manger[choice]()
            else:
                print('请请输入0-3的选项！')

welcome()#运行程序程序