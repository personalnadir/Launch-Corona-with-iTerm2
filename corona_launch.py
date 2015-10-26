import sys
import os
import subprocess

def main(directory,project,usePublic):

	inDir=False
	for root,dirs,files in os.walk(directory):
		if inDir:
			for f in files:
				if f=="main.lua":
					coronaDir="CoronaSDK" if not usePublic else "CoronaSDKPublic"
					command="osascript -l AppleScript itermlaunch.applescript '/Applications/"+ coronaDir+"/Corona\\ Simulator.app/Contents/MacOS/Corona\\ Simulator' '" + os.path.join(root,f) + " -no-console YES'"
					subprocess.call(command,shell=True)
					return
			
		if ".git" in dirs:
			dirs.remove(".git")

		if project in (d.lower() for d in dirs):
			while len(dirs)>0:
				dirs.pop()

			dirs.append(project)
			inDir=True

	if inDir:
		print ("Corona Launch: main.lua found in " + project)
	else:
		print ("Corona Launch: Directory named " + project + " not found in " + directory)
	
	
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
