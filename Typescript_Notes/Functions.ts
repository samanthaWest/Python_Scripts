
let a = { b: 'x'} // Labelling as an obj will narrow the type
console.log(a.b);

let c : {
    firstName: string,
    lastName: string
} = {
    firstName: 'john',
    lastName: 'smith'
}

class Person {
    constructor(public firstName: string, public lastName: string) {
        // public refers t0 a shorthand of 'this'
    }
}

let b = new Person('sam', 'west')

// Function Sig;nature and its implementation
type Log = (message: string, userId?: string) => void

let log: Log = (
    message,
    userId= 'Not Signed In'
) => {
    let time = new Date().toISOString()
    console.log(time, message, userId)
}

// Function Signature as a Param
function times(
    f: (index: number) => void,
    n: number
) {
    for(let i = 0; i < n; i++){
        f(i)
    }
}

// Overloaded Function Types

// Shorthand call signature (Preferable reg Funcs)
type Log2 = (message: string, userId?: string) => void
// Full Call Signature (More Complex Funcs)
type Log3 = {
    (message: string, userId?: string): void
}

// Overloaded Function - Function w/ multiple call signatures
// Typescript dynamism - if you pass params to a func with specific types it will guarentee call to that function unlike javascript

// Creating a Reservation Api Example w/ Overloading, avoid using any keyword in overloads
type Reservation = {
    from: Date,
    to?: Date,
    destination: string
}
type Reserve = {
    (from: Date, to: Date, destination: string): Reservation
    (from: Date, destination: string): Reservation
}
let reserve: Reserve = (
    from: Date,
    toOrDestination: Date | string, 
    destination?: string) => {
    let r: Reservation;
    if (toOrDestination instanceof Date && destination !== undefined) {
        console.log(" BOOK 1 WAY TRIP")
    } else if (typeof toOrDestination === 'string') {
        console.log(" BOOK A ROUND TRIP")
    }
    return r
}

// Named Func Syntax
// Function Expression
// Arrow Func
let greet7 = (name: string) => {
    return 'hi'
}

// Can have optional params

// Rest params

function summary(...numbers: number[]): number {
    return numbers.reduce((total, n) => total + n)
}

let numbers = [1,4,5,6,6,7]
// Spread iterator
let allNum = [...numbers]

// Destructor
let[one, two, three, ...rest] = numbers

// Polymorphism

function filter(array, f){
    let result = []
    for (let i = 0; i < array.length; i++) {
        let item = array[i]
        if (f(item)) {
            result.push(item)
        }
    }
    return result
}

filter([1,2,3,4], _ => _ < 3)

type Filter = {
    (array: number[], f: (item: number) => boolean): number[]
    (array: string[], f: (item:string) => boolean): string[]
    // incoming array of numbers, function where number results in true or false from func
    // returns a list of numbers
}

// We cant use object here because it doesn't know structure and wont let you access it
// Use generic Param aka placeholder type to enforce a type level constraint. Polymorphic type parameter

type FilterGeneric = {
    <T>(array: T[], f: (item: T) => boolean): T[]
}

let filter2: FilterGeneric = (array, f) => {
    let result = []
    for (let i = 0; i < array.length; i++) {
        let item = array[i]
        if (f(item)) {
            result.push(item)
        }
    }
    return result
}

filter2(['a','b'], _ => _ !== 'b')

let names = [
    {firstName: 'beth'},
    {firstName: 'caitlyn'},
    {firstName: 'xin'}
  ]
  filter2(names, _ => _.firstName.startsWith('b'))

// Because call deeclared T as part of call signature it will bind the concret Type T when func called
// if we instead scoped type Filter<T> ts would have required us to explicitly type when we used filter
// i.e Filter<number>

function map(array: unknown[], f: (item: unknown) => unknown): unknown[] {
    let result = []
    for (let i = 0; i < array.length; i++){
        result[i] = f(array[i])
    }
    return result
}

function map2<T,U>(array: T[], f: (item: T) => U): U[] {
    let result = []
    for (let i = 0; i < array.length; i++){
        result[i] = f(array[i])
    }
    return result
}

// Generic Type Interface

let promise = new Promise<number>(resolve =>
    resolve(45)
  )
  promise.then(result => // number
    result * 4
  )

// Generic Type Aliases
type MyEvent<T> = {
    target: T,
    type: string
}


type ButtonEvent = MyEvent<HTMLButtonElement>

// When ysing an explicist type like My Event youll have to bind its params they wont be inferred for ypu
// if you ref that type elsewhere

type TimedEvent<T> = {
    event: MyEvent<T>
    from: Date
    to: Date
  }