import requests
import os.path
from django.core.management.base import BaseCommand, CommandError
from edamame_diseases.models import Disease

do_filename = "doid.obo"

def obo_download():
	do_url = "http://purl.obolibrary.org/obo/" + do_filename

	r = requests.get(do_url)
	with open(do_filename, "w") as do_file:
		do_file.write(r.content)

	do_file.close()

# from http://blog.nextgenetics.net/?e=6
def getTerm(stream):
  block = []
  for line in stream:
    if line.strip() == "[Term]" or line.strip() == "[Typedef]":
      break
    else:
      if line.strip() != "":
        block.append(line.strip())

  return block

def parseTagValue(term):
  data = {}
  for line in term:
    tag = line.split(': ',1)[0]
    value = line.split(': ',1)[1]
    if not data.has_key(tag):
      data[tag] = []

    data[tag].append(value)

  return data

class Command(BaseCommand):

    def handle(self, *args, **options):
		if not os.path.isfile(do_filename):
			obo_download()

		oboFile = open(do_filename,'r')

		#declare a blank dictionary
		#keys are the goids
		terms = {}
		self.stdout.write("terms: %s" % terms)

		#skip the file header lines
		getTerm(oboFile)

		#infinite loop to go through the obo file.
		#Breaks when the term returned is empty, indicating end of file
		while 1:
		  #get the term using the two parsing functions
		  term = parseTagValue(getTerm(oboFile))
		  if len(term) != 0:
			termID = term['id'][0]
			termName = term['name'][0]
			new_term = Disease.objects.get_or_create(doid=termID, name=termName)
			self.stdout.write("new term: %s" % new_term[0])

			#only add to the structure if the term has a is_a tag
			#the is_a value contain GOID and term definition
			#we only want the GOID
			if term.has_key('is_a'):
			  termParents = [p.split()[0] for p in term['is_a']]

			  if not terms.has_key(termID):
				#each goid will have two arrays of parents and children
				terms[termID] = {'name': termName, 'p':[],'c':[]}

			  #append parents of the current term
			  terms[termID]['p'] = termParents

			  parent_term = Disease.objects.get_or_create(doid=termParents[0])


			  #for every parent term, add this current term as children
			  for termParent in termParents:
				if not terms.has_key(termParent):
				  terms[termParent] = {'p':[],'c':[]}
				terms[termParent]['c'].append(termID)
		  else:
			break

		self.stdout.write(terms)