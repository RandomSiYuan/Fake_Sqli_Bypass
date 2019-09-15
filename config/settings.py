class settings:
    url = "http://106.53.98.8/Less-1/?id=-1%27"
    str = "Your Login name:2"

    #代理池配置

    porxy_host = "127.0.0.1" #
    porxy_port = "8888"
    porxy_open = False

    #存储方式
    save_open = True
    save_method = "txt" #mysql | txt
    save_url = "reustl/"
    #Mysql 配置
    ysql_host ="127.0.0.1"
    mysql_port = "3306"
    mysql_db   = "fuzz_sql"

    #线程
    thread_num = 50

    #tamper生成
    tamper_dir  = 'tamper/'
    tamper_open = True

    #info
    debug = 0


    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.3 6 SE 2.X MetaSr 1.0"}