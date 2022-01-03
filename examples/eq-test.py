import sys
import matchering as mg

# Sending all log messages to the default print function
# Just delete the following line to work silently
mg.log(print)

if len(sys.argv) != 3:
    raise ValueError('Insufficient number of inputs: specify the source and reference wav files.')

source = sys.argv[1]
reference = sys.argv[2]

mg.process(
    # The track you want to master
    target=source,
    # Some "wet" reference track
    reference=reference,
    # Where and how to save your results
    results=[
        mg.pcm16(f"{source}-{reference}-16bit.wav"),
        mg.pcm24(f"{source}-{reference}-24bit.wav"),
    ],
    config=mg.Config(
        lowess_frac=0.1
    )
)
