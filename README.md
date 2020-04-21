# tsinghua-auth
一个简单的脚本，包含进行清华大学校园网认证的工具
### How to use

连接网络：
`python auth.py --connect`
断开连接
`python auth.py --disconnect`

### Advanced
这个工程可以和[AutoIPChangeNotifier](https://github.com/huangy10/AutoIPChangeNotifier)这个工程结合使用。当AutoIPChangeNotifier部署在你的服务器上时他会周期性的检查本机的ip，如果发生了变化，则通知给提前制定好的邮件账户。
但是当这个工具使用在校园网场景下时，服务器更换ip的时候，常常也意味着服务器掉线了。此时需要这个工程中提供的工具来接入校园网。
