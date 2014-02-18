PRODROOT=`dirname $PWD`
PATH_TO_CFG=${PRODROOT}/etc/frazer.cfg
echo "[general]" > ${PATH_TO_CFG}
echo "path_to_files=${PRODROOT}/data" >> ${PATH_TO_CFG}
echo "timeout=120" >> ${PATH_TO_CFG}
echo "max_notify_width=400" >> ${PATH_TO_CFG}
echo "width_coefficient=5" >> ${PATH_TO_CFG}
echo "*************"
echo "* Job done. *"
echo "*************"
