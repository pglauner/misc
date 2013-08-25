import solr
# create a connection to the Solr server
s = solr.SolrConnection('http://localhost:8983/solr')
# add documents to the index
s.add(id=1, title='The best solr book ever written', author='Author1')
s.add(id=2, title='The fastest computer', author='Author2')
s.add(id=3, title='Introduction to Solr', author='P. Glauner')
s.commit()