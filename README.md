# Fake_Sqli_Bypass-自动化Fuzz Sqli/生成tamper
### Fake框架的自动化Fuzz WAF/IDS 功能

太久没写代码了，写的好丑hhhhhhhhh
</br>
其实这个功能点的开发并没有我想的这么简单，但是又非常的有意思，于是决定给他独立出来单独当一个功能,当然并不会在框架上分离出来.
至于后续的更新可能需要看情况以及有没有人使用,所以也没有一下子把功能写的非常完整，规则也是非常的简陋，直接采用网上现成的结果稍做修改。
</br>
规则也是非常的简陋，直接采用网上现成的结果稍做修改。
</br>
后续可能会依次更新规则库里面的规则，让它变得灵活化，人性化。
</br>
关于tamper的生成也比较简陋，但也还勉强能用
</br>
规则库后期采用WAF/IDS指纹对比，对应使用规则库，毕竟不同的waf拦截方式也是不同的，一个思路可能在这个waf上行不通在另外一个waf上可以绕过，正所谓术业有专攻，指定的waf有指定的payload，对于通用的还是很少的。
</br>
前期脚本只是放出来给大家娱乐娱乐，毕竟没有什么特别好用的操作

>Author：思缘
>
>Team  : [08Sec安全团队](https://www.08sec.org/) @校长办公室


## 使用方法

具体配置请修改config/settings.py

```
git clone https://github.com/RandomSiYuan/Fake_Sqli_Bypass.git
cd Fake_Sqli_Bypass
python3 main.py
```


## 已更新
### Fake_Sqli_Bypass v0.1

1.Fuzz 规则库更新
</br>
2.tamper生成

## 预计更新
### Fake_Sqli_Bypass v0.2

1.Fuzz 规则库更新
</br>
2.porxy 代理池
</br>
3.WAF识别 对应WAF选择规则库
</br>
