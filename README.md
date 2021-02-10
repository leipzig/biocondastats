See 

```
git submodule add https://github.com/bioconda/bioconda-recipes.git
ls bioconda-recipes/recipes > recipes.txt
cat recipes.txt | parallel --jobs 5 "condastats overall {}  --start_month 2020-01 --end_month 2020-12 --data_source bioconda >> 2020.txt"
cat 2020.txt | grep -v 'pkg_name' | grep -v 'Name:' > 2020.clean.txt
```

```
#these trip up yaml parsers
perl -p -i -e 's/\{\{.+\}\}//' */*meta.yaml
perl -p -i -e 's/^\s*{%.+//' */*meta.yaml
perl -p -i -e 's/: -/:/g' */*meta.yaml
perl -p -i -e "s/    - '$//" */*meta.yaml
perl -p -i -e 's/>&1//' */*meta.yaml
perl -p -i -e "s/^'$//" */meta.yaml
perl -p -i -e 's/ +$//'  */meta.yaml
```