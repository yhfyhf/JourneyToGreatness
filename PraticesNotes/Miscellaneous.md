# Miscellaneous


## 算法分析与比较
+ Hashtable VS Trie
[How Do I Choose Between a Hash Table and a Trie (Prefix Tree)?](http://stackoverflow.com/questions/245878/how-do-i-choose-between-a-hash-table-and-a-trie-prefix-tree)

Pros: Predictable O(k) lookup time(k is the size of query string), ordered traversal
Cons: use too much space, hard to destroy
+ Bloom filter VS Hashtable
[What is the advantage to using bloom filters?](http://stackoverflow.com/questions/4282375/what-is-the-advantage-to-using-bloom-filters)

> You don't use a bloom filter to test if an element is present, you use it to test whether it's certainly not present, since it guarantees no false negatives.
