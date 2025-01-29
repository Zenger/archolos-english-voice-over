import os, subprocess

source_folder = "<root>/translated"

def convert_wav(input_file):
	temp_file = input_file + "_converted.wav"

	ffmpeg_command = [
        "ffmpeg",
        "-i", input_file,       # Input file
        "-ar", "44100",         # Set sample rate to 44100 Hz
        "-ac", "1",	 # Set channels to 1 (mono)
        "-sample_fmt", "s16p",  # Set sample format to s16p (signed 16-bit packed)
        "-codec:a", "adpcm_ima_wav", # Set codec to adpcm_ima_wav
        "-y",                   # Overwrite the output file without asking
        temp_file               # Temporary output file
    ]

	subprocess.run(ffmpeg_command, check=True)


	if os.path.exists(temp_file):
		os.replace(temp_file, input_file)
		print(f"Done: {input_file} has been overwritten.")
	else:
		raise("BOOM")


# Main function to loop over all .wav files in the folder
def main():
	# Change to the source folder
	os.chdir(source_folder)

	# Loop over all .wav files in the folder
	for filename in os.listdir(source_folder):
		if filename.lower().endswith(".wav"):
			input_file = os.path.join(source_folder, filename)
			print(f"Processing: {input_file}")
			convert_wav(input_file)

	print("All files processed.")

if __name__ == "__main__":
	main()