scrapy爬虫原理过程:
=====
    1、爬虫引擎获得初始请求开始抓取。 
    2、爬虫引擎开始请求调度程序，并准备对下一次的请求进行抓取。 
    3、爬虫调度器返回下一个请求给爬虫引擎。 
    4、引擎请求发送到下载器，通过下载中间件下载网络数据。 
    5、一旦下载器完成页面下载，将下载结果返回给爬虫引擎。 
    6、引擎将下载器的响应通过中间件返回给爬虫进行处理。 
    7、爬虫处理响应，并通过中间件返回处理后的items，以及新的请求给引擎。 
    8、引擎发送处理后的items到项目管道，然后把处理结果返回给调度器，调度器计划处理下一个请求抓取。 
    9、重复该过程（继续步骤1），直到爬取完所有的url请求。

爬虫引擎(ENGINE) 
爬虫引擎负责控制各个组件之间的数据流，当某些操作触发事件后都是通过engine来处理。

调度器 
调度接收来engine的请求并将请求放入队列中，并通过事件返回给engine。

下载器 
通过engine请求下载网络数据并将结果响应给engine。

Spider 
Spider发出请求，并处理engine返回给它下载器响应数据，以items和规则内的数据请求(urls)返回给engine。

管道项目(item pipeline) 
负责处理engine返回spider解析后的数据，并且将数据持久化，例如将数据存入数据库或者文件。

下载中间件 
下载中间件是engine和下载器交互组件，以钩子(插件)的形式存在，可以代替接收请求、处理数据的下载以及将结果响应给engine。

spider中间件 
spider中间件是engine和spider之间的交互组件，以钩子(插件)的形式存在，可以代替处理response以及返回给engine items及新的请求集。

scrapy项目结构
    items.py 负责数据模型的建立，类似于实体类。
    middlewares.py 自己定义的中间件。
    pipelines.py 负责对spider返回数据的处理。
    settings.py 负责对整个爬虫的配置。
    spiders目录 负责存放继承自scrapy的爬虫类。
    scrapy.cfg scrapy基础配置

参考网站：
    https://www.xncoding.com/2016/03/08/scrapy-01.html