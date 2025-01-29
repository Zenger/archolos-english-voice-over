## The Chronicles of Myrtana: Archolos - English Voice-Over Pack (AI Generated)
This is the technical repository for the mod. Here you will find some of the files and scripts I used to generate the audio for the mod. I'm also using this repository to keep track of any issues and if I have time I will work on them.

### Download
You can [download the mod on moddb](https://www.moddb.com/mods/the-chronicles-of-myrtana-archolos-english-voice-over-pack-ai-generated/downloads/english-voice-over-pack). Once you've downloaded the mod, unzip the contents to the Data folder of your Chronicles of Myrtana: Archolos installation folder.
For steam that would be \SteamLibrary\steamapps\common\TheChroniclesOfMyrtana\Data. Ensure you replace the KM_Speech1EN.mod with the one in the archive.

### Report and issue
This is a hobby project and I may or may not return to it. If theres a game breaking issue or a completely whacked audio file an issue and I'll do my best to replace it/fix it.

### Whats in these files?
- [actors.json](actors.json) - holds the list of all unique actors that I managed to extract, in addition I compiled a few WAV samples for each actor in the original language, as well as an english transcript, I generated a phenotype for each actor, even though I ended up not using, maybe in the future when TTS gets much better.

- [build-locale.vm](build-locale.vm) - is the script I used to generate the *.MOD files, this script needs to be used with the GothicVDFS tool. I only used one script and increased the folder # as I went on.

- [GothicVDFS.exe v2.6](GothicVDFS.exe) - is the actual tool made by [Nico Bendlin](https://github.com/nicodex), I've included it for ease of access. VDFS is virtual filesystem used by the Zengin engine (Gothic 1 and 2), it acts as an archive manager and allows to extract/compress data.

- [index.json](index.json) - is the main database of the whole project. The [original localization](https://github.com/TheChroniclesOfMyrtana/localization) files from the Chronicles of Myrtana Team only hold about 30k lines, alot of the Ambient sounds are missing the strings in the file. I took the original Polish WAVs and mapped them to the json files, then the missing 16k or so files I transcribed, then translated to english (hence some lines are going to be a bit odd or awkward). 

- [s16p_wav.py](s16p_wav.py) - is just a helper script to ensure all WAVs are encoded in 44100 Hz mono signed 16-bit packed adpcm_ima_wav codec, I found this works best and matches both polish and russian voice over packs WAVs.

- [split_to_folders.py](split_to_folders.py) - looking at the russian voice over pack I noticed  all the archives have an exact number of 8488 per archive, I dont know if its a technical limitation or arbitrary but I used it as well and it seems to work just fine. This script splits my 50k WAVs in a single directory and moves them in their own 8488 per directory.

- [transcribe-and-translate.py](transcribe-and-translate.py) - Is the script I used to transcribe polish audio, then translate to english. In the script I used sqlite3 but it can be changed to work with the json in this repo, its just a reference.

- [tts.py](tts.py) - Is the script I used to actually voice the audios. It uses the XTTSv2 project from the amazing people at [Coqui.ai](https://github.com/coqui-ai/TTS), it just loops over and generates audio trying to clone the polish voice, its far from perfect, in fact I found that [F5-TTS](https://github.com/SWivid/F5-TTS) is much better at voice cloning, but sadly doesn't do Polish and is not nearly as good at doing emotion and intonation as well as XTTSv2.


### Disclaimer:
This mod is a fan-created project made solely for the enjoyment of the community. All copyrights and trademarks associated with the original game belong to their respective owners.
copyright goes to its rightful owners. This is a hobby project.


[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/zengerowitch)
