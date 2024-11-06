#Branch formats
*develop
	-working main branch
	-protected by github, all code merges into this branch require a peer review prior to merges
	-only branch that should be merged into main
	-simple changes to .md files (like todo) can be made in this branch, but no code changes, and no meeting notes, or full documents. 

*main
	-main branch
	-can only be merged into from develop
	-no changes can be made from the main branch
	
*task/
	-all code changes wil be made inside of a task branch. 
	-name the branch task/[taskname]
	-branch off of develop
	-merge requests required
	
*note/
	-branch off of develop
	-any introduction a new markdown file (.md)
	-name the branch note/[docuementname]
	*meeting notes
		-new markdown files made for every weekly all hands meeting.
		-name note/meeting/[dateyymmdd]
	
*release/ ?? 
	-create a release branch evey time a merge is performed develop -> main
	-release/[dateyymmdd]