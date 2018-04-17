while IFS='' read -r line || [[ -n "$line" ]]; do 
	echo "$line"
	rel=`cat "$line" | grep "\->"`

	while IFS='' read -r subline || [[ -n "$subline" ]]; do
		echo "$subline"
	done <<< "$rel"

done < outlist
