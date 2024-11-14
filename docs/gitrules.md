# Branch formats
* dev
	- working main branch (develop)
	- protected by github, all code merges into this branch require a peer review prior to merges
	- only branch that should be merged into main
	- simple changes to .md files (like todo) can be made in this branch, but no code changes, and no meeting notes, or full documents. 

* main
	- main branch
	- can only be merged into from dev
	- no changes can be made from the main branch
	
* task/
	- all code changes wil be made inside of a task branch. 
	- name the branch task/[TaskName] using camelCase. Example: tasks/roomClass
	- branch off of dev
	- merge requests required
	
* docs/
	- branch off of dev
	- any introduction a new markdown file (.md)
	- any other type of document that is not code
	- name the branch docs/[DocuementName] using CamelCase. example: docs/GitRules
	- no merge request required
	* meeting notes
		- new markdown files made for every weekly all hands meeting.
		- name docs/meeting/[dateyymmdd] example: docs/meeting/241106 <- this will sort the files numerically by date with most recent at the top
		- actual file to be named Myymmdd example M241110
		- template saved to file path docs/meetings/M_template



# Tags??	-- NEED TO LEARN
* release/ 
	- create a release tag evey time a merge is performed from dev -> main
	- release/[dateyymmdd] example: release/241106 <- this will sort the files numerically by date with most recent at the top? maybe bottom lol we'll see