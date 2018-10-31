## 560 和为k的子数组

给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

用一个value_dict,sum遍历到当前数字的总和， value_dict的key值初始都为0,
value_dict(i)代表子数组累计之和为i。
value值代表为i的数目。  numbers来记录总结果数，每次遍历，
numbers+=value_dict(sum-k)
因为value为sum-k的那个元素到当前遍历的元素的总和sum的总和刚好为k。
同时，value_dict(sum)也应该+=1。
