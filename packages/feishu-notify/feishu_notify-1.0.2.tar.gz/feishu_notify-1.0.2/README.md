# Sentry DingTalk Notify People

Sentry 集成飞书机器人通知，并且通知人员 <br>
本插件是基于[sentry-dingtalk-notify](https://github.com/lanxuexing/sentry-dingtalk-notify) 进行的二次开发。

## Requirments 
- sentry >= 21.5.1

## 快速使用
### 安装
1. 使用 `pip` 命令
    ```bash
    $ pip install feishu-notify
    ```

2. 写入依赖文件 `onpremise-xxx/sentry/requirements.txt`
    ```bash
    $ echo feishu-notify >> requirements.txt
    ```

### 飞书机器人
[配置](https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN?lang=zh-CN#f62e72d5)飞书机器人并拿到对应的 webhook, 可以对机器人设置 关键词、签名、IP限制

### 配置
1. Sentry安装项目下的requirements.txt，添加feishu-notify==1.0.1；
2. 在 Sentry 面板 Settings > Integrations 中找到 FeiShu 并配置 webhook、关键词等信息，添加项目，创建告警规则；

#### 关于插件编写

1. 具体教程可以阅读这边文章[《如何开发自己的Python库》](https://zhuanlan.zhihu.com/p/60836179?utm_source=wechat_session&utm_medium=social&s_r=0)；

2. 编写自己的插件代码；

3. 打包自己的插件代码：

   ```
   python setup.py sdist bdist_wheel
   ```

4. 上传自己的插件：

   ```
   twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
   ```

   
