# feixiaoqiu2SRGF （非小酋到SRGF转换脚本）
基于Copilot编写的一个从非小酋到SRGF格式祈愿记录的Python脚本

使用必备条件：
1. 拥有一个非小酋账号，并且在其星穹铁道祈愿网站上有记录。
2. Python终端（Anaconda/VSCode/...，需要Python 3以上）

使用方法：
1. 登录非小酋，进入星穹铁道祈愿统计页面确认你的UID号
2. 在浏览器输入：**https://feixiaoqiu.com/query_xt_record/?uid=**
3. 在等于号（“**=** ”） 后面输入你的星穹铁道的UID号
4. 进入一个满是字符的界面，点击左上角的“美观输出”，右键空白处，点击“另存为”
5. 修改文件名为你想要的名字（最好为纯英文数字字符）加上文件名「**.json** 」
6. 保存到一个稳妥执行Python脚本的文件夹下
7. 用你的编辑器执行这个脚本（json路径时记得在终端去掉两端双引号）
8. 执行完毕后，打开 **https://schema.uigf.org/** 校验格式是否正确
9. 完成
