# 326736_1:常见的数据结构----字符串
# 1.字符串构造
# 单引号构造字符串:字符串中含有双引号时；
string1 = '"commentTime":"2020-04-29","content":"包装良心！丰富多彩"'
print(string1)
# 双引号构造字符串:字符串中含有单引号时；
string2 = "'commentTime':'2020-04-29','content':'包装良心！丰富多彩'"
print(string2)
# 三引号构造字符串：字符串中既含有单引号又含有双引号时，或需要多行显示时；
string3 = ''''nickName':"美美",'content':"环境不错，服务态度超好，就是有点小贵"'''  # 这个好像是把里面的双引号和单引号都原样输出了
string4 = '''据了解，持续降雪造成安徽部分地区农房倒损、种植养殖业大棚损毁，
其中合肥、马鞍山、铜陵3市倒塌农房8间、紧急转移安置8人。'''
print(string3)
print(string4)

# 2.字符串属于序列
# a、正向单索引指的是只获取列表中的某一个元素，并且是从左到右的方向索取对应位置下的元素，可以使用[index]表示。
# b、需要注意的是，索引值index是从0开始的，所以索引值与实际元素的位置正好差1。
price = '5元/瓶'
# 取出价格，并做整型转换
print(int(price[0]))
# 取出字符串中的“元”
print(price[1])
# 取出字符串中的“瓶”
print(price[3])
print(price[len(price) - 1])

# a、负向单索引是指在正向单索引的基础上添加一个负号“-”，所表达的含义是从右向左的方向
# 获取元素，可以用[-index]表示。
# b、需要注意的是，负索引index是从-1开始的。
price = '5元/瓶'
# 取出字符串中的“瓶”
print(price[-1])
# 根据身份证号码识别性别
ID = '123456198908187890'
if int(ID[-2]) % 2 == 0:
    print('女')
else:
    print('男')

# 字符串切片:按照固定长度，连续取出多个元素.可以用[start:end:step]表示。其中，start指定索引的起始位置；end指定索引的终止位置（注意，end位置的元素取不到！）；step指步长，默认为1，表示逐个取出子元素。
# 有限切片
price2 = '24.5元/500g'
# 取出价格，并转换为浮点型
print(float(price2[0:4]))
# 取出字符串中的“500g”
print(price2[6:len(price2)])
ID = '123456198908187890'
# 取出出生日期
print(ID[6:14])

# 无限切片
price2 = '24.5元/500g'
# 取出价格，并转换为浮点型
print(float(price2[:4]))
# 取出字符串中的“500g”
print(price2[6:])
print(price2[-4:])

# 字符串查询
price3 = '89.9元/桶'
# 查询“元”所在的位置
print(price3.index('元'))
# 取出价格，并转换为浮点型
print(float(price3[:price3.index('元')]))

# 字符串压缩--去掉首位特殊字符信息
prodName = '乒乓球拍（红双喜） '
# 压缩右侧的空白字符
print(prodName.rstrip())
price3 = '单价：18.9 元/Kg'
# 取出价格并转换为浮点数
print(float(price3[3:price3.index('元')].rstrip()))
sentence = '&&&^_^很喜欢，给满分！(＾－＾)'
# 剔除评论中首尾的特殊字符
print(sentence.strip('&^_^(＾－＾)'))

# 字符串方法--替换
# str.replace(old, new) old：指定被替换的子串； new：指定新的子串；
sentence = '别克英朗1.3t的排量家用足够了，1.3T对应的可是163马力！'
# 将小写的t替换为大写的T -- 按值替换
print(sentence.replace('t', 'T'))
tel = '13612347890'
# 隐藏手机号中间四位
print(tel.replace(tel[3:7], '****'))

# 格式化插入“方法” str.format (values)  values：指定格式化的值；
# 转换为格式化风格
print('尊敬的{}{}，您的话费余额为{}元，请及时充值，以免影响通话！'.format('刘', '先生', 6.78))
# 保留两位有效数字的格式化  ---:.2f ：标识了保留两位小数
print('ROC曲线下的AUC值为：{:.2f}'.format(0.8356444))
# 生成5个有规则的网页链接--{0}：指定对对应format里面的第一个参数 ，以此类推
for month in [1, 2, 3, 4, 5]:
    print('http://tianqi.2345.com/t/wea_history/js/20190{}/60008_20190{}.js'.format(month, month+1))

# 分割方法 str.split(sep)  sep ：指定待分割的分割符；
email = 'lsx1234567@163.com'
# 将邮箱分割为邮箱名称和域名
print(email.split('@'))
info = '博佳花园 | 2室2厅 | 94.44平米 | 南 北 | 精装'
# 取出二手房中的面积值，并转换为浮点型
size = info.split('|')[2]
print(float(size[:5].lstrip()))
