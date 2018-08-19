#encoding=utf-8
# 请实现一个函数，将一个字符串中的空格替换成“%20”。
# 例如，当字符串为We Are Happy.
# 则经过替换之后的字符串为We%20Are%20Happy。
import time
import re
start=time.time()
rs='We Are Happy'

s=re.sub('[\s]','%20',rs)


print(s)

end=time.time()
tim1=end-start
print(tim1)

start=time.time()
rs='We Are Happy'
rs=rs.replace(' ','%20')
print(rs)
end=time.time()
tim=end-start

print(tim)
if tim1>tim:
    print('调用更快')
else:
    print('正则更快')