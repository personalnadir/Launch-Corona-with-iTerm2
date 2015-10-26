import sys
import os
import subprocess
from os.path import expanduser

def main(directory,project,usePublic):
	if "~" in directory:
		directory=expanduser(directory)

	def pe(OSError):
		print (OSError)

	inDir=False
	for root,dirs,files in os.walk(directory,onerror=pe):
		if inDir and not project in root.lower():
			inDir=False
		print (root)
		if inDir:
			for f in files:
				if f=="main.lua":
					coronaDir="CoronaSDK" if not usePublic else "CoronaSDKPublic"
					command="osascript -l AppleScript itermlaunch.applescript '/Applications/"+ coronaDir+"/Corona\\ Simulator.app/Contents/MacOS/Corona\\ Simulator' '" + os.path.join(root,f) + " -no-console YES'"
					subprocess.call(command,shell=True)
					return
			
		if ".git" in dirs:
			dirs.remove(".git")
		for i in xrange(len(dirs)):
			if dirs[i].lower()==project:
				del dirs[0:i]
				del dirs[i+1:]
				inDir=True
				break

	if inDir:
		print ("Corona Launch: main.lua found in " + project)
	else:
		return ("Corona Launch: Directory named " + project + " not found in " + directory)
	
	
if __name__ == '__main__':
	directory=sys.argv[1]
	project=sys.argv[2]
	usePublic=False
	if len(sys.argv)>3:
		usePublic=sys.argv[3]=="True"
		if usePublic:
			print ("Corona Launch: using public build")
	
	assert(directory)
	assert(project)
	project=project.lower()
	main(directory,project,usePublic)
