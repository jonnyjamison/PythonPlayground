import re, argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy as np

def findDuplicates(fileName):
    print('Finding duplicate tracks in %s...' % fileName)
    # read in a playlist file, will return top level dictionary
    plist = plistlib.readPlist(fileName) 
    # get the tracks from the Tracks dictionary
    tracks = plist['Tracks']
    # create a track name dictionary
    trackNames = {}
    # iterate through the tracks
    for trackId, track in tracks.items(): #items 
        try: #if an exception is raised, go to except block 
            name = track['Name']
            duration = track['Total Time']
            # look for existing entries
            if name in trackNames:
                # if a name and duration match, increment the count
                # round the track length to the nearest second
                if duration//1000 == trackNames[name][0]//1000: 
                    count = trackNames[name][1] #retrieving count as it is the
                    # second arguement 
                    trackNames[name] = (duration, count+1) #reassinging with new count value 
                else:
                    # add dictionary entry as tuple (duration, count)
                    trackNames[name] = (duration, 1)
        except:
            # have to have a try-except block some tracks might not have name defined 
            
            # ignore
            pass

# store duplicates as (name, count) tuples
    dups = [] #creating empty list 
    for k, v in trackNames.items():
        if v[1] > 1: #[1] corresponds to count 
            dups.append((v[1], k))
    # save duplicates to a file
    if len(dups) > 0:
        print("Found %d duplicates. Track names saved to dup.txt" % len(dups))
    else:
        print("No duplicate tracks found!")
    f = open("dups.txt", "w") #creates file 
    for val in dups: #iterates through the dups list 
        f.write("[%d] %s\n" % (val[0], val[1]))
    f.close()


def findCommonTracks(fileNames): #input will be a list of playlist filenames 
    # a list of sets of track names
    trackNameSets = []
    for fileName in fileNames:
        # create a new set
        trackNames = set() #python set object
        # read in playlist
        plist = plistlib.readPlist(fileName)
        # get the tracks
        tracks = plist['Tracks']
        # iterate through the tracks
        for trackId, track in tracks.items():
            try:
                # add the track name to a set
                trackNames.add(track['Name'])
  
            except:
                # ignore
                pass
        # add to list
        trackNameSets.append(trackNames)
        # get the set of common tracks
        commonTracks = set.intersection(*trackNameSets) 
        # write to file
        if len(commonTracks) > 0:
            f = open("common.txt", "w")
            for val in commonTracks:
                s = "%s\n" % val
                f.write(s.encode("UTF-8"))
            f.close()
            print("%d common tracks found. "
                "Track names written to common.txt." % len(commonTracks))
        else:
            print("No common tracks!")


def plotStats(fileName):
    # read in a playlist
    plist = plistlib.readPlist(fileName)
    # get the tracks from the playlist
    tracks = plist['Tracks']
    # create lists of song ratings and track durations
    ratings = []
    durations = []
    # iterate through the tracks
    for trackId, track in tracks.items():
        try:
            ratings.append(track['Album Rating'])
            durations.append(track['Total Time'])
        except:
            # ignore
            pass
    
    # ensure that valid data was collected
    if ratings == [] or durations == []:
        print("No valid Album Rating/Total Time data in %s." % fileName)
        return #exit function 
    
    
    # scatter plot
    x = np.array(durations, np.int32) #convert into 32bit integer array
    # convert to minutes
    x = x/60000.0
    y = np.array(ratings, np.int32)
    pyplot.subplot(2, 1, 1)
    pyplot.plot(x, y, 'o')
    pyplot.axis([0, 1.05*np.max(x), -1, 110])
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Track rating')
    # plot histogram
    pyplot.subplot(2, 1, 2)
    pyplot.hist(x, bins=20)
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Count')
    # show plot
    pyplot.show()
    
    
    
def main():
    # create parser
    descStr = """
    This program analyzes playlist files (.xml) exported from iTunes.
    """
    
    # creating arguement parsing object using argparse module
    parser = argparse.ArgumentParser(description=descStr)
    # add a mutually exclusive group of arguments
    group = parser.add_mutually_exclusive_group() #as program has different functions, suhc as finding duplicates etc, we can specify that it can only have one input at a time 
    
    # add expected arguments
    
    group.add_argument('--common', nargs='*', dest='plFiles', required=False)
    group.add_argument('--stats', dest='plFile', required=False)
    group.add_argument('--dup', dest='plFileD', required=False)
    
    # parse args
    args = parser.parse_args()
    
    if args.plFiles:
        # find common tracks
        findCommonTracks(args.plFiles)
    elif args.plFile:
        # plot stats
        plotStats(args.plFile)
    elif args.plFileD:
        # find duplicate tracks
        findDuplicates(args.plFileD)
    else:
        print("These are not the tracks you are looking for.")
        
        
# main method
if __name__ == '__main__':
    main()