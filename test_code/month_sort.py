from datetime import datetime

def monthsort(list):
	return [datetime.strftime(datetime.strptime(j,'%m'),'%b') for j in sorted([datetime.strftime(datetime.strptime(i, '%b'), '%m') for i in list])]
