# sbv-combiner
I wrote this script because I needed a large video transcribed. Youtube has an automatic transcription service but it seems to only work on videos under a certain time limit (not exactly sure - somewhere around 25-30 mins.) 

I took a video that was 1h15 long that I split up using [ffmpeg](https://ffmpeg.org/), uploaded the separate parts to youtube, downloaded all of the generated .sbv files for each part, then concatenated them together using this python script.

There might be some errors if special characters somehow show up in the transcript. The output is a new .sbv file, however I might make some additions in the future to get a second file with the plain text transcript - not that difficult if you wish to do that in the mean time.

##How to use
1. Put all of your .sbv files in a folder with the script. 
2. Rename all of your files to the number in which they occur (IE if you have three files, name them 1.sbv, 2.sbv and 3.sbv). 
3. In the code, modify num_files to the number of files you have to concatenate
4. Run!

####Please let me know if there are any questions, errors, or issues! Always looking to improve (: