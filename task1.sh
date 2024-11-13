mkdir -p ~/TXT

count=0

for file in ~/*.txt; do

    if [ -f /$file' ]; then
        mv '$file' ~/TXT
        count=$((count + 1))
    fi 
done

echo '$count txt files moved'