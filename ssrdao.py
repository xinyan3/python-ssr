
import base64
from Crypto.Cipher import AES
import re
import redis

'''
本模块一共４个ｄｅｆ，组成解析ｓｓｒ订阅地址的密文到ｓｓｒ明文的ｄｉｃｔ

'''
 

def base64_decode(base64_encode_str):
   base64_encode_str = fill_padding(base64_encode_str)
   return base64.urlsafe_b64decode(base64_encode_str).decode('utf-8')
def fill_padding(base64_encode_str):

   need_padding = len(base64_encode_str) % 4 != 0

   if need_padding:
       missing_padding = 4 - need_padding
       base64_encode_str += '=' * missing_padding
   return base64_encode_str
def parse_ssr(base64_encode_str):
   decode_str = base64_decode(base64_encode_str)
   parts = decode_str.split(':')
   if len(parts) != 6:
       print('不能解析SSR链接: %s' % base64_encode_str)
       return

   server = parts[0]
   port = parts[1]
   protocol = parts[2]
   method = parts[3]
   obfs = parts[4]
   password_and_params = parts[5]

   password_and_params = password_and_params.split("/?")

   password_encode_str = password_and_params[0]
   password = base64_decode(password_encode_str)
   params = password_and_params[1]

   param_parts = params.split('&')

   param_dic = {}
   for part in param_parts:
       key_and_value = part.split('=')
       param_dic[key_and_value[0]] = key_and_value[1]
   print(param_dic)
   if len(param_dic)>=10:
      obfsparam = base64_decode(param_dic['obfsparam'])
      protoparam = base64_decode(param_dic['obfsparam'])
      remarks = base64_decode(param_dic['remarks'])
      group = base64_decode(param_dic['group'])
   else:
      obfsparam,protoparam,="",""
      remarks = base64_decode(param_dic['remarks'])
      group = base64_decode(param_dic['group'])
   print('server: %s, port: %s, 协议: %s, 加密方法: %s, 密码: %s, 混淆: %s, 混淆参数: %s, 协议参数: %s, 备注: %s, 分组: %s'
         % (server, port, protocol, method, password, obfs, obfsparam, protoparam, remarks, group))
   ssr_dict={
       "server": server,
       "port" : port,
       "协议":protocol,
       "加密方法":method,
       "密码":password,
       "混淆":obfs,
       "混淆参数":obfsparam,
       "协议参数":protoparam,
       "备注":remarks,
       "分组":group
   }
   r = redis.Redis(host='xinyan3.vicp.cc', port=6379,db=1)
# 使用连接池连接数据库。这样就可以实现多个Redis实例共享一个连接池
   pool = redis.ConnectionPool(host='xinyan3.vicp.cc', port=6379)
   r = redis.Redis(connection_pool=pool)
   r.hmset(remarks,ssr_dict)
   if r.hgetall(remarks)!=ssr_dict:
      r.hmset(remarks,ssr_dict)
   return ssr_dict

def zhenze(base_64_code):
    len_need=len(base_64_code)%4 !=0
    if len_need:
        missing_padding = 4 - len_need
        base_64_code += '=' * missing_padding
    return base_64_code
