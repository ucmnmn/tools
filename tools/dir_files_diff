import os,sys



def get_files(dir):
	works=os.walk(dir)
	myf=[]
	for r,d,f_list in works:
		myf.extend(f_list)
	return myf

if __name__ == '__main__':

	print("")
	print("")
	print("USAGE:PYHTON {} COMPARED_FILE,SOURCE_FILE".format(sys.argv[0]))
	print("")
	print("")

	
	
	paths=sys.argv[1:]
	old_dir, new_dir=paths[0],paths[1]


	# old_dir = "/Users/fengkai/Music/QQ音乐/已转 mp3"
	# new_dir = "/Users/fengkai/Music/converter-mp3-86"
	
	f_o=get_files(old_dir)
	f_n=get_files(new_dir)

	old_music=[x.split(".oggl")[0] for x in f_o]
	new_music= [x.split(".mp3")[0] for x in f_n]
	print("*********************************************")
	print(old_dir)
	print(new_dir)
	print("******以上两个目录下文件，有差异的列表***")
	print([x for x in old_music if x not in new_music])
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
