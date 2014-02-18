PRODROOT=`dirname $PWD`
export PRODROOT
PYSRCROOT=${PRODROOT}/src
python ${PYSRCROOT}/frazer.py $1
