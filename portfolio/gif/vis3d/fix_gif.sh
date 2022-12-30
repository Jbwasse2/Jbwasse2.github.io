for FILE in *; do
    convert -loop 0 $FILE $FILE
done
