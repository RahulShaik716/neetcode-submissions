class DynamicArray {
    /**
     * @constructor
     * @param {number} capacity
     */
    capacity;
    dataStore = [];
    constructor(capacity) {
        this.capacity = capacity
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {return this.dataStore[i];}

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.dataStore.splice(i,1,n);
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {
        if(this.dataStore.length == this.capacity)
        this.resize();
        this.dataStore.push(n);
    }

    /**
     * @returns {number}
     */
    popback() {
        return this.dataStore.pop();
    }

    /**
     * @returns {void}
     */
    resize() {
        this.capacity = 2*this.capacity;
        
    }

    /**
     * @returns {number}
     */
    getSize() {
       if(this.dataStore.length == 0) return 0; 
       else return this.dataStore.length;
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity;
    }
}
