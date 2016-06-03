# gitlab pages自动发布

大家知道github的pages很好用，只需要编写markdown源码按照它的规则提交到github仓库就能自动生成web站点。而企业内部往往也有这些需求，因为企业内部使用的是gitlab，此文章就介绍如何在gitlab上实现github pages功能


## gitlab的webhook功能

**author:** linxuhua@unionpay.com

webhook功能介绍： [webhook](https://gitlab.com/gitlab-org/gitlab-ce/blob/master/doc/web_hooks/web_hooks.md)

## gitbook

[gitbook](https://www.gitbook.com/)不是必须，可以直接把静态的web页面放入git仓库，也可以使用其它的文档框架[jekyll](http://jekyllcn.com/) ,[hexo](https://hexo.io/zh-cn/index.html)等等都可以实现。

gitbook是一个把markdown转换为多种格式文档的工具，具体使用参考官方文档。

## gitlab 的deploy key
[deploy key](http://doc.gitlab.com/ce/api/deploy_keys.html)
使用此功能可以让服务器只有迁出代码的权限，而且不必输入用户名/密码信息。


## 实现思路
由于是简单实现，不考虑任何分支和提交，如果要考虑，需要解析webhook `post`过来的`json`格式。
利用`gitlab` 的 `webhook` 功能，在服务器部署一个web应用，可以通过一个url触发如下动作

 - 从git仓库迁出最新的版本
 - 使用工具产生出静态的html文档
 - 部署静态文档进`apache` or `nginx` 服务器目录

然后把此url配置为gitlab文档源码的`webhook`

### 参考示例

这里有两个示例，一个`indexhook`更新git仓库到apache静态站点的目录、一个`shellhook`执行一段脚本；使用python编写。注意，这里应用较简单，不建议在频繁push的仓库使用，如果有频繁push的仓库，需要优化后台的代码。支持`http`的 `get` 和 `post`访问触发，`webhook`是`post`触发。

[示例](http://172.17.249.122/xhlin/githook)
