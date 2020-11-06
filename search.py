# coding=utf-8
#查询文件获取备案信息
#备案查询文件放至re.txt
#备案数据放至doc.txt
import os,sys
import tldextract
icpdir = '/cache/icpcode/icp.out'
#test = input('输入要查询的域名')
f = open('/cache/icpcode/re.txt','r')
os.remove('/cache/icpcode/doc.txt')
lines = f.readlines()
for line in lines:
    val = tldextract.extract( "%s" % line )
    sldname = ('{0}.{1}'.format(val.domain,val.suffix))
    icp = os.popen('grep ^%s /cache/icpcode/icp.out | head -n 1' % sldname  )
    with open('/cache/icpcode/doc.txt','a') as file:
        file.write(icp.read())