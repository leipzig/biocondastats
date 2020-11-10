```
git submodule add https://github.com/bioconda/bioconda-recipes.git
ls bioconda-recipes/recipes > recipes.txt
cat recipes.txt | parallel --jobs 5 "condastats overall {} 2020-01 --data_source bioconda >> output.txt"
```