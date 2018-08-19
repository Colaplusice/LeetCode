def url_route():
    ''' input formate
6 4
/articles/2003/ special_case_2003
/articles/<int>/ year_archive
/articles/<int>/<int>/ month_archive
/articles/<int>/<int>/<str>/ article_detail
/articles/<str>/ article_HELLO
/static/<path> static_serve
/articles/2004/
/articles/1985/09/aloSADha/
/articles/hello/
/static/js/jquery.js/02

'''
    import sys
    a=sys.stdin.readline().strip().split(' ')
    rule_num=int(a[0])
    url_num=int(a[1])
    rule_list=[]
    url_list=[]
    success_url=[]
    parameter_list=[]
    for i in range(rule_num):
        a=sys.stdin.readline().strip().split(' ')
        rule_list.append((a[0],a[1]))

    for i in range(url_num):
        a=sys.stdin.readline().strip()
        url_list.append(a)
    for each_url in url_list:
        is_match=True
        for each_rout in rule_list:
            url_li=each_url.split('/')
            rout_li=each_rout[0].split('/')
            for index,each in enumerate(rout_li):
                is_match=True
                if each.startswith('<'):
                    if each=='<int>':
                        if url_li[index].isnumeric():
                            parameter_list.append(url_li[index])
                            continue
                        else:
                            parameter_list=[]
                            is_match=False
                            break
                    elif each=='<str>':
                        if not '/' in  url_li[index] and url_li[index]:
                            parameter_list.append(url_li[index])
                            continue
                        else:
                            parameter_list=[]
                            is_match=False
                            break
                    elif each=='<path>':
                        if url_li[index]:
                            parameter_list.append('/'.join(url_li[index:]))
                            continue
                        else:
                            parameter_list=[]
                            is_match=False
                            break
                else:
                    if each==url_li[index]:
                        continue

                    else:
                        parameter_list=[]
                        is_match=False
                        break
            if is_match:
                success_url.append((parameter_list,each_rout[1]))
                break
        if not is_match:
            success_url.append(404)
    # print(success_url)

    for each in success_url:
        if each == 404:
            print(each)
            continue
        aslist=[]
        for each_p in each[0]:
            if each_p.isnumeric():
                aslist.append(str(int(each_p)))
            else:
                aslist.append(each_p)
        print('{} {}'.format(each[1],' '.join(aslist)))




url_route()







