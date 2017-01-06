#
# 			put this bad boy in a folder with all ur lovely sbv timestamp files
#			change num_files to the number of files u got
#			make sure each file is numbered n.sbv in the order they happen
#
#

import datetime

end_timestamp = 0
temp_end_time = 0

#set this values before running the script
num_files = 4
#track lines to alternate between timestamp & non timestamp lines
is_time_ln = 0
full_script = ""

for num in range(1,num_files+1):
	sbv = open('{}.sbv'.format(num))
	for line in sbv:
		if is_time_ln%3 == 0:
			times = line.split(',')
			times[1] = times[1].strip('\n')
			dTime1 = datetime.datetime.strptime(times[0], "%H:%M:%S.%f")
			dTime2 = datetime.datetime.strptime(times[1], "%H:%M:%S.%f")
			dt1 = datetime.timedelta(minutes=dTime1.minute, seconds=dTime1.second, microseconds=dTime1.microsecond)
			dt2 = datetime.timedelta(minutes=dTime2.minute, seconds=dTime2.second, microseconds=dTime2.microsecond)
		
			if end_timestamp:
				dt1 = dt1 + end_timestamp
				dt2 = dt2 + end_timestamp
			temp_end_time = dt2

			new_ts_line = "{},{}\n".format(str(dt1)[:-3].upper(), str(dt2)[:-3].upper())
			full_script += new_ts_line
		else:
			full_script += line
		is_time_ln += 1
	end_timestamp = temp_end_time
	is_time_ln = 0
	sbv.close
new_file = open('full.sbv', 'w')
new_file.write(full_script)
new_file.close()




