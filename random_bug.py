from launchpadlib.launchpad import Launchpad
import json
import random
cachedir = "/home/jane/.launchpadlib/cache"

launchpad = Launchpad.login_anonymously('lplib.evergreen.randombug', 'production', cachedir, version = 'devel')
project = launchpad.projects['evergreen'] 
bugs = project.searchTasks(status = ['New', 'Triaged', 'Confirmed'])

bug = random.choice(bugs)
browser = launchpad._browser
bugInfo = json.loads(browser.get(bug.self_link))
print(bugInfo['title'])
print(bugInfo['web_link'])
