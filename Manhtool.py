import zlib
import base64
# ad: Võ Duy Mạnh 
# sdt: 0347447265
# cd /sdcard/download 
exec(__import__('zlib').decompress(base64.b64decode(b'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')).decode('utf-8'))