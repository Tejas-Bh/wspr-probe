from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent / "weakmon"))

import ft8
import weakutil

from decode_ft8 import message

sender = ft8.FT8Send()

# Standard FT8 message format:
# CALLSIGN CALLSIGN GRID_OR_REPORT
bits77 = sender.pack(message, 1)



# 1000 Hz is the lowest of the eight FSK tones.
# FT8 tone frequencies will be:
# 1000.0, 1006.25, ..., 1043.75 Hz
sample_rate = 12000
audio = sender.tones(bits77, 1000, sample_rate)

# Scale to a reasonable 16-bit WAV amplitude.
audio = audio / max(abs(audio)) * 12000
weakutil.writewav(audio, "ft8.wav", sample_rate)

print(f"Generated {len(audio)} samples")
print(f"Duration: {len(audio) / sample_rate:.3f} seconds")