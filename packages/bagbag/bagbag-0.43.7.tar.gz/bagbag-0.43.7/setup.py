# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bagbag',
 'bagbag.Funcs',
 'bagbag.Os',
 'bagbag.Os.Path',
 'bagbag.Socket',
 'bagbag.Tools',
 'bagbag.Tools.orator',
 'bagbag.Tools.orator.commands',
 'bagbag.Tools.orator.commands.migrations',
 'bagbag.Tools.orator.commands.models',
 'bagbag.Tools.orator.commands.seeds',
 'bagbag.Tools.orator.connections',
 'bagbag.Tools.orator.connectors',
 'bagbag.Tools.orator.dbal',
 'bagbag.Tools.orator.dbal.exceptions',
 'bagbag.Tools.orator.dbal.platforms',
 'bagbag.Tools.orator.dbal.platforms.keywords',
 'bagbag.Tools.orator.dbal.types',
 'bagbag.Tools.orator.events',
 'bagbag.Tools.orator.exceptions',
 'bagbag.Tools.orator.migrations',
 'bagbag.Tools.orator.orm',
 'bagbag.Tools.orator.orm.mixins',
 'bagbag.Tools.orator.orm.relations',
 'bagbag.Tools.orator.orm.scopes',
 'bagbag.Tools.orator.pagination',
 'bagbag.Tools.orator.query',
 'bagbag.Tools.orator.query.grammars',
 'bagbag.Tools.orator.query.processors',
 'bagbag.Tools.orator.schema',
 'bagbag.Tools.orator.schema.grammars',
 'bagbag.Tools.orator.seeds',
 'bagbag.Tools.orator.support',
 'bagbag.Tools.orator.utils']

package_data = \
{'': ['*']}

install_requires = \
['Faker>=0.8',
 'Flask>=2.1.3',
 'OpenCC>=0.2',
 'Pillow>=9.2.0',
 'PyMySQL>=1.0.2',
 'Pygments>=2.2',
 'backpack>=0.1',
 'blinker>=1.4',
 'cleo>=0.6',
 'inflection>=0.3',
 'ipdb>=0.13.9',
 'jieba>=0.42.1',
 'langid>=1.1.6',
 'lazy-object-proxy>=1.2',
 'loguru>=0.6.0',
 'lxml>=4.9.1',
 'openpyxl>=3.0.10',
 'paramiko>=2.11.0',
 'pendulum>=1.4',
 'prometheus-client>=0.14.1',
 'pyTelegramBotAPI>=4.6.1',
 'pyaml>=16.12',
 'pycrypto>=2.6.1',
 'pygtrans>=1.4.0',
 'python-dateutil>=2.8.2',
 'pythonping>=1.1.3',
 'pyyaml>=5.1',
 'random-user-agent>=1.0.1',
 'redis>=4.3.4',
 'requests-toolbelt>=0.9.1',
 'requests>=2.28.1',
 'schedule>=1.1.0',
 'selenium>=4.3.0',
 'shortuuid>=1.0.9',
 'simplejson>=3.10',
 'six>=1.10',
 'telethon>=1.24.0',
 'tqdm>=4.64.0',
 'wrapt>=1.10']

extras_require = \
{':sys_platform == "win32"': ['windows-curses>=2.3.0']}

