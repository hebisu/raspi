# Register microphone device
export ALSADEV="plughw:1,0"

# Run Julius
DICT=~/raspberrypi-sample/src/julius-dict/am-gmm.jconf
GRAM=~/raspberrypi-sample/src/raspi/raspi-piano/julius/inst_voice
julius -C $DICT -gram $GRAM -nostrip -module

