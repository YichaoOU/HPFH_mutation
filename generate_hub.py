import glob, os
import trackhub
# exec(open("test.py").read())
# First we initialize the components of a track hub
hub, genomes_file, genome, trackdb = trackhub.default_hub(
    hub_name="myhub",
    short_label='myhub',
    long_label='myhub',
    genome="hg19",
    email="Yichao.Li@stjude.org")

# Next, we add a track for every bigwig found.  In practice, you would
# point to your own files. In this example we use the path to the data
# included with trackhub.

for bigwig in glob.glob('*.bw'):
    name = trackhub.helpers.sanitize(os.path.basename(bigwig))
    track = trackhub.Track(
        name=name,          # track names can't have any spaces or special chars.
        source=bigwig,      # filename to build this track from
        visibility='full',  # shows the full signal
        color='123,204,196',    # brick red
        autoScale='on',     # allow the track to autoscale
        tracktype='bigWig', # required when making a track
    )

    # Each track is added to the trackdb
    trackdb.add_tracks(track)

# In this example we "upload" the hub locally. Files are created in the
# "example_hub" directory, along with symlinks to the tracks' data files.
# This directory can then be pushed to GitHub or rsynced to a server.
trackhub.upload.upload_hub(hub=hub, host='localhost', remote_dir='example_hub')

