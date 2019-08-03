# デバイスに応じて以下を書き換えます
export ALSADEV="plughw:1,0"

# Juliusの起動
DICT=~/raspberrypi-sample/src/julius-dict/am-gmm.jconf
GRAM=~/raspberrypi-sample/src/raspi-piano/julius/inst_voice
julius -C $DICT -gram $GRAM -nostrip -module

