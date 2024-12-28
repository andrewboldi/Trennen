while read p; do
  efetch -db pccompound -id $p -format docsum | xtract -pattern DocumentSummary -element IsomericSmiles >> ilovesmiles.txt
  echo $p
done <iloveu.txt
