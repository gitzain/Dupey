import os
import hashlib

def hashy(file):
	hasher = hashlib.md5()
	with open(file, 'rb') as afile:
		buf = afile.read()
		hasher.update(buf)
		return hasher.hexdigest()

fileHashes = []
def checkIfAlreadyExists(hash):
	if hash in fileHashes:
		return True
	else:
		return False

deleted = 0
def shouldIDeleteThisFile(fileName):
	global deleted
	hash = hashy(fileName)
	if checkIfAlreadyExists(hash):
		# os.remove(fileName)
		# print hash + ' : ' + fileName + ' - Deleted'
		deleted += 1
	else:
		fileHashes.append(hash)
		# print hash + ' : ' + fileName + ' - Added to list'

totalNumberOfFiles = 0
for (dir, _, files) in os.walk(os.curdir):
	for f in files:
		path = os.path.join(dir, f)
		totalNumberOfFiles += 1
		shouldIDeleteThisFile(path)

print 'Finished. ' + str(deleted) + '/' + str(totalNumberOfFiles) + ' files were duplicates. They have been deleted.'