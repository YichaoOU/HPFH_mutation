# HPFH_mutation
UCSC track hub, follow templates from: https://github.com/mhalushka/UCSC_miRNA_barchart


https://gist.github.com/ctokheim/5209723


http://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&hubUrl=https://raw.githubusercontent.com/YichaoOU/HPFH_mutation/master/hub.txt&position=chr11%3A5238662-5315734


## How to

If your institude provide public URL to host data, then this should be the easiest way. If not, like me, currently I'm using figshare, which is free to host your data but the download link has the random IDs that you can't get then in one click. luckly, I only need to do it 22 times. If you have too many data, you many want to write some code to get the links.

### Step 1: upload data to figshare

This is easy. Create an account, download figshare desktop and drag your files in.

Once uploaded, create a project, put title, author, descriptions, and move all data to this project and publish all data. (so that it create download links)

### Step 2: create hub.txt, genomes.txt and hg19/trackDb.txt

The logic is to provide hub.txt, where it specifies genomes.txt that specifies trackDb.txt that specifies all bw files.

This files can be automatically generated using a python library called trackHub. example code provided in `generate_hub.py`

### edit hub.txt and genomes.txt to fix some descriptions.


### copy and paste links to trackDb.txt
