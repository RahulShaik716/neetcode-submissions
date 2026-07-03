class Node
{
        constructor(val) {
        this.value = val; 
        this.next = null; 
     }
};
class LinkedList {
    constructor() {
        this.head = null;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        let count = 0;
        let currNode =  this.head; 
        while(count!=index)
        {
            if(!currNode)
            return -1;
            currNode = currNode.next;
            count++;
        }
        if(!currNode) return -1;
        return currNode.value;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
         let temp = new Node(val);
         if(!this.head)
         this.head = temp;
         else
         {
            temp.next = this.head;
            this.head = temp;
         }
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        let temp = new Node(val);
        let temp2 = this.head;
        if(temp2 == null)
        this.head = temp;
        else{
        while(temp2.next!=null)
        temp2 = temp2.next; 
        temp2.next = temp;
        }
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        let count = 0; 
        let currNode = this.head; 
        let prevNode;
        if(this.head == null) return false;
        if(index == 0 && this.head!=null)
        {this.head = this.head.next; return true;}
        while(count!=index)
        {
            prevNode = currNode; 
            if(!currNode)
            return false;
            console.log(currNode.value);
            currNode = currNode.next; 
            count++;
        }
        if(currNode==null)
        return false; 
        prevNode.next = currNode.next; 
        return true;

    }

    /**
     * @return {number[]}
     */
    getValues() {
        let array = [];
        let currNode = this.head; 
        if(!currNode) return [[]];
        while(currNode.next!=null)
        {
            array.push(currNode.value);
            currNode = currNode.next; 
        }
        array.push(currNode.value);
        return array;
    }
}
