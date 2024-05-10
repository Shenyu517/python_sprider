爬虫项目实战

说明

所有项目均为作者练手分享项目，如遇侵权请联系删除，仅作学习分享，不能进行任何商业活动。
由于程序完成的时间问题，部分项目可能无法复用。
练习笔记见note.txt

基础篇：


	——itzmx_png：

	        这段代码是一个使用Python编写的图片下载器，可以采用多线程下载的方式。实现原理是使用了`requests`库来发送HTTP请求，获取图片内容。然后，使用`ThreadPoolExecutor`来并发下载所有图片。
	
	        代码的用途是下载网站"https://www.itzmx.com/"上存在的图片。网站上的图片以.webp为后缀，所以代码中使用了.webp作为图片链接的后缀。
	
	        注意事项：
	
	        1. 网站上的图片可能会有防盗链措施，因此需要设置有效的User-Agent。代码中已设置为："Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.237.400 QQBrowser/12.4.5621.400"。
	
	        2. 代码中设置了随机等待1到3秒，以避免频繁的HTTP请求。
	
	        3. 下载的图片会保存在当前目录下的"itzmx_png/image"文件夹中。如果需要更改保存路径，可以在`ImageDownloader`类中修改`save_path`变量。
	
	        4. 代码中的`download_images_multithreading`方法会下载所有给定的图片链接，但是没有处理下载失败的情况。在实际应用中，应该捕获异常并进行适当的错误处理。
	
	        5. 代码中使用了`ThreadPoolExecutor`来并发下载图片，但是没有限制最大线程数，可能会导致同时运行的线程过多，影响系统性能。在实际应用中，应该根据系统和硬件环境来设置合适的线程数。

 
scrapy：

	——zufang58：

            这段代码是一个使用Scrapy框架编写的爬虫，用于爬取"https://bj.zufang58.com/"网站上的租房信息。

            实现原理是使用Scrapy框架的`Request`和`Item`类，通过发送HTTP请求来获取网页内容，并使用`Item`类来提取需要的数据。

            注意事项：

            1. 需要安装Scrapy框架，并确保已经正确配置了Scrapy的环境。

            2. 在中间件中设置RandomProxyMiddleware，以实现网站屏蔽及防验证码。
进阶：

	——js逆向：

		——mou翻译：
		    是一个使用翻译API的Python脚本，用于将英语文本翻译成中文。
	
		    注意事项：
	
		    1. 一个简单的JavaScript逆向示例，用于将英语文本翻译成中文。

自动化：

	——TB_Buy:
	
	        这段代码是一个基于Python的自动化脚本，用于在淘宝网站上购买商品。脚本的主要功能包括：登录淘宝账号、进入购物车、全选所有商品、提交订单和计算点击购买的时间差。
	
	        实现原理：
	
	        1. 导入所需的库，如datetime、time、selenium等。
	        2. 定义一些函数，如wait_for_element、click_button、login、go_to_cart、select_all、go_to_checkout和submit_order。这些函数分别用于等待元素出现、点击按钮、登录、进入购物车、全选商品、提交订单和计算点击购买的时间差。
	        3. 在main函数中，获取用户输入的抢购时间，创建Chrome浏览器实例，设置隐式等待时间，访问淘宝网站，预加载页面内容。
	        4. 调用login、go_to_cart、select_all、go_to_checkout和submit_order函数，完成登录、进入购物车、全选商品、提交订单和计算点击购买的时间差。
	        5. 如果成功提交订单，计算点击购买的时间差，并退出浏览器。
	
	        用途：
	
	        淘宝抢购商品时，由于网络延迟等因素，可能需要通过脚本来自动完成登录、进入购物车、全选商品、提交订单等操作。这样，用户只需在抢购时间前输入抢购时间，脚本自动完成抢购流程。
	
	        注意事项：
	
	        1. 请确保已经安装了Python和selenium库，可以使用pip进行安装。
	        2. 请确保已经下载了Chrome浏览器，并安装了对应的WebDriver。
	        4. 请确保网络畅通，淘宝服务器能够访问。


