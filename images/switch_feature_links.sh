#!/bin/bash
ITEM1="pillow.jpg"
ITEM2="book1.jpg"
PIC1="stuff.jpg"
PIC2="books2.jpg"
ITEM_LINK="item.jpg"
PIC_LINK="big_picture.jpg"

CURR_ITEM=`readlink ${ITEM_LINK}`
CURR_PIC=`readlink ${PIC_LINK}`

rm -f ${ITEM_LINK} ${PIC_LINK}

if [ "${CURR_ITEM}" =  "${ITEM1}" ] 
then
    ln -s  ${ITEM2} ${ITEM_LINK}
    ln -s  ${PIC2} ${PIC_LINK}
else
    ln -s ${ITEM1} ${ITEM_LINK}
    ln -s ${PIC1} ${PIC_LINK}
fi
    
