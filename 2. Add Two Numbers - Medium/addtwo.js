// Faster than 96.88% online js submission
// Use less mem than 39.68% online js submission
var addTwoNumbers = function(l1, l2) {
    let a = ""
    let b = ""
    let c = []
    while(l1!=null || l2!=null){
        if(l1!=null){
            a = l1.val.toString()+a
            l1=l1.next
        }
        if(l2!=null){
            b = l2.val.toString()+ b
            l2=l2.next
        } 
    }
    let d = (BigInt(a)+BigInt(b)).toString()
    for(let i =0;i<d.length;i++){
        c.push(new ListNode(parseInt(d[i])))
        if(i>0){
            c[i].next = c[i-1]
        }
    }
    return c[c.length-1]
};