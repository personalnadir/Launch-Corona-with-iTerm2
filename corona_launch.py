import sys
import os
import subprocess


def main(directory,project):
	inDir=False
	for root,dirs,files in os.walk(directory):
		if inDir:
			for f in files:
				if f=="main.lua":

					command="osascript -l AppleScript itermlaunch.applescript " +os.path.join(root,f)
					print command
					subprocess.call(command,shell=True)
					return
			
		if ".git" in dirs:
			dirs.remove(".git")

		if project in (d.lower() for d in dirs):
			while len(dirs)>0:
				dirs.pop()

			dirs.append(project)
			inDir=True
		print root
	
if __name__ == '__main__':
	directory=sys.argv[1]
	project=sys.argv[2]
	assert(directory)
	assert(project.lower())
	main(directory,project)