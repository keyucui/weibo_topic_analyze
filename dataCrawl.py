import sys
sys.path.append("..")
import requests
import time
import random
from bs4 import BeautifulSoup
# from tools import Cookie_Process
# from tools.Emoji_Process import filter_emoji
import pandas as pd

from configs import Cookie, headers, headers_topic, headers_sub_topic


# Cookie = {
#         "Cookie":'SINAGLOBAL=611428576138.9926.1529031585340; wb_view_log=1280*7201.5; wvr=6; Ugrow-G0=140ad66ad7317901fc818d7fd7743564; login_sid_t=738f2639b7ec9ed4bda4bda71f80fbe1; cross_origin_proto=SSL; _s_tentry=login.sina.com.cn; Apache=1358246560106.4663.1574947692615; ULV=1574947692624:5:4:2:1358246560106.4663.1574947692615:1574945962066; ALF=1606483698; SSOLoginState=1574947698; SCF=Al_WvdbtXEH8Yao4ordpDA-hA_gh9UtndibTXXHvBmUFzHYP1JlL3i6hA8vy0DzC5TNsedQkLtWUdvNHGhm8UmE.; SUB=_2A25w27sjDeRhGeBK6FQU8CvJwjSIHXVTkKvrrDV8PUNbmtBeLRPNkW9NR93hbGsq6Cqd6bUBQo17s-KlQu2Y7IRL; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5zny7FLIxKUOfwzh7B98AA5JpX5KzhUgL.FoqXe0qfeh-f1Kn2dJLoIfQLxKqL1K.L1-2LxKBLBonL122LxKML1-BLBK2LxKBLBonL12BLxKqL1hnLBoeLxKML1-2L1hBLxK-L1K5LB-eLxKqLB-BL12eLxK-LBo5L1K2LxK-LBo.LBoBt; SUHB=04W-JfJec9qftr; YF-V5-G0=260e732907e3bd813efaef67866e5183; UOR=www.google.com.hk,weibo.com,www.google.com; YF-Page-G0=7f483edf167a381b771295af62b14a27|1574954484|1574954484; wb_view_log_6436505598=1280*7201.5; webim_unReadCount=%7B%22time%22%3A1574954492285%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
#           }

# Cookie = {
#     # "Cookie":"SINAGLOBAL=611428576138.9926.1529031585340; Ugrow-G0=140ad66ad7317901fc818d7fd7743564; login_sid_t=738f2639b7ec9ed4bda4bda71f80fbe1; cross_origin_proto=SSL; _s_tentry=login.sina.com.cn; Apache=1358246560106.4663.1574947692615; ULV=1574947692624:5:4:2:1358246560106.4663.1574947692615:1574945962066; YF-V5-G0=260e732907e3bd813efaef67866e5183; YF-Page-G0=7f483edf167a381b771295af62b14a27|1574954499|1574954484; crossidccode=CODE-gz-1IAwCP-43YF5X-Pks0uH6BiIchdC4a9cfb2; ALF=1606532846; SSOLoginState=1574996846; SCF=Al_WvdbtXEH8Yao4ordpDA-hA_gh9UtndibTXXHvBmUFdV0yXBqO484CDzp5Bj7z_mKcBav8xgTRM0uEdohuprg.; SUB=_2A25w5Ps_DeRhGeBK6FQU8CvJwjSIHXVTkGv3rDV8PUNbmtBeLUXakW9NR93hbJIseJD1haFYH8STgaMVsRkpM1yY; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5zny7FLIxKUOfwzh7B98AA5JpX5KzhUgL.FoqXe0qfeh-f1Kn2dJLoIfQLxKqL1K.L1-2LxKBLBonL122LxKML1-BLBK2LxKBLBonL12BLxKqL1hnLBoeLxKML1-2L1hBLxK-L1K5LB-eLxKqLB-BL12eLxK-LBo5L1K2LxK-LBo.LBoBt; SUHB=0FQ7qQX89hc79G; wvr=6; webim_unReadCount=%7B%22time%22%3A1574996883376%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A56%2C%22msgbox%22%3A0%7D; UOR=www.google.com.hk,weibo.com,www.google.com"
#     "Cookie":"OUTFOX_SEARCH_USER_ID_NCOO=190685000.04271516; _T_WM=98250732886; MLOGIN=1; ALF=1577588846; SCF=Al_WvdbtXEH8Yao4ordpDA-hA_gh9UtndibTXXHvBmUFmyO4zBrfxMlN7lhYijtYCVMofHDmXW5FC2WkqI33Inc.; SUB=_2A25w5PyKDeRhGeBK6FQU8CvJwjSIHXVQJoTCrDV6PUJbktANLU_TkW1NR93hbEKLhuRhdBRHhHRwXA89Ut8v0cKO; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5zny7FLIxKUOfwzh7B98AA5JpX5K-hUgL.FoqXe0qfeh-f1Kn2dJLoIfQLxKqL1K.L1-2LxKBLBonL122LxKML1-BLBK2LxKBLBonL12BLxKqL1hnLBoeLxKML1-2L1hBLxK-L1K5LB-eLxKqLB-BL12eLxK-LBo5L1K2LxK-LBo.LBoBt; SUHB=0oU4rKHNUbbvXs; SSOLoginState=1574997210"
# }
# headers = {
#     'User-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
#     'Host': 'weibo.cn',
#     'Accept' : 'application/json, text/plain, */*',
#     'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
#     'Accept-Encoding' : 'gzip, deflate, br',
#     'Connection' : 'keep-alive',
#     }
# headers_sub_topic = {
#     'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
#     'Host': 's.weibo.com',
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Connection': 'keep-alive',
# }
# headers_topic = {
#     'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
#     'Host': 's.weibo.com',
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
#     'Accept-Encoding': 'gzip, deflate, br',
# }
# df_comment = pd.DataFrame(columns=(
#    'idx', 'wid', 'content', 'uid', 'uname', 'likes', 'created_time', 'keyword'
# ))
# line = 0

