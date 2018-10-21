import csv

# reader 
# writer 
# DictReader 
# DictWriter  

# fp = open("test_emp.csv","r")

with open("test_emp.csv","a+") as fp:
	help(csv)
	# reader = csv.reader(fp)
	# print(reader)

	# print(next(reader))
	# for row in reader:
	# 	print(row)	

	# reader = csv.DictReader(fp)
	# print(next(reader))
	# print(next(reader))		

	# writer = csv.writer(fp,lineterminator = "\n")
	# writer.writerow(["POY","poy@gmail.com","71234567"])
	# writer.writerow(["POR","por@gmail.com","71234567"])
	# writer.writerows([["POZ","poz@gmail.com","71234567"],["POA","poa@gmail.com","71234567"],["POQ","poq@gmail.com","71234567"]])
# 	fileds = ['Name','Email','Contact']
# 	writer = csv.DictWriter(fp,lineterminator="\n",fieldnames = fileds)
# 	# writer.writerow({"Name":"KLP","Contact":"766555544"})
# 	writer.writerows([{"Name":"KLO","Contact":"766555544"},{"Name":"KLI","Contact":"766555544"}])
# # writerow 
# writerows