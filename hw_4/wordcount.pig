tweets = LOAD './wordcount_data.txt' AS (tweet:chararray);

targets = LOAD './targets.txt' AS (target:chararray);

words = FOREACH tweets GENERATE FLATTEN(TOKENIZE(REPLACE(REPLACE(tweet,':',' '),'-',' '))) AS word;

j = JOIN targets BY LOWER(target) LEFT, words BY LOWER(word);

g = GROUP j by target;

s = FOREACH g GENERATE group, COUNT(j.word);

STORE s INTO './wordcount_results';