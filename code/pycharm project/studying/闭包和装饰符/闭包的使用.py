#coding=utf-8
'''需求: 根据配置信息使用闭包实现不同人的对话信息，例如对话:
张三: 到北京了吗? 李四: 已经到了，放心吧。'''

def config_name(name):
    def say_info(info):
        print("%s:%s" % (name, info))
    return say_info

#创建闭包
p = config_name("张三")
p("到北京了吗？")
p2 = config_name("李四")
p2("已经到了，放心吧。")