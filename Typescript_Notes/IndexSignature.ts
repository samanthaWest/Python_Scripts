// Index Signatures
// Dynamic way of saying keys, an object can have more keys we define it as
// Keys having type T must have a signature of U.  Key must be assignable to either
// number or string.
// can also use optional ? and readonly when declaring keys

let airplane: {
    [seatNumber: string]: string
} = {
    '34D': 'Sam'
}

// Saying this thing of generic type T has to have the same type T isn't enough.
// You may also want to say the type U should be at least T. We call this putting an 
// upper bound on U

// Why might we want to do this? Say we are implementing a binary tree with 3 types of nodes:
// 1. Regular Tree Node
// 2. Leaf node ( dont have children )
// 3. Inner node ( have children )

type TreeNode = {
    value: string
}

type LeafNode = TreeNode & {
    isLeaf: true
}

type InnerNode = TreeNode & {
    children: [TreeNode] | [TreeNode, TreeNode]
}

// Tree node is an object w/ a single prop.
// Leaf node has isLeaf plus tree node values
// Inner node has tree node values + points to either 1 or 2 children

let a: TreeNode = { value: 'a' }
let b: LeafNode = { value: 'b', isLeaf: true }
let c: InnerNode = { value: 'c', children: [b] }

let a1 = mapNode(a, _ => _.toUpperCase())

// Generic type is upper bound to Tree node therefore it can be either Tree node or
// a subtype of tree node
function mapNode<T extends TreeNode> (
    node: T,
    f: (value: string) => string
) : T {
    return {
        ...node,
        value: f(node.value)
    }
}

// Generic Type Defaults

type MyEvent<T> = {
    target: T
    type: string
}

// let buttonEvent: MyEvent<HTMLButtonElement> = {
//     target: myButton,
//     type: string
// }

// Add a bound to T to make sure T is an html element
type MyEvent2<T extends HTMLElement = HTMLElement> = {
    target: T
    type: string
}