# 4shared Download Time Bypass

A family member of mine had several links of songs hosted on 4shared that he wanted to download. I was asked to help download the list of songs so I decided to write a python script to automate the process.

# How the Script Works
First you need a file that contains links to each song on 4shared. In addition each of those links needs to be wrapped in HTML anchor tags (e.g. &#x3C;a href=&#x22;4sharedlink&#x22;&#x3E;Link&#x3C;/a&#x3E;)

When the python script runs it looks at each link, views the source code of those links and then uses a regular expression to locate a link that ends with a .mp3 within that source code. This is where the song is actually located on the host. By downloading from the .mp3 link directly, the user can avoid waiting the madatory 45 seconds 4shared forces on the user in order to download the song.

The script not only automates the download process, but also bypasses the wait time for each song.

4shared might have updated their source code since the script was last tested

Last time script was tested: June 2015
