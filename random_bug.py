from launchpadlib.launchpad import Launchpad
import json
import random

cachedir = "./.cache/"
launchpad = Launchpad.login_anonymously('lplib.evergreen.bug.report', 'production', cachedir, version='devel')

project = random.choice(['evergreen', 'opensrf'])
bugs = launchpad.projects[project].searchTasks(status = ['New', 'Triaged', 'Confirmed'], tags = 'pullrequest')

bug = random.choice(bugs)
print(bug.title + ' -- ' + bug.web_link)