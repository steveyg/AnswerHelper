# 常见问题

## Q:提示No module named aip

A：由于未安装百度ocr依赖导致找不到aip，通过pip install baidu-aip安装即可解决

## Q:提示No module named PIL

A：使用PIL库进行图像处理，尝试安装PIL或pillow即可

## Q:已经将手机投影至电脑中，如何切换OCR模式？

A：需要修改一下几个文件
- 修改config.py中GET_TYPE的值为TYPE_IMG
- 在img_utils的spot方法中用get_ios_img()方法代替crop()方法
- 调整get_ios_img()方法中box的值，确定截图位置

## Q:提示cannot write mode RGBA as JPEG

A: 修改config.py中的图片路径，把jpg改为png即可

## Q:提示NO such file or directory :'img.jpg '

A：图片路径指向错误，请讲config.py中的图片路径指向截图，或者排查是否截图没有生成

## Q:提示No JSON Object could be decode

A：出现这个说明已经成功运行，但是对于接口的异常没有进行处理，最新的代码已经修复这个缺陷，可以更新最新代码进行

## Q:如何选择不打开浏览器

A: 设置config中的OPEN_BROWSER为False

## Q:Windows投屏窗口化截图如何操作

A: 有两种方法

**方法一**
- 修改`config.py`中`PC_USE_WINDOW_CAPTURE`的值为1
- 打开目录下的`WindowFinder.exe`文件，根据界面提示拖拽鼠标到目标窗口，界面将显示目标窗口的信息，点击**生成配置文件**。当前目录就会生成`window.ini`配置文件。

**方法二**
- 修改`config.py`中`PC_USE_WINDOW_CAPTURE`的值为1
- 打开目录下的`WindowFinder.exe`文件，根据界面提示拖拽鼠标到目标窗口，界面将显示目标窗口的信息，**复制界面显示的句柄值**
- 修改`config.py`中`PC_WINDOW_CONFIG`的值为`'#句柄值'`

注：句柄值只在窗口被关闭前有效，若窗口被重新打开，需要重新做一遍方法二。**截图过程中窗口不能最小化**。

### 窗口化截图异常情况

#### 提示Cannot find target window
请检查是否已经使用WindowFinder生成配置文件。若已生成配置文件，请检查窗口是否已经打开。如果这两项都没有问题，就意味着窗口结构较复杂，解决方法见方法二。

#### 截到错误的图片
这种情况可能出现在窗口结构存在相似的软件中，解决方法见方法二。

#### 截到黑屏的图片
窗口不能最小化，请检查窗口是否最小化。如果还是黑屏，请尝试使用兼容模式：修改`config.py`中`PC_WINDOW_FALLBACK`的值为1。此模式在屏幕截图上裁剪出目标窗口区域，所以投屏窗口不能被遮挡。你也可以尝试其他投屏软件或者禁用窗口化截图。
