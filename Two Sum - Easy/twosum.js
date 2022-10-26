/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
// 99.73 %  faster than online js submission
// 23.60% less mem than online js submission
 var twoSum = function(o, t) {
    const a = {};
    for(let i = 0; i < o.length; i ++) {
      if (a[t - o[i]] !== undefined) {
          return [a[t - o[i]], i]
      } else {
        a[o[i]] = i;
      }
    }
  };