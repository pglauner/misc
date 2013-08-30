import solr
# create a connection to the Solr server
s = solr.SolrConnection('http://localhost:8983/solr')
response = s.query('title:Solr')
for hit in response.results:
    print '%s: %s' % (hit[u'score'], hit[u'title'][0])