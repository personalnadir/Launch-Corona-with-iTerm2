on run argv
	set Applescript's text item delimiters to {"\\ "}
	set f to "" & argv

	tell application "iTerm"
		activate
		try
			terminate the first session of the first terminal
		end try
		set myterm to (make new terminal)
	
		tell myterm
			
			set mysession to (make new session at the end of sessions)
		
			tell mysession
				exec command "/Applications/CoronaSDK/Corona\\ Terminal " & f
				--quoted form of f
			
			end tell
		end tell
	end tell
end run

