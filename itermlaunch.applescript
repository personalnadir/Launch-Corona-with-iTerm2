on run argv
	set AppleScript's text item delimiters to {"\\ "}
	set prog to "" & item 1 of argv
	set param to "" & item 2 of argv
	set commandLine to prog & " " & param
	
	tell application "iTerm"
		activate
		try
			terminate the first session of the first terminal
		end try
		set myterm to (make new terminal)
		
		tell myterm
			
			set mysession to (make new session at the end of sessions)
			
			tell mysession
				
				exec command commandLine
			end tell
		end tell
	end tell
end run