setup_kwargs = {
    'name': 'bagbag',
    'version': '0.43.7',
    'description': 'An all in one python library',
    'long_description': '# bagbag\n\nAn all in one python library\n\n# Install \n\n```bash\npip3 install bagbag --upgrade\n```\n\n# Docker \n\n```bash\ndocker run --rm --name bagbag -v /path/to/file/run.py:/app/run.py darren2046/bagbag:latest\n```\n\n# Library\n\n* File(path:str)\n  * Write(data:str)\n  * Append(data:str)\n* Lg 日志模块\n  * Lg.SetLevel(level:日志级别:str)\n  * Lg.SetFile(path:日志路径:str, size:文件大小，MB:int, during:日志保留时间，天:int, color:是否带ANSI颜色:bool=True, json:是否格式化为json:bool=False)\n  * Lg.Debug(message:str)\n  * Lg.Trace(message:str)\n  * Lg.Info(message:str)\n  * Lg.Warn(message:str)\n  * Lg.Error(message:str)\n* String(string:str) 一些字符串处理函数\n  * HasChinese() -> bool 是否包含中文\n  * Language() -> str 语言\n  * Repr() -> str\n  * SimplifiedChineseToTraditional() -> str\n  * TraditionalChineseToSimplified() -> str\n  * Ommit(length:int) -> str\n* Time 时间\n  * Strftime(timestamp:float|int, format:str="%Y-%m-%d %H:%M:%S") -> str\n  * Strptime(timestring:str, format:str=None) -> int\n* Re 正则\n  """\n  If the message is too long, split it into chunks of 4096 characters and send them one by one\n  \n  :param msg: the message to be sent\n  :type msg: str\n  :param : `chatid` - the chat ID of the chat you want to send messages to\n  :type : str\n  """\n  * FindAll(pattern: str | Pattern[str], string: str, flags: _FlagsType = ...) -> list\n* Base64\n  * Encode(s:str|bytes) -> str\n  * Decode(s:str) -> str|bytes\n* Json\n  * Dumps(obj, indent=4, ensure_ascii=False) -> str\n  * Loads(s:str) -> list | dict\n  * ExtraValueByKey(obj:list|dict, key:str) -> list\n* Hash\n  * Md5sum(string:str) -> str\n* Os\n  * Exit(num:int=0)\n  * Mkdir(path:str)\n  * Getenv(varname:str, defaultValue:str=None) -> str | None\n  * ListDir(path:str) -> list[str]\n  * Unlink(path:str)\n  * Move(src:str, dst:str, force:bool=True)\n  * Copy(src:str, dst:str, force:bool=True)\n  * Path\n    * Basedir(path:str) -> str\n    * Join(*path) -> str\n    * Exists(path:str) -> bool\n    * Uniquify(path:str) -> str\n    * IsDir(path:str) -> bool\n    * Basename(path:str) -> str\n* Http\n  * Head(url:str, Timeout:str=None, ReadBodySize:int=None, FollowRedirect:bool=True, HttpProxy:str=None, TimeoutRetryTimes:int=0, InsecureSkipVerify:int=False,Debug:bool=False)\n  * Get(url:str, Timeout:str=None, ReadBodySize:int=None, FollowRedirect:bool=True, HttpProxy:str=None,  TimeoutRetryTimes:int=0, InsecureSkipVerify:int=False,Debug:bool=False)\n  * PostRaw(url:str, Data:str, Timeout:str=None, ReadBodySize:int=None, FollowRedirect:bool=True, HttpProxy:str=None, TimeoutRetryTimes:int=0, InsecureSkipVerify:int=False,Debug:bool=False)\n  * PostJson(url:str, Json:dict,Timeout:str=None, ReadBodySize:int=None, FollowRedirect:bool=True, HttpProxy:str=None, TimeoutRetryTimes:int=0, InsecureSkipVerify:int=False,Debug:bool=False)\n  * PostForm(url:str, Data:dict, Timeout:str=None, ReadBodySize:int=None, FollowRedirect:bool=True, HttpProxy:str=None, TimeoutRetryTimes:int=0, InsecureSkipVerify:int=False,Debug:bool=False)\n  * Delete(url:str, Timeout:str=None, ReadBodySize:int=None, FollowRedirect:bool=True, HttpProxy:str=None, TimeoutRetryTimes:int=0, InsecureSkipVerify:int=False,Debug:bool=False)\n  * PutForm(url:str, Data:dict,Timeout:str=None, ReadBodySize:int=None, FollowRedirect:bool=True, HttpProxy:str=None, TimeoutRetryTimes:int=0, InsecureSkipVerify:int=False,Debug:bool=False)\n  * PutRaw(url:str, Data:str, Timeout:str=None, ReadBodySize:int=None, FollowRedirect:bool=True, HttpProxy:str=None, TimeoutRetryTimes:int=0, InsecureSkipVerify:int=False, Debug:bool=False)\n  * PutJson(url:str, Json:dict, Timeout:str=None, ReadBodySize:int=None, FollowRedirect:bool=True, HttpProxy:str=None, TimeoutRetryTimes:int=0, InsecureSkipVerify:int=False,Debug:bool=False)\n* Socket\n  * TCP\n    * Listen(host:str, port:int, waitQueue:int=5)\n      * Accept() -> Chan[StreamConnection]\n      * AcceptOne() -> StreamConnection\n    * Connect(host:str, port:int) -> StreamConnection\n      * PeerAddress() -> TCPPeerAddress\n      * Send(data:str)\n      * SendBytes(data:bytes)\n      * Recv(length:int) -> str\n      * RecvBytes(length:int) -> bytes\n      * Close()\n* Random\n  * Int(min:int, max:int) -> int\n  * Choice(obj:list|str) -> Any\n  * String(length:int, charset:str="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") -> str\n  * Shuffle(li:list) -> list\n* Funcs\n  * Wget(url:str, dest:str=None, override=True)\n  * IP2Int(ip:str) -> int\n  * Int2IP(intip:int) -> str\n  * ResizeImage(src:str, dst:str, width:int, quality:int=95)\n  * UUID() -> str\n* Tools 一些工具\n  * SSH(host:str, port:int=None, user:str=None, password:str=None, pkey:str=None)\n    * GetOutput(command:str) -> str\n    * Close()\n    * Upload(localpath:str, remotepath:str=None)\n    * Download(remotepath:str, localpath:str=None)\n    * FileInfo(filepath:str)\n    * ListDir(dirpath:str=".") -> dict\n  * Translater\n    * Baidu(appid:str, secretkey:str)\n      * SetLang(To:str="zh", From:str="auto") -> Baidu\n      * Translate(text:str) -> dict\n    * Google(httpProxy:str=None)\n      * SetLang(To:str="zh-CN", From:str="auto") -> Google \n      * Translate(text:str, format:str="html") -> str\n  * XPath(html:str)\n    * Find(xpath:str) -> XPath | None\n    * Attribute(name:str) -> str | None\n    * Text() -> str\n    * Html() -> str\n  * WaitGroup()\n    * Add()\n    * Done()\n    * Wait()\n  * Crontab()\n    * Every(interval: int = 1) -> Crontab\n    * Second() -> Crontab\n    * Minute() -> Crontab\n    * Hour() -> Crontab\n    * Day() -> Crontab\n    * Week() -> Crontab\n    * At(time: str) -> Crontab\n    * Do(job_func, *args, **kwargs)\n    * Monday()\n    * Tuesday()\n    * Wednesday()\n    * Thursday()\n    * Friday()\n    * Saturday()\n    * Sunday()\n  * Elasticsearch(url:str)\n    * Delete(IndexName:str)\n    * Collection(IndexName:str)\n      * Index(id:int, data:dict, refresh:bool=False, Timeout:int=15)\n      * Refresh(Timeout:int=15)\n      * Delete(id:int)\n      * Search(key:str, value:str, page:int=1, pagesize:int=50, OrderByKey:str=None, OrderByOrder:str="ase", Highlight:str=None, mustIncludeAllWords:bool=True)\n  * CSV\n    * Reader(fpath:str)\n      * Read() -> dict\n      * Close()\n    * Writer(fpath:str, mode:str="w")\n      * SetHeaders(*headers)\n      * Write(row:dict[str])\n      * Close()\n      * Flush()\n  * Xlsx\n    * Reader(fpath:str)\n      * Read() -> dict\n      * Close()\n    * Writer(fpath:str, mode:str="w")\n      * SetHeaders(*headers)\n      * Write(row:dict[str])\n      * Close()\n      * Flush()\n  * WebServer(name:str=None) # 例子见源码文件Web.py的后半部分\n    * Run(host:str, port:int, block:bool=True) # 监听HTTP服务\n    * Route: (path:str, methods:list=["GET", "HEAD", "OPTIONS"]) # 例子见Web.py文件, 是一个装饰器\n    * Request()\n      * Method() -> str # 请求的HTTP方法\n      * Json() -> dict | list # 格式化请求的post内容为json\n      * Data() -> str # post的http的body\n      * Form()\n        * Get(name:str, default:str="") -> str | None # 获取表单的数据\n      * Args()\n        * Get(name:str, default:str="") -> str | None # 获取URL的参数\n  * Chan() 内存队列, 跟go的chan一样\n  * RateLimit(rate:str) rate可以是 次数/时间区间, 时间可以是s, m, h, d, 即秒,分,时,天. 例如一分钟限制五次: 5/m. 在低速率的时候能限制准确, 例如低于1秒10次. 高速率例如每秒50次以上, 实际速率会降低, 速率越高降低越多. \n    * Take(sleep:bool=True) sleep=True的时候会添加一个sleep, 可以把请求平均在时间段内. 在低速率的时候能限制准确. 高速率例如每秒50次以上, 实际速率会降低, 速率越高降低越多. sleep=False的时候没有sleep, 会全在一开始扔出去, 然后block住, 等下一个周期, 在需要速率很高的时候可以这样, 例如发包的时候, 一秒限制2000个包这样.\n  * URL(url:str)\n    * Parse() -> URLParseResult\n    * Encode() -> str\n    * Decode() -> str\n  * PrometheusMetricServer(listen:str="0.0.0.0", port:int=9105)\n    * NewCounter(name:str, help:str) -> prometheusCounter\n      * Add(num:int|float=1)\n    * NewCounterWithLabel(name:str, labels:list[str], help:str) -> prometheusCounterVec\n      * Add(labels:dict|list, num:int|float=1)\n    * NewGauge(name:str, help:str) -> prometheusGauge\n      * Set(num:int|float)\n    * NewGaugeWithLabel(name:str, labels:list[str], help:str) -> prometheusGaugeVec\n      * Set(labels:dict|list, num:int|float=1)\n  * Queue(db:Tools.MySql|Tools.SQLite)\n    * New(queueName="__queue__empty__name__") -> NamedQueue\n      * Size() -> int\n      * Get(waiting=True) -> str|None\n      * Put(string:str)\n  * Selenium\n    * Firefox(seleniumServer:str=None, PACFileURL:str=None, sessionID:str=None)\n    * Chrome(seleniumServer:str=None, httpProxy:str=None, sessionID=None)\n      * Except(*xpath:str, timeout:int=30) -> int | None\n      * ResizeWindow(width:int, height:int)\n      * ScrollRight(pixel:int)\n      * ScrollLeft(pixel:int)\n      * ScrollUp(pixel:int)\n      * ScrollDown(pixel:int)\n      * Url() -> str\n      * Cookie() -> list[dict]\n      * SetCookie(cookie_dict:dict)\n      * Refresh()\n      * GetSession() -> str\n      * Get(url:str)\n      * PageSource() -> str\n      * Title() -> str\n      * Close()\n      * SwitchTabByID(number:int)\n      * SwitchTabByIdent(ident:str)\n      * Tabs() -> list[str]\n      * NewTab() -> str\n      * Find(xpath:str, waiting=True) -> SeleniumElement\n        * Clear() -> SeleniumElement\n        * Click() -> SeleniumElement\n        * Text() -> str\n        * Attribute(name:str) -> str\n        * Input(string:str) -> SeleniumElement\n        * Submit() -> SeleniumElement\n        * PressEnter() -> SeleniumElement\n        * ScrollIntoElement() -> SeleniumElement\n  * Telegram(appid:str, apphash:str, sessionString:str=None)\n    * SessionString() -> str\n    * ResolvePeerByUsername(username:str) -> TelegramPeer\n    * PeerByIDAndHash(ID:int, Hash:int, Type:str="channel") -> TelegramPeer\n      * Messages(limit:int=100, offset:int=0) -> list[TelegramMessage]\n      * Message(id:str) -> TelegramMessage\n      * Resolve() # 如果手动根据ID初始化一个TelegramPeer实例, 调用这个函数可以补全这个ID对应的Peer的信息\n  * TelegramBot(token:str)\n    * GetMe() -> telebot.types.User\n    * SetChatID(chatid:int) -> TelegramBot\n    * SetTags(*tags:str) -> TelegramBot\n    * SendFile(path:str)\n    * SendImage(path:str)\n    * SendVideo(path:str)\n    * SendAudio(path:str)\n    * SendLocation(latitude:float, longitude:float)\n    * SendMsg(msg:str, *tags:str)\n  * ProgressBar(iterable_obj, total=None, title=None, leave=False)\n  * Redis(host: str, port: int = 6379, database: int = 0, password: str = "")\n    * Set(key:str, value:str, ttl:int=None) -> (bool | None)\n    * Get(key:str) -> (str | None)\n    * Del(key:str) -> int\n    * Lock(key:str) -> RedisLock\n      * Acquire()\n      * Release()\n  * MySQL(host: str, port: int, user: str, password: str, database: str, prefix:str = "") # 跟5.7兼容. 因为orator跟5.7兼容, 跟8.0会有小问题, 作者很久不更新, 有空换掉这个orm. **注意, Python的MySQL操作不支持多线程, 需要每个线程连接一次MySQL, 不过这个是自动的, 在Get, Update等操作的时候如果链接异常就重连**\n  * SQLite(path: str, prefix:str = "") **由于SQLite每次只能一个线程进行操作, 所以这里默认会有一个锁, 线程安全**\n    * Execute(sql: str) -> (bool | int | list)\n    * Tables() -> list\n    * Table(tbname: str) -> MySQLSQLiteTable\n      * AddColumn(colname: str, coltype: str, default=None, nullable:bool = True) -> MySQLSQLiteTable\n      * AddIndex(*cols: str) -> MySQLSQLiteTable\n      * Fields(*cols: str) -> MySQLSQLiteTable\n      * Where(key:str, opera:str, value:str) -> MySQLSQLiteTable\n      * WhereIn(key:str, value: list) -> MySQLSQLiteTable\n      * WhereNotIn(key:str, value: list) -> MySQLSQLiteTable\n      * WhereNull(key:str) -> MySQLSQLiteTable\n      * WhereNotNull(key:str) -> MySQLSQLiteTable\n      * WhereBetween(key:str, start:int|float|str, end:int|float|str) -> MySQLSQLiteTable\n      * WhereNotBetween(key:str, start:int|float|str, end:int|float|str) -> MySQLSQLiteTable\n      * OrWhere(key:str, opera:str, value:str) -> MySQLSQLiteTable\n      * OrWhereIn(key:str, value: list) -> MySQLSQLiteTable\n      * OrderBy(*key:str) -> MySQLSQLiteTable\n      * Limit(num:int) -> MySQLSQLiteTable\n      * Paginate(size:int, page:int) -> MySQLSQLiteTable\n      * Data(value:map) -> MySQLSQLiteTable\n      * Offset(num:int) -> MySQLSQLiteTable\n      * Insert()\n      * Update()\n      * Delete()\n      * InsertGetID() -> int\n      * Exists() -> bool\n      * Count() -> int\n      * Find(id:int) -> map\n      * First() -> map\n      * Get() -> list\n      * Columns() -> list[map]\n    * KeyValue(tbname:str)\n      * Get(key:str) -> Any\n      * Set(key:str, value:Any)\n      * Del(key:str)\n      * Keys() -> list[str]\n\n其它的\n\n* Thread(func, *args:Any, daemon:bool=True) -> threading.Thread # 启动线程, daemon=True\n* Process(func, *args:Any, daemon:bool=True) -> multiprocessing.Process # 启动进程, daemon=True',
    'author': 'Darren',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/darren2046/bagbag',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
