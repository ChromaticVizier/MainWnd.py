"""
获取bilibili的热门的数据并且保存起来
主题 标题 播放量 点赞 评论 投币
- get请求
"""
'''

'''
import urllib.request
import json
import urllib.parse
import pandas as pd

# 这里注意 bilibili 通过requests模块进行数据爬取无法每次实现所见及所得，
# 有些数据是通过非浏览器地址栏中的url请求到的数据，而是其他请求请求到的数据，那么这些通过其他请求请求到的数据就是动态加载的数据
def create_request(page: int):
    """
    请求对象定制（使用UA），解决反爬的第一种手段
    :param page: 页码
    :return: 请求对象定制的结果request
    """
    # 请求地址
    base_url = 'https://api.bilibili.com/x/web-interface/popular?web_location=333.934&'
    data = {
        'pn': page,
        'ps': 20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data +'&w_rid=f079959238019ab7f4bdfd50289f132b&wts=1709946519'
    # 请求头
    headers = {
        'User-Agent': 'ozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Hot Lingo 2.0)'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    """
    获取page页数据
    :param request: 请求对象定制的结果
    :return: 第page页数据
    """
    # (1).模拟浏览器向服务器发送请求
    response = urllib.request.urlopen(request)
    # (2).获取响应的数据
    content = response.read().decode('UTF-8')
    return content


def deal_content(content, content_changed):
    """
    处理page页数据,假设本次只想储存序号和电影名字
    :param content: 从bilibili上获取的某一页的原始数据
    :param content_changed: 根据需要修改后只含需要的数据
    :return: 返回处理原始数据后的只含想要的数据
    """
    content = json.loads(content)  # json字符串转成python中的json对象
    for index in content['data']['list']:
        content_changed.append({'tname': index['tname'], 'title': index['title'], 'view': index['stat']['view'], 'like': index['stat']['like'], 'danmaku': index['stat']['danmaku'], 'share': index['stat']['share'], 'coin':index['stat']['share']})
    return content_changed


def down_load(content_changed):
    """
    数据下载到本地
    :param content_changed: 处理过后的数据
    :return: 无返回值
    """
    # 将数据转为json类型
    content_changed = json.dumps(content_changed, ensure_ascii=False)
    # ensure_ascii=False表示不用转换成ASCII码  如果为了节省空间，请不要写ensure_ascii=False
    '''
        open方法默认情况下使用的是gbk的编码
        - 如果我们要想保存汉字那么需要在open方法中指定编码格式为utf-8
    '''
    # 法1
    # fp = open('douban.json', 'w', encoding='UTF-8')
    # fp.write(content)
    # fp.close()  # 别忘了关闭文件

    # 法2
    with open('bilibili.json', '', encoding='utf-8') as fp:
        fp.write(content_changed)


# 程序的入口
if __name__ == '__main__':
    # 1.输入起始、结束页码
    start_page = int(input("请输入起始的页码："))
    end_page = int(input("请输入结束的页码："))

    # 2.从bilibili上获取对应数据
    content_changed = []
    for page in range(start_page, end_page + 1):
        # 2.1 第page页的请求对象定制
        request = create_request(page)
        # 2.2 获取page页数据
        content = get_content(request)
        # 假设本次只想储存主题 标题 播放量 点赞 评论 投币
        content_changed = deal_content(content, content_changed)

    # 3.数据下载到本地
    down_load(content_changed)
    # 读取JSON文件
    data = pd.read_json('bilibili.json')

    # 将数据保存为CSV文件
    data.to_csv('bilibili.csv', index=False,encoding='utf-8-sig')

    print("转换完成，已保存为bilibili.csv文件")