df_comment = pd.read_csv('comments\comment_v1.csv')
line = df_comment.shape[0]

url_comment = 'https://weibo.cn/comment/{}?&page={}'
'''爬取某个微博的的评论信息'''

def fetch_comment_data(wbid, keyword, cookies):
    global line

    print('https://weibo.cn/comment/{}'.format(wbid))
    r_comment = requests.get('https://weibo.cn/comment/{}'.format(wbid), headers=headers, cookies=cookies)
    soup_comment = BeautifulSoup(r_comment.text, 'lxml')
    flag = False
    try:
        flag = soup_comment.select('.c')[-1].text.startswith('还没有人针对')
    except Exception as e:
        page_num = 1

    if flag:
        print("--------- 此微博没有人评论！ ---------\n")
        return
    else:
        try:
            page_num = int(soup_comment.select_one(".pa").text.split()[-1].split("/")[-1].split("页")[0])
        except Exception as e:
            page_num = 1

    print(page_num)
    if page_num > 200:
        page_num = 200

    page_id = 1
    flag = -1
    # commentinfos = []
    print("--------- 此微博 {} 的评论页数共有 {} 页 ---------\n".format(wbid, page_num))
    while page_id < page_num:
        if flag == line:
            print('可能已经被阻塞了------')
            break
        elif flag != line:
            flag = line
        print('已经爬取了 {} 条评论......'.format(line))
        time.sleep(random.uniform(1,2))  #设置睡眠时间

        print("++++++ 正在爬取此微博 {} 的第 {} 页评论...... ++++++\n".format(wbid, page_id))
        r_comment = requests.get(url_comment.format(wbid, page_id), headers=headers, cookies=cookies)
        time.sleep(random.uniform(2, 3))  # 设置睡眠时间

        soup_comment = BeautifulSoup(r_comment.text, 'lxml')
        comment_list = soup_comment.select(".c")  # 选取class为c的内容

        for l in comment_list:
            if str(l.get("id")).startswith("C_"):
                # comment_content = filter_emoji(l.select_one(".ctt").text)
                comment_content = l.select_one(".ctt").text
                comment_userid = l.select_one("a").get("href")[3:]
                comment_username = l.select_one("a").text
                comment_like = l.select_one(".cc").text.strip()[2:-1]
                # comment_createtime = time_process(l.select_one(".ct").text.strip()[:-5])
                comment_createtime = l.select_one(".ct").text.strip()[:-5]

                commentinfo = [line, wbid, comment_content, comment_userid,
                               comment_username, comment_like, comment_createtime, keyword]

                df_comment.loc[line] = commentinfo
                line += 1
                if line%100==0:
                    df_comment.to_csv('comments\comment_v1.csv', index=False)
                    time.sleep(20)
        page_id = page_id + 1

    df_comment.to_csv('comments\comment_v1.csv', index=False)
    print("--------- 此微博的全部评论爬取完毕！---------\n\n")


