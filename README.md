#Apache Solr Instance for Scientific Acrticle Indexing

This project contains a distribution of Apache Solr 4.10.2 with an index of documents on scientific articles for the biology domain.


##Installaion Instructions under Windows
To install this Solr instance, download the project into a dicrector of your choice and in the command line type the following:
+ `cd \`
+ `cd INSTANCE-DIR`
+ `cd MFNLiteratureApp`
+ `java -jar start.jar` to enable clustering the search result type instead: `java -Dsolr.clustering.enabled=true -jar start.jar`
+ Go to: [http://localhost:8983/solr](http://localhost:8983/solr)

##Query
The index is defined under the core "core0". To query the instance use the standard Solr query syntax. You can post the query from the command line using curl or by directly typing in your browser. For example, to query articles about "fish" type the following:

+ In your command line: `curl http://localhost:8983/solr/core0/select/?q=fish`
+ In your browser: `http://localhost:8983/solr/core0/select/?q=fish`

##Adding new documents to the index
To add new document to the index, you can the Post tool provided by Solr. The post.jar can be found in "/MFNLiteratureApp/posttool/". Note that the added documents must be compatible with the indexing schema as defined in MFNLiteratureApp/solr/HJDcollection/conf/schema.xml (more details below). Suppose that the new documents are stored in a directory called "myDocs". The corresponding command is:

+ `java -Dfile.encoding=UTF8 -Dauto=yes -Drecursive=yes  -Durl=http://localhost:8983/solr/core0/update -jar post.jar "myDocs"`





