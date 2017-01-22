_input = IO.read("access.log")
ip_list = _input.scan(/(?:25[0-5]|2[0-4]\d|[0-1]?\d{1,2})(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d{1,2})){3}\b/)
ip_dic = Hash.new
for ip in ip_list
	if ip_dic.has_key?(ip) then
		ip_dic[ip] += 1
	else
		ip_dic[ip] = 1
	end
end

fd = IO.sysopen("output.txt", "w")
_output = IO.new(fd, "w")
sum = ip_dic.keys
subnets = sum.join(' ').scan(/[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\./).uniq!
for subnet in subnets
	for subnet_sum in sum
		if subnet_sum.start_with?(subnet) then
			_output.print(subnet_sum, ' ', ip_dic[subnet_sum], "\n")
		end
	end
	_output.print("\n")
end