def search_topic_content_id(keyword):
    #按照关键词，从话题来搜索该话题下的微博，能保证评论数量
    topic_content = requests.get('https://s.weibo.com/topic?q={}&pagetype=topic&topic=1&Refer=weibo_topic'.format(keyword), headers=headers_topic)
    if topic_content.status_code!=200:
        print('connected error')
        return -1

    soup_content = BeautifulSoup(topic_content.text, 'lxml')
    names = soup_content.select(".name")
    sub_topic_herfs = []
    sub_topic_name = []

    for name in names:
        # print(name.get("href"))  #每个话题下面的分话题的链接
        sub_topic_herfs.append(name.get("href"))
        # print(name.text.strip('#'))  #每个话题下面的分话题名称
        sub_topic_name.append(name.text.strip('#'))
    # print(len(names))
    # print(names[0])

    return sub_topic_herfs, sub_topic_name

def crawl_sub_topic_content(sub_topic_url, cookies):
    '''
    :param sub_topic_url: 分话题的链接
    :return: ——> list   每个元素为单个微博的链接,个数为20
    '''
    sub_topic_url += '&xsort=hot&suball=1&tw=hotweibo&Refer=weibo_hot'  #将子话题下的微博的排序变为热门微博，单个微博评论数量更多
    sub_contents = requests.get(sub_topic_url, headers=headers_sub_topic, cookies=cookies)
    # print(sub_contents.status_code)
    if sub_contents.status_code!=200:
        print('connect to sub topic error')
        return 0
    # print(sub_contents.text)
    soup_contents = BeautifulSoup(sub_contents.text, 'lxml')

    content_urls = soup_contents.select('.from')  # 为了获取单个微博9位唯一字符串标识, 形如 Ii5QKf6EH
    comment_urls = []

    for c_str in content_urls:
        # print(c_str)
        only_str = c_str.select_one("a").get("href")[2:].split('/')[2][:9]  # 得到单个微博的唯一9位字符串
        comment_urls.append('https://weibo.cn/comment/' + only_str)
    return comment_urls


if __name__ == '__main__':
    # cookie = Cookie_Process.write_cookie() # 获取文件中存储的cookie
    df_comment_urls = pd.DataFrame(columns=(
        'sub_topic_name', 'comment_url'
    ))
    line_url = 0
    time_start = time.time()
    sub_topic_urls, sub_names = search_topic_content_id('高以翔')
    for url, name in zip(sub_topic_urls, sub_names):
        print(line_url)
        sub_comment_urls = crawl_sub_topic_content(url, cookies=Cookie)
        for comment_url in sub_comment_urls:
            df_comment_urls.loc[line_url] = [name, comment_url]
            line_url += 1
        time.sleep(2)
    print(df_comment_urls.shape)
    df_comment_urls.to_csv('comments\comment_urls.csv', index=False)
        # crawl_sub_topic_content('https://s.weibo.com/weibo?q=%23%E9%AB%98%E4%BB%A5%E7%BF%94%23', cookies=Cookie)
    # search_all_comment(input("请输入要搜索的微博评论的关键字："))
    # contents_strs = ['Ii7jlyQvu', 'Ii6ZY7972', 'Iihqa5WM7', 'IigXmr5Wv', 'IipNXjNZe', 'IipRscSR6'] #'Ii8Y09uyw', 'Ii7KAig2u','Ii9fuDZtm','IicxftnLC','IiltQpmgz'] #'Ii6s9xVZP', 'Ii7MN70E2']
    # for content_str in contents_strs:
    #     fetch_comment_data(content_str, '高以翔', Cookie)
    #     time.sleep(20)

    time_end = time.time()

    print('本次操作数据全部爬取成功，爬取用时秒数:', (time_end - time_start))






