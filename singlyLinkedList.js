class ListNode {
  constructor(value) {
    this.val = value;
    this.next = null;
  }
}

class LinkedList {

  #head;
  #tail;


  constructor() {
    this.#head = new ListNode(-1);
    this.#tail = this.#head;
  }

  /**
   * @param {number} index
   * @return {number}
   */
  get(index) {
    let i = 0;
    let curr = this.#head.next;
    while (curr) {
      if (i === index) {
        return curr.val;
      }
      i++;
      curr = curr.next;
    }
    return -1; // Index out of bounds or list is empty
  }

  /**
   * @param {number} val
   * @return {void}
   */
  insertHead(val) {
    const newNode = new ListNode(val);
    newNode.next = this.#head.next;
    this.#head.next = newNode;

    // If the list was empty before insertion:
    if (!newNode.next) {
      this.#tail = newNode;
    }
  }

  /**
   * @param {number} val
   * @return {void}
   */
  insertTail(val) {
    this.#tail.next = new ListNode(val);
    this.#tail = this.#tail.next;
  }

  /**
   * @param {number} index
   * @return {boolean}
   */
  remove(index) {
    let i = 0;
    let curr = this.#head;
    while (i < index && curr) {
      i++;
      curr = curr.next;
    }

    // Remove the node ahead of curr:
    if (curr && curr.next) {
      if (curr.next === this.tail) {
        this.tail = curr;
      }
      curr.next = curr.next.next;
      return true;
    }
    return false;
  }

  /**
   * @return {number[]}
   */
  getValues() {
    let curr = this.#head.next;
    const vals = [];
    while (curr) {
      vals.push(curr.val);
      curr = curr.next;
    }
    return vals;
  }
}

