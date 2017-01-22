import re
_input = open('access.log', 'r')
ip_list = re.findall(r'(?:25[0-5]|2[0-4]\d|[0-1]?\d{1,2})(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d{1,2})){3}\b', _input.read())
_input.close()
ip_dic = {}
for ip in ip_list:
    if ip in ip_dic:
        ip_dic[ip] += 1
    else:
        ip_dic[ip] = 1
_output = open('output.txt', 'w')
sum = ip_dic.keys()
subnets = set(re.findall(r'[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.', str(sum))) 
for subnet in subnets:
    for subnet_sum in sum:
        if subnet_sum.startswith(subnet):
            _output.write(subnet_sum)
            _output.write(' ')
            _output.write(str(ip_dic[subnet_sum]))
            _output.write('\n')
    _output.write('\n')
_output.close()
print(subnets)
