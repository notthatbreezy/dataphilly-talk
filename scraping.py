import re
import lxml.html as lh
import os
import requests

link = "http://memeorandum.com/"
tree = lh.parse(link)

# Separate out topic clusters
clusters = tree.xpath('///div[@class="clus"]')

# Cites - want to exclude these. These are usually #
# just links to the front pages of sources like    #
# www.politico.com, etc.                           #
cites = [l.values()[0] for l in tree.xpath('///cite/a')]


# Save links for each cluster in its own list      #
# while separating out non-links, permanent links  #
# to memeorandum, and other unncessary data        #
cluster_list = []
link_counter = 0

print "Extracting links from topics on Memeorandum homepage"
for cluster in clusters:
    new_cluster = []
    for l in cluster.findall(".//a"):
        if (l.values()[0] in cites or 'name' in l.keys()
            or 'class' in l.keys() or 'title' in l.keys()):
            continue
        elif re.search(r'javascript', l.values()[0]):
            continue
        else:
            new_cluster.append(l.values()[0])
    # Remove Duplicates
    new_cluster = list(set(new_cluster))
    link_counter += len(new_cluster)
    cluster_list.append(new_cluster)

# Download and Save Articles for each topic #
save_path = './memeorandum_pages/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

print "Downloading {0} links".format(link_counter)
for t_counter, topic in enumerate(cluster_list):
    for l_counter, link in enumerate(topic):
        # Had to use requests - got weird errors with urllib2 #
        html = requests.get(link).content
        # First number = topic, Second number = id for page #
        output = open(save_path+'{0}_{1}.html'.format(t_counter, l_counter), 'w')
        output.write(html)
        output.close()

print "Summary of Clusters"
for counter, topic in enumerate(cluster_list):
    print"Cluster {0}: {1} articles".format(counter, len(topic))